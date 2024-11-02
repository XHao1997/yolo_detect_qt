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
    QListView, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStatusBar, QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1268, 785)
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
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setUnderline(False)
        self.label_6.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout_3.addWidget(self.horizontalFrame, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.horizontalWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(True)
        font2.setKerning(True)
        font2.setHintingPreference(QFont.PreferDefaultHinting)
        self.groupBox_3.setFont(font2)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(2)
        sizePolicy3.setHeightForWidth(self.label_display.sizePolicy().hasHeightForWidth())
        self.label_display.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.label_display)

        self.widget_2 = QWidget(self.groupBox_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy4)
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_video_mode = QRadioButton(self.widget_2)
        self.radioButton_video_mode.setObjectName(u"radioButton_video_mode")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setKerning(True)
        font3.setHintingPreference(QFont.PreferDefaultHinting)
        self.radioButton_video_mode.setFont(font3)

        self.horizontalLayout.addWidget(self.radioButton_video_mode)

        self.radioButton_image_mode = QRadioButton(self.widget_2)
        self.radioButton_image_mode.setObjectName(u"radioButton_image_mode")
        self.radioButton_image_mode.setFont(font3)

        self.horizontalLayout.addWidget(self.radioButton_image_mode)

        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font3)

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_stop = QPushButton(self.widget_2)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setFont(font3)

        self.horizontalLayout.addWidget(self.pushButton_stop)

        self.pushButton_select_file = QPushButton(self.widget_2)
        self.pushButton_select_file.setObjectName(u"pushButton_select_file")
        self.pushButton_select_file.setFont(font3)

        self.horizontalLayout.addWidget(self.pushButton_select_file)

        self.pushButton_Detect = QPushButton(self.widget_2)
        self.pushButton_Detect.setObjectName(u"pushButton_Detect")
        self.pushButton_Detect.setFont(font3)

        self.horizontalLayout.addWidget(self.pushButton_Detect)


        self.verticalLayout_3.addWidget(self.widget_2)


        self._2.addLayout(self.verticalLayout_3)


        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.horizontalWidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy5)
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        font4.setUnderline(True)
        font4.setKerning(True)
        self.groupBox.setFont(font4)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy6)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy7)
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setUnderline(True)
        font5.setKerning(True)
        self.label_7.setFont(font5)

        self.verticalLayout.addWidget(self.label_7)

        self.listView = QListView(self.widget)
        self.listView.setObjectName(u"listView")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy8)
        self.listView.setMinimumSize(QSize(120, 100))
        self.listView.setMaximumSize(QSize(197, 600))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setUnderline(True)
        font6.setKerning(True)
        font6.setHintingPreference(QFont.PreferDefaultHinting)
        self.listView.setFont(font6)

        self.verticalLayout.addWidget(self.listView)


        self.verticalLayout_2.addWidget(self.widget)

        self.horizontalWidget1 = QWidget(self.groupBox)
        self.horizontalWidget1.setObjectName(u"horizontalWidget1")
        sizePolicy7.setHeightForWidth(self.horizontalWidget1.sizePolicy().hasHeightForWidth())
        self.horizontalWidget1.setSizePolicy(sizePolicy7)
        self.formLayout = QFormLayout(self.horizontalWidget1)
        self.formLayout.setObjectName(u"formLayout")
        self.toolBox = QToolBox(self.horizontalWidget1)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setFrameShadow(QFrame.Shadow.Plain)
        self.widget1 = QWidget()
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 0, 184, 152))
        self.gridLayout_2 = QGridLayout(self.widget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lcdNumber_landslide = QLCDNumber(self.widget1)
        self.lcdNumber_landslide.setObjectName(u"lcdNumber_landslide")
        self.lcdNumber_landslide.setMinimumSize(QSize(80, 0))
        self.lcdNumber_landslide.setMaximumSize(QSize(50, 20))
        font7 = QFont()
        font7.setFamilies([u"Ubuntu"])
        font7.setPointSize(20)
        font7.setBold(True)
        font7.setItalic(False)
        font7.setUnderline(True)
        font7.setKerning(True)
        self.lcdNumber_landslide.setFont(font7)
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
        self.lcdNumber_stone.setFont(font7)
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
        self.lcdNumber_fallentree.setFont(font7)
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
        font8 = QFont()
        font8.setPointSize(15)
        font8.setBold(False)
        font8.setUnderline(False)
        font8.setKerning(True)
        self.label.setFont(font8)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font8)

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font8)

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.lcdNumber_roadcollapse = QLCDNumber(self.widget1)
        self.lcdNumber_roadcollapse.setObjectName(u"lcdNumber_roadcollapse")
        self.lcdNumber_roadcollapse.setMinimumSize(QSize(80, 0))
        self.lcdNumber_roadcollapse.setMaximumSize(QSize(50, 20))
        self.lcdNumber_roadcollapse.setFont(font7)
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
        self.label_4.setFont(font8)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.toolBox.addItem(self.widget1, u"\u5206\u7c7b\u7edf\u8ba1")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.toolBox)


        self.verticalLayout_2.addWidget(self.horizontalWidget1)


        self.gridLayout_3.addWidget(self.groupBox, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.horizontalWidget, 0, 1, 3, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1268, 27))
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
        MainWindow.setWindowTitle("")
        self.label_2.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"    \u516c\u8def\u57fa\u7840\u8bbe\u65bd\u707e\u635f\u68c0\u6d4b\u5e73\u53f0", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u663e\u793a", None))
        self.label_display.setText("")
        self.radioButton_video_mode.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891", None))
        self.radioButton_image_mode.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6570\u636e", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.pushButton_select_file.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u76ee\u5f55", None))
        self.pushButton_Detect.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u7edf\u8ba1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d", None))
        self.lcdNumber_landslide.setStyleSheet(QCoreApplication.translate("MainWindow", u"font: 700 20pt \"Ubuntu\";", None))
        self.lcdNumber_fallentree.setStyleSheet(QCoreApplication.translate("MainWindow", u"font: 700 20pt \"Ubuntu\";", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u843d\u6728", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8def\u9762\u574d\u584c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6ed1\u5761", None))
        self.lcdNumber_roadcollapse.setStyleSheet(QCoreApplication.translate("MainWindow", u"font: 700 20pt \"Ubuntu\";", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5de8\u77f3", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.widget1), QCoreApplication.translate("MainWindow", u"\u5206\u7c7b\u7edf\u8ba1", None))
        self.menuhi.setTitle(QCoreApplication.translate("MainWindow", u"\u707e\u635f\u68c0\u6d4b", None))
    # retranslateUi

