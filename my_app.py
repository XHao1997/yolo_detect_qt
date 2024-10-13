import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox,QWidget, QFileDialog
from PySide6.QtCore import QRunnable, Slot, Signal, QObject, QThreadPool, Qt
from PySide6 import QtGui, QtCore
import numpy as np
from PySide6.QtGui import QImage, QPixmap
from main_window_ui import Ui_MainWindow
import signal
from ultralytics import YOLO
from PIL import ImageQt
import cv2
from singleton_decorator import singleton

def load_custom_style():
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

def exit_with_sigint():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

class WorkerSignals(QObject):
    """Defines the signals available from a running worker thread."""
    frame_signal = Signal(np.ndarray)  # Signal to send video frame data (as numpy array)

class VideoWorker(QRunnable):
    """
    Worker thread that captures video frames in the background.
    """
    def __init__(self, video_path):
        super().__init__()
        self.predictor = Predictor('best.pt')
        self.signals = WorkerSignals()
        self.cap =  cv2.VideoCapture(video_path)
        self.is_running = True  # Flag to control the worker
    @Slot()  # Marks this method as a slot that can be invoked from Qt code
    def run(self):
        """
        Capture frames from the video feed in the background thread.
        """
        while self.is_running:
            ret, frame = self.cap.read()  # Capture frame from the webcam
            if ret:
                self.signals.frame_signal.emit(frame)  # Emit the captured frame as a signal
            else:
                break

    def stop(self):
        """Stop the video capture."""
        self.is_running = False
        self.cap.release()  # Release the webcam

@singleton
class Predictor():
    def __init__(self, model_name):
        self.yolo = YOLO(model_name)
        
        return
                


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.model = Predictor('best.pt').yolo
        self.image = None
        self.setupUi(self)
        self.pushButton_loadImage.clicked.connect(self.update_frame)
        self.threadpool = QThreadPool()
    def uncheck(self, state): 
        # checking if state is checked 
        if state == QCheckBox.checkStateChanged(): 
            # if first check box is selected 
            if self.sender() == self.checkButton_image: 
                # making other check box to uncheck 
                self.checkButton_video(False) 
            # if third check box is selected 
            elif self.sender() == self.checkButton_video: 
                # making other check box to uncheck 
                self.checkButton_image(False) 

    def open_directory_callback(self):
        # Paths
        self._base_dir = os.getcwd()
        self._images_dir = os.path.join(self._base_dir, 'test_images')
        # Open a File Dialog and select the folder path
        dialog = QFileDialog()
        self._folder_path = dialog.getExistingDirectory(None, "Select Folder")
        # Get the list of images in the folder and read using matplotlib and print its shape
        self.list_of_images = os.listdir(self._folder_path)
        self.list_of_images = sorted(self.list_of_images)
        # Length of Images
        print('Number of Images in the selected folder: {}'.format(len(self.list_of_images)))
        input_img_raw_string = '{}\\{}'.format(self._images_dir, self.list_of_images[0])
        # Show the first Image in the same window. (self.label comes from the Ui_main_window class)
        self.label.setPixmap(QtGui.QPixmap(input_img_raw_string))
        self.label.show()

    def load_image(self):
        # Open a file dialog to select an image
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_name:
            pixmap = QtGui.QPixmap(file_name)  # Load the image
            scaled_pixmap = self.scale_qpix(pixmap)
            self.image = self.pixmap_to_pil_image(scaled_pixmap)
            self.display_image(scaled_pixmap)

    def update_frame(self):
        if self.checkButton_video.isChecked():
            self.start_video()
        elif self.checkButton_image.isChecked():
            self.load_image()

    def scale_qpix(self, pixmap):
        # Set fixed width and height for the image to fit the label
        label_width = self.label_display.width()  # Get the label's width
        label_height = self.label_display.height()  # Get the label's height
        # Scale the pixmap to fit the label while keeping aspect ratio
        scaled_pixmap = pixmap.scaled(label_width, label_height, QtCore.Qt.AspectRatioMode.IgnoreAspectRatio)
        return scaled_pixmap
    
    def display_image(self,pixmap):
        self.label_display.setPixmap(pixmap)  # Set the scaled image on the label
        self.label_display.setScaledContents(False)  # Disable automatic scaling (since we manually scaled it)

    def detect_image(self):
        if self.image:
            # Run the YOLO detection on the loaded image
            results = self.model(self.image,conf=0.5, iou=0.3)[0]

            results.save(filename = 'result.jpg')  # This will save the results (detected image with bounding boxes)
            # Load and display the detection result
            detected_img_path = 'result.jpg'  # Path of the image with bounding boxes
            pixmap = QtGui.QPixmap(detected_img_path)  # Load the detection result image
            self.display_image(pixmap)
    
    def start_video(self):
        """
        Start video playback using QRunnable.
        """
        video_path = "data/8552756-hd_1080_1920_30fps.mp4"  # Path to your MP4 video file
        self.worker = VideoWorker(video_path)  # Create the video worker
        self.worker.signals.frame_signal.connect(self.update_video_frame)  # Connect frame signal to the update slot
        self.threadpool.start(self.worker)  # Start the worker in a separate thread

    def update_video_frame(self, frame):
        """
        Slot to update the QLabel with the video frame.
        """
        # Convert the frame (numpy array) to QImage
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR (OpenCV default) to RGB
        h, w, ch = frame_rgb.shape
        bytes_per_line = ch * w
        qt_image = self.scale_qpix(QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888))
        # Set the QImage as a QPixmap in the QLabel
        self.label_display.setPixmap(QPixmap.fromImage(qt_image))


    @staticmethod
    def pixmap_to_pil_image(pixmap):
        return ImageQt.fromqpixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_custom_style()
    exit_with_sigint()
    window = MainWindow()
    window.show()

    sys.exit(app.exec())