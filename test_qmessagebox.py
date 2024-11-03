from PySide6.QtWidgets import QMessageBox, QApplication
import sys

app = QApplication(sys.argv)

msgBox = QMessageBox()
msgBox.setWindowTitle("Document Status")
msgBox.setText("The document has been modified.")
msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

# Customize button text
ok_button = msgBox.button(QMessageBox.Ok)
ok_button.setText("确定")  # Set text for the OK button
cancel_button = msgBox.button(QMessageBox.Cancel)
cancel_button.setText("取消")  # Set text for the Cancel button

response = msgBox.exec()

if response == QMessageBox.Ok:
    print("User clicked OK")
elif response == QMessageBox.Cancel:
    print("User clicked Cancel")

sys.exit(app.exit())
