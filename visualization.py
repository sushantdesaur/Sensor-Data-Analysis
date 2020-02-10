# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Visualization.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(806, 705)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 3, 3, 1, 1)
        self.dateTimeEdit = QtGui.QDateTimeEdit(Form)
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.gridLayout.addWidget(self.dateTimeEdit, 1, 0, 1, 2)
        self.dateTimeEdit_2 = QtGui.QDateTimeEdit(Form)
        self.dateTimeEdit_2.setObjectName(_fromUtf8("dateTimeEdit_2"))
        self.gridLayout.addWidget(self.dateTimeEdit_2, 1, 3, 1, 2)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 5)
        self.pushButton_Stats = QtGui.QPushButton(Form)
        self.pushButton_Stats.setObjectName(_fromUtf8("pushButton_Stats"))
        self.gridLayout.addWidget(self.pushButton_Stats, 3, 2, 1, 1)
        self.label_From = QtGui.QLabel(Form)
        self.label_From.setObjectName(_fromUtf8("label_From"))
        self.gridLayout.addWidget(self.label_From, 0, 0, 1, 1)
        self.label_To = QtGui.QLabel(Form)
        self.label_To.setObjectName(_fromUtf8("label_To"))
        self.gridLayout.addWidget(self.label_To, 0, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_2.setText(_translate("Form", "Exit", None))
        self.pushButton.setText(_translate("Form", "Load", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "S/N", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "T1", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "T2", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "T3", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "T4", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "T5", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Date", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Time", None))
        self.pushButton_Stats.setText(_translate("Form", "Stats", None))
        self.label_From.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">From</span></p></body></html>", None))
        self.label_To.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Till</span></p></body></html>", None))

