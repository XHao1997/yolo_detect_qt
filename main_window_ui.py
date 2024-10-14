# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1205, 831)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1205, 200))
        MainWindow.setMaximumSize(QSize(1205, 4095))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(570, 0, 60, 60))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMaximumSize(QSize(60, 60))
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setPixmap(QPixmap(u"images.jpeg"))
        self.label_2.setScaledContents(True)
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(30, 80, 1171, 671))
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_display = QLabel(self.groupBox_3)
        self.label_display.setObjectName(u"label_display")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_display.sizePolicy().hasHeightForWidth())
        self.label_display.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.label_display)

        self.checkButton_video = QRadioButton(self.groupBox_3)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.checkButton_video)
        self.checkButton_video.setObjectName(u"checkButton_video")
        self.checkButton_video.setIconSize(QSize(8, 8))
        self.checkButton_video.setChecked(False)

        self.verticalLayout_3.addWidget(self.checkButton_video)

        self.checkButton_image = QRadioButton(self.groupBox_3)
        self.buttonGroup.addButton(self.checkButton_image)
        self.checkButton_image.setObjectName(u"checkButton_image")
        self.checkButton_image.setIconSize(QSize(8, 8))
        self.checkButton_image.setChecked(True)

        self.verticalLayout_3.addWidget(self.checkButton_image)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_display_2 = QPushButton(self.groupBox_3)
        self.pushButton_display_2.setObjectName(u"pushButton_display_2")
        self.pushButton_display_2.setMinimumSize(QSize(80, 25))

        self.horizontalLayout.addWidget(self.pushButton_display_2)

        self.pushButton_display = QPushButton(self.groupBox_3)
        self.pushButton_display.setObjectName(u"pushButton_display")
        self.pushButton_display.setMinimumSize(QSize(80, 25))

        self.horizontalLayout.addWidget(self.pushButton_display)

        self.pushButton_loadImage = QPushButton(self.groupBox_3)
        self.pushButton_loadImage.setObjectName(u"pushButton_loadImage")

        self.horizontalLayout.addWidget(self.pushButton_loadImage)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1205, 22))
        self.menuhi = QMenu(self.menubar)
        self.menuhi.setObjectName(u"menuhi")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuhi.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Yolo Disaster Detection", None))
        self.label_2.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Display", None))
        self.label_display.setText("")
        self.checkButton_video.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.checkButton_image.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.pushButton_display_2.setText(QCoreApplication.translate("MainWindow", u"Save Result", None))
        self.pushButton_display.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_loadImage.setText(QCoreApplication.translate("MainWindow", u"Choose Directory", None))
        self.menuhi.setTitle(QCoreApplication.translate("MainWindow", u"Yolo Detect", None))
    # retranslateUi

