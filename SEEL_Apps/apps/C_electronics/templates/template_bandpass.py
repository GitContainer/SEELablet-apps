# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template_bandpass.ui'
#
# Created: Thu May  5 23:57:20 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(804, 628)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.widgetFrameOuter = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetFrameOuter.sizePolicy().hasHeightForWidth())
        self.widgetFrameOuter.setSizePolicy(sizePolicy)
        self.widgetFrameOuter.setStyleSheet(_fromUtf8(""))
        self.widgetFrameOuter.setFrameShape(QtGui.QFrame.StyledPanel)
        self.widgetFrameOuter.setFrameShadow(QtGui.QFrame.Raised)
        self.widgetFrameOuter.setObjectName(_fromUtf8("widgetFrameOuter"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widgetFrameOuter)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frame = QtGui.QFrame(self.widgetFrameOuter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 80))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.tracesBox = QtGui.QComboBox(self.frame)
        self.tracesBox.setObjectName(_fromUtf8("tracesBox"))
        self.gridLayout.addWidget(self.tracesBox, 0, 3, 1, 1)
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(94, 30))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 4, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(94, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 4, 1, 1)
        self.stopFreq = QtGui.QDoubleSpinBox(self.frame)
        self.stopFreq.setMinimumSize(QtCore.QSize(0, 30))
        self.stopFreq.setMinimum(5.0)
        self.stopFreq.setMaximum(5000.0)
        self.stopFreq.setSingleStep(1.0)
        self.stopFreq.setProperty("value", 500.0)
        self.stopFreq.setObjectName(_fromUtf8("stopFreq"))
        self.gridLayout.addWidget(self.stopFreq, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.progress = QtGui.QProgressBar(self.frame)
        self.progress.setProperty("value", 0)
        self.progress.setObjectName(_fromUtf8("progress"))
        self.gridLayout.addWidget(self.progress, 3, 2, 1, 2)
        self.startFreq = QtGui.QDoubleSpinBox(self.frame)
        self.startFreq.setMinimumSize(QtCore.QSize(0, 30))
        self.startFreq.setMinimum(5.0)
        self.startFreq.setMaximum(5000.0)
        self.startFreq.setSingleStep(1.0)
        self.startFreq.setObjectName(_fromUtf8("startFreq"))
        self.gridLayout.addWidget(self.startFreq, 0, 1, 1, 1)
        self.stepFreq = QtGui.QSpinBox(self.frame)
        self.stepFreq.setMinimumSize(QtCore.QSize(0, 30))
        self.stepFreq.setMinimum(10)
        self.stepFreq.setMaximum(5000)
        self.stepFreq.setProperty("value", 100)
        self.stepFreq.setObjectName(_fromUtf8("stepFreq"))
        self.gridLayout.addWidget(self.stepFreq, 4, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(94, 30))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 4, 4, 1, 1)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(self.widgetFrameOuter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_2.setMargin(2)
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.frame_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 794, 465))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_4 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setMargin(2)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.plot_area = QtGui.QGridLayout()
        self.plot_area.setObjectName(_fromUtf8("plot_area"))
        self.gridLayout_4.addLayout(self.plot_area, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.gridLayout_3.addWidget(self.widgetFrameOuter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.run)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.delete_curve)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.savePlots)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.widgetFrameOuter.setProperty("class", _translate("MainWindow", "PeripheralCollection", None))
        self.frame.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))
        self.label_6.setText(_translate("MainWindow", "Total Datapoints", None))
        self.label_2.setText(_translate("MainWindow", "Acquired Data", None))
        self.label_5.setText(_translate("MainWindow", "Stop Frequency", None))
        self.pushButton.setText(_translate("MainWindow", "Start Sweep", None))
        self.pushButton_2.setText(_translate("MainWindow", "DEL", None))
        self.label_4.setText(_translate("MainWindow", "Start Frequency", None))
        self.pushButton_3.setText(_translate("MainWindow", "Save Plots", None))
        self.frame_2.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner", None))

