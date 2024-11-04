import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox,QWidget, QFileDialog
from PySide6.QtCore import QRunnable, Slot, Signal, QObject, QThreadPool, QThread, QTimer
from PySide6 import QtGui, QtCore
import numpy as np
from PySide6.QtGui import QImage, QPixmap
from main_window_ui import Ui_MainWindow
import signal
from PIL import ImageQt
import cv2
from ultralytics import YOLO  # Assuming you're using ultralytics YOLO
from PIL import ImageQt
from collections import Counter
import utils
from collections import defaultdict
import matplotlib.pyplot as plt
def load_custom_style():
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

def exit_with_sigint():
    signal.signal(signal.SIGINT, signal.SIG_DFL)


class WorkerSignals(QObject):
    frame_signal = Signal(np.ndarray)  # Signal for the frame



def Singleton(cls):  # This is a function that aims to implement a "decorator" for types.
    """
    cls: represents a class name, i.e., the name of the singleton class to be designed.
         Since in Python everything is an object, class names can also be passed as arguments.
    """
    instance = {}

    def singleton(*args, **kargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kargs)  # If the class does not exist in the dictionary, create an instance
            # and save it in the dictionary.
        return instance[cls]

    return singleton

@Singleton
class Predictor():
    def __init__(self):
        self.model_video = None
        self.model_img = None
        self.results = None
        self.plotted_result = None
        self.image = None  # Store the input image
        self.is_video = True
        self.total_count = {'stone': 0, 'fallen tree': 0, 'road collapse': 0, 'landslide': 0}
        self.track_history = defaultdict(lambda: [])
        self.load()

    def load(self):
        self.model_video = YOLO("best_v11s2.pt")  # Load your model
        self.model_img = YOLO("best_v11s2.pt")
        self.model_img.fuse()
        self.model_video.fuse()

    def reset(self):
        self.track_history= defaultdict(lambda: [])
        self.total_count = {'stone': 0, 'fallen tree': 0, 'road collapse': 0, 'landslide': 0}
        self.results = None

    def predict(self, img):
        """
        Perform prediction on the input image and store the result.
        """
        # Store the resized image for plotting later
        if self.is_video:
            self.results = self.model_video.track(img, conf=0.05, iou=0.3, persist=True,tracker="custom_tracker.yaml")[0]  # Perform inference

        else: 
            self.results = self.model_img.track(img, conf=0.01, iou=0.3)[0]  # Perform inference

        self.image = img
        self.detections = self.results

    def get_plotted_result(self, line_thickness=1):
        if self.results is not None:
        # Plot the result as usual
            img = self.results.plot(line_thickness)
            return img
        else:
            return self.image
    
    def get_result(self):
        return self.results
        
    def count_class_num(self):
        if self.results is not None: # fix video stop bug
            if (self.results.boxes.id) is not None:
                # Process detections
                track_ids = self.results.boxes.id.int().cpu().tolist()
                classes = self.results.boxes.cls.numpy()
                
                # Store tracking information and count classes
                result, self.track_history = utils.store_track_info(track_ids, classes, self.track_history)
                self.total_count = utils.count_from_track_history(self.track_history)
                self.total_count = utils.remap_dictionary(self.total_count)
        return self.total_count




class VideoWorker(QRunnable):
    """
    Worker thread that captures video frames in the background.
    """
    def __init__(self, model:Predictor, video_path):
        super().__init__()
        self.predictor = model
        self.signals = WorkerSignals()
        self.cap =  cv2.VideoCapture(video_path)
        self.cap.set(cv2.CAP_PROP_FPS, 4)  # Set FPS to 10
        self.is_running = True  # Flag to control the worker

    @Slot()  # Marks this method as a slot that can be invoked from Qt code
    def run(self):
        """
        Capture frames from the video feed in the background thread.
        """
        while self.is_running:
            ret, frame = self.cap.read()  # Capture frame from the webcam
            if ret:
                frame = cv2.resize(frame, (640, 480))
                self.predictor.predict(frame)
                # Emit the first signal with the plotted 
                print("frame")
                self.signals.frame_signal.emit(self.predictor.get_plotted_result())
                # Emit the second signal with the class count
            else:
                self.stop()
        self.stop()

    def stop(self):
        """Stop the video capture."""
        self.is_running = False
        self.cap.release()  # Release the webcam
        self.predictor.reset()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.model = Predictor()
        self.image = None
        self.setupUi(self)
        self.pushButton_select_file.clicked.connect(self.update_frame)
        self.pushButton_Detect.clicked.connect(self.detect_image)
        self.pushButton_stop.clicked.connect(self.stop_video)
        self.threadpool = QThreadPool()
        self.file_path = None
        self.worker = None
        self.class_count = {'stone':0, "landslide":0, "fallen tree":0, "road collapse":0 }
        self.resize_to_screen_fraction(fraction=1)

    def resize_to_screen_fraction(self, fraction):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        width = int(screen_geometry.width() * fraction)
        height = int(screen_geometry.height() * fraction)
        self.setGeometry(0, 0, width, height)

    def load_image(self):
        # Open a file dialog to select an image
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_name:
            pixmap = QtGui.QPixmap(file_name)  # Load the image
            scaled_pixmap = self.scale_qpix(pixmap)
            self.image = self.pixmap_to_pil_image(scaled_pixmap)
            self.display_image(scaled_pixmap)
    
    def show_msg_box(self):
        
        return

    def update_listview(self):
        return 
    
    def load_video(self):
        # Open a file dialog to select an image
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Video File", "", "Videos (*.mp4)")
        return file_name

    def stop_video(self):
        self.worker.is_running = False
        self.worker.stop()

    def update_frame(self):
        self.model.reset()
        if self.radioButton_video_mode.isChecked():
            self.start_video()
        elif self.radioButton_image_mode.isChecked():
            self.load_image()

    def scale_qpix(self, pixmap):
        # Set fixed width and height for the image to fit the label
        label_width = self.label_display.width()  # Get the label's width
        label_height = self.label_display.height()  # Get the label's height
        # Scale the pixmap to fit the label while keeping aspect ratio
        scaled_pixmap = pixmap.scaled(label_width*1, label_height*1, QtCore.Qt.AspectRatioMode.IgnoreAspectRatio)
        return scaled_pixmap
    
    def display_image(self,pixmap):
        self.label_display.setPixmap(pixmap)  # Set the scaled image on the label
        self.label_display.setScaledContents(False)  # Disable automatic scaling (since we manually scaled it)

    def detect_image(self):
        if self.image is not None:
            # Run the YOLO detection on the loaded image
            self.model.is_video = False
            self.model.predict(self.image)
            # Get the plotted result (annotated image)
            plotted_result = self.model.get_plotted_result()
            self.update_display_frame(plotted_result)
    
    def update_class_count(self):
        # Ensure self.class_count is initialized
        if not hasattr(self, 'class_count'):
            self.class_count = {'stone': 0, 'fallen tree': 0, 'road collapse': 0, 'landslide': 0}
        
        # Get the count from the model
        total_count = self.model.count_class_num()
        # Update the LCD displays
        if 'stone' in total_count:
            self.lcdNumber_stone.display(total_count['stone'])
        if 'fallen tree' in total_count:
            self.lcdNumber_fallentree.display(total_count['fallen tree'])
        if 'road collapse' in total_count:
            self.lcdNumber_roadcollapse.display(total_count['road collapse'])
        if 'landslide' in total_count:
            self.lcdNumber_landslide.display(total_count['landslide'])

        # Update self.class_count with the new counts
        for key in total_count:
            if key in self.class_count:
                self.class_count[key] = total_count[key]
        
    
    def start_video(self):
        """
        Start video playback using QRunnable.
        """
        video_path = self.load_video()  # Path to your MP4 video file
        self.worker = VideoWorker(self.model, video_path)  # Create the video worker
        # Connect signals to the appropriate slots
        self.worker.signals.frame_signal.connect(self.update_display_frame)
        self.model.is_video = True
        self.threadpool.start(self.worker)  # Start the worker in a separate thread

    def update_display_frame(self, frame):
        """
        Slot to update the QLabel with the video frame.
        """
        pixmap = self.numpy_to_qpixmap(frame)
        scaled_pixmap = self.scale_qpix(pixmap)
        # Display the image in your label or widget
        self.display_image(scaled_pixmap)
        self.update_class_count()

    def pil_to_pixmap(self, pil_image):
        """Convert PIL image to QPixmap for displaying in QLabel."""
        qimage = ImageQt.ImageQt(pil_image)  # Convert PIL.Image to PIL.ImageQt
        pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(qimage))  # Convert QImage to QPixmap
        return pixmap

    def closeEvent(self, event):
        # do stuff
        if can_exit:
            event.accept() # let the window close
        else:
            event.ignore()
            
    @staticmethod
    def pixmap_to_pil_image(pixmap):
        return ImageQt.fromqpixmap(pixmap)
    @staticmethod
    def numpy_to_qpixmap(np_image):
        # Check if the image is grayscale (2D array)
        if len(np_image.shape) == 2:
            # Convert grayscale to RGB (by repeating channels)
            np_image = cv2.cvtColor(np_image, cv2.COLOR_GRAY2RGB)
        # If image is BGR (OpenCV default), convert it to RGB
        if np_image.shape[2] == 3:  # BGR to RGB
            np_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2RGB)
        # Check if the NumPy array has 3 or 4 channels (3 for RGB, 4 for RGBA)
        if np_image.ndim == 3 and np_image.shape[2] == 3:
            # Convert RGB image
            height, width, channel = np_image.shape
            bytes_per_line = channel * width
            q_image = QImage(np_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        elif np_image.ndim == 3 and np_image.shape[2] == 4:
            # Convert RGBA image
            height, width, channel = np_image.shape
            bytes_per_line = channel * width
            q_image = QImage(np_image.data, width, height, bytes_per_line, QImage.Format_RGBA8888)
        else:
            raise ValueError("Unsupported image format!")

        # Convert QImage to QPixmap
        qpixmap = QPixmap.fromImage(q_image)
        return qpixmap
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_custom_style()
    exit_with_sigint()
    window = MainWindow()
    window.show()

    sys.exit(app.exec())