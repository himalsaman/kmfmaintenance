# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_searchTO.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox

from Control.userControl import getLoginDataPKL
from models.ouboundModel import select_all_outbound
from models.toolsModel import select_tools, select_tools_by_gen_code, delete_tools


class Ui_searchTODialog(QDialog):
	def __init__(self):
		super(Ui_searchTODialog, self).__init__()
		self.setupUi(self)

	def setupUi(self, searchTODialog):
		self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

		searchTODialog.setObjectName("searchTODialog")
		searchTODialog.resize(711, 544)
		self.label = QtWidgets.QLabel(searchTODialog)
		self.label.setGeometry(QtCore.QRect(13, 10, 50, 13))
		self.label.setObjectName("label")
		self.loggeduserlbl = QtWidgets.QLabel(searchTODialog)
		self.loggeduserlbl.setGeometry(QtCore.QRect(64, 11, 230, 13))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggeduserlbl.setFont(font)
		self.loggeduserlbl.setText("")
		self.loggeduserlbl.setObjectName("loggeduserlbl")
		self.line = QtWidgets.QFrame(searchTODialog)
		self.line.setGeometry(QtCore.QRect(6, 29, 700, 3))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.groupBox = QtWidgets.QGroupBox(searchTODialog)
		self.groupBox.setGeometry(QtCore.QRect(10, 35, 281, 61))
		self.groupBox.setObjectName("groupBox")
		self.searchled = QtWidgets.QLineEdit(self.groupBox)
		self.searchled.setGeometry(QtCore.QRect(10, 23, 180, 20))
		self.searchled.setObjectName("searchled")
		self.searchbtn = QtWidgets.QPushButton(self.groupBox)
		self.searchbtn.setGeometry(QtCore.QRect(203, 18, 60, 30))
		self.searchbtn.setObjectName("searchbtn")
		self.groupBox_2 = QtWidgets.QGroupBox(searchTODialog)
		self.groupBox_2.setGeometry(QtCore.QRect(10, 96, 330, 431))
		self.groupBox_2.setObjectName("groupBox_2")
		self.searchResultlistWidget = QtWidgets.QListWidget(self.groupBox_2)
		self.searchResultlistWidget.setGeometry(QtCore.QRect(4, 14, 320, 410))
		self.searchResultlistWidget.setObjectName("searchResultlistWidget")
		self.groupBox_3 = QtWidgets.QGroupBox(searchTODialog)
		self.groupBox_3.setGeometry(QtCore.QRect(360, 40, 330, 131))
		self.groupBox_3.setObjectName("groupBox_3")
		self.label_4 = QtWidgets.QLabel(self.groupBox_3)
		self.label_4.setGeometry(QtCore.QRect(13, 32, 40, 13))
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(self.groupBox_3)
		self.label_5.setGeometry(QtCore.QRect(13, 64, 40, 13))
		self.label_5.setObjectName("label_5")
		self.label_8 = QtWidgets.QLabel(self.groupBox_3)
		self.label_8.setGeometry(QtCore.QRect(10, 91, 30, 13))
		self.label_8.setObjectName("label_8")
		self.label_9 = QtWidgets.QLabel(self.groupBox_3)
		self.label_9.setGeometry(QtCore.QRect(110, 91, 110, 13))
		self.label_9.setObjectName("label_9")

		self.label_99 = QtWidgets.QLabel(self.groupBox_3)
		self.label_99.setGeometry(QtCore.QRect(230, 91, 110, 13))
		self.label_99.setObjectName("label_9")

		self.codeled = QtWidgets.QLineEdit(self.groupBox_3)
		self.codeled.setEnabled(False)
		self.codeled.setGeometry(QtCore.QRect(50, 30, 150, 20))
		self.codeled.setObjectName("codeled")
		self.nameled = QtWidgets.QLineEdit(self.groupBox_3)
		self.nameled.setEnabled(False)
		self.nameled.setGeometry(QtCore.QRect(50, 60, 271, 20))
		self.nameled.setObjectName("nameled")
		self.unitled = QtWidgets.QLineEdit(self.groupBox_3)
		self.unitled.setEnabled(False)
		self.unitled.setGeometry(QtCore.QRect(40, 89, 60, 20))
		self.unitled.setObjectName("unitled")
		self.invQtyled = QtWidgets.QLineEdit(self.groupBox_3)
		self.invQtyled.setEnabled(False)
		self.invQtyled.setGeometry(QtCore.QRect(162, 89, 60, 20))
		self.invQtyled.setObjectName("invQtyled")

		self.miniQtyled = QtWidgets.QLineEdit(self.groupBox_3)
		self.miniQtyled.setEnabled(False)
		self.miniQtyled.setGeometry(QtCore.QRect(280, 89, 40, 20))
		self.miniQtyled.setObjectName("miniQtyled")

		self.costled = QtWidgets.QLineEdit(self.groupBox_3)
		self.costled.setEnabled(False)
		self.costled.setGeometry(QtCore.QRect(241, 30, 80, 20))
		self.costled.setObjectName("costled")
		self.label_11 = QtWidgets.QLabel(self.groupBox_3)
		self.label_11.setGeometry(QtCore.QRect(210, 32, 30, 13))
		self.label_11.setObjectName("label_11")
		self.line_2 = QtWidgets.QFrame(searchTODialog)
		self.line_2.setGeometry(QtCore.QRect(349, 43, 3, 490))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.statuslbl = QtWidgets.QLabel(searchTODialog)
		self.statuslbl.setGeometry(QtCore.QRect(361, 172, 330, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.statuslbl.setFont(font)
		self.statuslbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.statuslbl.setText("")
		self.statuslbl.setAlignment(QtCore.Qt.AlignCenter)
		self.statuslbl.setObjectName("statuslbl")
		self.groupBox_4 = QtWidgets.QGroupBox(searchTODialog)
		self.groupBox_4.setGeometry(QtCore.QRect(360, 212, 331, 60))
		self.groupBox_4.setTitle("")
		self.groupBox_4.setObjectName("groupBox_4")
		self.deletebtn = QtWidgets.QPushButton(self.groupBox_4)
		self.deletebtn.setGeometry(QtCore.QRect(8, 9, 75, 40))
		self.deletebtn.setObjectName("deletebtn")
		self.editbtn = QtWidgets.QPushButton(self.groupBox_4)
		self.editbtn.setGeometry(QtCore.QRect(126, 9, 75, 40))
		self.editbtn.setObjectName("editbtn")
		self.closebtn = QtWidgets.QPushButton(self.groupBox_4)
		self.closebtn.setGeometry(QtCore.QRect(246, 9, 75, 40))
		self.closebtn.setObjectName("closebtn")

		font = QtGui.QFont()
		font.setPointSize(8)
		font.setBold(True)
		font.setWeight(75)
		self.codeled.setFont(font)
		self.codeled.setStyleSheet("color: rgb(255, 0, 0);")
		self.costled.setFont(font)
		self.costled.setStyleSheet("color: rgb(255, 0, 0);")
		self.invQtyled.setFont(font)
		self.invQtyled.setStyleSheet("color: rgb(255, 0, 0);")
		self.miniQtyled.setFont(font)
		self.miniQtyled.setStyleSheet("color: rgb(255, 0, 0);")
		self.nameled.setFont(font)
		self.nameled.setStyleSheet("color: rgb(255, 0, 0);")
		self.unitled.setFont(font)
		self.unitled.setStyleSheet("color: rgb(255, 0, 0);")

		self.searchbtn.clicked.connect(self.do_search)
		self.searchResultlistWidget.itemClicked.connect(self.Clicked)
		self.deletebtn.clicked.connect(self.do_delete)
		self.editbtn.clicked.connect(self.do_edit)
		self.closebtn.clicked.connect(self.close)
		self.deletebtn.setEnabled(False)
		self.editbtn.setEnabled(False)

		self.retranslateUi(searchTODialog)
		QtCore.QMetaObject.connectSlotsByName(searchTODialog)

	def retranslateUi(self, searchTODialog):
		_translate = QtCore.QCoreApplication.translate
		searchTODialog.setWindowTitle(_translate("searchTODialog", "Tools Search"))
		self.label.setText(_translate("searchTODialog", "Welcome, "))
		self.groupBox.setTitle(_translate("searchTODialog", "Please Enter tool name"))
		self.searchbtn.setText(_translate("searchTODialog", "Search"))
		self.groupBox_2.setTitle(_translate("searchTODialog", "Search Results"))
		self.groupBox_3.setTitle(_translate("searchTODialog", "Item Detailes"))
		self.label_4.setText(_translate("searchTODialog", "Code :"))
		self.label_5.setText(_translate("searchTODialog", "Name :"))
		self.label_8.setText(_translate("searchTODialog", "Unit :"))
		self.label_9.setText(_translate("searchTODialog", "Inv. Qty :"))
		self.label_99.setText(_translate("searchTODialog", "Min. Qty :"))
		self.label_11.setText(_translate("searchTODialog", "Cost :"))
		self.deletebtn.setText(_translate("searchTODialog", "Delete"))
		self.editbtn.setText(_translate("searchTODialog", "Edit"))
		self.closebtn.setText(_translate("searchTODialog", "Close"))

	def Clicked(self, item):
		role = getLoginDataPKL()['role']
		if int(role) == 1 or int(role) == 2:
			self.deletebtn.setEnabled(False)
		self.editbtn.setEnabled(True)
		self.deletebtn.setEnabled(True)
		gencode = before(item.text(), ' -')
		if select_tools_by_gen_code(gencode):
			spart = select_tools_by_gen_code(gencode)
			print(gencode)
			self.nameled.setText(spart.name)
			self.unitled.setText(spart.unit)
			self.codeled.setText(spart.gen_code)
			self.costled.setText(str(spart.price))
			self.invQtyled.setText(str(spart.inv_qty))
			self.miniQtyled.setText(str(spart.mini_qty))
		if not select_all_outbound() == []:
			for item in select_all_outbound():
				if item.tools_id == spart.id:
					self.deletebtn.setEnabled(False)

		return spart

	def do_search(self):
		self.searchResultlistWidget.clear()
		for item in select_tools('name', self.searchled.text()):
			self.searchResultlistWidget.addItem(item.gen_code + " - " + item.name)

	def do_delete(self):
		code = self.codeled.text()
		if select_tools_by_gen_code(code):
			rawMat = select_tools_by_gen_code(code)
		reply = QMessageBox.question(QMessageBox(), "OOP'S",
									 'Are you sure to delete ?\n Tool  \n System Code : {}'
									 .format(rawMat.gen_code) + '\n Name : {}'.format(
										 rawMat.name) + '\n This Action Cant Undo',
									 QMessageBox.Yes | QMessageBox.No)
		if reply == QMessageBox.Yes:
			delete_tools(rawMat.id)

	def do_edit(self):
		from uiview.ui_updatereNewTO import Ui_editTODialog
		spp = select_tools_by_gen_code(self.codeled.text())
		self.dd = Ui_editTODialog(spp)
		self.dd.exec_()


def before(value, a):
	# Find first part and return slice before it.
	pos_a = value.find(a)
	if pos_a == -1: return ""
	return value[0:pos_a]


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myapp = Ui_searchTODialog()
	myapp.show()
	myapp.exec_()
