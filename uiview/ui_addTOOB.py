# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addTOOB.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

from Control.materialsControl import decreaseToolsInvQty
from Control.ouboundControl import OutBCode
from models.dbUtile import Employees, Customers
from models.ouboundModel import add_outbound
from models.toolsModel import select_tools_by_gen_code, select_all_tools


class Ui_addTOOBDialog(QDialog):
	def __init__(self, obj):
		super(Ui_addTOOBDialog, self).__init__()
		self.obj = obj
		self.setupUi(self)

	def setupUi(self, addTOOBDialog):
		self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

		addTOOBDialog.setObjectName("addTOOBDialog")
		addTOOBDialog.resize(726, 240)
		self.label = QtWidgets.QLabel(addTOOBDialog)
		self.label.setGeometry(QtCore.QRect(10, 10, 150, 13))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(addTOOBDialog)
		self.label_2.setGeometry(QtCore.QRect(380, 16, 120, 13))
		self.label_2.setObjectName("label_2")
		self.spnameled = QtWidgets.QLineEdit(addTOOBDialog)
		self.spnameled.setEnabled(False)
		self.spnameled.setGeometry(QtCore.QRect(486, 14, 230, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.spnameled.setFont(font)
		self.spnameled.setStyleSheet("color: rgb(255, 0, 0);")
		self.spnameled.setObjectName("spnameled")
		self.spinqtyled = QtWidgets.QLineEdit(addTOOBDialog)
		self.spinqtyled.setEnabled(False)
		self.spinqtyled.setGeometry(QtCore.QRect(643, 46, 70, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.spinqtyled.setFont(font)
		self.spinqtyled.setStyleSheet("color: rgb(255, 0, 0);")
		self.spinqtyled.setObjectName("spinqtyled")
		self.label_4 = QtWidgets.QLabel(addTOOBDialog)
		self.label_4.setGeometry(QtCore.QRect(564, 49, 80, 13))
		self.label_4.setObjectName("label_4")
		self.reqqtyled_2 = QtWidgets.QLineEdit(addTOOBDialog)
		self.reqqtyled_2.setGeometry(QtCore.QRect(466, 107, 150, 20))
		self.reqqtyled_2.setObjectName("reqqtyled_2")
		self.reqqtyled = QtWidgets.QLabel(addTOOBDialog)
		self.reqqtyled.setGeometry(QtCore.QRect(478, 86, 130, 13))
		self.reqqtyled.setObjectName("reqqtyled")
		self.spgencodeled = QtWidgets.QLineEdit(addTOOBDialog)
		self.spgencodeled.setEnabled(False)
		self.spgencodeled.setGeometry(QtCore.QRect(450, 47, 100, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.spgencodeled.setFont(font)
		self.spgencodeled.setStyleSheet("color: rgb(255, 0, 0);")
		self.spgencodeled.setObjectName("spgencodeled")
		self.label_6 = QtWidgets.QLabel(addTOOBDialog)
		self.label_6.setGeometry(QtCore.QRect(379, 50, 70, 13))
		self.label_6.setObjectName("label_6")
		self.line = QtWidgets.QFrame(addTOOBDialog)
		self.line.setGeometry(QtCore.QRect(380, 80, 340, 3))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.addbtn = QtWidgets.QPushButton(addTOOBDialog)
		self.addbtn.setGeometry(QtCore.QRect(458, 206, 70, 30))
		self.addbtn.setObjectName("addbtn")
		self.closebtn = QtWidgets.QPushButton(addTOOBDialog)
		self.closebtn.setGeometry(QtCore.QRect(548, 206, 70, 30))
		self.closebtn.setObjectName("closebtn")
		self.listView = QtWidgets.QListWidget(addTOOBDialog)
		self.listView.setGeometry(QtCore.QRect(10, 27, 360, 210))
		self.listView.setObjectName("listView")
		self.line_2 = QtWidgets.QFrame(addTOOBDialog)
		self.line_2.setGeometry(QtCore.QRect(374, 3, 3, 230))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.label_3 = QtWidgets.QLabel(addTOOBDialog)
		self.label_3.setGeometry(QtCore.QRect(516, 143, 47, 13))
		self.label_3.setObjectName("label_3")
		self.reasonled = QtWidgets.QLineEdit(addTOOBDialog)
		self.reasonled.setGeometry(QtCore.QRect(387, 161, 330, 20))
		self.reasonled.setObjectName("reasonled")
		self.line_3 = QtWidgets.QFrame(addTOOBDialog)
		self.line_3.setGeometry(QtCore.QRect(379, 196, 340, 3))
		self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		for item in select_all_tools():
			self.listView.addItem(item.gen_code + " - " + item.name)

		self.listView.itemClicked.connect(self.Clicked)
		self.addbtn.clicked.connect(self.do_add)
		self.closebtn.clicked.connect(self.close)

		self.retranslateUi(addTOOBDialog)
		QtCore.QMetaObject.connectSlotsByName(addTOOBDialog)

	def retranslateUi(self, addTOOBDialog):
		_translate = QtCore.QCoreApplication.translate
		addTOOBDialog.setWindowTitle(_translate("addTOOBDialog", "Add Tool Outbound"))
		self.label.setText(_translate("addTOOBDialog", "Select Tools From List :"))
		self.label_2.setText(_translate("addTOOBDialog", "Selected Tool :"))
		self.label_4.setText(_translate("addTOOBDialog", "Inventory QTY:"))
		self.reqqtyled.setText(_translate("addTOOBDialog", "How mauch qty you want ?"))
		self.label_6.setText(_translate("addTOOBDialog", "System Code :"))
		self.addbtn.setText(_translate("addTOOBDialog", "Add"))
		self.closebtn.setText(_translate("addTOOBDialog", "Close"))
		self.label_3.setText(_translate("addTOOBDialog", "Reason"))

	def Clicked(self, item):
		self.addbtn.setEnabled(True)
		code = before(item.text(), '-')
		if select_tools_by_gen_code(code):
			rawMat = select_tools_by_gen_code(code)
			if rawMat.back == 0:
				self.spnameled.setText(rawMat.name + "/ Not Backable")
			if rawMat.back == 1:
				self.spnameled.setText(rawMat.name)
			self.spinqtyled.setText(str(rawMat.inv_qty))
			self.spgencodeled.setText(rawMat.gen_code)
		return rawMat

	def do_add(self):
		datetimestr = datetime.now()
		timestampstr = datetimestr.strftime('%Y-%m-%d %H:%M:%S')
		code = self.spgencodeled.text()
		rawmat = select_tools_by_gen_code(code)
		qty = self.reqqtyled_2.text()
		reas = self.reasonled.text()
		if qty != '' or reas != '':
			if type(self.obj) == Employees:
				add_outbound(OutBCode(), timestampstr, reas, None, self.obj.id, None
							 , None, rawmat.id, None, qty, 1)
			if type(self.obj) == Customers:
				add_outbound(OutBCode(), timestampstr, reas, self.obj.id, None, None
							 , None, rawmat.id, None, qty, 1)
			decreaseToolsInvQty(rawmat, int(qty))
			self.close()
			#     # print(str(OutBCode()))


def before(value, a):
	# Find first part and return slice before it.
	pos_a = value.find(a)
	if pos_a == -1: return ""
	return value[0:pos_a]

# if __name__ == '__main__':
# 	app = QtWidgets.QApplication(sys.argv)
# 	myapp = Ui_addTOOBDialog()
# 	myapp.exec_()
