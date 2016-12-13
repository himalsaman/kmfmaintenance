# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addSPOB.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

from Control.materialsControl import decreaseSparePartsInvQty
from Control.ouboundControl import OutBCode
from models.dbUtile import Employees, Customers
from models.ouboundModel import add_outbound
from models.sparePartsModel import select_spare_parts_bycode, select_all_spare_parts


class Ui_addSPOBDialog(QDialog):
	def __init__(self, obj):
		super(Ui_addSPOBDialog, self).__init__()
		self.obj = obj
		self.setupUi(self)

	def setupUi(self, addSPOBDialog):
		self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

		addSPOBDialog.setObjectName("addSPOBDialog")
		addSPOBDialog.resize(726, 266)
		self.label = QtWidgets.QLabel(addSPOBDialog)
		self.label.setGeometry(QtCore.QRect(10, 10, 150, 13))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(addSPOBDialog)
		self.label_2.setGeometry(QtCore.QRect(380, 16, 120, 13))
		self.label_2.setObjectName("label_2")
		self.spnameled = QtWidgets.QLineEdit(addSPOBDialog)
		self.spnameled.setEnabled(False)
		self.spnameled.setGeometry(QtCore.QRect(486, 14, 230, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.spnameled.setFont(font)
		self.spnameled.setStyleSheet("color: rgb(255, 0, 0);")
		self.spnameled.setObjectName("spnameled")
		self.spcodeled = QtWidgets.QLineEdit(addSPOBDialog)
		self.spcodeled.setEnabled(False)
		self.spcodeled.setGeometry(QtCore.QRect(418, 46, 90, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.spcodeled.setFont(font)
		self.spcodeled.setStyleSheet("color: rgb(255, 0, 0);")
		self.spcodeled.setObjectName("spcodeled")
		self.label_3 = QtWidgets.QLabel(addSPOBDialog)
		self.label_3.setGeometry(QtCore.QRect(383, 48, 30, 13))
		self.label_3.setObjectName("label_3")
		self.spinqtyled = QtWidgets.QLineEdit(addSPOBDialog)
		self.spinqtyled.setEnabled(False)
		self.spinqtyled.setGeometry(QtCore.QRect(596, 46, 80, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.spinqtyled.setFont(font)
		self.spinqtyled.setStyleSheet("color: rgb(255, 0, 0);")
		self.spinqtyled.setObjectName("spinqtyled")
		self.label_4 = QtWidgets.QLabel(addSPOBDialog)
		self.label_4.setGeometry(QtCore.QRect(517, 49, 80, 13))
		self.label_4.setObjectName("label_4")
		self.reqqtyled_2 = QtWidgets.QLineEdit(addSPOBDialog)
		self.reqqtyled_2.setGeometry(QtCore.QRect(466, 134, 150, 20))
		self.reqqtyled_2.setObjectName("reqqtyled_2")
		self.reqqtyled = QtWidgets.QLabel(addSPOBDialog)
		self.reqqtyled.setGeometry(QtCore.QRect(478, 113, 130, 13))
		self.reqqtyled.setObjectName("reqqtyled")
		self.spgencodeled = QtWidgets.QLineEdit(addSPOBDialog)
		self.spgencodeled.setEnabled(False)
		self.spgencodeled.setGeometry(QtCore.QRect(456, 76, 160, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.spgencodeled.setFont(font)
		self.spgencodeled.setStyleSheet("color: rgb(255, 0, 0);")
		self.spgencodeled.setObjectName("spgencodeled")
		self.label_6 = QtWidgets.QLabel(addSPOBDialog)
		self.label_6.setGeometry(QtCore.QRect(385, 79, 70, 13))
		self.label_6.setObjectName("label_6")
		self.line = QtWidgets.QFrame(addSPOBDialog)
		self.line.setGeometry(QtCore.QRect(380, 104, 340, 3))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.addbtn = QtWidgets.QPushButton(addSPOBDialog)
		self.addbtn.setGeometry(QtCore.QRect(465, 232, 70, 30))
		self.addbtn.setObjectName("addbtn")
		self.closebtn = QtWidgets.QPushButton(addSPOBDialog)
		self.closebtn.setGeometry(QtCore.QRect(555, 232, 70, 30))
		self.closebtn.setObjectName("closebtn")
		self.listView = QtWidgets.QListWidget(addSPOBDialog)
		self.listView.setGeometry(QtCore.QRect(8, 30, 360, 230))
		self.listView.setObjectName("listView")
		self.line_2 = QtWidgets.QFrame(addSPOBDialog)
		self.line_2.setGeometry(QtCore.QRect(374, 3, 3, 260))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.label_5 = QtWidgets.QLabel(addSPOBDialog)
		self.label_5.setGeometry(QtCore.QRect(521, 168, 40, 13))
		self.label_5.setObjectName("label_5")
		self.resonled = QtWidgets.QLineEdit(addSPOBDialog)
		self.resonled.setGeometry(QtCore.QRect(387, 189, 330, 20))
		self.resonled.setObjectName("resonled")
		self.line_3 = QtWidgets.QFrame(addSPOBDialog)
		self.line_3.setGeometry(QtCore.QRect(379, 221, 340, 3))
		self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		for item in select_all_spare_parts():
			self.listView.addItem(item.gen_code + " - " + item.name + '({})'.format(item.code))

		self.listView.itemClicked.connect(self.Clicked)
		self.addbtn.clicked.connect(self.do_add)
		self.closebtn.clicked.connect(self.close)

		self.retranslateUi(addSPOBDialog)
		QtCore.QMetaObject.connectSlotsByName(addSPOBDialog)

	def retranslateUi(self, addSPOBDialog):
		_translate = QtCore.QCoreApplication.translate
		addSPOBDialog.setWindowTitle(_translate("addSPOBDialog", "Add Spare Part Outbound"))
		self.label.setText(_translate("addSPOBDialog", "Select Spare Part From List :"))
		self.label_2.setText(_translate("addSPOBDialog", "Selected Spare Part :"))
		self.label_3.setText(_translate("addSPOBDialog", "Code :"))
		self.label_4.setText(_translate("addSPOBDialog", "Inventory QTY:"))
		self.reqqtyled.setText(_translate("addSPOBDialog", "How mauch qty you want ?"))
		self.label_6.setText(_translate("addSPOBDialog", "System Code :"))
		self.addbtn.setText(_translate("addSPOBDialog", "Add"))
		self.closebtn.setText(_translate("addSPOBDialog", "Close"))
		self.label_5.setText(_translate("addSPOBDialog", "Reason"))

	def Clicked(self, item):
		self.addbtn.setEnabled(True)
		code = before(item.text(), '-')
		if select_spare_parts_bycode(code):
			rawMat = select_spare_parts_bycode(code)
			self.spnameled.setText(rawMat.name)
			self.spcodeled.setText(rawMat.code)
			self.spinqtyled.setText(str(rawMat.inv_qty))
			self.spgencodeled.setText(rawMat.gen_code)
		return rawMat

	def do_add(self):
		datetimestr = datetime.now()
		timestampstr = datetimestr.strftime('%Y-%m-%d %H:%M:%S')
		code = self.spgencodeled.text()
		rawmat = select_spare_parts_bycode(code)
		qty = self.reqqtyled_2.text()
		reas = self.resonled.text()
		if qty != '' or reas != '':
			if type(self.obj) == Employees:
				add_outbound(OutBCode(), timestampstr, reas, None, self.obj.id, None
							 , rawmat.id, None, None, qty, 1)
			if type(self.obj) == Customers:
				add_outbound(OutBCode(), timestampstr, reas, self.obj.id, None, None
							 , rawmat.id, None, None, qty, 1)
			decreaseSparePartsInvQty(rawmat, int(qty))
			self.close()
			# print(str(OutBCode()))


def before(value, a):
	# Find first part and return slice before it.
	pos_a = value.find(a)
	if pos_a == -1: return ""
	return value[0:pos_a]


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myapp = Ui_addSPOBDialog()
	myapp.exec_()
