# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(581, 627)
        self.formLayout = QtGui.QFormLayout(Dialog)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit_Name = QtGui.QLineEdit(Dialog)
        self.lineEdit_Name.setObjectName(_fromUtf8("lineEdit_Name"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_Name)
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_Username = QtGui.QLineEdit(Dialog)
        self.lineEdit_Username.setText(_fromUtf8(""))
        self.lineEdit_Username.setObjectName(_fromUtf8("lineEdit_Username"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_Username)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_Email = QtGui.QLineEdit(Dialog)
        self.lineEdit_Email.setObjectName(_fromUtf8("lineEdit_Email"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_Email)
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_Password = QtGui.QLineEdit(Dialog)
        self.lineEdit_Password.setText(_fromUtf8(""))
        self.lineEdit_Password.setObjectName(_fromUtf8("lineEdit_Password"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_Password)
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.label_11)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_DOB = QtGui.QLineEdit(Dialog)
        self.lineEdit_DOB.setText(_fromUtf8(""))
        self.lineEdit_DOB.setObjectName(_fromUtf8("lineEdit_DOB"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_DOB)
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.label_10)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_2)
        self.textEdit_Address = QtGui.QTextEdit(Dialog)
        self.textEdit_Address.setObjectName(_fromUtf8("textEdit_Address"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.textEdit_Address)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.SpanningRole, self.label_5)
        self.lineEdit_Designation = QtGui.QLineEdit(Dialog)
        self.lineEdit_Designation.setObjectName(_fromUtf8("lineEdit_Designation"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.lineEdit_Designation)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_PhoneNo = QtGui.QLineEdit(Dialog)
        self.lineEdit_PhoneNo.setObjectName(_fromUtf8("lineEdit_PhoneNo"))
        self.formLayout.setWidget(13, QtGui.QFormLayout.FieldRole, self.lineEdit_PhoneNo)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(14, QtGui.QFormLayout.SpanningRole, self.label_4)
        self.lineEdit_Qualification = QtGui.QLineEdit(Dialog)
        self.lineEdit_Qualification.setObjectName(_fromUtf8("lineEdit_Qualification"))
        self.formLayout.setWidget(15, QtGui.QFormLayout.FieldRole, self.lineEdit_Qualification)
        self.lineEdit_UserId = QtGui.QLineEdit(Dialog)
        self.lineEdit_UserId.setObjectName(_fromUtf8("lineEdit_UserId"))
        self.formLayout.setWidget(19, QtGui.QFormLayout.FieldRole, self.lineEdit_UserId)
        self.saveRegisteration_btn = QtGui.QDialogButtonBox(Dialog)
        self.saveRegisteration_btn.setOrientation(QtCore.Qt.Horizontal)
        self.saveRegisteration_btn.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.saveRegisteration_btn.setObjectName(_fromUtf8("saveRegisteration_btn"))
        self.formLayout.setWidget(20, QtGui.QFormLayout.FieldRole, self.saveRegisteration_btn)
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout.setWidget(18, QtGui.QFormLayout.LabelRole, self.label_12)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.saveRegisteration_btn, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.saveRegisteration_btn, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Name", None))
        self.label_8.setText(_translate("Dialog", "Username", None))
        self.label_6.setText(_translate("Dialog", "Email", None))
        self.label_9.setText(_translate("Dialog", "Password", None))
        self.label_11.setText(_translate("Dialog", "8 Characters", None))
        self.label_7.setText(_translate("Dialog", "D.O.B.", None))
        self.label_10.setText(_translate("Dialog", "DD/MM/YYYY", None))
        self.label_2.setText(_translate("Dialog", "Address", None))
        self.label_5.setText(_translate("Dialog", "Designation ", None))
        self.label_3.setText(_translate("Dialog", "Phone No.", None))
        self.label_4.setText(_translate("Dialog", "Qualification", None))
        self.label_12.setText(_translate("Dialog", "User Id", None))

