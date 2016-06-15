# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seel_res/GUI/B_ELECTRONICS/A_electronics/templates/transistor.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 528)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widgetFrameOuter = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetFrameOuter.sizePolicy().hasHeightForWidth())
        self.widgetFrameOuter.setSizePolicy(sizePolicy)
        self.widgetFrameOuter.setStyleSheet("")
        self.widgetFrameOuter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.widgetFrameOuter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.widgetFrameOuter.setObjectName("widgetFrameOuter")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widgetFrameOuter)
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.widgetFrameOuter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.biasV = QtWidgets.QDoubleSpinBox(self.frame)
        self.biasV.setMinimumSize(QtCore.QSize(0, 30))
        self.biasV.setDecimals(3)
        self.biasV.setMinimum(-3.3)
        self.biasV.setMaximum(3.3)
        self.biasV.setSingleStep(0.01)
        self.biasV.setProperty("value", -1.2)
        self.biasV.setObjectName("biasV")
        self.gridLayout.addWidget(self.biasV, 1, 5, 1, 1)
        self.msg = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg.sizePolicy().hasHeightForWidth())
        self.msg.setSizePolicy(sizePolicy)
        self.msg.setText("")
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")
        self.gridLayout.addWidget(self.msg, 5, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(94, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 9, 1, 2)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 0, 6, 1)
        self.startV = QtWidgets.QDoubleSpinBox(self.frame)
        self.startV.setMinimumSize(QtCore.QSize(0, 30))
        self.startV.setMinimum(-3.3)
        self.startV.setMaximum(3.3)
        self.startV.setSingleStep(0.2)
        self.startV.setProperty("value", 0.0)
        self.startV.setObjectName("startV")
        self.gridLayout.addWidget(self.startV, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 2, 1, 1)
        self.totalPoints = QtWidgets.QSpinBox(self.frame)
        self.totalPoints.setMinimumSize(QtCore.QSize(0, 30))
        self.totalPoints.setMinimum(10)
        self.totalPoints.setMaximum(1000)
        self.totalPoints.setProperty("value", 100)
        self.totalPoints.setObjectName("totalPoints")
        self.gridLayout.addWidget(self.totalPoints, 5, 3, 1, 1)
        self.progress = QtWidgets.QProgressBar(self.frame)
        self.progress.setProperty("value", 0)
        self.progress.setObjectName("progress")
        self.gridLayout.addWidget(self.progress, 5, 9, 1, 2)
        self.sweepLabel = QtWidgets.QLabel(self.frame)
        self.sweepLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sweepLabel.setObjectName("sweepLabel")
        self.gridLayout.addWidget(self.sweepLabel, 0, 2, 1, 2)
        self.plotButton = QtWidgets.QPushButton(self.frame)
        self.plotButton.setMinimumSize(QtCore.QSize(94, 30))
        self.plotButton.setObjectName("plotButton")
        self.gridLayout.addWidget(self.plotButton, 5, 5, 1, 1)
        self.optionsBox = QtWidgets.QComboBox(self.frame)
        self.optionsBox.setObjectName("optionsBox")
        self.gridLayout.addWidget(self.optionsBox, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 0, 4, 6, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 2, 2, 1)
        self.stopV = QtWidgets.QDoubleSpinBox(self.frame)
        self.stopV.setMinimumSize(QtCore.QSize(0, 30))
        self.stopV.setMinimum(-3.3)
        self.stopV.setMaximum(3.3)
        self.stopV.setSingleStep(0.2)
        self.stopV.setProperty("value", 3.3)
        self.stopV.setObjectName("stopV")
        self.gridLayout.addWidget(self.stopV, 2, 3, 2, 1)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 6, 6, 2)
        self.biasLabel = QtWidgets.QLabel(self.frame)
        self.biasLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.biasLabel.setObjectName("biasLabel")
        self.gridLayout.addWidget(self.biasLabel, 0, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 9, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 10, 1, 1)
        self.tracesBox = QtWidgets.QComboBox(self.frame)
        self.tracesBox.setMinimumSize(QtCore.QSize(140, 0))
        self.tracesBox.setObjectName("tracesBox")
        self.gridLayout.addWidget(self.tracesBox, 1, 9, 1, 1)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.widgetFrameOuter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 366))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plot_area = QtWidgets.QGridLayout()
        self.plot_area.setObjectName("plot_area")
        self.gridLayout_4.addLayout(self.plot_area, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.gridLayout_3.addWidget(self.widgetFrameOuter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.delete_curve)
        self.pushButton_3.clicked.connect(MainWindow.savePlots)
        self.plotButton.clicked.connect(MainWindow.run)
        self.optionsBox.currentIndexChanged['int'].connect(MainWindow.typeChanged)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.widgetFrameOuter.setProperty("class", _translate("MainWindow", "PeripheralCollection"))
        self.frame.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner"))
        self.biasV.setSuffix(_translate("MainWindow", " V"))
        self.pushButton_3.setText(_translate("MainWindow", "Save Plots"))
        self.startV.setSuffix(_translate("MainWindow", " V"))
        self.label_6.setText(_translate("MainWindow", "Total Steps"))
        self.sweepLabel.setText(_translate("MainWindow", "sweep"))
        self.plotButton.setText(_translate("MainWindow", "Plot"))
        self.label_4.setText(_translate("MainWindow", "Initial Voltage"))
        self.label_5.setText(_translate("MainWindow", "Final Voltage"))
        self.stopV.setSuffix(_translate("MainWindow", " V"))
        self.biasLabel.setText(_translate("MainWindow", "bias"))
        self.label_2.setText(_translate("MainWindow", "Acquired Data"))
        self.pushButton_2.setText(_translate("MainWindow", "DEL"))
        self.frame_2.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner"))

