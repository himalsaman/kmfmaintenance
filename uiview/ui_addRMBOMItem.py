# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addRMBOMItem.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

from Control.bomItemControl import createNewBOMItem
from models.rawMaterialModel import select_all_raw_material, select_row_material_bycode


class Ui_addRMBOMItemDialog(QDialog):
	def __init__(self, bomObj,parent=None):
		super(Ui_addRMBOMItemDialog, self).__init__()
		self.bomObj = bomObj
		self.setupUi(self)

	def setupUi(self, addRMBOMItemDialog):
		addRMBOMItemDialog.setObjectName("addRMBOMItemDialog")
		addRMBOMItemDialog.resize(726, 231)
		self.label = QtWidgets.QLabel(addRMBOMItemDialog)
		self.label.setGeometry(QtCore.QRect(10, 10, 150, 13))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(addRMBOMItemDialog)
		self.label_2.setGeometry(QtCore.QRect(380, 30, 120, 13))
		self.label_2.setObjectName("label_2")
		self.rmnameled = QtWidgets.QLineEdit(addRMBOMItemDialog)
		self.rmnameled.setEnabled(False)
		self.rmnameled.setGeometry(QtCore.QRect(495, 28, 220, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.rmnameled.setFont(font)
		self.rmnameled.setStyleSheet("color: rgb(255, 0, 0);")
		self.rmnameled.setObjectName("rmnameled")
		self.rmcodeled = QtWidgets.QLineEdit(addRMBOMItemDialog)
		self.rmcodeled.setEnabled(False)
		self.rmcodeled.setGeometry(QtCore.QRect(418, 60, 90, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.rmcodeled.setFont(font)
		self.rmcodeled.setStyleSheet("color: rgb(255, 0, 0);")
		self.rmcodeled.setObjectName("rmcodeled")
		self.label_3 = QtWidgets.QLabel(addRMBOMItemDialog)
		self.label_3.setGeometry(QtCore.QRect(383, 62, 30, 13))
		self.label_3.setObjectName("label_3")
		self.rminqtyled = QtWidgets.QLineEdit(addRMBOMItemDialog)
		self.rminqtyled.setEnabled(False)
		self.rminqtyled.setGeometry(QtCore.QRect(596, 60, 80, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.rminqtyled.setFont(font)
		self.rminqtyled.setStyleSheet("color: rgb(255, 0, 0);")
		self.rminqtyled.setObjectName("rminqtyled")
		self.label_4 = QtWidgets.QLabel(addRMBOMItemDialog)
		self.label_4.setGeometry(QtCore.QRect(517, 63, 80, 13))
		self.label_4.setObjectName("label_4")
		self.reqqtyled_2 = QtWidgets.QLineEdit(addRMBOMItemDialog)
		self.reqqtyled_2.setGeometry(QtCore.QRect(466, 145, 150, 20))
		self.reqqtyled_2.setObjectName("reqqtyled_2")
		self.reqqtyled = QtWidgets.QLabel(addRMBOMItemDialog)
		self.reqqtyled.setGeometry(QtCore.QRect(478, 127, 130, 13))
		self.reqqtyled.setObjectName("reqqtyled")
		self.rmdefaultsizeled = QtWidgets.QLineEdit(addRMBOMItemDialog)
		self.rmdefaultsizeled.setEnabled(False)
		self.rmdefaultsizeled.setGeometry(QtCore.QRect(452, 90, 160, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.rmdefaultsizeled.setFont(font)
		self.rmdefaultsizeled.setStyleSheet("color: rgb(255, 0, 0);")
		self.rmdefaultsizeled.setObjectName("rmdefaultsizeled")
		self.label_6 = QtWidgets.QLabel(addRMBOMItemDialog)
		self.label_6.setGeometry(QtCore.QRect(385, 93, 70, 13))
		self.label_6.setObjectName("label_6")
		self.line = QtWidgets.QFrame(addRMBOMItemDialog)
		self.line.setGeometry(QtCore.QRect(385, 118, 330, 3))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.addbtn = QtWidgets.QPushButton(addRMBOMItemDialog)
		self.addbtn.setGeometry(QtCore.QRect(458, 190, 70, 30))
		self.addbtn.setObjectName("addbtn")
		self.addbtn.setEnabled(False)
		self.addbtn.clicked.connect(self.do_add)

		self.closebtn = QtWidgets.QPushButton(addRMBOMItemDialog)
		self.closebtn.setGeometry(QtCore.QRect(548, 190, 70, 30))
		self.closebtn.setObjectName("closebtn")

		self.closebtn.clicked.connect(self.close)

		self.listView = QtWidgets.QListWidget(addRMBOMItemDialog)
		self.listView.setGeometry(QtCore.QRect(10, 30, 360, 192))
		self.listView.setObjectName("listView")

		for item in select_all_raw_material():
			self.listView.addItem(item.code + " - " + item.name)
		self.listView.itemClicked.connect(self.Clicked)

		self.line_2 = QtWidgets.QFrame(addRMBOMItemDialog)
		self.line_2.setGeometry(QtCore.QRect(374, 6, 3, 220))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")

		self.statulbl = QtWidgets.QLabel(addRMBOMItemDialog)
		self.statulbl.setGeometry(QtCore.QRect(440, 155, 200, 41))
		self.statulbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.statulbl.setAlignment(QtCore.Qt.AlignCenter)
		self.statulbl.setText("")
		self.statulbl.setAlignment(QtCore.Qt.AlignCenter)
		self.statulbl.setObjectName("statulbl")

		self.retranslateUi(addRMBOMItemDialog)
		QtCore.QMetaObject.connectSlotsByName(addRMBOMItemDialog)

	def retranslateUi(self, addRMBOMItemDialog):
		_translate = QtCore.QCoreApplication.translate
		addRMBOMItemDialog.setWindowTitle(_translate("addRMBOMItemDialog", "Add Row Material As BOM Item"))
		self.label.setText(_translate("addRMBOMItemDialog", "Select Raw Material From List :"))
		self.label_2.setText(_translate("addRMBOMItemDialog", "Selected Raw Material :"))
		self.label_3.setText(_translate("addRMBOMItemDialog", "Code :"))
		self.label_4.setText(_translate("addRMBOMItemDialog", "Inventory QTY:"))
		self.reqqtyled.setText(_translate("addRMBOMItemDialog", "How mauch qty you want ?"))
		self.label_6.setText(_translate("addRMBOMItemDialog", "Default Size :"))
		self.addbtn.setText(_translate("addRMBOMItemDialog", "Add"))
		self.closebtn.setText(_translate("addRMBOMItemDialog", "Close"))

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
		code = self.rmcodeled.text()
		rawmat = select_row_material_bycode(code)
		qty = self.reqqtyled_2.text()
		if not qty == '':
			# print(self.bomObj)
			self.close()
			createNewBOMItem(self.bomObj.id,rawmat.id, None, int(qty))
		else:
			self.statulbl.setText("You must enter quantity you want")



def before(value, a):
	# Find first part and return slice before it.
	pos_a = value.find(a)
	if pos_a == -1: return ""
	return value[0:pos_a]


if __name__ == "__main__":
	cnc_dialog = Ui_addRMBOMItemDialog()
	cnc_dialog.show()
