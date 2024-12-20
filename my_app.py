import sys, os
import shutil
import PIL
import PIL.ImageQt
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox,QWidget, QFileDialog,QMessageBox
from PySide6.QtCore import QRunnable, Slot, Signal, QObject, QThreadPool, QThread, QMutex,Slot, QWaitCondition, QMutexLocker
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
        self.model_video = YOLO("weights/best3.pt")  # Load your model
        self.model_img = YOLO("weights/best3.pt")
        self.model_img.fuse()
        self.model_video.fuse()

    def reset(self):
        self.track_history= defaultdict(lambda: [])
        self.total_count = {'stone': 0, 'fallen tree': 0, 'road collapse': 0, 'landslide': 0}
        self.model_video = YOLO("weights/best3.pt")  # Load your model
        self.results = None

    def predict(self, img):
        """
        Perform prediction on the input image and store the result.
        """
        # Store the resized image for plotting later
        if self.is_video:
            self.results = self.model_video.track(img, conf=0.05, iou=0.3, persist=True, tracker="custom_tracker.yaml")[0]  # Perform inference

        else: 
            self.results = self.model_img(img, conf=0.15, iou=0.15)[0]  # Perform inference

        self.image = img

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
            if (self.results.boxes) is not None:
                if self.is_video:
                    # Process detections
                    track_ids = self.results.boxes.id.int().cpu().tolist()
                    classes = self.results.boxes.cls.numpy()
                    # Store tracking information and count classes
                    result, self.track_history = utils.store_track_info(track_ids, classes, self.track_history)
                    self.total_count = utils.count_from_track_history(self.track_history)
                else:
                    self.total_count = utils.count_yolo_pred(self.results)
                    print(self.total_count)

                self.total_count = utils.remap_dictionary(self.total_count)
        return self.total_count


class Counter:
    def __init__(self):
        self.counting_info = {'stone': 0, 'fallen tree': 0, 'road collapse': 0, 'landslide': 0}
    
    def update(self, new_result):
        if isinstance(new_result, dict):
            for key, value in new_result.items():
                if key in self.counting_info:
                    self.counting_info[key] += value
    
    def clear(self):
        self.counting_info = {'stone': 0, 'fallen tree': 0, 'road collapse': 0, 'landslide': 0}  

    def get_result(self):
        return self.counting_info
    
class VideoWorker(QRunnable):
    """
    Worker thread that captures video frames in the background.
    """
    def __init__(self, model: Predictor):
        super().__init__()
        self.predictor = model
        self.signals = WorkerSignals()
        self.cap = None  # Initialize as None until a video is loaded
        self.is_running = True  # Flag to control the worker
        self.paused = False  # Flag to pause the worker
        self.condition = QWaitCondition()  # Condition variable for pausing/resuming
        self.mutex = QMutex()  # Mutex for thread-safe operations

    def load_video(self, video_path):
        """
        Loads a video file for processing.
        """
        # Release any existing video capture
        if self.cap:
            self.cap.release()
        
        self.cap = cv2.VideoCapture(video_path)
        if not self.cap.isOpened():
            raise ValueError(f"Failed to open video: {video_path}")
        
        # Set FPS to 10 if the video supports it
        self.cap.set(cv2.CAP_PROP_FPS, 10)
        
    @Slot()  # Marks this method as a slot that can be invoked from Qt code
    def run(self):
        """
        Capture frames from the video feed in the background thread.
        """
        while self.is_running:
            with QMutexLocker(self.mutex):
                if self.paused:
                    self.condition.wait(self.mutex)  # Wait until resumed
            
            ret, frame = self.cap.read()  # Capture frame from the webcam
            if ret:
                frame = cv2.resize(frame, (640, 480))
                self.predictor.predict(frame)
                # Emit the first signal with the plotted result
                self.signals.frame_signal.emit(self.predictor.get_plotted_result())
                # Emit the second signal with the class count if needed
            else:
                self.stop_thread()
        
    def pause_thread(self):
        with QMutexLocker(self.mutex):
            self.paused = True

    def resume_thread(self):
        with QMutexLocker(self.mutex):
            self.paused = False
            self.condition.wakeAll()  # Wake up all waiting threads

    def stop_thread(self):
        """Stop the video capture."""
        with QMutexLocker(self.mutex):
            self.is_running = False
            self.paused = False
            self.condition.wakeAll()  # Ensure the thread wakes up and exits cleanly
        
        if self.cap is not None:
            self.cap.release()  # Release the webcam
        self.predictor.reset()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.model = Predictor()
        self.image = None
        self.image_list_disp = []

        self.setupUi(self)
        self.list_model = QtGui.QStandardItemModel()
        self.listView.setModel(self.list_model)
        self.pushButton_select_file.clicked.connect(self.update_frame)
        self.pushButton_reformat.clicked.connect(self.reformat_filename)
        self.listView.clicked.connect(self.on_item_clicked)
        self.pushButton_Detect.clicked.connect(self.detect_image)
        self.pushButton_stop.clicked.connect(self.stop_video)
        self.pushButton_Resume.clicked.connect(self.resume_video)
        self.threadpool = QThreadPool()
        self.file_path = None
        self.worker = VideoWorker(self.model)  # Create the video worker
        self.counter  = Counter()
        self.class_count = {'stone':0, "landslide":0, "fallen tree":0, "road collapse":0 }
        self.resize_to_screen_fraction(fraction=1)

    def on_item_clicked(self, index):
        # Get the clicked item text
        item_text = self.list_model.data(index)
        # Use index.row() to access the correct item in image_list_disp
        pixmap = QtGui.QPixmap(self.image_list_disp[index.row()])  # Load the first image with full path
        self.image = self.pixmap_to_pil_image(pixmap)
        if self.radioButton_autodetect.isChecked():
            # Call the detection function
            self.detect_image()
        else:
            qpix = self.pil_to_pixmap(self.image)
            # Display the image in your label or widget
            self.display_image(qpix)

    def resize_to_screen_fraction(self, fraction):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        width = int(screen_geometry.width() * fraction)
        height = int(screen_geometry.height() * fraction)
        self.setGeometry(0, 0, width, height)

    def load_image(self):
        # Open a file dialog to select a folder
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            # List images in the folder
            self.list_images(folder_path)
            self.set_list_view()
            if self.image_list_disp:  # Check if there are any images
                pixmap = QtGui.QPixmap(self.image_list_disp[0])  # Load the first image with full path
                scaled_pixmap = self.scale_qpix(pixmap)
                self.image = self.pixmap_to_pil_image(pixmap)

    def resume_video(self):
        if self.worker is not None:
            self.worker.resume_thread()

    def set_list_view(self):
        entries = self.image_list_disp
        # add item to list view 
        self.list_model = QtGui.QStandardItemModel()
        self.listView.setModel(self.list_model)
        for file_path in entries:
            # Extract just the filename from the full path
            file_name = os.path.basename(file_path)
            item = QtGui.QStandardItem(file_name)  # Use only the filename for display
            self.list_model.appendRow(item)

    def list_images(self, folder_path):
        # Supported image file extensions
        image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"}
        
        # Clear the image list
        self.image_list_disp = []  # Initialize as an empty list

        # Find, store, and sort all image files with their full paths by index
        self.image_list_disp = sorted(
            [
                os.path.join(folder_path, f)  # Get full path for each image
                for f in os.listdir(folder_path)
                if os.path.splitext(f)[1].lower() in image_extensions
            ],
            key=lambda x: int(''.join(filter(str.isdigit, os.path.splitext(os.path.basename(x))[0])))
        )
        
        self.folder_path = folder_path  # Save the folder path


    def reformat_filename(self):
        model = self.listView.model()
        model.removeRows(0, model.rowCount())
        
        for index, file_path in enumerate(self.image_list_disp):
            # Get the directory and original filename
            directory, original_filename = os.path.split(file_path)
            file_extension = os.path.splitext(original_filename)[1]
            if "sample" not in original_filename:
                # Create a unique new filename with a 'sample_' prefix
                new_file_path = os.path.join(directory, f"sample_{index}{file_extension}")
                counter = 1
                while os.path.exists(new_file_path):
                    new_file_path = os.path.join(directory, f"sample_{index + counter}{file_extension}")
                    counter += 1
                # Rename the file
                shutil.move(file_path, new_file_path)
                # Update the list with the new file path
                self.image_list_disp[index] = new_file_path  # Update to the new full path
            
            # Refresh the QListView with the updated image_list
            self.set_list_view()



    def pop_msg_box(self):
        return



    def show_msg_box(self):
        
        return

    def update_listview(self):
        return 
        
    def load_video(self):
        # Open a file dialog to select a video
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Video File", "", "Videos (*.mp4 *.avi *.mov)")
        
        # Check if a file was selected
        if not file_name:  # file_name is an empty string if no file is selected
            print("No file selected. Operation canceled.")
            return None  # Explicitly return None if no file is selected
        
        return file_name


    def stop_video(self):
        """
        Stops the video processing worker gracefully.
        """
        # if self.worker:
        #     self.worker.is_running = False  # Signal the thread to stop
        #     if self.worker.cap and self.worker.cap.isOpened():
        #         self.worker.cap.release()  # Release video capture resources
        #     self.worker.stop_thread()
        self.worker.pause_thread()
            # self.worker = None  # Clear the reference to the worker

    def update_frame(self):
        self.model.reset()
        if self.radioButton_video_mode.isChecked():
            video_path = self.load_video()
            if video_path is not None:
                self.start_video(video_path)
        elif self.radioButton_image_mode.isChecked():
            self.model.is_video = False

            self.load_image()
            if self.radioButton_image_mode.isChecked() and self.radioButton_preview.isChecked():
                qpix = self.pil_to_pixmap(self.image)

                # Display the image in your label or widget
                self.display_image(qpix)
                pass
            else:
                self.detect_image()
            
    def scale_qpix(self, pixmap):
        # Set fixed width and height for the image to fit the label
        label_width = self.label_display.width()  # Get the label's width
        label_height = self.label_display.height()  # Get the label's height
        # Scale the pixmap to fit the label while keeping aspect ratio
        scaled_pixmap = pixmap.scaled(label_width*1, label_height*1, QtCore.Qt.AspectRatioMode.IgnoreAspectRatio)
        return scaled_pixmap
    
    def display_image(self, pixmap):
        scaled_pixmap = self.scale_qpix(pixmap)
        self.label_display.setPixmap(scaled_pixmap)  # Set the scaled image on the label
        self.label_display.setScaledContents(False)  # Disable automatic scaling (since we manually scaled it)

    def detect_image(self):
        if self.worker.is_running:
            self.stop_video()
        if self.image is not None:
            # Run the YOLO detection on the loaded image
            print(self.image)
            # Resize the image to 640x640
            img_resized = self.image.resize((640, 640))
            self.model.predict(img_resized)
            # Get the plotted result (annotated image)
            plotted_result = self.model.get_plotted_result()
            self.update_display_frame(plotted_result)
    
    def update_class_count(self):
        # Ensure self.class_count is initialized
        if not hasattr(self, 'class_count'):
            self.class_count = {'stone': 0, 'fallen tree': 0, 'road collapse': 0, 'landslide': 0}
        
        # Get the count from the model
        if self.model.is_video:
            self.counter.clear()
        self.counter.update(self.model.count_class_num())
        total_count = self.counter.get_result()
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
        
    
    def start_video(self, video_path):
        """
        Start video playback using QRunnable.
        """
        self.listView.model().clear()
        # Connect signals to the appropriate slots
        self.worker = VideoWorker(self.model)
        self.worker.signals.frame_signal.connect(self.update_display_frame)
        self.worker.load_video(video_path)
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
        event.accept() # let the window close
        

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