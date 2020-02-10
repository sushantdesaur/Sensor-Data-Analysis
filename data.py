# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Data_Settings(object):
    def setupUi(self, Data_Settings):
        Data_Settings.setObjectName(_fromUtf8("Data_Settings"))
        Data_Settings.resize(511, 214)
        self.formLayout = QtGui.QFormLayout(Data_Settings)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Data_Settings)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit_StartByte = QtGui.QLineEdit(Data_Settings)
        self.lineEdit_StartByte.setObjectName(_fromUtf8("lineEdit_StartByte"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_StartByte)
        self.label_2 = QtGui.QLabel(Data_Settings)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_EndByte = QtGui.QLineEdit(Data_Settings)
        self.lineEdit_EndByte.setObjectName(_fromUtf8("lineEdit_EndByte"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_EndByte)
        self.label_3 = QtGui.QLabel(Data_Settings)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_Seperator = QtGui.QLineEdit(Data_Settings)
        self.lineEdit_Seperator.setObjectName(_fromUtf8("lineEdit_Seperator"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_Seperator)
        self.label_4 = QtGui.QLabel(Data_Settings)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_4)
        self.comboBox_Checksum = QtGui.QComboBox(Data_Settings)
        self.comboBox_Checksum.setObjectName(_fromUtf8("comboBox_Checksum"))
        self.comboBox_Checksum.addItem(_fromUtf8(""))
        self.comboBox_Checksum.addItem(_fromUtf8(""))
        self.comboBox_Checksum.addItem(_fromUtf8(""))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.comboBox_Checksum)
        self.label_5 = QtGui.QLabel(Data_Settings)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_5)
        self.comboBox_Parameters = QtGui.QComboBox(Data_Settings)
        self.comboBox_Parameters.setObjectName(_fromUtf8("comboBox_Parameters"))
        self.comboBox_Parameters.addItem(_fromUtf8(""))
        self.comboBox_Parameters.addItem(_fromUtf8(""))
        self.comboBox_Parameters.addItem(_fromUtf8(""))
        self.comboBox_Parameters.addItem(_fromUtf8(""))
        self.comboBox_Parameters.addItem(_fromUtf8(""))
        self.comboBox_Parameters.addItem(_fromUtf8(""))
        self.comboBox_Parameters.addItem(_fromUtf8(""))
        self.comboBox_Parameters.addItem(_fromUtf8(""))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.comboBox_Parameters)
        self.pushButton_Parameter = QtGui.QPushButton(Data_Settings)
        self.pushButton_Parameter.setObjectName(_fromUtf8("pushButton_Parameter"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.pushButton_Parameter)
        self.buttonBox = QtGui.QDialogButtonBox(Data_Settings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(Data_Settings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Data_Settings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Data_Settings.reject)
        QtCore.QMetaObject.connectSlotsByName(Data_Settings)

    def retranslateUi(self, Data_Settings):
        Data_Settings.setWindowTitle(_translate("Data_Settings", "Dialog", None))
        self.label.setText(_translate("Data_Settings", "Start Byte", None))
        self.label_2.setText(_translate("Data_Settings", "End Byte", None))
        self.label_3.setText(_translate("Data_Settings", "Seperator", None))
        self.label_4.setText(_translate("Data_Settings", "Checksum", None))
        self.comboBox_Checksum.setItemText(0, _translate("Data_Settings", "CRC", None))
        self.comboBox_Checksum.setItemText(1, _translate("Data_Settings", "EXOR", None))
        self.comboBox_Checksum.setItemText(2, _translate("Data_Settings", "CRICTT", None))
        self.label_5.setText(_translate("Data_Settings", "Parameters", None))
        self.comboBox_Parameters.setItemText(0, _translate("Data_Settings", "1", None))
        self.comboBox_Parameters.setItemText(1, _translate("Data_Settings", "2", None))
        self.comboBox_Parameters.setItemText(2, _translate("Data_Settings", "3", None))
        self.comboBox_Parameters.setItemText(3, _translate("Data_Settings", "4", None))
        self.comboBox_Parameters.setItemText(4, _translate("Data_Settings", "5", None))
        self.comboBox_Parameters.setItemText(5, _translate("Data_Settings", "6", None))
        self.comboBox_Parameters.setItemText(6, _translate("Data_Settings", "7", None))
        self.comboBox_Parameters.setItemText(7, _translate("Data_Settings", "8", None))
        self.pushButton_Parameter.setText(_translate("Data_Settings", "Set Parameters", None))

