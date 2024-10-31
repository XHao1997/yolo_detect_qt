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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLCDNumber, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1131, 730)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setKerning(True)
        self.groupBox.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalWidget = QWidget(self.groupBox)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy2)
        self.formLayout = QFormLayout(self.horizontalWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.horizontalWidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setUnderline(False)
        font1.setKerning(True)
        self.label_3.setFont(font1)

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.lcdNumber_stone = QLCDNumber(self.horizontalWidget)
        self.lcdNumber_stone.setObjectName(u"lcdNumber_stone")
        self.lcdNumber_stone.setMinimumSize(QSize(80, 0))
        self.lcdNumber_stone.setMaximumSize(QSize(50, 20))
        font2 = QFont()
        font2.setFamilies([u"Ubuntu"])
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(True)
        font2.setKerning(True)
        self.lcdNumber_stone.setFont(font2)
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

        self.lcdNumber_landslide = QLCDNumber(self.horizontalWidget)
        self.lcdNumber_landslide.setObjectName(u"lcdNumber_landslide")
        self.lcdNumber_landslide.setMinimumSize(QSize(80, 0))
        self.lcdNumber_landslide.setMaximumSize(QSize(50, 20))
        self.lcdNumber_landslide.setFont(font2)
#if QT_CONFIG(accessibility)
        self.lcdNumber_landslide.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.lcdNumber_landslide.setAutoFillBackground(True)
        self.lcdNumber_landslide.setFrameShadow(QFrame.Shadow.Plain)
        self.lcdNumber_landslide.setLineWidth(1)
        self.lcdNumber_landslide.setMidLineWidth(1)
        self.lcdNumber_landslide.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_landslide, 3, 1, 1, 1)

        self.label = QLabel(self.horizontalWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_4 = QLabel(self.horizontalWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.horizontalWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.lcdNumber_fallentree = QLCDNumber(self.horizontalWidget)
        self.lcdNumber_fallentree.setObjectName(u"lcdNumber_fallentree")
        self.lcdNumber_fallentree.setMinimumSize(QSize(80, 0))
        self.lcdNumber_fallentree.setMaximumSize(QSize(50, 20))
        self.lcdNumber_fallentree.setFont(font2)
#if QT_CONFIG(accessibility)
        self.lcdNumber_fallentree.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.lcdNumber_fallentree.setAutoFillBackground(True)
        self.lcdNumber_fallentree.setFrameShadow(QFrame.Shadow.Plain)
        self.lcdNumber_fallentree.setLineWidth(1)
        self.lcdNumber_fallentree.setMidLineWidth(1)
        self.lcdNumber_fallentree.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_fallentree, 1, 1, 1, 1)

        self.lcdNumber_roadcollapse = QLCDNumber(self.horizontalWidget)
        self.lcdNumber_roadcollapse.setObjectName(u"lcdNumber_roadcollapse")
        self.lcdNumber_roadcollapse.setMinimumSize(QSize(80, 0))
        self.lcdNumber_roadcollapse.setMaximumSize(QSize(50, 20))
        self.lcdNumber_roadcollapse.setFont(font2)
#if QT_CONFIG(accessibility)
        self.lcdNumber_roadcollapse.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.lcdNumber_roadcollapse.setAutoFillBackground(True)
        self.lcdNumber_roadcollapse.setFrameShadow(QFrame.Shadow.Plain)
        self.lcdNumber_roadcollapse.setLineWidth(1)
        self.lcdNumber_roadcollapse.setMidLineWidth(1)
        self.lcdNumber_roadcollapse.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.gridLayout_2.addWidget(self.lcdNumber_roadcollapse, 2, 1, 1, 1)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.gridLayout_2)


        self.verticalLayout_2.addWidget(self.horizontalWidget)


        self.gridLayout.addWidget(self.groupBox, 2, 3, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(True)
        font3.setKerning(True)
        font3.setHintingPreference(QFont.PreferDefaultHinting)
        self.groupBox_3.setFont(font3)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_display.sizePolicy().hasHeightForWidth())
        self.label_display.setSizePolicy(sizePolicy4)

        self.verticalLayout_3.addWidget(self.label_display)

        self.widget_2 = QWidget(self.groupBox_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy5)
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_video_mode = QRadioButton(self.widget_2)
        self.radioButton_video_mode.setObjectName(u"radioButton_video_mode")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setKerning(True)
        font4.setHintingPreference(QFont.PreferDefaultHinting)
        self.radioButton_video_mode.setFont(font4)

        self.horizontalLayout.addWidget(self.radioButton_video_mode)

        self.radioButton_image_mode = QRadioButton(self.widget_2)
        self.radioButton_image_mode.setObjectName(u"radioButton_image_mode")
        self.radioButton_image_mode.setFont(font4)

        self.horizontalLayout.addWidget(self.radioButton_image_mode)

        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font4)

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_stop = QPushButton(self.widget_2)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setFont(font4)

        self.horizontalLayout.addWidget(self.pushButton_stop)

        self.pushButton_select_file = QPushButton(self.widget_2)
        self.pushButton_select_file.setObjectName(u"pushButton_select_file")
        self.pushButton_select_file.setFont(font4)

        self.horizontalLayout.addWidget(self.pushButton_select_file)

        self.pushButton_Detect = QPushButton(self.widget_2)
        self.pushButton_Detect.setObjectName(u"pushButton_Detect")
        self.pushButton_Detect.setFont(font4)

        self.horizontalLayout.addWidget(self.pushButton_Detect)


        self.verticalLayout_3.addWidget(self.widget_2)


        self._2.addLayout(self.verticalLayout_3)


        self.gridLayout.addWidget(self.groupBox_3, 1, 2, 2, 1)

        self.horizontalWidget1 = QWidget(self.centralwidget)
        self.horizontalWidget1.setObjectName(u"horizontalWidget1")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.horizontalWidget1.sizePolicy().hasHeightForWidth())
        self.horizontalWidget1.setSizePolicy(sizePolicy6)
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(250, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.horizontalWidget1)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(60, 60))
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)
        self.label_2.setPixmap(QPixmap(u"images.jpeg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_6 = QLabel(self.horizontalWidget1)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setPointSize(20)
        font5.setBold(True)
        self.label_6.setFont(font5)

        self.horizontalLayout_2.addWidget(self.label_6)


        self.gridLayout.addWidget(self.horizontalWidget1, 0, 1, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1131, 27))
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
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u7edf\u8ba1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8def\u9762\u574d\u584c", None))
        self.lcdNumber_landslide.setStyleSheet(QCoreApplication.translate("MainWindow", u"font: 700 20pt \"Ubuntu\";", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u843d\u6728", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5de8\u77f3", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6ed1\u5761", None))
        self.lcdNumber_fallentree.setStyleSheet(QCoreApplication.translate("MainWindow", u"font: 700 20pt \"Ubuntu\";", None))
        self.lcdNumber_roadcollapse.setStyleSheet(QCoreApplication.translate("MainWindow", u"font: 700 20pt \"Ubuntu\";", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u663e\u793a", None))
        self.label_display.setText("")
        self.radioButton_video_mode.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891", None))
        self.radioButton_image_mode.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6570\u636e", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.pushButton_select_file.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u76ee\u5f55", None))
        self.pushButton_Detect.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b", None))
        self.label_2.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"    \u516c\u8def\u57fa\u7840\u8bbe\u65bd\u707e\u635f\u68c0\u6d4b\u5e73\u53f0", None))
        self.menuhi.setTitle(QCoreApplication.translate("MainWindow", u"\u707e\u635f\u68c0\u6d4b", None))
    # retranslateUi

