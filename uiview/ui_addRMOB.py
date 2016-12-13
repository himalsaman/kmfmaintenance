# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addRMOB.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

from Control.materialsControl import decreaseRawMaterialInvQty
from Control.ouboundControl import OutBCode
from models.dbUtile import Customers, Employees
from models.ouboundModel import add_outbound
from models.rawMaterialModel import select_all_raw_material, select_row_material_bycode


class Ui_addRMOBDialog(QDialog):
	def __init__(self, obj):
		super(Ui_addRMOBDialog, self).__init__()
		self.obj = obj
		self.setupUi(self)

	def setupUi(self, addRMOBDialog):
		self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

		addRMOBDialog.setObjectName("addRMOBDialog")
		addRMOBDialog.resize(726, 270)
		self.label = QtWidgets.QLabel(addRMOBDialog)
		self.label.setGeometry(QtCore.QRect(10, 10, 150, 13))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(addRMOBDialog)
		self.label_2.setGeometry(QtCore.QRect(380, 20, 120, 13))
		self.label_2.setObjectName("label_2")
		self.rmnameled = QtWidgets.QLineEdit(addRMOBDialog)
		self.rmnameled.setEnabled(False)
		self.rmnameled.setGeometry(QtCore.QRect(495, 18, 220, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.rmnameled.setFont(font)
		self.rmnameled.setStyleSheet("color: rgb(255, 0, 0);")
		self.rmnameled.setObjectName("rmnameled")
		self.rmcodeled = QtWidgets.QLineEdit(addRMOBDialog)
		self.rmcodeled.setEnabled(False)
		self.rmcodeled.setGeometry(QtCore.QRect(418, 50, 90, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.rmcodeled.setFont(font)
		self.rmcodeled.setStyleSheet("color: rgb(255, 0, 0);")
		self.rmcodeled.setObjectName("rmcodeled")
		self.label_3 = QtWidgets.QLabel(addRMOBDialog)
		self.label_3.setGeometry(QtCore.QRect(383, 54, 30, 13))
		self.label_3.setObjectName("label_3")
		self.rminqtyled = QtWidgets.QLineEdit(addRMOBDialog)
		self.rminqtyled.setEnabled(False)
		self.rminqtyled.setGeometry(QtCore.QRect(596, 50, 80, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.rminqtyled.setFont(font)
		self.rminqtyled.setStyleSheet("color: rgb(255, 0, 0);")
		self.rminqtyled.setObjectName("rminqtyled")
		self.label_4 = QtWidgets.QLabel(addRMOBDialog)
		self.label_4.setGeometry(QtCore.QRect(517, 53, 80, 13))
		self.label_4.setObjectName("label_4")
		self.reqqtyled_2 = QtWidgets.QLineEdit(addRMOBDialog)
		self.reqqtyled_2.setGeometry(QtCore.QRect(466, 138, 150, 20))
		self.reqqtyled_2.setObjectName("reqqtyled_2")
		self.reqqtyled = QtWidgets.QLabel(addRMOBDialog)
		self.reqqtyled.setGeometry(QtCore.QRect(478, 117, 130, 13))
		self.reqqtyled.setObjectName("reqqtyled")
		self.rmdefaultsizeled = QtWidgets.QLineEdit(addRMOBDialog)
		self.rmdefaultsizeled.setEnabled(False)
		self.rmdefaultsizeled.setGeometry(QtCore.QRect(452, 80, 160, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.rmdefaultsizeled.setFont(font)
		self.rmdefaultsizeled.setStyleSheet("color: rgb(255, 0, 0);")
		self.rmdefaultsizeled.setObjectName("rmdefaultsizeled")
		self.label_6 = QtWidgets.QLabel(addRMOBDialog)
		self.label_6.setGeometry(QtCore.QRect(385, 83, 70, 13))
		self.label_6.setObjectName("label_6")
		self.line = QtWidgets.QFrame(addRMOBDialog)
		self.line.setGeometry(QtCore.QRect(379, 108, 340, 3))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.addbtn = QtWidgets.QPushButton(addRMOBDialog)
		self.addbtn.setGeometry(QtCore.QRect(461, 233, 70, 30))
		self.addbtn.setObjectName("addbtn")
		self.closebtn = QtWidgets.QPushButton(addRMOBDialog)
		self.closebtn.setGeometry(QtCore.QRect(551, 233, 70, 30))
		self.closebtn.setObjectName("closebtn")
		self.listView = QtWidgets.QListWidget(addRMOBDialog)
		self.listView.setGeometry(QtCore.QRect(10, 30, 360, 230))
		self.listView.setObjectName("listView")
		self.line_2 = QtWidgets.QFrame(addRMOBDialog)
		self.line_2.setGeometry(QtCore.QRect(374, 6, 3, 260))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.reasonled = QtWidgets.QLineEdit(addRMOBDialog)
		self.reasonled.setGeometry(QtCore.QRect(387, 192, 330, 20))
		self.reasonled.setObjectName("reasonled")
		self.rlabel = QtWidgets.QLabel(addRMOBDialog)
		self.rlabel.setGeometry(QtCore.QRect(528, 172, 40, 13))
		self.rlabel.setObjectName("rlabel")
		self.line_3 = QtWidgets.QFrame(addRMOBDialog)
		self.line_3.setGeometry(QtCore.QRect(379, 227, 340, 3))
		self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		for item in select_all_raw_material():
			self.listView.addItem(item.code + " - " + item.name)

		self.listView.itemClicked.connect(self.Clicked)
		self.addbtn.clicked.connect(self.do_add)
		self.retranslateUi(addRMOBDialog)
		QtCore.QMetaObject.connectSlotsByName(addRMOBDialog)

	def retranslateUi(self, addRMOBDialog):
		_translate = QtCore.QCoreApplication.translate
		addRMOBDialog.setWindowTitle(_translate("addRMOBDialog", "Add Row Material Outbound"))
		self.label.setText(_translate("addRMOBDialog", "Select Raw Material From List :"))
		self.label_2.setText(_translate("addRMOBDialog", "Selected Raw Material :"))
		self.label_3.setText(_translate("addRMOBDialog", "Code :"))
		self.label_4.setText(_translate("addRMOBDialog", "Inventory QTY:"))
		self.reqqtyled.setText(_translate("addRMOBDialog", "How mauch qty you want ?"))
		self.label_6.setText(_translate("addRMOBDialog", "Default Size :"))
		self.addbtn.setText(_translate("addRMOBDialog", "Add"))
		self.closebtn.setText(_translate("addRMOBDialog", "Close"))
		self.rlabel.setText(_translate("addRMOBDialog", "Reason"))

	def Clicked(self, item):
		self.addbtn.setEnabled(True)
		code = before(item.text(), '-')
		if select_row_material_bycode(code):
			rawMat = select_row_material_bycode(code)
			self.rmcodeled.setText(rawMat.code)
			self.rmnameled.setText(rawMat.name)
			self.rmdefaultsizeled.setText(str(rawMat.default_size))
			self.rminqtyled.setText(str(rawMat.inv_qty))
		return rawMat

	def do_add(self):
		datetimestr = datetime.now()
		timestampstr = datetimestr.strftime('%Y-%m-%d %H:%M:%S')
		code = self.rmcodeled.text()
		rawmat = select_row_material_bycode(code)
		qty = self.reqqtyled_2.text()
		reas = self.reasonled.text()
		if qty != '' or reas != '':
			if type(self.obj) == Employees:
				add_outbound(OutBCode(), timestampstr, reas, None, self.obj.id, rawmat.id
							 , None, None, None, qty, 1)
			if type(self.obj) == Customers:
				add_outbound(OutBCode(), timestampstr, reas, self.obj.id, None, rawmat.id
							 , None, None, None, qty, 1)
			decreaseRawMaterialInvQty(rawmat, int(qty))
			self.do_close()
			# print(str(OutBCode()))

	def do_close(self):
		self.close()


def before(value, a):
	# Find first part and return slice before it.
	pos_a = value.find(a)
	if pos_a == -1: return ""
	return value[0:pos_a]


# if __name__ == '__main__':
# 	app = QtWidgets.QApplication(sys.argv)
# 	myapp = Ui_addRMOBDialog()
# 	myapp.show()
# 	myapp.exec_()
