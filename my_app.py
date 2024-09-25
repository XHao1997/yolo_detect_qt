import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox,QWidget, QFileDialog
from PySide6 import QtGui, QtCore
from main_window_ui import Ui_MainWindow
import signal
from ultralytics import YOLO
from PIL import ImageQt
def load_custom_style():
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

def exit_with_sigint():
    signal.signal(signal.SIGINT, signal.SIG_DFL)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.model = YOLO('best.pt')
        self.image = None
        self.setupUi(self)
        self.pushButton_loadImage.clicked.connect(self.load_image)
        self.pushButton_display.clicked.connect(self.detect_image)
        print(self.pushButton_addItem.isChecked)

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
            self.image = self.pixmap_to_pil_image(pixmap)
            self.display_image(pixmap)
    def display_image(self,pixmap):
        # Set fixed width and height for the image to fit the label
        label_width = self.label_display.width()  # Get the label's width
        label_height = self.label_display.height()  # Get the label's height
        # Scale the pixmap to fit the label while keeping aspect ratio
        scaled_pixmap = pixmap.scaled(label_width, label_height, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.label_display.setPixmap(scaled_pixmap)  # Set the scaled image on the label
        # self.label_display.setScaledContents(False)  # Disable automatic scaling (since we manually scaled it)

    def detect_image(self):
        if self.image:
            # Run the YOLO detection on the loaded image
            results = self.model(self.image)[0]

            results.save(filename = 'result.jpg')  # This will save the results (detected image with bounding boxes)
            # Load and display the detection result
            detected_img_path = 'result.jpg'  # Path of the image with bounding boxes
            pixmap = QtGui.QPixmap(detected_img_path)  # Load the detection result image
            self.display_image(pixmap)
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