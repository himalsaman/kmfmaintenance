# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addSPBOMItem.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QDialog

from Control.bomItemControl import createNewBOMItem
from models.sparePartsModel import select_all_spare_parts, select_spare_parts_bycode


class Ui_addSPBOMItemDialog(QDialog):
	def __init__(self, bomObj, parent=None):
		super(Ui_addSPBOMItemDialog, self).__init__()
		self.bomObj = bomObj
		self.setupUi(self)

	def setupUi(self, addSPBOMItemDialog):
		self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

		addSPBOMItemDialog.setObjectName("addSPBOMItemDialog")
		addSPBOMItemDialog.resize(726, 231)
		self.label = QtWidgets.QLabel(addSPBOMItemDialog)
		self.label.setGeometry(QtCore.QRect(10, 10, 150, 13))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(addSPBOMItemDialog)
		self.label_2.setGeometry(QtCore.QRect(380, 30, 120, 13))
		self.label_2.setObjectName("label_2")
		self.spnameled = QtWidgets.QLineEdit(addSPBOMItemDialog)
		self.spnameled.setEnabled(False)
		self.spnameled.setGeometry(QtCore.QRect(486, 28, 230, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.spnameled.setFont(font)
		self.spnameled.setStyleSheet("color: rgb(255, 0, 0);")
		self.spnameled.setObjectName("spnameled")
		self.spcodeled = QtWidgets.QLineEdit(addSPBOMItemDialog)
		self.spcodeled.setEnabled(False)
		self.spcodeled.setGeometry(QtCore.QRect(418, 60, 90, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.spcodeled.setFont(font)
		self.spcodeled.setStyleSheet("color: rgb(255, 0, 0);")
		self.spcodeled.setObjectName("spcodeled")
		self.label_3 = QtWidgets.QLabel(addSPBOMItemDialog)
		self.label_3.setGeometry(QtCore.QRect(383, 62, 30, 13))
		self.label_3.setObjectName("label_3")
		self.spinqtyled = QtWidgets.QLineEdit(addSPBOMItemDialog)
		self.spinqtyled.setEnabled(False)
		self.spinqtyled.setGeometry(QtCore.QRect(596, 60, 80, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.spinqtyled.setFont(font)
		self.spinqtyled.setStyleSheet("color: rgb(255, 0, 0);")
		self.spinqtyled.setObjectName("spinqtyled")
		self.label_4 = QtWidgets.QLabel(addSPBOMItemDialog)
		self.label_4.setGeometry(QtCore.QRect(517, 63, 80, 13))
		self.label_4.setObjectName("label_4")
		self.reqqtyled_2 = QtWidgets.QLineEdit(addSPBOMItemDialog)
		self.reqqtyled_2.setGeometry(QtCore.QRect(466, 145, 150, 20))
		self.reqqtyled_2.setObjectName("reqqtyled_2")
		self.reqqtyled_2.setValidator(QDoubleValidator())
		self.reqqtyled = QtWidgets.QLabel(addSPBOMItemDialog)
		self.reqqtyled.setGeometry(QtCore.QRect(478, 127, 130, 13))
		self.reqqtyled.setObjectName("reqqtyled")
		self.spgencodeled = QtWidgets.QLineEdit(addSPBOMItemDialog)
		self.spgencodeled.setEnabled(False)
		self.spgencodeled.setGeometry(QtCore.QRect(456, 90, 160, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.spgencodeled.setFont(font)
		self.spgencodeled.setStyleSheet("color: rgb(255, 0, 0);")
		self.spgencodeled.setObjectName("spgencodeled")
		self.label_6 = QtWidgets.QLabel(addSPBOMItemDialog)
		self.label_6.setGeometry(QtCore.QRect(385, 93, 70, 13))
		self.label_6.setObjectName("label_6")
		self.line = QtWidgets.QFrame(addSPBOMItemDialog)
		self.line.setGeometry(QtCore.QRect(385, 118, 330, 3))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.addbtn = QtWidgets.QPushButton(addSPBOMItemDialog)
		self.addbtn.setGeometry(QtCore.QRect(458, 190, 70, 30))
		self.addbtn.setObjectName("addbtn")
		self.addbtn.setEnabled(False)
		self.addbtn.clicked.connect(self.do_add)
		self.closebtn = QtWidgets.QPushButton(addSPBOMItemDialog)
		self.closebtn.setGeometry(QtCore.QRect(548, 190, 70, 30))
		self.closebtn.setObjectName("closebtn")
		self.closebtn.clicked.connect(self.close)
		self.listView = QtWidgets.QListWidget(addSPBOMItemDialog)
		self.listView.setGeometry(QtCore.QRect(10, 30, 360, 192))
		self.listView.setObjectName("listView")
		for item in select_all_spare_parts():
			self.listView.addItem(item.gen_code + " - ( " + item.code + " ) " + item.name)
		self.listView.itemClicked.connect(self.Clicked)
		self.line_2 = QtWidgets.QFrame(addSPBOMItemDialog)
		self.line_2.setGeometry(QtCore.QRect(374, 6, 3, 220))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.statulbl = QtWidgets.QLabel(addSPBOMItemDialog)
		self.statulbl.setGeometry(QtCore.QRect(465, 155, 150, 41))
		self.statulbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.statulbl.setAlignment(QtCore.Qt.AlignCenter)
		self.statulbl.setText("")
		self.statulbl.setAlignment(QtCore.Qt.AlignCenter)
		self.statulbl.setObjectName("statulbl")
		self.retranslateUi(addSPBOMItemDialog)
		QtCore.QMetaObject.connectSlotsByName(addSPBOMItemDialog)

	def retranslateUi(self, addSPBOMItemDialog):
		_translate = QtCore.QCoreApplication.translate
		addSPBOMItemDialog.setWindowTitle(_translate("addSPBOMItemDialog", "Add Spare Part As BOM Item"))
		self.label.setText(_translate("addSPBOMItemDialog", "Select Spare Part From List :"))
		self.label_2.setText(_translate("addSPBOMItemDialog", "Selected Spare Part :"))
		self.label_3.setText(_translate("addSPBOMItemDialog", "Code :"))
		self.label_4.setText(_translate("addSPBOMItemDialog", "Inventory QTY:"))
		self.reqqtyled.setText(_translate("addSPBOMItemDialog", "How mauch qty you want ?"))
		self.label_6.setText(_translate("addSPBOMItemDialog", "System Code :"))
		self.addbtn.setText(_translate("addSPBOMItemDialog", "Add"))
		self.closebtn.setText(_translate("addSPBOMItemDialog", "Close"))

	def Clicked(self, item):
		self.addbtn.setEnabled(True)
		code = before(item.text(), '-')
		if select_spare_parts_bycode(code):
			spare = select_spare_parts_bycode(code)
			self.spcodeled.setText(spare.code)
			self.spnameled.setText(spare.name)
			self.spgencodeled.setText(str(spare.gen_code))
			self.spinqtyled.setText(str(spare.inv_qty))
		return spare

	def do_add(self):
		code = self.spgencodeled.text()
		spare = select_spare_parts_bycode(code)
		qty = self.reqqtyled_2.text()
		if not qty == '':
			self.close()
			createNewBOMItem(self.bomObj.id, None, spare.id, int(qty))
		else:
			self.statulbl.setText("You must enter quantity you want")


def before(value, a):
	# Find first part and return slice before it.
	pos_a = value.find(a)
	if pos_a == -1: return ""
	return value[0:pos_a]
