# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addFPOB.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

from Control.materialsControl import decreaseFinishProductInvQty
from Control.ouboundControl import OutBCode
from models.dbUtile import Employees, Customers
from models.finishProductsModel import select_all_finish_product, select_finish_product_by_gen_code
from models.ouboundModel import add_outbound


class Ui_addFPOBDialog(QDialog):
	def __init__(self, obj):
		super(Ui_addFPOBDialog, self).__init__()
		self.obj = obj
		self.setupUi(self)

	def setupUi(self, addFPOBDialog):
		self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
		addFPOBDialog.setObjectName("addFPOBDialog")
		addFPOBDialog.resize(726, 244)
		self.label = QtWidgets.QLabel(addFPOBDialog)
		self.label.setGeometry(QtCore.QRect(10, 10, 150, 13))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(addFPOBDialog)
		self.label_2.setGeometry(QtCore.QRect(380, 14, 120, 13))
		self.label_2.setObjectName("label_2")
		self.spnameled = QtWidgets.QLineEdit(addFPOBDialog)
		self.spnameled.setEnabled(False)
		self.spnameled.setGeometry(QtCore.QRect(486, 12, 230, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.spnameled.setFont(font)
		self.spnameled.setStyleSheet("color: rgb(255, 0, 0);")
		self.spnameled.setObjectName("spnameled")
		self.spcodeled = QtWidgets.QLineEdit(addFPOBDialog)
		self.spcodeled.setEnabled(False)
		self.spcodeled.setGeometry(QtCore.QRect(418, 44, 90, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.spcodeled.setFont(font)
		self.spcodeled.setStyleSheet("color: rgb(255, 0, 0);")
		self.spcodeled.setObjectName("spcodeled")
		self.label_3 = QtWidgets.QLabel(addFPOBDialog)
		self.label_3.setGeometry(QtCore.QRect(383, 46, 30, 13))
		self.label_3.setObjectName("label_3")
		self.spinqtyled = QtWidgets.QLineEdit(addFPOBDialog)
		self.spinqtyled.setEnabled(False)
		self.spinqtyled.setGeometry(QtCore.QRect(596, 44, 80, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.spinqtyled.setFont(font)
		self.spinqtyled.setStyleSheet("color: rgb(255, 0, 0);")
		self.spinqtyled.setObjectName("spinqtyled")
		self.label_4 = QtWidgets.QLabel(addFPOBDialog)
		self.label_4.setGeometry(QtCore.QRect(517, 47, 80, 13))
		self.label_4.setObjectName("label_4")
		self.reqqtyled_2 = QtWidgets.QLineEdit(addFPOBDialog)
		self.reqqtyled_2.setGeometry(QtCore.QRect(466, 125, 150, 20))
		self.reqqtyled_2.setObjectName("reqqtyled_2")
		self.reqqtyled = QtWidgets.QLabel(addFPOBDialog)
		self.reqqtyled.setGeometry(QtCore.QRect(478, 106, 130, 13))
		self.reqqtyled.setObjectName("reqqtyled")
		self.spgencodeled = QtWidgets.QLineEdit(addFPOBDialog)
		self.spgencodeled.setEnabled(False)
		self.spgencodeled.setGeometry(QtCore.QRect(456, 74, 160, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.spgencodeled.setFont(font)
		self.spgencodeled.setStyleSheet("color: rgb(255, 0, 0);")
		self.spgencodeled.setObjectName("spgencodeled")
		self.label_6 = QtWidgets.QLabel(addFPOBDialog)
		self.label_6.setGeometry(QtCore.QRect(385, 77, 70, 13))
		self.label_6.setObjectName("label_6")
		self.line = QtWidgets.QFrame(addFPOBDialog)
		self.line.setGeometry(QtCore.QRect(385, 101, 330, 3))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.addbtn = QtWidgets.QPushButton(addFPOBDialog)
		self.addbtn.setGeometry(QtCore.QRect(461, 211, 70, 30))
		self.addbtn.setObjectName("addbtn")
		self.closebtn = QtWidgets.QPushButton(addFPOBDialog)
		self.closebtn.setGeometry(QtCore.QRect(551, 211, 70, 30))
		self.closebtn.setObjectName("closebtn")
		self.listView = QtWidgets.QListWidget(addFPOBDialog)
		self.listView.setGeometry(QtCore.QRect(10, 27, 360, 211))
		self.listView.setObjectName("listView")
		self.line_2 = QtWidgets.QFrame(addFPOBDialog)
		self.line_2.setGeometry(QtCore.QRect(374, 6, 3, 230))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.label_5 = QtWidgets.QLabel(addFPOBDialog)
		self.label_5.setGeometry(QtCore.QRect(520, 154, 47, 13))
		self.label_5.setObjectName("label_5")
		self.reasonled = QtWidgets.QLineEdit(addFPOBDialog)
		self.reasonled.setGeometry(QtCore.QRect(387, 173, 330, 20))
		self.reasonled.setObjectName("reasonled")
		self.line_3 = QtWidgets.QFrame(addFPOBDialog)
		self.line_3.setGeometry(QtCore.QRect(380, 204, 340, 3))
		self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		for item in select_all_finish_product():
			self.listView.addItem(item.gen_code + " - " + item.name + '({})'.format(item.code))

		self.listView.itemClicked.connect(self.Clicked)
		self.addbtn.clicked.connect(self.do_add)
		self.closebtn.clicked.connect(self.close)

		self.retranslateUi(addFPOBDialog)
		QtCore.QMetaObject.connectSlotsByName(addFPOBDialog)

	def retranslateUi(self, addFPOBDialog):
		_translate = QtCore.QCoreApplication.translate
		addFPOBDialog.setWindowTitle(_translate("addFPOBDialog", "Add Finish Product Outbound"))
		self.label.setText(_translate("addFPOBDialog", "Select Spare Part From List :"))
		self.label_2.setText(_translate("addFPOBDialog", "Selected Spare Part :"))
		self.label_3.setText(_translate("addFPOBDialog", "Code :"))
		self.label_4.setText(_translate("addFPOBDialog", "Inventory QTY:"))
		self.reqqtyled.setText(_translate("addFPOBDialog", "How mauch qty you want ?"))
		self.label_6.setText(_translate("addFPOBDialog", "System Code :"))
		self.addbtn.setText(_translate("addFPOBDialog", "Add"))
		self.closebtn.setText(_translate("addFPOBDialog", "Close"))
		self.label_5.setText(_translate("addFPOBDialog", "Reason"))

	#
	def Clicked(self, item):
		self.addbtn.setEnabled(True)
		code = before(item.text(), '-')
		if select_finish_product_by_gen_code(code):
			rawMat = select_finish_product_by_gen_code(code)
			self.spnameled.setText(rawMat.name)
			self.spcodeled.setText(rawMat.code)
			self.spinqtyled.setText(str(rawMat.inv_qty))
			self.spgencodeled.setText(rawMat.gen_code)
		return rawMat

	#
	def do_add(self):
		datetimestr = datetime.now()
		timestampstr = datetimestr.strftime('%Y-%m-%d %H:%M:%S')
		code = self.spgencodeled.text()
		rawmat = select_finish_product_by_gen_code(code)
		qty = self.reqqtyled_2.text()
		reas = self.reasonled.text()
		if qty != '' or reas != '':
			if type(self.obj) == Employees:
				add_outbound(OutBCode(), timestampstr, reas, None, self.obj.id, None
							 , None, None, rawmat.id, qty, 1)
			if type(self.obj) == Customers:
				add_outbound(OutBCode(), timestampstr, reas, self.obj.id, None, None
							 , None, None, rawmat.id, qty, 1)
			decreaseFinishProductInvQty(rawmat, int(qty))
			self.close()
			# print(str(OutBCode()))


def before(value, a):
	# Find first part and return slice before it.
	pos_a = value.find(a)
	if pos_a == -1: return ""
	return value[0:pos_a]

