# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pwmWidget.ui'
#
# Created: Sat May  7 14:01:02 2016
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(367, 268)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_7 = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.frame = QtGui.QFrame(self.frame_7)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout_5.addWidget(self.frame)
        self.Frame_4 = QtGui.QFrame(self.frame_7)
        self.Frame_4.setProperty("PeripheralCollectionInner", _fromUtf8(""))
        self.Frame_4.setObjectName(_fromUtf8("Frame_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.Frame_4)
        self.gridLayout_4.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_21 = QtGui.QLabel(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_4.addWidget(self.label_21, 0, 2, 1, 1)
        self.SQR4P = QtGui.QDoubleSpinBox(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SQR4P.sizePolicy().hasHeightForWidth())
        self.SQR4P.setSizePolicy(sizePolicy)
        self.SQR4P.setDecimals(3)
        self.SQR4P.setMaximum(360.0)
        self.SQR4P.setSingleStep(1.0)
        self.SQR4P.setProperty("value", 0.0)
        self.SQR4P.setObjectName(_fromUtf8("SQR4P"))
        self.gridLayout_4.addWidget(self.SQR4P, 4, 1, 1, 1)
        self.SQR1DC = QtGui.QDoubleSpinBox(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SQR1DC.sizePolicy().hasHeightForWidth())
        self.SQR1DC.setSizePolicy(sizePolicy)
        self.SQR1DC.setDecimals(3)
        self.SQR1DC.setMaximum(1.0)
        self.SQR1DC.setSingleStep(0.1)
        self.SQR1DC.setProperty("value", 0.5)
        self.SQR1DC.setObjectName(_fromUtf8("SQR1DC"))
        self.gridLayout_4.addWidget(self.SQR1DC, 1, 2, 1, 1)
        self.SQR4DC = QtGui.QDoubleSpinBox(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SQR4DC.sizePolicy().hasHeightForWidth())
        self.SQR4DC.setSizePolicy(sizePolicy)
        self.SQR4DC.setDecimals(3)
        self.SQR4DC.setMaximum(1.0)
        self.SQR4DC.setSingleStep(0.1)
        self.SQR4DC.setProperty("value", 0.5)
        self.SQR4DC.setObjectName(_fromUtf8("SQR4DC"))
        self.gridLayout_4.addWidget(self.SQR4DC, 4, 2, 1, 1)
        self.SQR2DC = QtGui.QDoubleSpinBox(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SQR2DC.sizePolicy().hasHeightForWidth())
        self.SQR2DC.setSizePolicy(sizePolicy)
        self.SQR2DC.setDecimals(3)
        self.SQR2DC.setMaximum(1.0)
        self.SQR2DC.setSingleStep(0.1)
        self.SQR2DC.setProperty("value", 0.5)
        self.SQR2DC.setObjectName(_fromUtf8("SQR2DC"))
        self.gridLayout_4.addWidget(self.SQR2DC, 2, 2, 1, 1)
        self.SQRSF = QtGui.QDoubleSpinBox(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SQRSF.sizePolicy().hasHeightForWidth())
        self.SQRSF.setSizePolicy(sizePolicy)
        self.SQRSF.setDecimals(3)
        self.SQRSF.setMinimum(100.0)
        self.SQRSF.setMaximum(1000000.0)
        self.SQRSF.setSingleStep(10.0)
        self.SQRSF.setProperty("value", 1000.0)
        self.SQRSF.setObjectName(_fromUtf8("SQRSF"))
        self.gridLayout_4.addWidget(self.SQRSF, 6, 1, 1, 1)
        self.label_22 = QtGui.QLabel(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_4.addWidget(self.label_22, 1, 1, 1, 1)
        self.SQR3DC = QtGui.QDoubleSpinBox(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SQR3DC.sizePolicy().hasHeightForWidth())
        self.SQR3DC.setSizePolicy(sizePolicy)
        self.SQR3DC.setDecimals(3)
        self.SQR3DC.setMaximum(1.0)
        self.SQR3DC.setSingleStep(0.1)
        self.SQR3DC.setProperty("value", 0.5)
        self.SQR3DC.setObjectName(_fromUtf8("SQR3DC"))
        self.gridLayout_4.addWidget(self.SQR3DC, 3, 2, 1, 1)
        self.label_34 = QtGui.QLabel(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout_4.addWidget(self.label_34, 3, 0, 1, 1)
        self.line = QtGui.QFrame(self.Frame_4)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_4.addWidget(self.line, 5, 0, 1, 3)
        self.pushButton_6 = QtGui.QPushButton(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_4.addWidget(self.pushButton_6, 6, 2, 1, 1)
        self.label_35 = QtGui.QLabel(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.gridLayout_4.addWidget(self.label_35, 4, 0, 1, 1)
        self.label_20 = QtGui.QLabel(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_4.addWidget(self.label_20, 0, 1, 1, 1)
        self.label_33 = QtGui.QLabel(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout_4.addWidget(self.label_33, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.Frame_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 6, 0, 1, 1)
        self.label_19 = QtGui.QLabel(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)
        self.SQR3P = QtGui.QDoubleSpinBox(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SQR3P.sizePolicy().hasHeightForWidth())
        self.SQR3P.setSizePolicy(sizePolicy)
        self.SQR3P.setDecimals(3)
        self.SQR3P.setMaximum(360.0)
        self.SQR3P.setSingleStep(1.0)
        self.SQR3P.setProperty("value", 0.0)
        self.SQR3P.setObjectName(_fromUtf8("SQR3P"))
        self.gridLayout_4.addWidget(self.SQR3P, 3, 1, 1, 1)
        self.SQR2P = QtGui.QDoubleSpinBox(self.Frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SQR2P.sizePolicy().hasHeightForWidth())
        self.SQR2P.setSizePolicy(sizePolicy)
        self.SQR2P.setDecimals(3)
        self.SQR2P.setMaximum(360.0)
        self.SQR2P.setSingleStep(1.0)
        self.SQR2P.setProperty("value", 0.0)
        self.SQR2P.setObjectName(_fromUtf8("SQR2P"))
        self.gridLayout_4.addWidget(self.SQR2P, 2, 1, 1, 1)
        self.toolButton = QtGui.QToolButton(self.Frame_4)
        self.toolButton.setMinimumSize(QtCore.QSize(0, 0))
        self.toolButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.toolButton.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid red;\n"
""))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.gridLayout_4.addWidget(self.toolButton, 1, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.Frame_4)
        self.verticalLayout.addWidget(self.frame_7)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.setSQRS)
        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.fireSQR1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.frame_7.setProperty("class", _translate("Form", "ControlWidget", None))
        self.label_4.setText(_translate("Form", "Configure PWM ( sine waves will be disabled )", None))
        self.Frame_4.setProperty("class", _translate("Form", "ControlWidgetInner", None))
        self.label_21.setText(_translate("Form", "Duty Cycle", None))
        self.label_22.setText(_translate("Form", "0", None))
        self.label_34.setText(_translate("Form", "SQR3", None))
        self.pushButton_6.setText(_translate("Form", "SET", None))
        self.label_35.setText(_translate("Form", "SQR4", None))
        self.label_20.setText(_translate("Form", "Phase", None))
        self.label_33.setText(_translate("Form", "SQR2", None))
        self.label.setText(_translate("Form", "Frequency", None))
        self.label_19.setText(_translate("Form", "Output", None))
        self.toolButton.setToolTip(_translate("Form", "Click to fire oscillating packets . IR remote", None))
        self.toolButton.setText(_translate("Form", "SQR1", None))

