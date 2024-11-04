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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLCDNumber, QLabel,
    QListView, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1268, 806)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setUnderline(False)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalWidget = QWidget(self.centralwidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy1)
        self.gridLayout_3 = QGridLayout(self.horizontalWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalFrame = QFrame(self.horizontalWidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.horizontalFrame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(60, 60))
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)
        self.label_2.setPixmap(QPixmap(u"images.jpeg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_6 = QLabel(self.horizontalFrame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setUnderline(False)
        self.label_6.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout_3.addWidget(self.horizontalFrame, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.horizontalWidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setUnderline(False)
        font2.setKerning(True)
        self.groupBox.setFont(font2)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setUnderline(True)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        self.label_7.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_7)

        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listView = QListView(self.widget)
        self.listView.setObjectName(u"listView")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy5)
        self.listView.setMinimumSize(QSize(250, 100))
        self.listView.setMaximumSize(QSize(600, 600))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(True)
        font4.setKerning(True)
        font4.setHintingPreference(QFont.PreferDefaultHinting)
        self.listView.setFont(font4)

        self.verticalLayout.addWidget(self.listView)


        self.verticalLayout_2.addWidget(self.widget)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_8)

        self.horizontalWidget1 = QWidget(self.groupBox)
        self.horizontalWidget1.setObjectName(u"horizontalWidget1")
        sizePolicy3.setHeightForWidth(self.horizontalWidget1.sizePolicy().hasHeightForWidth())
        self.horizontalWidget1.setSizePolicy(sizePolicy3)
        self.formLayout = QFormLayout(self.horizontalWidget1)
        self.formLayout.setObjectName(u"formLayout")
        self.widget1 = QWidget(self.horizontalWidget1)
        self.widget1.setObjectName(u"widget1")
        self.gridLayout_2 = QGridLayout(self.widget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lcdNumber_landslide = QLCDNumber(self.widget1)
        self.lcdNumber_landslide.setObjectName(u"lcdNumber_landslide")
        self.lcdNumber_landslide.setMinimumSize(QSize(80, 0))
        self.lcdNumber_landslide.setMaximumSize(QSize(50, 20))
        font5 = QFont()
        font5.setFamilies([u"Ubuntu"])
        font5.setPointSize(20)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(True)
        font5.setKerning(True)
        self.lcdNumber_landslide.setFont(font5)
#if QT_CONFIG(accessibility)
        self.lcdNumber_landslide.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.lcdNumber_landslide.setAutoFillBackground(True)
        self.lcdNumber_landslide.setFrameShadow(QFrame.Shadow.Plain)
        self.lcdNumber_landslide.setLineWidth(1)
        self.lcdNumber_landslide.setMidLineWidth(1)
        self.lcdNumber_landslide.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_landslide, 3, 1, 1, 1)

        self.lcdNumber_stone = QLCDNumber(self.widget1)
        self.lcdNumber_stone.setObjectName(u"lcdNumber_stone")
        self.lcdNumber_stone.setMinimumSize(QSize(80, 0))
        self.lcdNumber_stone.setMaximumSize(QSize(50, 20))
        self.lcdNumber_stone.setFont(font5)
#if QT_CONFIG(accessibility)
        self.lcdNumber_stone.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.lcdNumber_stone.setAutoFillBackground(True)
        self.lcdNumber_stone.setStyleSheet(u"font: 700 20pt \"Ubuntu\";")
        self.lcdNumber_stone.setFrameShadow(QFrame.Shadow.Plain)
        self.lcdNumber_stone.setLineWidth(1)
        self.lcdNumber_stone.setMidLineWidth(1)
        self.lcdNumber_stone.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_stone, 0, 1, 1, 1)

        self.lcdNumber_fallentree = QLCDNumber(self.widget1)
        self.lcdNumber_fallentree.setObjectName(u"lcdNumber_fallentree")
        self.lcdNumber_fallentree.setMinimumSize(QSize(80, 0))
        self.lcdNumber_fallentree.setMaximumSize(QSize(50, 20))
        self.lcdNumber_fallentree.setFont(font5)
#if QT_CONFIG(accessibility)
        self.lcdNumber_fallentree.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.lcdNumber_fallentree.setAutoFillBackground(True)
        self.lcdNumber_fallentree.setFrameShadow(QFrame.Shadow.Plain)
        self.lcdNumber_fallentree.setLineWidth(1)
        self.lcdNumber_fallentree.setMidLineWidth(1)
        self.lcdNumber_fallentree.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_fallentree, 1, 1, 1, 1)

        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setUnderline(False)
        font6.setKerning(True)
        self.label.setFont(font6)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font6)

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font6)

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.lcdNumber_roadcollapse = QLCDNumber(self.widget1)
        self.lcdNumber_roadcollapse.setObjectName(u"lcdNumber_roadcollapse")
        self.lcdNumber_roadcollapse.setMinimumSize(QSize(80, 0))
        self.lcdNumber_roadcollapse.setMaximumSize(QSize(50, 20))
        self.lcdNumber_roadcollapse.setFont(font5)
#if QT_CONFIG(accessibility)
        self.lcdNumber_roadcollapse.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.lcdNumber_roadcollapse.setAutoFillBackground(True)
        self.lcdNumber_roadcollapse.setFrameShadow(QFrame.Shadow.Plain)
        self.lcdNumber_roadcollapse.setLineWidth(1)
        self.lcdNumber_roadcollapse.setMidLineWidth(1)
        self.lcdNumber_roadcollapse.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_roadcollapse, 2, 1, 1, 1)

        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font6)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)


        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.widget1)


        self.verticalLayout_2.addWidget(self.horizontalWidget1)


        self.gridLayout_3.addWidget(self.groupBox, 1, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.horizontalWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy6)
        font7 = QFont()
        font7.setPointSize(15)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setUnderline(False)
        font7.setKerning(True)
        font7.setHintingPreference(QFont.PreferDefaultHinting)
        self.groupBox_3.setFont(font7)
        self.groupBox_3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.groupBox_3.setFlat(False)
        self._2 = QVBoxLayout(self.groupBox_3)
        self._2.setObjectName(u"_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_display = QLabel(self.groupBox_3)
        self.label_display.setObjectName(u"label_display")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(2)
        sizePolicy7.setVerticalStretch(2)
        sizePolicy7.setHeightForWidth(self.label_display.sizePolicy().hasHeightForWidth())
        self.label_display.setSizePolicy(sizePolicy7)

        self.verticalLayout_3.addWidget(self.label_display)

        self.widget_2 = QWidget(self.groupBox_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy8)
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalFrame = QFrame(self.widget_2)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout_5 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.radioButton_video_mode = QRadioButton(self.verticalFrame)
        self.radioButton_video_mode.setObjectName(u"radioButton_video_mode")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.radioButton_video_mode.sizePolicy().hasHeightForWidth())
        self.radioButton_video_mode.setSizePolicy(sizePolicy9)
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setUnderline(False)
        font8.setKerning(True)
        font8.setHintingPreference(QFont.PreferDefaultHinting)
        self.radioButton_video_mode.setFont(font8)
        self.radioButton_video_mode.setChecked(True)

        self.verticalLayout_5.addWidget(self.radioButton_video_mode)

        self.radioButton_image_mode = QRadioButton(self.verticalFrame)
        self.radioButton_image_mode.setObjectName(u"radioButton_image_mode")
        sizePolicy9.setHeightForWidth(self.radioButton_image_mode.sizePolicy().hasHeightForWidth())
        self.radioButton_image_mode.setSizePolicy(sizePolicy9)
        self.radioButton_image_mode.setFont(font8)

        self.verticalLayout_5.addWidget(self.radioButton_image_mode)


        self.horizontalLayout.addWidget(self.verticalFrame)

        self.formFrame = QFrame(self.widget_2)
        self.formFrame.setObjectName(u"formFrame")
        self.gridLayout_4 = QGridLayout(self.formFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_4 = QPushButton(self.formFrame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy10)
        self.pushButton_4.setMinimumSize(QSize(180, 0))
        self.pushButton_4.setFont(font8)

        self.gridLayout_4.addWidget(self.pushButton_4, 4, 1, 1, 1)

        self.pushButton_Detect = QPushButton(self.formFrame)
        self.pushButton_Detect.setObjectName(u"pushButton_Detect")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.pushButton_Detect.sizePolicy().hasHeightForWidth())
        self.pushButton_Detect.setSizePolicy(sizePolicy11)
        self.pushButton_Detect.setMinimumSize(QSize(180, 0))
        self.pushButton_Detect.setFont(font8)

        self.gridLayout_4.addWidget(self.pushButton_Detect, 1, 0, 1, 1)

        self.pushButton_select_file = QPushButton(self.formFrame)
        self.pushButton_select_file.setObjectName(u"pushButton_select_file")
        sizePolicy10.setHeightForWidth(self.pushButton_select_file.sizePolicy().hasHeightForWidth())
        self.pushButton_select_file.setSizePolicy(sizePolicy10)
        self.pushButton_select_file.setMinimumSize(QSize(180, 0))
        self.pushButton_select_file.setFont(font8)

        self.gridLayout_4.addWidget(self.pushButton_select_file, 1, 1, 1, 1)

        self.pushButton_reformat = QPushButton(self.formFrame)
        self.pushButton_reformat.setObjectName(u"pushButton_reformat")
        self.pushButton_reformat.setFont(font8)

        self.gridLayout_4.addWidget(self.pushButton_reformat, 3, 1, 1, 1)

        self.pushButton = QPushButton(self.formFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font8)

        self.gridLayout_4.addWidget(self.pushButton, 4, 0, 1, 1)

        self.pushButton_stop = QPushButton(self.formFrame)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        sizePolicy11.setHeightForWidth(self.pushButton_stop.sizePolicy().hasHeightForWidth())
        self.pushButton_stop.setSizePolicy(sizePolicy11)
        self.pushButton_stop.setMinimumSize(QSize(180, 0))
        self.pushButton_stop.setFont(font8)

        self.gridLayout_4.addWidget(self.pushButton_stop, 3, 0, 1, 1)


        self.horizontalLayout.addWidget(self.formFrame)


        self.verticalLayout_3.addWidget(self.widget_2)


        self._2.addLayout(self.verticalLayout_3)


        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.horizontalWidget, 0, 1, 3, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.label_2.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Traffic Disaster Detection Platform", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Filename", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Object Count", None))
        self.lcdNumber_landslide.setStyleSheet(QCoreApplication.translate("MainWindow", u"font: 700 20pt \"Ubuntu\";", None))
        self.lcdNumber_fallentree.setStyleSheet(QCoreApplication.translate("MainWindow", u"font: 700 20pt \"Ubuntu\";", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fallen Tree", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Road Collapse", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Landslide", None))
        self.lcdNumber_roadcollapse.setStyleSheet(QCoreApplication.translate("MainWindow", u"font: 700 20pt \"Ubuntu\";", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Rock", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Display", None))
        self.label_display.setText("")
        self.radioButton_video_mode.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.radioButton_image_mode.setText(QCoreApplication.translate("MainWindow", u"Figure", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Save Data", None))
        self.pushButton_Detect.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.pushButton_select_file.setText(QCoreApplication.translate("MainWindow", u"Choose Directory", None))
        self.pushButton_reformat.setText(QCoreApplication.translate("MainWindow", u"Format Filename", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Detect", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
    # retranslateUi

