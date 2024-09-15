import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox,QWidget
from main_window_ui import Ui_MainWindow
import signal

def load_custom_style():
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

def exit_with_sigint():
    signal.signal(signal.SIGINT, signal.SIG_DFL)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
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
if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_custom_style()
    exit_with_sigint()
    window = MainWindow()
    window.show()

    sys.exit(app.exec())