# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testerNlyrr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

#import PyQt5.Qt
from PyQt5 import Qt
from PyQt5.QtCore import QSize, QCoreApplication, QMetaObject
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QFrame, QVBoxLayout, QLabel, QSizePolicy, QPushButton, QGridLayout, \
        QStackedWidget, QApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1315, 681)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamily(u"Verdana")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"background-color: rgb(33, 43, 51);\n"
"}\n"
"\n"
"#left_menu_widget{\n"
"background-color: rgba(61, 80, 95, 100);\n"
"}\n"
"\n"
"#header_frame, #frame_3, #frame_5{\n"
"background-color: rgb(61, 80, 95);\n"
"}\n"
"\n"
"#frame_4 QPushButton{\n"
"background-color: rgba(33, 43, 51, 100);\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"#header_nav QPushButton{\n"
"background-color: rgb(61, 80, 95);\n"
"border-radius: 15px;\n"
"border: 3px solid rgb(120, 157, 186)\n"
"}\n"
"\n"
"#header_nav QPushButton:hover{\n"
"	background-color: rgb(120, 157, 186);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_widget = QFrame(self.centralwidget)
        self.left_menu_widget.setObjectName(u"left_menu_widget")
        self.left_menu_widget.setFrameShape(QFrame.StyledPanel)
        self.left_menu_widget.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_menu_widget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 0, 0, 0)
        self.frame_3 = QFrame(self.left_menu_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u"Icons/zap.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Verdana")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setScaledContents(False)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame_3, 0, PyQt5.Qt.AlignTop)

        self.frame_4 = QFrame(self.left_menu_widget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(250, 0))
        font2 = QFont()
        font2.setFamily(u"Verdana")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton.setFont(font2)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setFocusPolicy(Qt.StrongFocus)
        self.pushButton.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"Icons/bar-chart-2_disabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(False)

        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignLeft)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(250, 0))
        self.pushButton_4.setMaximumSize(QSize(250, 16777215))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton_4.setFont(font3)
        icon1 = QIcon()
        icon1.addFile(u"Icons/dollar-sign_disabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.pushButton_4, 0, Qt.AlignLeft)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(250, 0))
        self.pushButton_2.setMaximumSize(QSize(250, 16777215))
        self.pushButton_2.setFont(font3)
        icon2 = QIcon()
        icon2.addFile(u"Icons/percent_disabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.pushButton_2, 0, Qt.AlignLeft)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(250, 0))
        self.pushButton_3.setFont(font3)
        icon3 = QIcon()
        icon3.addFile(u"Icons/pie-chart_focus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.pushButton_3, 0, Qt.AlignLeft)

        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(250, 0))
        self.pushButton_5.setFont(font2)

        self.verticalLayout_2.addWidget(self.pushButton_5, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.left_menu_widget)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(40, 40))
        self.label_3.setMaximumSize(QSize(40, 40))
        self.label_3.setPixmap(QPixmap(u"Icons/meh.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setFamily(u"Verdana")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_4.setFont(font4)
        self.label_4.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.frame_5, 0, Qt.AlignBottom)

        self.frame_6 = QFrame(self.left_menu_widget)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(30, 30))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        font5.setPointSize(10)
        self.label_5.setFont(font5)
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5.setWordWrap(False)

        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        font6 = QFont()
        font6.setFamily(u"MS Shell Dlg 2")
        font6.setPointSize(10)
        font6.setItalic(False)
        self.label_7.setFont(font6)
        self.label_7.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font5)
        self.label_6.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_6, 1, 1, 1, 1)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(30, 30))
        self.label_12.setMaximumSize(QSize(30, 30))
        self.label_12.setPixmap(QPixmap(u"Icons/mail.png"))
        self.label_12.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)

        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(30, 30))
        self.label_13.setMaximumSize(QSize(30, 30))
        self.label_13.setPixmap(QPixmap(u"Icons/instagram.png"))
        self.label_13.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(30, 30))
        self.label_14.setMaximumSize(QSize(30, 30))
        self.label_14.setPixmap(QPixmap(u"Icons/phone.png"))
        self.label_14.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.left_menu_widget)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.frame_2)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 6)
        self.MENU = QFrame(self.header_frame)
        self.MENU.setObjectName(u"MENU")
        self.MENU.setMinimumSize(QSize(200, 0))
        self.MENU.setMaximumSize(QSize(106, 50))
        self.MENU.setStyleSheet(u"#MENU QPushButton{\n"
"padding: 10px;\n"
"border-radius: 15px;\n"
"border: 3px solid rgb(120, 157, 186);\n"
"}\n"
"\n"
"#MENU QPushButton:hover{\n"
"	background-color: rgb(120, 157, 186);\n"
"}")
        self.MENU.setFrameShape(QFrame.StyledPanel)
        self.MENU.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.MENU)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.MENU)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setMinimumSize(QSize(40, 40))
        self.pushButton_6.setMaximumSize(QSize(40, 40))
        icon4 = QIcon()
        icon4.addFile(u"Icons/menu_disabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.pushButton_6)

        self.label_8 = QLabel(self.MENU)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 40))
        self.label_8.setMaximumSize(QSize(40, 40))
        font7 = QFont()
        font7.setFamily(u"Verdana")
        font7.setPointSize(12)
        font7.setBold(False)
        font7.setWeight(50)
        self.label_8.setFont(font7)
        self.label_8.setToolTipDuration(0)
        self.label_8.setScaledContents(False)
        self.label_8.setIndent(-1)

        self.horizontalLayout_7.addWidget(self.label_8, 0, Qt.AlignVCenter)


        self.horizontalLayout_4.addWidget(self.MENU, 0, Qt.AlignLeft)

        self.frame_11 = QFrame(self.header_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_9, 0, Qt.AlignHCenter)


        self.horizontalLayout_4.addWidget(self.frame_11)

        self.header_nav = QFrame(self.header_frame)
        self.header_nav.setObjectName(u"header_nav")
        self.header_nav.setStyleSheet(u"")
        self.header_nav.setFrameShape(QFrame.StyledPanel)
        self.header_nav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.header_nav)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.header_nav)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(40, 40))
        self.pushButton_8.setMaximumSize(QSize(40, 40))
        icon5 = QIcon()
        icon5.addFile(u"Icons/minus_disabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon5)
        self.pushButton_8.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.header_nav)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(40, 40))
        self.pushButton_7.setMaximumSize(QSize(40, 40))
        icon6 = QIcon()
        icon6.addFile(u"Icons/maximize-2_disabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_9 = QPushButton(self.header_nav)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(40, 40))
        self.pushButton_9.setMaximumSize(QSize(40, 40))
        icon7 = QIcon()
        icon7.addFile(u"Icons/x_disabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.pushButton_9)


        self.horizontalLayout_4.addWidget(self.header_nav, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.frame_8)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_14 = QFrame(self.page)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_14)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_11, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.frame_14, 0, Qt.AlignTop)

        self.frame_15 = QFrame(self.page)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_15)
        self.gridLayout.setObjectName(u"gridLayout")

        self.verticalLayout_7.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.footer_frame = QFrame(self.frame_2)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.footer_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_5.addWidget(self.label_10)


        self.horizontalLayout_6.addWidget(self.frame_10, 0, Qt.AlignBottom)

        self.frame_13 = QFrame(self.footer_frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_13)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.SIZE_GRIP = QFrame(self.frame_13)
        self.SIZE_GRIP.setObjectName(u"SIZE_GRIP")
        self.SIZE_GRIP.setFrameShape(QFrame.StyledPanel)
        self.SIZE_GRIP.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.SIZE_GRIP)


        self.horizontalLayout_6.addWidget(self.frame_13, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_4.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DEMANDA OTIMA", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Registrar Hist\u00f3rico", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Registrar Tarifas", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Compara\u00e7\u00e3o de economia", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1ficos", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"SUPPORT ME", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"INSTAGRAM", None))
        self.label_12.setText("")
        self.label_13.setText("")
        self.label_14.setText("")
        self.pushButton_6.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"DEMANDA \u00d3TIMA", None))
        self.pushButton_8.setText("")
        self.pushButton_7.setText("")
        self.pushButton_9.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"REGISTRE SEU HIST\u00d3RICO DE DEMANDA/CONSUMO", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"COPYRIGHT SPINN CO. V. 1.0", None))
    # retranslateUi



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_window = Ui_MainWindow()
    ui_window.show()
    sys.exit(app.exec_())
