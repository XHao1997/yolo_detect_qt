import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox,QWidget, QFileDialog
from PySide6 import QtGui
from main_window_ui import Ui_MainWindow
import signal

def load_custom_style():
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

def exit_with_sigint():
    signal.signal(signal.SIGINT, signal.SIG_DFL)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_custom_style()
    exit_with_sigint()
    window = MainWindow()
    window.show()

    sys.exit(app.exec())