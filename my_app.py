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
import supervision as sv 

def load_custom_style():
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

def exit_with_sigint():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

class WorkerSignals(QObject):
    """Defines the signals available from a running worker thread."""
    frame_signal = Signal(np.ndarray)  # Signal to send video frame data (as numpy array)


@singleton
class Predictor():
    def __init__(self, model_name):
        self.yolo = YOLO(model_name)
        self.result = None
        self.plotted_result = None
    
    def predict(self,img):
        self.results = self.yolo(img, conf=0.3, iou=0.2) 

    def plot(self):
        # Extract bounding boxes, confidence scores, and class labels
        boxes = np.array(self.results.boxes)  # Bounding box coordinates as a NumPy array
        scores = np.array(self.results.scores)  # Confidence scores as a NumPy array
        labels = np.array(self.results.labels)  # Class labels as a NumPy array (could be names or indices)

        # Assuming self.image is already a NumPy array (image)
        image = self.image.copy()

        # Create detection objects using supervision
        detections = sv.Detections(
            xyxy=boxes,       # Bounding boxes in the format (x1, y1, x2, y2)
            confidence=scores,  # Confidence scores
            class_id=labels    # Class labels
        )

        # Set the box annotator (with optional class map and color settings)
        box_annotator = sv.BoxAnnotator(
            thickness=2,  # Bounding box thickness
            text_thickness=1,  # Text thickness
            text_scale=0.5,  # Text size
            color=sv.Color.green(),  # Box color
            text_color=sv.Color.blue()  # Text color
        )

        # Annotate the image with bounding boxes and labels
        annotated_image = box_annotator.annotate(
            scene=image,       # The input image
            detections=detections)
        self.plotted_result = annotated_image

    def get_plotted_result(self):
        return self.plotted_result
    
class VideoWorker(QRunnable):
    """
    Worker thread that captures video frames in the background.
    """
    def __init__(self, model:Predictor, video_path):
        super().__init__()
        self.predictor = model
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
            self.predictor.predict(frame)
            self.predictor.plot()

            if ret:
                self.signals.frame_signal.emit(self.predictor.get_plotted_result)  # Emit the captured frame as a signal
            else:
                break

    def stop(self):
        """Stop the video capture."""
        self.is_running = False
        self.cap.release()  # Release the webcam

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.model = Predictor('best_v11.pt')
        self.image = None
        self.setupUi(self)
        self.pushButton_loadImage.clicked.connect(self.update_frame)
        self.pushButton_display.clicked.connect(self.detect_image)
        self.threadpool = QThreadPool()
        # Resize window to 3/4 of the screen size

    def resize_to_screen_fraction(self, fraction):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        width = int(screen_geometry.width() * fraction)
        height = int(screen_geometry.height() * fraction)
        self.setGeometry(0, 0, width, height)

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
            results = self.model.predict(self.image)[0]

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
        self.worker = VideoWorker(self.model, video_path)  # Create the video worker
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