# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGraphicsView, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1309, 518)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 2, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.pushButton_addItem = QPushButton(self.widget)
        self.pushButton_addItem.setObjectName(u"pushButton_addItem")
        sizePolicy.setHeightForWidth(self.pushButton_addItem.sizePolicy().hasHeightForWidth())
        self.pushButton_addItem.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.pushButton_addItem)

        self.pushButton_deleteItem = QPushButton(self.widget)
        self.pushButton_deleteItem.setObjectName(u"pushButton_deleteItem")

        self.verticalLayout_2.addWidget(self.pushButton_deleteItem)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.widget)

        self.listWidget = QListWidget(self.groupBox)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.listWidget)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 2, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMaximumSize(QSize(60, 60))
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)
        self.label_2.setPixmap(QPixmap(u"images.jpeg"))
        self.label_2.setScaledContents(True)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout = QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.graphicsView = QGraphicsView(self.groupBox_4)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy1.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.graphicsView)

        self.checkBox_1 = QWidget(self.groupBox_4)
        self.checkBox_1.setObjectName(u"checkBox_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.checkBox_1.sizePolicy().hasHeightForWidth())
        self.checkBox_1.setSizePolicy(sizePolicy2)
        self.checkBox_1.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_3 = QHBoxLayout(self.checkBox_1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 1)
        self.checkButton_image = QRadioButton(self.checkBox_1)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.checkButton_image)
        self.checkButton_image.setObjectName(u"checkButton_image")
        self.checkButton_image.setIconSize(QSize(8, 8))
        self.checkButton_image.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkButton_image)

        self.checkButton_video = QRadioButton(self.checkBox_1)
        self.buttonGroup.addButton(self.checkButton_video)
        self.checkButton_video.setObjectName(u"checkButton_video")
        self.checkButton_video.setIconSize(QSize(8, 8))
        self.checkButton_video.setChecked(False)

        self.horizontalLayout_3.addWidget(self.checkButton_video)


        self.verticalLayout.addWidget(self.checkBox_1)

        self.pushButton_loadImage = QPushButton(self.groupBox_4)
        self.pushButton_loadImage.setObjectName(u"pushButton_loadImage")

        self.verticalLayout.addWidget(self.pushButton_loadImage)


        self.gridLayout.addWidget(self.groupBox_4, 1, 2, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1309, 22))
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
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Display", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Class Statistics", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"item", None))
        self.pushButton_addItem.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.pushButton_deleteItem.setText(QCoreApplication.translate("MainWindow", u"Delete Item", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"landslide", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"road collapse", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"fallen tree", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"rock", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_2.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.checkButton_image.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.checkButton_video.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.pushButton_loadImage.setText(QCoreApplication.translate("MainWindow", u"Choose Image File", None))
        self.menuhi.setTitle(QCoreApplication.translate("MainWindow", u"Yolo Detect", None))
    # retranslateUi

