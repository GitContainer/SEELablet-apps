# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seel_res/GUI/A_TEST_AND_MEASUREMENT/A_TandM/templates/arbitStream.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(743, 447)
        MainWindow.setMinimumSize(QtCore.QSize(300, 0))
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../usr/share/pixmaps/cubeview48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTip("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.cmdlist = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmdlist.sizePolicy().hasHeightForWidth())
        self.cmdlist.setSizePolicy(sizePolicy)
        self.cmdlist.setMinimumSize(QtCore.QSize(250, 0))
        self.cmdlist.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.cmdlist.setEditable(True)
        self.cmdlist.setObjectName("cmdlist")
        self.cmdlist.addItem("")
        self.cmdlist.addItem("")
        self.cmdlist.addItem("")
        self.cmdlist.addItem("")
        self.cmdlist.addItem("")
        self.gridLayout.addWidget(self.cmdlist, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.msg = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg.sizePolicy().hasHeightForWidth())
        self.msg.setSizePolicy(sizePolicy)
        self.msg.setBaseSize(QtCore.QSize(0, 17))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.msg.setFont(font)
        self.msg.setStyleSheet("color: rgb(255, 255, 255);")
        self.msg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.msg.setWordWrap(True)
        self.msg.setObjectName("msg")
        self.gridLayout.addWidget(self.msg, 1, 2, 2, 1)
        self.averageCount = QtWidgets.QSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.averageCount.sizePolicy().hasHeightForWidth())
        self.averageCount.setSizePolicy(sizePolicy)
        self.averageCount.setMinimum(1)
        self.averageCount.setMaximum(501)
        self.averageCount.setObjectName("averageCount")
        self.gridLayout.addWidget(self.averageCount, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 3, 1, 1)
        self.pause = QtWidgets.QCheckBox(self.frame)
        self.pause.setObjectName("pause")
        self.gridLayout.addWidget(self.pause, 1, 3, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.plot_area_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_area_frame.sizePolicy().hasHeightForWidth())
        self.plot_area_frame.setSizePolicy(sizePolicy)
        self.plot_area_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plot_area_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plot_area_frame.setObjectName("plot_area_frame")
        self.plot_area = QtWidgets.QVBoxLayout(self.plot_area_frame)
        self.plot_area.setContentsMargins(0, 0, 0, 0)
        self.plot_area.setSpacing(2)
        self.plot_area.setObjectName("plot_area")
        self.verticalLayout_2.addWidget(self.plot_area_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.stream)
        self.pushButton_2.clicked.connect(MainWindow.setAveraging)
        self.pushButton_3.clicked.connect(MainWindow.saveData)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Streaming Utility"))
        self.pushButton_2.setText(_translate("MainWindow", "Set Averaging"))
        self.cmdlist.setItemText(0, _translate("MainWindow", "get_average_voltage(\'CH1\')"))
        self.cmdlist.setItemText(1, _translate("MainWindow", "get_freq(\'CNTR\')"))
        self.cmdlist.setItemText(2, _translate("MainWindow", "get_high_freq(\'CNTR\')"))
        self.cmdlist.setItemText(3, _translate("MainWindow", "DutyCycle(\'ID1\')[1]"))
        self.cmdlist.setItemText(4, _translate("MainWindow", "MeasureInterval(\'ID1\',\'ID2\',\'rising\',\'rising\')"))
        self.pushButton.setText(_translate("MainWindow", "Stream Now"))
        self.msg.setText(_translate("MainWindow", ">"))
        self.pushButton_3.setText(_translate("MainWindow", "Save"))
        self.pause.setText(_translate("MainWindow", "Pause"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))

