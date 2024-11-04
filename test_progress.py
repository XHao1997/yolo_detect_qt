import sys
from PySide6.QtWidgets import QApplication, QWidget, QProgressDialog
from PySide6.QtCore import QTimer

class Operation(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Initialize steps and the progress dialog
        self.steps = 0
        self.pd = QProgressDialog("Operation in progress.", "Cancel", 0, 100, self)
        self.pd.setWindowTitle("Progress")
        self.pd.canceled.connect(self.cancel)
        
        # Initialize a timer to simulate the progress
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.perform)
        
        # Start the timer with an interval of 100 milliseconds
        self.timer.start(50)

    def perform(self):
        # Increment the steps and update the progress dialog
        self.pd.setValue(self.steps)
        self.steps += 1
        
        # Stop the timer if the operation is complete
        if self.steps > self.pd.maximum():
            self.timer.stop()

    def cancel(self):
        # Stop the timer and perform any necessary cleanup
        self.timer.stop()
        print("Operation canceled")

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Operation()
    window.show()
    sys.exit(app.exec())
