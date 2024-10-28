# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLCDNumber, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1312, 647)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(60, 60))
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)
        self.label_2.setPixmap(QPixmap(u"images.jpeg"))
        self.label_2.setScaledContents(True)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalWidget = QWidget(self.groupBox)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.horizontalWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.label = QLabel(self.horizontalWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.label_3 = QLabel(self.horizontalWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.label_5 = QLabel(self.horizontalWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lcdNumber_stone = QLCDNumber(self.horizontalWidget)
        self.lcdNumber_stone.setObjectName(u"lcdNumber_stone")
        self.lcdNumber_stone.setMinimumSize(QSize(100, 0))
        self.lcdNumber_stone.setMaximumSize(QSize(50, 20))
#if QT_CONFIG(accessibility)
        self.lcdNumber_stone.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.lcdNumber_stone.setAutoFillBackground(True)
        self.lcdNumber_stone.setStyleSheet(u"font: 700 11pt \"Ubuntu\";")
        self.lcdNumber_stone.setFrameShadow(QFrame.Shadow.Plain)
        self.lcdNumber_stone.setLineWidth(1)
        self.lcdNumber_stone.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.verticalLayout_4.addWidget(self.lcdNumber_stone)

        self.lcdNumber_fallentree = QLCDNumber(self.horizontalWidget)
        self.lcdNumber_fallentree.setObjectName(u"lcdNumber_fallentree")
        self.lcdNumber_fallentree.setMinimumSize(QSize(100, 0))
        self.lcdNumber_fallentree.setMaximumSize(QSize(50, 20))
#if QT_CONFIG(accessibility)
        self.lcdNumber_fallentree.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.lcdNumber_fallentree.setAutoFillBackground(True)
        self.lcdNumber_fallentree.setFrameShadow(QFrame.Shadow.Plain)
        self.lcdNumber_fallentree.setLineWidth(1)
        self.lcdNumber_fallentree.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.verticalLayout_4.addWidget(self.lcdNumber_fallentree)

        self.lcdNumber_roadcollapse = QLCDNumber(self.horizontalWidget)
        self.lcdNumber_roadcollapse.setObjectName(u"lcdNumber_roadcollapse")
        self.lcdNumber_roadcollapse.setMinimumSize(QSize(100, 0))
        self.lcdNumber_roadcollapse.setMaximumSize(QSize(50, 20))
#if QT_CONFIG(accessibility)
        self.lcdNumber_roadcollapse.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.lcdNumber_roadcollapse.setAutoFillBackground(True)
        self.lcdNumber_roadcollapse.setFrameShadow(QFrame.Shadow.Plain)
        self.lcdNumber_roadcollapse.setLineWidth(1)
        self.lcdNumber_roadcollapse.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.verticalLayout_4.addWidget(self.lcdNumber_roadcollapse)

        self.lcdNumber_landslide = QLCDNumber(self.horizontalWidget)
        self.lcdNumber_landslide.setObjectName(u"lcdNumber_landslide")
        self.lcdNumber_landslide.setMinimumSize(QSize(100, 0))
        self.lcdNumber_landslide.setMaximumSize(QSize(50, 20))
#if QT_CONFIG(accessibility)
        self.lcdNumber_landslide.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.lcdNumber_landslide.setAutoFillBackground(True)
        self.lcdNumber_landslide.setFrameShadow(QFrame.Shadow.Plain)
        self.lcdNumber_landslide.setLineWidth(1)
        self.lcdNumber_landslide.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.verticalLayout_4.addWidget(self.lcdNumber_landslide)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addWidget(self.horizontalWidget)

        self.verticalWidget = QWidget(self.groupBox)
        self.verticalWidget.setObjectName(u"verticalWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.verticalWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_2.addWidget(self.verticalWidget)

        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_2.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 2, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_display = QLabel(self.groupBox_3)
        self.label_display.setObjectName(u"label_display")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_display.sizePolicy().hasHeightForWidth())
        self.label_display.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.label_display)

        self.widget_2 = QWidget(self.groupBox_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_video_mode = QRadioButton(self.widget_2)
        self.radioButton_video_mode.setObjectName(u"radioButton_video_mode")

        self.horizontalLayout.addWidget(self.radioButton_video_mode)

        self.radioButton_image_mode = QRadioButton(self.widget_2)
        self.radioButton_image_mode.setObjectName(u"radioButton_image_mode")

        self.horizontalLayout.addWidget(self.radioButton_image_mode)

        self.pushButton_stop = QPushButton(self.widget_2)
        self.pushButton_stop.setObjectName(u"pushButton_stop")

        self.horizontalLayout.addWidget(self.pushButton_stop)

        self.pushButton_select_file = QPushButton(self.widget_2)
        self.pushButton_select_file.setObjectName(u"pushButton_select_file")

        self.horizontalLayout.addWidget(self.pushButton_select_file)

        self.pushButton_Detect = QPushButton(self.widget_2)
        self.pushButton_Detect.setObjectName(u"pushButton_Detect")

        self.horizontalLayout.addWidget(self.pushButton_Detect)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.verticalLayout.addLayout(self.verticalLayout_3)


        self.gridLayout.addWidget(self.groupBox_3, 1, 2, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1312, 22))
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
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Class Statistics", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Stone", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fallen Tree", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Road Collapse", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Landslide", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Save Data", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Display", None))
        self.label_display.setText("")
        self.radioButton_video_mode.setText(QCoreApplication.translate("MainWindow", u"video", None))
        self.radioButton_image_mode.setText(QCoreApplication.translate("MainWindow", u"image", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton_select_file.setText(QCoreApplication.translate("MainWindow", u"Select file", None))
        self.pushButton_Detect.setText(QCoreApplication.translate("MainWindow", u"Detect", None))
        self.menuhi.setTitle(QCoreApplication.translate("MainWindow", u"Yolo Detect", None))
    # retranslateUi

