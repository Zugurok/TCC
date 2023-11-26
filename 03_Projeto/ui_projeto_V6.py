# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Projeto_V6inAdBm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1870, 782)
        MainWindow.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u"../../../../../.designer/backup/Icons/sliders.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
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
"color: silver;\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"text-align:left;\n"
"}\n"
"\n"
"#frame_4 QPushButton:hover {\n"
"	background-color: rgb(138, 203, 250);\n"
"    color: white;\n"
"}\n"
"\n"
"#frame_4 QPushButton:disabled\n"
"{\n"
"    background-color: #302F2F;\n"
"    padding: 10px;\n"
"    color: #808080;\n"
"}\n"
"\n"
"#frame_4 QPushButton:pressed\n"
"{\n"
"    background-color: rgb(33, 43, 51);\n"
"}\n"
"\n"
"\n"
"#header_nav QPushButton{\n"
"background-color: rgb(61, 80, 95);\n"
"border-radius: 15px;\n"
"border: 3px solid rgb(120, 157, 186)\n"
"}\n"
"\n"
"#header_nav QPushButton:hover{\n"
"	background-color: rgb(120, 157, 186);\n"
"}\n"
"\n"
"\n"
"#frame_6 QLabel {\n"
"    \n"
"	color: #3d8"
                        "ec9;\n"
"	font: 77 14px \"Verdana\";\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_widget = QFrame(self.centralwidget)
        self.left_menu_widget.setObjectName(u"left_menu_widget")
        self.left_menu_widget.setStyleSheet(u"")
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


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.left_menu_widget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_0 = QPushButton(self.frame_4)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setMinimumSize(QSize(250, 0))
        font2 = QFont()
        font2.setFamily(u"Verdana")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton_0.setFont(font2)
        self.pushButton_0.setMouseTracking(False)
        self.pushButton_0.setFocusPolicy(Qt.StrongFocus)
        self.pushButton_0.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.pushButton_0.setAutoFillBackground(False)
        self.pushButton_0.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"Icons/bar-chart-2_disabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_0.setIcon(icon1)
        self.pushButton_0.setAutoDefault(False)
        self.pushButton_0.setFlat(False)

        self.verticalLayout_2.addWidget(self.pushButton_0, 0, Qt.AlignLeft)

        self.pushButton_1 = QPushButton(self.frame_4)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(250, 0))
        self.pushButton_1.setMaximumSize(QSize(250, 16777215))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton_1.setFont(font3)
        icon2 = QIcon()
        icon2.addFile(u"Icons/dollar-sign_disabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_1.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.pushButton_1, 0, Qt.AlignLeft)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(250, 0))
        self.pushButton_3.setFont(font3)
        icon3 = QIcon()
        icon3.addFile(u"Icons/pie-chart_focus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.pushButton_3)


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
        self.label_3.setPixmap(QPixmap(u"Icons/smile.png"))
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
        font5.setFamily(u"Verdana")
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(9)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"")
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignLeading)
        self.label_5.setWordWrap(False)

        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)
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
        self.frame_11 = QFrame(self.header_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_4.addWidget(self.frame_11, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_9 = QLabel(self.header_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_9)

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
        icon4 = QIcon()
        icon4.addFile(u"../../../../../.designer/backup/Icons/minimize-2_disabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon4)
        self.pushButton_8.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.header_nav)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(40, 40))
        self.pushButton_7.setMaximumSize(QSize(40, 40))
        icon5 = QIcon()
        icon5.addFile(u"../../../../../.designer/backup/Icons/maximize-2_disabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon5)
        self.pushButton_7.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_9 = QPushButton(self.header_nav)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(40, 40))
        self.pushButton_9.setMaximumSize(QSize(40, 40))
        icon6 = QIcon()
        icon6.addFile(u"../../../../../.designer/backup/Icons/x_disabled.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon6)
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
        self.stackedWidget.setFont(font1)
        self.page_0_Registrar_Historico = QWidget()
        self.page_0_Registrar_Historico.setObjectName(u"page_0_Registrar_Historico")
        self.page_0_Registrar_Historico.setStyleSheet(u"QLabel {\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 14px \"Verdana\";\n"
"}\n"
"\n"
"QDoubleSpinBox\n"
"{\n"
"    selection-background-color: #302F2F;\n"
"    background-color: #201F1F;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 2px;\n"
"	color: silver;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #302F2F;\n"
"    background-color: #201F1F;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 2px;\n"
"	color: silver;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.page_0_Registrar_Historico)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.page_0_Registrar_Historico)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setEnabled(True)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_15)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame_14 = QFrame(self.frame_15)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_14.setStyleSheet(u"#frame_16, #frame_15 QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignLeft;\n"
"	color: #3d8ec9;\n"
"	font: 77 14px \"Verdana\";\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_14)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_15 = QLabel(self.frame_14)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"#frame_16, #frame_15 QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 20px \"Verdana\";\n"
"}")

        self.gridLayout_14.addWidget(self.label_15, 0, 0, 1, 4)

        self.label_60 = QLabel(self.frame_14)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setStyleSheet(u"#frame_16, #frame_15 QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 16px \"Verdana\";\n"
"}")

        self.gridLayout_14.addWidget(self.label_60, 1, 0, 1, 2)

        self.label_61 = QLabel(self.frame_14)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setStyleSheet(u"#frame_16, #frame_15 QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 16px \"Verdana\";\n"
"}")

        self.gridLayout_14.addWidget(self.label_61, 1, 2, 1, 2)

        self.label_63 = QLabel(self.frame_14)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_14.addWidget(self.label_63, 2, 0, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox, 2, 1, 1, 1)

        self.label_79 = QLabel(self.frame_14)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_14.addWidget(self.label_79, 2, 2, 1, 1)

        self.doubleSpinBox_30 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_30.setObjectName(u"doubleSpinBox_30")
        self.doubleSpinBox_30.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_30, 2, 3, 1, 1)

        self.label_64 = QLabel(self.frame_14)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_14.addWidget(self.label_64, 3, 0, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_2, 3, 1, 1, 1)

        self.label_84 = QLabel(self.frame_14)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_14.addWidget(self.label_84, 3, 2, 1, 1)

        self.doubleSpinBox_29 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_29.setObjectName(u"doubleSpinBox_29")
        self.doubleSpinBox_29.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_29, 3, 3, 1, 1)

        self.label_66 = QLabel(self.frame_14)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_14.addWidget(self.label_66, 4, 0, 1, 1)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_3, 4, 1, 1, 1)

        self.label_81 = QLabel(self.frame_14)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_14.addWidget(self.label_81, 4, 2, 1, 1)

        self.doubleSpinBox_22 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_22.setObjectName(u"doubleSpinBox_22")
        self.doubleSpinBox_22.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_22, 4, 3, 1, 1)

        self.label_65 = QLabel(self.frame_14)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_14.addWidget(self.label_65, 5, 0, 1, 1)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_4, 5, 1, 1, 1)

        self.label_86 = QLabel(self.frame_14)
        self.label_86.setObjectName(u"label_86")

        self.gridLayout_14.addWidget(self.label_86, 5, 2, 1, 1)

        self.doubleSpinBox_37 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_37.setObjectName(u"doubleSpinBox_37")
        self.doubleSpinBox_37.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_37, 5, 3, 1, 1)

        self.label_68 = QLabel(self.frame_14)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_14.addWidget(self.label_68, 6, 0, 1, 1)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_5, 6, 1, 1, 1)

        self.label_85 = QLabel(self.frame_14)
        self.label_85.setObjectName(u"label_85")

        self.gridLayout_14.addWidget(self.label_85, 6, 2, 1, 1)

        self.doubleSpinBox_34 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_34.setObjectName(u"doubleSpinBox_34")
        self.doubleSpinBox_34.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_34, 6, 3, 1, 1)

        self.label_67 = QLabel(self.frame_14)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_14.addWidget(self.label_67, 7, 0, 1, 1)

        self.doubleSpinBox_17 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_17.setObjectName(u"doubleSpinBox_17")
        self.doubleSpinBox_17.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_17, 7, 1, 1, 1)

        self.label_90 = QLabel(self.frame_14)
        self.label_90.setObjectName(u"label_90")

        self.gridLayout_14.addWidget(self.label_90, 7, 2, 1, 1)

        self.doubleSpinBox_28 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_28.setObjectName(u"doubleSpinBox_28")
        self.doubleSpinBox_28.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_28, 7, 3, 1, 1)

        self.label_74 = QLabel(self.frame_14)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_14.addWidget(self.label_74, 8, 0, 1, 1)

        self.doubleSpinBox_15 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_15.setObjectName(u"doubleSpinBox_15")
        self.doubleSpinBox_15.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_15, 8, 1, 1, 1)

        self.label_80 = QLabel(self.frame_14)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_14.addWidget(self.label_80, 8, 2, 1, 1)

        self.doubleSpinBox_36 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_36.setObjectName(u"doubleSpinBox_36")
        self.doubleSpinBox_36.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_36, 8, 3, 1, 1)

        self.label_73 = QLabel(self.frame_14)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_14.addWidget(self.label_73, 9, 0, 1, 1)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_6, 9, 1, 1, 1)

        self.label_87 = QLabel(self.frame_14)
        self.label_87.setObjectName(u"label_87")

        self.gridLayout_14.addWidget(self.label_87, 9, 2, 1, 1)

        self.doubleSpinBox_31 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_31.setObjectName(u"doubleSpinBox_31")
        self.doubleSpinBox_31.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_31, 9, 3, 1, 1)

        self.label_76 = QLabel(self.frame_14)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_14.addWidget(self.label_76, 10, 0, 1, 1)

        self.doubleSpinBox_13 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_13.setObjectName(u"doubleSpinBox_13")
        self.doubleSpinBox_13.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_13, 10, 1, 1, 1)

        self.label_88 = QLabel(self.frame_14)
        self.label_88.setObjectName(u"label_88")

        self.gridLayout_14.addWidget(self.label_88, 10, 2, 1, 1)

        self.doubleSpinBox_35 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_35.setObjectName(u"doubleSpinBox_35")
        self.doubleSpinBox_35.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_35, 10, 3, 1, 1)

        self.label_75 = QLabel(self.frame_14)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_14.addWidget(self.label_75, 11, 0, 1, 1)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")
        self.doubleSpinBox_7.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_7, 11, 1, 1, 1)

        self.label_89 = QLabel(self.frame_14)
        self.label_89.setObjectName(u"label_89")

        self.gridLayout_14.addWidget(self.label_89, 11, 2, 1, 1)

        self.doubleSpinBox_33 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_33.setObjectName(u"doubleSpinBox_33")
        self.doubleSpinBox_33.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_33, 11, 3, 1, 1)

        self.label_78 = QLabel(self.frame_14)
        self.label_78.setObjectName(u"label_78")

        self.gridLayout_14.addWidget(self.label_78, 12, 0, 1, 1)

        self.doubleSpinBox_20 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_20.setObjectName(u"doubleSpinBox_20")
        self.doubleSpinBox_20.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_20, 12, 1, 1, 1)

        self.label_83 = QLabel(self.frame_14)
        self.label_83.setObjectName(u"label_83")

        self.gridLayout_14.addWidget(self.label_83, 12, 2, 1, 1)

        self.doubleSpinBox_21 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_21.setObjectName(u"doubleSpinBox_21")
        self.doubleSpinBox_21.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_21, 12, 3, 1, 1)

        self.label_77 = QLabel(self.frame_14)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout_14.addWidget(self.label_77, 13, 0, 1, 1)

        self.doubleSpinBox_19 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_19.setObjectName(u"doubleSpinBox_19")
        self.doubleSpinBox_19.setMaximum(99999999999.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_19, 13, 1, 1, 1)

        self.label_82 = QLabel(self.frame_14)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_14.addWidget(self.label_82, 13, 2, 1, 1)

        self.doubleSpinBox_32 = QDoubleSpinBox(self.frame_14)
        self.doubleSpinBox_32.setObjectName(u"doubleSpinBox_32")
        self.doubleSpinBox_32.setWrapping(False)
        self.doubleSpinBox_32.setFrame(True)
        self.doubleSpinBox_32.setReadOnly(False)
        self.doubleSpinBox_32.setMaximum(99999999999.000000000000000)
        self.doubleSpinBox_32.setStepType(QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_32.setValue(0.000000000000000)

        self.gridLayout_14.addWidget(self.doubleSpinBox_32, 13, 3, 1, 1)


        self.gridLayout_15.addWidget(self.frame_14, 1, 0, 1, 2)

        self.frame_25 = QFrame(self.frame_15)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_25)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_11 = QLabel(self.frame_25)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"#frame_16, #frame_15 QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 20px \"Verdana\";\n"
"}")

        self.gridLayout_13.addWidget(self.label_11, 0, 0, 1, 2)

        self.label_59 = QLabel(self.frame_25)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"#frame_16, #frame_15 QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 16px \"Verdana\";\n"
"}")

        self.gridLayout_13.addWidget(self.label_59, 1, 0, 1, 1)

        self.label_44 = QLabel(self.frame_25)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"#frame_16, #frame_15 QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 16px \"Verdana\";\n"
"}")

        self.gridLayout_13.addWidget(self.label_44, 1, 1, 1, 1)

        self.comboBox = QComboBox(self.frame_25)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)

        self.gridLayout_13.addWidget(self.comboBox, 2, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.frame_25)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(4)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy2)

        self.gridLayout_13.addWidget(self.comboBox_2, 2, 1, 1, 1)


        self.gridLayout_15.addWidget(self.frame_25, 0, 0, 1, 2, Qt.AlignTop)

        self.horizontalSpacer = QSpacerItem(430, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.frame_26 = QFrame(self.frame_15)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy3)
        self.frame_26.setMinimumSize(QSize(118, 75))
        self.frame_26.setMaximumSize(QSize(200, 19))
        self.frame_26.setFont(font1)
        self.frame_26.setStyleSheet(u"")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_26)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setMaximumSize(QSize(200, 40))
        font6 = QFont()
        font6.setFamily(u"Verdana")
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(9)
        self.pushButton_5.setFont(font6)
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"/*background-color: rgba(33, 43, 51, 100);*/\n"
"	background-color: rgba(61, 80, 95, 100);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	text-align: center;\n"
"	font: 75 14pt \"Verdana\";\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #302F2F;\n"
"    /*border-width: 2px;\n"
"    border-color: #3A3939;\n"
"    border-style: solid;*/\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    /*border-radius: 2px;*/\n"
"    color: #808080;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(138, 203, 250);\n"
"    color: white;\n"
"}")

        self.horizontalLayout_7.addWidget(self.pushButton_5)


        self.gridLayout_15.addWidget(self.frame_26, 2, 1, 1, 2)

        self.frame_27 = QFrame(self.frame_15)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_27)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_46 = QLabel(self.frame_27)
        self.label_46.setObjectName(u"label_46")
        sizePolicy1.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy1)
        self.label_46.setMinimumSize(QSize(0, 0))
        self.label_46.setMaximumSize(QSize(16777215, 16777215))
        self.label_46.setStyleSheet(u"#frame_16, #frame_15 QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 20px \"Verdana\";\n"
"}")

        self.gridLayout_16.addWidget(self.label_46, 0, 0, 1, 2)

        self.label_45 = QLabel(self.frame_27)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"#frame_16, #frame_15 QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 16px \"Verdana\";\n"
"}")

        self.gridLayout_16.addWidget(self.label_45, 1, 0, 1, 1)

        self.label_58 = QLabel(self.frame_27)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"#frame_16, #frame_15 QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 16px \"Verdana\";\n"
"}")

        self.gridLayout_16.addWidget(self.label_58, 1, 1, 1, 1)

        self.SpinBox_DCp_17 = QDoubleSpinBox(self.frame_27)
        self.SpinBox_DCp_17.setObjectName(u"SpinBox_DCp_17")
        self.SpinBox_DCp_17.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.SpinBox_DCp_17.sizePolicy().hasHeightForWidth())
        self.SpinBox_DCp_17.setSizePolicy(sizePolicy1)
        self.SpinBox_DCp_17.setMinimumSize(QSize(204, 25))
        self.SpinBox_DCp_17.setMaximumSize(QSize(95, 20))
        self.SpinBox_DCp_17.setWrapping(False)
        self.SpinBox_DCp_17.setFrame(True)
        self.SpinBox_DCp_17.setAccelerated(False)
        self.SpinBox_DCp_17.setKeyboardTracking(True)
        self.SpinBox_DCp_17.setProperty("showGroupSeparator", False)
        self.SpinBox_DCp_17.setMaximum(99999999999.000000000000000)

        self.gridLayout_16.addWidget(self.SpinBox_DCp_17, 2, 0, 1, 1)

        self.SpinBox_DCp_18 = QDoubleSpinBox(self.frame_27)
        self.SpinBox_DCp_18.setObjectName(u"SpinBox_DCp_18")
        self.SpinBox_DCp_18.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.SpinBox_DCp_18.sizePolicy().hasHeightForWidth())
        self.SpinBox_DCp_18.setSizePolicy(sizePolicy1)
        self.SpinBox_DCp_18.setMinimumSize(QSize(204, 25))
        self.SpinBox_DCp_18.setMaximumSize(QSize(95, 20))
        self.SpinBox_DCp_18.setWrapping(False)
        self.SpinBox_DCp_18.setFrame(True)
        self.SpinBox_DCp_18.setAccelerated(False)
        self.SpinBox_DCp_18.setKeyboardTracking(True)
        self.SpinBox_DCp_18.setProperty("showGroupSeparator", False)
        self.SpinBox_DCp_18.setMaximum(99999999999.000000000000000)

        self.gridLayout_16.addWidget(self.SpinBox_DCp_18, 2, 1, 1, 1)


        self.gridLayout_15.addWidget(self.frame_27, 0, 2, 1, 2, Qt.AlignTop)

        self.horizontalSpacer_2 = QSpacerItem(429, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.frame_24 = QFrame(self.frame_15)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setStyleSheet(u"#frame_16, #frame_15 QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignLeft;\n"
"	color: #3d8ec9;\n"
"	font: 77 14px \"Verdana\";\n"
"}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_24)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_104 = QLabel(self.frame_24)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setStyleSheet(u"#frame_16, #frame_15 QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 20px \"Verdana\";\n"
"}")

        self.gridLayout.addWidget(self.label_104, 0, 0, 1, 4)

        self.label_106 = QLabel(self.frame_24)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setStyleSheet(u"#frame_16, #frame_15 QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 16px \"Verdana\";\n"
"}")

        self.gridLayout.addWidget(self.label_106, 1, 0, 1, 2)

        self.label_113 = QLabel(self.frame_24)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setStyleSheet(u"#frame_16, #frame_15 QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 16px \"Verdana\";\n"
"}")

        self.gridLayout.addWidget(self.label_113, 1, 2, 1, 2)

        self.label_98 = QLabel(self.frame_24)
        self.label_98.setObjectName(u"label_98")

        self.gridLayout.addWidget(self.label_98, 2, 0, 1, 1)

        self.doubleSpinBox_52 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_52.setObjectName(u"doubleSpinBox_52")
        self.doubleSpinBox_52.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_52, 2, 1, 1, 1)

        self.label_115 = QLabel(self.frame_24)
        self.label_115.setObjectName(u"label_115")

        self.gridLayout.addWidget(self.label_115, 2, 2, 1, 1)

        self.doubleSpinBox_51 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_51.setObjectName(u"doubleSpinBox_51")
        self.doubleSpinBox_51.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_51, 2, 3, 1, 1)

        self.label_105 = QLabel(self.frame_24)
        self.label_105.setObjectName(u"label_105")

        self.gridLayout.addWidget(self.label_105, 3, 0, 1, 1)

        self.doubleSpinBox_56 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_56.setObjectName(u"doubleSpinBox_56")
        self.doubleSpinBox_56.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_56, 3, 1, 1, 1)

        self.label_103 = QLabel(self.frame_24)
        self.label_103.setObjectName(u"label_103")

        self.gridLayout.addWidget(self.label_103, 3, 2, 1, 1)

        self.doubleSpinBox_60 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_60.setObjectName(u"doubleSpinBox_60")
        self.doubleSpinBox_60.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_60, 3, 3, 1, 1)

        self.label_101 = QLabel(self.frame_24)
        self.label_101.setObjectName(u"label_101")

        self.gridLayout.addWidget(self.label_101, 4, 0, 1, 1)

        self.doubleSpinBox_57 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_57.setObjectName(u"doubleSpinBox_57")
        self.doubleSpinBox_57.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_57, 4, 1, 1, 1)

        self.label_114 = QLabel(self.frame_24)
        self.label_114.setObjectName(u"label_114")

        self.gridLayout.addWidget(self.label_114, 4, 2, 1, 1)

        self.doubleSpinBox_58 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_58.setObjectName(u"doubleSpinBox_58")
        self.doubleSpinBox_58.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_58, 4, 3, 1, 1)

        self.label_99 = QLabel(self.frame_24)
        self.label_99.setObjectName(u"label_99")

        self.gridLayout.addWidget(self.label_99, 5, 0, 1, 1)

        self.doubleSpinBox_48 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_48.setObjectName(u"doubleSpinBox_48")
        self.doubleSpinBox_48.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_48, 5, 1, 1, 1)

        self.label_93 = QLabel(self.frame_24)
        self.label_93.setObjectName(u"label_93")

        self.gridLayout.addWidget(self.label_93, 5, 2, 1, 1)

        self.doubleSpinBox_55 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_55.setObjectName(u"doubleSpinBox_55")
        self.doubleSpinBox_55.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_55, 5, 3, 1, 1)

        self.label_91 = QLabel(self.frame_24)
        self.label_91.setObjectName(u"label_91")

        self.gridLayout.addWidget(self.label_91, 6, 0, 1, 1)

        self.doubleSpinBox_54 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_54.setObjectName(u"doubleSpinBox_54")
        self.doubleSpinBox_54.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_54, 6, 1, 1, 1)

        self.label_94 = QLabel(self.frame_24)
        self.label_94.setObjectName(u"label_94")

        self.gridLayout.addWidget(self.label_94, 6, 2, 1, 1)

        self.doubleSpinBox_47 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_47.setObjectName(u"doubleSpinBox_47")
        self.doubleSpinBox_47.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_47, 6, 3, 1, 1)

        self.label_100 = QLabel(self.frame_24)
        self.label_100.setObjectName(u"label_100")

        self.gridLayout.addWidget(self.label_100, 7, 0, 1, 1)

        self.doubleSpinBox_45 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_45.setObjectName(u"doubleSpinBox_45")
        self.doubleSpinBox_45.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_45, 7, 1, 1, 1)

        self.label_97 = QLabel(self.frame_24)
        self.label_97.setObjectName(u"label_97")

        self.gridLayout.addWidget(self.label_97, 7, 2, 1, 1)

        self.doubleSpinBox_49 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_49.setObjectName(u"doubleSpinBox_49")
        self.doubleSpinBox_49.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_49, 7, 3, 1, 1)

        self.label_108 = QLabel(self.frame_24)
        self.label_108.setObjectName(u"label_108")

        self.gridLayout.addWidget(self.label_108, 8, 0, 1, 1)

        self.doubleSpinBox_39 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_39.setObjectName(u"doubleSpinBox_39")
        self.doubleSpinBox_39.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_39, 8, 1, 1, 1)

        self.label_102 = QLabel(self.frame_24)
        self.label_102.setObjectName(u"label_102")

        self.gridLayout.addWidget(self.label_102, 8, 2, 1, 1)

        self.doubleSpinBox_41 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_41.setObjectName(u"doubleSpinBox_41")
        self.doubleSpinBox_41.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_41, 8, 3, 1, 1)

        self.label_116 = QLabel(self.frame_24)
        self.label_116.setObjectName(u"label_116")

        self.gridLayout.addWidget(self.label_116, 9, 0, 1, 1)

        self.doubleSpinBox_38 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_38.setObjectName(u"doubleSpinBox_38")
        self.doubleSpinBox_38.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_38, 9, 1, 1, 1)

        self.label_110 = QLabel(self.frame_24)
        self.label_110.setObjectName(u"label_110")

        self.gridLayout.addWidget(self.label_110, 9, 2, 1, 1)

        self.doubleSpinBox_43 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_43.setObjectName(u"doubleSpinBox_43")
        self.doubleSpinBox_43.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_43, 9, 3, 1, 1)

        self.label_117 = QLabel(self.frame_24)
        self.label_117.setObjectName(u"label_117")

        self.gridLayout.addWidget(self.label_117, 10, 0, 1, 1)

        self.doubleSpinBox_44 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_44.setObjectName(u"doubleSpinBox_44")
        self.doubleSpinBox_44.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_44, 10, 1, 1, 1)

        self.label_109 = QLabel(self.frame_24)
        self.label_109.setObjectName(u"label_109")

        self.gridLayout.addWidget(self.label_109, 10, 2, 1, 1)

        self.doubleSpinBox_59 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_59.setObjectName(u"doubleSpinBox_59")
        self.doubleSpinBox_59.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_59, 10, 3, 1, 1)

        self.label_92 = QLabel(self.frame_24)
        self.label_92.setObjectName(u"label_92")

        self.gridLayout.addWidget(self.label_92, 11, 0, 1, 1)

        self.doubleSpinBox_42 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_42.setObjectName(u"doubleSpinBox_42")
        self.doubleSpinBox_42.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_42, 11, 1, 1, 1)

        self.label_96 = QLabel(self.frame_24)
        self.label_96.setObjectName(u"label_96")

        self.gridLayout.addWidget(self.label_96, 11, 2, 1, 1)

        self.doubleSpinBox_46 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_46.setObjectName(u"doubleSpinBox_46")
        self.doubleSpinBox_46.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_46, 11, 3, 1, 1)

        self.label_111 = QLabel(self.frame_24)
        self.label_111.setObjectName(u"label_111")

        self.gridLayout.addWidget(self.label_111, 12, 0, 1, 1)

        self.doubleSpinBox_61 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_61.setObjectName(u"doubleSpinBox_61")
        self.doubleSpinBox_61.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_61, 12, 1, 1, 1)

        self.label_107 = QLabel(self.frame_24)
        self.label_107.setObjectName(u"label_107")

        self.gridLayout.addWidget(self.label_107, 12, 2, 1, 1)

        self.doubleSpinBox_50 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_50.setObjectName(u"doubleSpinBox_50")
        self.doubleSpinBox_50.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_50, 12, 3, 1, 1)

        self.label_95 = QLabel(self.frame_24)
        self.label_95.setObjectName(u"label_95")

        self.gridLayout.addWidget(self.label_95, 13, 0, 1, 1)

        self.doubleSpinBox_40 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_40.setObjectName(u"doubleSpinBox_40")
        self.doubleSpinBox_40.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_40, 13, 1, 1, 1)

        self.label_112 = QLabel(self.frame_24)
        self.label_112.setObjectName(u"label_112")

        self.gridLayout.addWidget(self.label_112, 13, 2, 1, 1)

        self.doubleSpinBox_53 = QDoubleSpinBox(self.frame_24)
        self.doubleSpinBox_53.setObjectName(u"doubleSpinBox_53")
        self.doubleSpinBox_53.setMaximum(99999999999.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_53, 13, 3, 1, 1)


        self.gridLayout_15.addWidget(self.frame_24, 1, 2, 1, 2)


        self.verticalLayout_7.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.page_0_Registrar_Historico)
        self.page_1_Registrar_Tarifas = QWidget()
        self.page_1_Registrar_Tarifas.setObjectName(u"page_1_Registrar_Tarifas")
        self.page_1_Registrar_Tarifas.setStyleSheet(u"QLabel {\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 14px \"Verdana\";\n"
"}\n"
"\n"
"QDoubleSpinBox\n"
"{\n"
"    selection-background-color: #302F2F;\n"
"    background-color: #201F1F;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 2px;\n"
"	color: silver;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #302F2F;\n"
"    background-color: #201F1F;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 2px;\n"
"	color: silver;\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.page_1_Registrar_Tarifas)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.frame_16 = QFrame(self.page_1_Registrar_Tarifas)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_16)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_16)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_7)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_10.addWidget(self.label_21, 3, 0, 1, 1)

        self.doubleSpinBox_23 = QDoubleSpinBox(self.frame_7)
        self.doubleSpinBox_23.setObjectName(u"doubleSpinBox_23")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.doubleSpinBox_23.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_23.setSizePolicy(sizePolicy4)
        self.doubleSpinBox_23.setMaximum(99999999999.000000000000000)

        self.gridLayout_10.addWidget(self.doubleSpinBox_23, 2, 4, 1, 1)

        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_10.addWidget(self.label_17, 2, 0, 1, 1)

        self.label_38 = QLabel(self.frame_7)
        self.label_38.setObjectName(u"label_38")
        sizePolicy1.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy1)
        self.label_38.setStyleSheet(u"QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 20px \"Verdana\";\n"
"}")

        self.gridLayout_10.addWidget(self.label_38, 0, 2, 1, 1)

        self.doubleSpinBox_24 = QDoubleSpinBox(self.frame_7)
        self.doubleSpinBox_24.setObjectName(u"doubleSpinBox_24")
        sizePolicy4.setHeightForWidth(self.doubleSpinBox_24.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_24.setSizePolicy(sizePolicy4)
        self.doubleSpinBox_24.setMaximum(99999999999.000000000000000)

        self.gridLayout_10.addWidget(self.doubleSpinBox_24, 2, 1, 1, 1)

        self.label_18 = QLabel(self.frame_7)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_10.addWidget(self.label_18, 2, 3, 1, 1)

        self.label_22 = QLabel(self.frame_7)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_10.addWidget(self.label_22, 3, 3, 1, 1)

        self.label_69 = QLabel(self.frame_7)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setStyleSheet(u"QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 16px \"Verdana\";\n"
"}")

        self.gridLayout_10.addWidget(self.label_69, 1, 0, 1, 2)

        self.label_71 = QLabel(self.frame_7)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setStyleSheet(u"QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 16px \"Verdana\";\n"
"}")

        self.gridLayout_10.addWidget(self.label_71, 1, 3, 1, 2)

        self.doubleSpinBox_27 = QDoubleSpinBox(self.frame_7)
        self.doubleSpinBox_27.setObjectName(u"doubleSpinBox_27")

        self.gridLayout_10.addWidget(self.doubleSpinBox_27, 3, 1, 1, 1)

        self.doubleSpinBox_62 = QDoubleSpinBox(self.frame_7)
        self.doubleSpinBox_62.setObjectName(u"doubleSpinBox_62")

        self.gridLayout_10.addWidget(self.doubleSpinBox_62, 3, 4, 1, 1)


        self.gridLayout_3.addWidget(self.frame_7, 3, 1, 1, 1, Qt.AlignTop)

        self.frame_9 = QFrame(self.frame_16)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy5)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_9)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.frame_9)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 16px \"Verdana\";\n"
"}")

        self.gridLayout_7.addWidget(self.label_42, 1, 3, 1, 2)

        self.label_41 = QLabel(self.frame_9)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 16px \"Verdana\";\n"
"}")

        self.gridLayout_7.addWidget(self.label_41, 1, 0, 1, 2)

        self.label_33 = QLabel(self.frame_9)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 20px \"Verdana\";\n"
"}")

        self.gridLayout_7.addWidget(self.label_33, 0, 0, 1, 5)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.frame_9)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")
        self.doubleSpinBox_8.setMaximum(99999999999.000000000000000)

        self.gridLayout_7.addWidget(self.doubleSpinBox_8, 2, 4, 1, 1)

        self.doubleSpinBox_14 = QDoubleSpinBox(self.frame_9)
        self.doubleSpinBox_14.setObjectName(u"doubleSpinBox_14")
        self.doubleSpinBox_14.setMaximum(99999999999.000000000000000)

        self.gridLayout_7.addWidget(self.doubleSpinBox_14, 2, 1, 1, 1)

        self.label_29 = QLabel(self.frame_9)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_7.addWidget(self.label_29, 2, 0, 1, 1)

        self.label_30 = QLabel(self.frame_9)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_7.addWidget(self.label_30, 2, 3, 1, 1)


        self.gridLayout_3.addWidget(self.frame_9, 3, 0, 1, 1)

        self.frame_22 = QFrame(self.frame_16)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy1.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy1)
        self.frame_22.setMinimumSize(QSize(0, 168))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.frame_22.setMidLineWidth(0)
        self.gridLayout_8 = QGridLayout(self.frame_22)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_28 = QLabel(self.frame_22)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_8.addWidget(self.label_28, 4, 0, 1, 1)

        self.doubleSpinBox_10 = QDoubleSpinBox(self.frame_22)
        self.doubleSpinBox_10.setObjectName(u"doubleSpinBox_10")
        self.doubleSpinBox_10.setMaximum(99999999999.000000000000000)

        self.gridLayout_8.addWidget(self.doubleSpinBox_10, 4, 1, 1, 1)

        self.doubleSpinBox_12 = QDoubleSpinBox(self.frame_22)
        self.doubleSpinBox_12.setObjectName(u"doubleSpinBox_12")
        self.doubleSpinBox_12.setMaximum(99999999999.000000000000000)

        self.gridLayout_8.addWidget(self.doubleSpinBox_12, 4, 4, 1, 1)

        self.label_34 = QLabel(self.frame_22)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 20px \"Verdana\";\n"
"}")

        self.gridLayout_8.addWidget(self.label_34, 0, 0, 1, 5)

        self.label_48 = QLabel(self.frame_22)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 12px \"Verdana\";\n"
"}")

        self.gridLayout_8.addWidget(self.label_48, 4, 3, 1, 1)

        self.label_51 = QLabel(self.frame_22)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 12px \"Verdana\";\n"
"}")

        self.gridLayout_8.addWidget(self.label_51, 3, 3, 1, 1)

        self.doubleSpinBox_11 = QDoubleSpinBox(self.frame_22)
        self.doubleSpinBox_11.setObjectName(u"doubleSpinBox_11")
        self.doubleSpinBox_11.setMaximum(99999999999.000000000000000)

        self.gridLayout_8.addWidget(self.doubleSpinBox_11, 3, 4, 1, 1)

        self.label_56 = QLabel(self.frame_22)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 16px \"Verdana\";\n"
"}")

        self.gridLayout_8.addWidget(self.label_56, 2, 3, 1, 2)

        self.doubleSpinBox_9 = QDoubleSpinBox(self.frame_22)
        self.doubleSpinBox_9.setObjectName(u"doubleSpinBox_9")
        self.doubleSpinBox_9.setMaximum(99999999999.000000000000000)

        self.gridLayout_8.addWidget(self.doubleSpinBox_9, 3, 1, 1, 1)

        self.label_27 = QLabel(self.frame_22)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_8.addWidget(self.label_27, 3, 0, 1, 1)

        self.label_47 = QLabel(self.frame_22)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 16px \"Verdana\";\n"
"}")

        self.gridLayout_8.addWidget(self.label_47, 2, 0, 1, 2)


        self.gridLayout_3.addWidget(self.frame_22, 1, 0, 1, 1)

        self.frame = QFrame(self.frame_16)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(6)
        self.gridLayout_9.setVerticalSpacing(0)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.frame)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 20px \"Verdana\";\n"
"}")

        self.gridLayout_9.addWidget(self.label_40, 0, 2, 1, 1)

        self.label_72 = QLabel(self.frame)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setStyleSheet(u"QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 16px \"Verdana\";\n"
"}")

        self.gridLayout_9.addWidget(self.label_72, 1, 3, 1, 2)

        self.label_70 = QLabel(self.frame)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setStyleSheet(u"QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 16px \"Verdana\";\n"
"}")

        self.gridLayout_9.addWidget(self.label_70, 1, 0, 1, 2)

        self.doubleSpinBox_25 = QDoubleSpinBox(self.frame)
        self.doubleSpinBox_25.setObjectName(u"doubleSpinBox_25")
        sizePolicy4.setHeightForWidth(self.doubleSpinBox_25.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_25.setSizePolicy(sizePolicy4)
        self.doubleSpinBox_25.setMaximum(99999999999.000000000000000)

        self.gridLayout_9.addWidget(self.doubleSpinBox_25, 2, 1, 1, 1)

        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_9.addWidget(self.label_23, 2, 0, 1, 1, Qt.AlignTop)

        self.label_24 = QLabel(self.frame)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_9.addWidget(self.label_24, 2, 3, 1, 1, Qt.AlignTop)

        self.doubleSpinBox_26 = QDoubleSpinBox(self.frame)
        self.doubleSpinBox_26.setObjectName(u"doubleSpinBox_26")
        sizePolicy4.setHeightForWidth(self.doubleSpinBox_26.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_26.setSizePolicy(sizePolicy4)
        self.doubleSpinBox_26.setMaximum(99999999999.000000000000000)

        self.gridLayout_9.addWidget(self.doubleSpinBox_26, 2, 4, 1, 1)

        self.label_26 = QLabel(self.frame)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_9.addWidget(self.label_26, 3, 3, 1, 1, Qt.AlignTop)

        self.doubleSpinBox_18 = QDoubleSpinBox(self.frame)
        self.doubleSpinBox_18.setObjectName(u"doubleSpinBox_18")

        self.gridLayout_9.addWidget(self.doubleSpinBox_18, 3, 4, 1, 1)

        self.label_25 = QLabel(self.frame)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_9.addWidget(self.label_25, 3, 0, 1, 1, Qt.AlignTop)

        self.doubleSpinBox_16 = QDoubleSpinBox(self.frame)
        self.doubleSpinBox_16.setObjectName(u"doubleSpinBox_16")

        self.gridLayout_9.addWidget(self.doubleSpinBox_16, 3, 1, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 1, 1, 1, 1)

        self.label_37 = QLabel(self.frame_16)
        self.label_37.setObjectName(u"label_37")
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setStyleSheet(u"QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: white;\n"
"	font: 77 24px \"Verdana\";\n"
"}")

        self.gridLayout_3.addWidget(self.label_37, 2, 0, 1, 2, Qt.AlignBottom)

        self.label_36 = QLabel(self.frame_16)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"QLabel {\n"
"   /* background-color: #FFFFFF;*/\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: white;\n"
"	font: 77 24px \"Verdana\";\n"
"}")

        self.gridLayout_3.addWidget(self.label_36, 0, 0, 1, 2, Qt.AlignBottom)


        self.verticalLayout_10.addWidget(self.frame_16)

        self.frame_21 = QFrame(self.page_1_Registrar_Tarifas)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy3.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy3)
        self.frame_21.setMinimumSize(QSize(0, 75))
        self.frame_21.setMaximumSize(QSize(200, 19))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_21)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMaximumSize(QSize(200, 40))
        font7 = QFont()
        font7.setFamily(u"Verdana")
        font7.setPointSize(14)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(50)
        self.pushButton.setFont(font7)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"/*background-color: rgba(33, 43, 51, 100);*/\n"
"background-color: rgba(61, 80, 95, 100);\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"text-align:center;\n"
"	font: 14pt \"Verdana\";\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    background-color: #302F2F;\n"
"    /*border-width: 2px;\n"
"    border-color: #3A3939;\n"
"    border-style: solid;*/\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    /*border-radius: 2px;*/\n"
"    color: #808080;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(138, 203, 250);\n"
"    color: white;\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButton)


        self.verticalLayout_10.addWidget(self.frame_21, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_1_Registrar_Tarifas)
        self.page_2_Graficos = QWidget()
        self.page_2_Graficos.setObjectName(u"page_2_Graficos")
        self.page_2_Graficos.setStyleSheet(u"QLabel {\n"
"    qproperty-alignment: AlignCenter;\n"
"	color: #3d8ec9;\n"
"	font: 77 14px \"Verdana\";\n"
"}\n"
"\n"
"QDoubleSpinBox\n"
"{\n"
"    selection-background-color: #302F2F;\n"
"    background-color: #201F1F;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 2px;\n"
"	color: silver;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #302F2F;\n"
"    background-color: #201F1F;\n"
"    border-style: solid;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 2px;\n"
"    padding: 2px;\n"
"	color: silver;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.page_2_Graficos)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_19 = QFrame(self.page_2_Graficos)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_19)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_18 = QFrame(self.frame_19)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_18)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.line = QFrame(self.frame_18)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 2, 0, 1, 12)

        self.label_35 = QLabel(self.frame_18)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_4.addWidget(self.label_35, 5, 0, 1, 1)

        self.label_121 = QLabel(self.frame_18)
        self.label_121.setObjectName(u"label_121")

        self.gridLayout_4.addWidget(self.label_121, 3, 2, 1, 1)

        self.label_54 = QLabel(self.frame_18)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_4.addWidget(self.label_54, 5, 3, 1, 1)

        self.label_57 = QLabel(self.frame_18)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_4.addWidget(self.label_57, 3, 3, 1, 1)

        self.label_124 = QLabel(self.frame_18)
        self.label_124.setObjectName(u"label_124")

        self.gridLayout_4.addWidget(self.label_124, 4, 7, 1, 1)

        self.label_129 = QLabel(self.frame_18)
        self.label_129.setObjectName(u"label_129")

        self.gridLayout_4.addWidget(self.label_129, 1, 8, 1, 1)

        self.label_39 = QLabel(self.frame_18)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_4.addWidget(self.label_39, 1, 2, 1, 1)

        self.label_52 = QLabel(self.frame_18)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_4.addWidget(self.label_52, 1, 6, 1, 1)

        self.label_62 = QLabel(self.frame_18)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_4.addWidget(self.label_62, 3, 4, 1, 1)

        self.label_55 = QLabel(self.frame_18)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_4.addWidget(self.label_55, 4, 3, 1, 1)

        self.label_134 = QLabel(self.frame_18)
        self.label_134.setObjectName(u"label_134")

        self.gridLayout_4.addWidget(self.label_134, 0, 10, 1, 1)

        self.label_123 = QLabel(self.frame_18)
        self.label_123.setObjectName(u"label_123")

        self.gridLayout_4.addWidget(self.label_123, 4, 6, 1, 1)

        self.label_138 = QLabel(self.frame_18)
        self.label_138.setObjectName(u"label_138")

        self.gridLayout_4.addWidget(self.label_138, 4, 10, 1, 1)

        self.label_50 = QLabel(self.frame_18)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_4.addWidget(self.label_50, 0, 2, 1, 3)

        self.label_125 = QLabel(self.frame_18)
        self.label_125.setObjectName(u"label_125")

        self.gridLayout_4.addWidget(self.label_125, 3, 7, 1, 1)

        self.label_118 = QLabel(self.frame_18)
        self.label_118.setObjectName(u"label_118")

        self.gridLayout_4.addWidget(self.label_118, 4, 4, 1, 1)

        self.label_119 = QLabel(self.frame_18)
        self.label_119.setObjectName(u"label_119")

        self.gridLayout_4.addWidget(self.label_119, 5, 4, 1, 1)

        self.label_127 = QLabel(self.frame_18)
        self.label_127.setObjectName(u"label_127")

        self.gridLayout_4.addWidget(self.label_127, 3, 8, 1, 1)

        self.label_136 = QLabel(self.frame_18)
        self.label_136.setObjectName(u"label_136")

        self.gridLayout_4.addWidget(self.label_136, 5, 10, 1, 1)

        self.line_2 = QFrame(self.frame_18)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 0, 1, 2, 1)

        self.label_137 = QLabel(self.frame_18)
        self.label_137.setObjectName(u"label_137")

        self.gridLayout_4.addWidget(self.label_137, 3, 10, 1, 1)

        self.label_133 = QLabel(self.frame_18)
        self.label_133.setObjectName(u"label_133")

        self.gridLayout_4.addWidget(self.label_133, 4, 8, 1, 1)

        self.label_49 = QLabel(self.frame_18)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_4.addWidget(self.label_49, 1, 4, 1, 1)

        self.label_126 = QLabel(self.frame_18)
        self.label_126.setObjectName(u"label_126")

        self.gridLayout_4.addWidget(self.label_126, 1, 7, 1, 1)

        self.label_120 = QLabel(self.frame_18)
        self.label_120.setObjectName(u"label_120")

        self.gridLayout_4.addWidget(self.label_120, 4, 2, 1, 1)

        self.label_32 = QLabel(self.frame_18)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_4.addWidget(self.label_32, 4, 0, 1, 1)

        self.label_130 = QLabel(self.frame_18)
        self.label_130.setObjectName(u"label_130")

        self.gridLayout_4.addWidget(self.label_130, 5, 6, 1, 1)

        self.line_4 = QFrame(self.frame_18)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_4, 0, 9, 2, 1)

        self.label_43 = QLabel(self.frame_18)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_4.addWidget(self.label_43, 1, 3, 1, 1)

        self.label_135 = QLabel(self.frame_18)
        self.label_135.setObjectName(u"label_135")

        self.gridLayout_4.addWidget(self.label_135, 1, 10, 1, 1)

        self.label_31 = QLabel(self.frame_18)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_4.addWidget(self.label_31, 3, 0, 1, 1)

        self.label_132 = QLabel(self.frame_18)
        self.label_132.setObjectName(u"label_132")

        self.gridLayout_4.addWidget(self.label_132, 3, 6, 1, 1)

        self.line_3 = QFrame(self.frame_18)
        self.line_3.setObjectName(u"line_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy6)
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 0, 5, 2, 1)

        self.label_131 = QLabel(self.frame_18)
        self.label_131.setObjectName(u"label_131")

        self.gridLayout_4.addWidget(self.label_131, 5, 7, 1, 1)

        self.label_53 = QLabel(self.frame_18)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_4.addWidget(self.label_53, 0, 6, 1, 3)

        self.label_128 = QLabel(self.frame_18)
        self.label_128.setObjectName(u"label_128")

        self.gridLayout_4.addWidget(self.label_128, 5, 8, 1, 1)

        self.label_122 = QLabel(self.frame_18)
        self.label_122.setObjectName(u"label_122")

        self.gridLayout_4.addWidget(self.label_122, 5, 2, 1, 1)

        self.line_5 = QFrame(self.frame_18)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_5, 0, 11, 2, 1)


        self.gridLayout_6.addWidget(self.frame_18, 0, 0, 1, 3)

        self.frame_17 = QFrame(self.frame_19)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_17)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")

        self.verticalLayout_16.addLayout(self.verticalLayout_13)


        self.gridLayout_6.addWidget(self.frame_17, 2, 2, 1, 2)

        self.frame_12 = QFrame(self.frame_19)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")

        self.verticalLayout_14.addLayout(self.verticalLayout_11)


        self.gridLayout_6.addWidget(self.frame_12, 2, 0, 1, 2)

        self.frame_28 = QFrame(self.frame_19)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_28)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")

        self.verticalLayout_22.addLayout(self.verticalLayout_12)


        self.gridLayout_6.addWidget(self.frame_28, 1, 2, 1, 2)

        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_20)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.verticalLayout_21.addLayout(self.verticalLayout_8)


        self.gridLayout_6.addWidget(self.frame_20, 1, 0, 1, 2)

        self.frame_23 = QFrame(self.frame_19)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_23)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_139 = QLabel(self.frame_23)
        self.label_139.setObjectName(u"label_139")

        self.gridLayout_5.addWidget(self.label_139, 0, 0, 1, 2)

        self.label_140 = QLabel(self.frame_23)
        self.label_140.setObjectName(u"label_140")

        self.gridLayout_5.addWidget(self.label_140, 1, 0, 1, 1)

        self.label_141 = QLabel(self.frame_23)
        self.label_141.setObjectName(u"label_141")

        self.gridLayout_5.addWidget(self.label_141, 1, 1, 1, 1)

        self.line_6 = QFrame(self.frame_23)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_6, 2, 0, 1, 2)

        self.label_142 = QLabel(self.frame_23)
        self.label_142.setObjectName(u"label_142")

        self.gridLayout_5.addWidget(self.label_142, 3, 0, 1, 1)

        self.label_143 = QLabel(self.frame_23)
        self.label_143.setObjectName(u"label_143")

        self.gridLayout_5.addWidget(self.label_143, 3, 1, 1, 1)

        self.label_144 = QLabel(self.frame_23)
        self.label_144.setObjectName(u"label_144")

        self.gridLayout_5.addWidget(self.label_144, 4, 0, 1, 1)

        self.label_146 = QLabel(self.frame_23)
        self.label_146.setObjectName(u"label_146")

        self.gridLayout_5.addWidget(self.label_146, 4, 1, 1, 1)

        self.label_145 = QLabel(self.frame_23)
        self.label_145.setObjectName(u"label_145")

        self.gridLayout_5.addWidget(self.label_145, 5, 0, 1, 1)

        self.label_147 = QLabel(self.frame_23)
        self.label_147.setObjectName(u"label_147")

        self.gridLayout_5.addWidget(self.label_147, 5, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_23, 0, 3, 1, 1)


        self.verticalLayout_15.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.page_2_Graficos)

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

        self.pushButton_0.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(accessibility)
        MainWindow.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DEMANDA \u00d3TIMA", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"Registrar Hist\u00f3rico", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"Registrar Tarifas", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Compara\u00e7\u00e3o Econ\u00f4mica", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"SUPPORT ME", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"viniciuspessoa1997@gmail.com", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"(19) 9 8400-8480", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"@viniperson", None))
        self.label_12.setText("")
        self.label_13.setText("")
        self.label_14.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"DEMANDA \u00d3TIMA", None))
        self.pushButton_8.setText("")
        self.pushButton_7.setText("")
        self.pushButton_9.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Demanda Medida (kW)", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Fora Ponta", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Ponta", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Janeiro", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Janeiro", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Fevereiro", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Fevereiro", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Mar\u00e7o", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Mar\u00e7o", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Abril", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Abril", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Maio", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Maio", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Junho", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Junho", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Julho", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Julho", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Agosto", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Agosto", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Setembro", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Setembro", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Outubro", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Outubro", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Novembro", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Novembro", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Dezembro", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Dezembro", None))
        self.doubleSpinBox_32.setSpecialValueText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Insira o Modalidade Tarif\u00e1ria Atual", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Grupo Tarif\u00e1rio", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Modalidade Tarif\u00e1ria", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"A1 (\u2265 230 kV)", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"A2 (88 kV a 138 kV)", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"A3 (69 kV)", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"A3a (30 kV a 44 kV)", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"A4 (2.3 a 25 kV)", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"AS (\u2264 2.3 kV subterr\u00e2neo)", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Hor\u00e1ria Azul", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Hor\u00e1ria Verde", None))

        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Demanda Contratada", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Fora Ponta", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Ponta", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Consumo (kWh)", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Fora Ponta", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u" Ponta", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Janeiro", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Janeiro", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Fevereiro", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Fevereiro", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Mar\u00e7o", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Mar\u00e7o", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Abril", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Abril", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Maio", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Maio", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Junho", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Junho", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Julho", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Julho", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Agosto", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Agosto", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Setembro", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Setembro", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Outubro", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Outubro", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Novembro", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Novembro", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Dezembro", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Dezembro", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"TE:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"TUSD:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Consumo (R$/kWh)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"TUSD:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"TE:", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Fora Ponta", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Ponta", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Sem Imposto", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Com Imposto", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Demanda (R$/kW)", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Fora Ponta / Ponta:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Fora Ponta / Ponta:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Ponta:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Demanda (R$/kW)", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Ponta:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Fora Ponta:", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Sem Imposto", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Fora de Ponta:", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Com Imposto", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Consumo (R$/kWh)", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Ponta", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Fora Ponta", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"TUSD:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"TUSD:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"TE:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"TE:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Modalidade Tarif\u00e1ria Verde", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Modalidade Tarif\u00e1ria Azul", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Azul", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"FP", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"FP", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"Despesa", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Consumo", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Verde", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Atual", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Demanda", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"Economia", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"R$", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"REF", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"REF", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"0,0%", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"0,0%", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"COPYRIGHT SPINN CO. V. 1.0", None))
    # retranslateUi

