# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_searchFP.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox

from Control.userControl import getLoginDataPKL
from models.finishProductsModel import select_finish_product, select_finish_product_by_gen_code, delete_finish_product


class Ui_searchFPDialog(QDialog):
	def __init__(self):
		super(Ui_searchFPDialog, self).__init__()
		self.setupUi(self)

	def setupUi(self, searchFPDialog):
		self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

		searchFPDialog.setObjectName("searchFPDialog")
		searchFPDialog.resize(711, 580)
		self.label = QtWidgets.QLabel(searchFPDialog)
		self.label.setGeometry(QtCore.QRect(13, 10, 50, 13))
		self.label.setObjectName("label")
		self.loggeduserlbl = QtWidgets.QLabel(searchFPDialog)
		self.loggeduserlbl.setGeometry(QtCore.QRect(64, 11, 230, 13))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggeduserlbl.setFont(font)
		self.loggeduserlbl.setText("")
		self.loggeduserlbl.setObjectName("loggeduserlbl")
		self.line = QtWidgets.QFrame(searchFPDialog)
		self.line.setGeometry(QtCore.QRect(6, 29, 700, 3))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.groupBox = QtWidgets.QGroupBox(searchFPDialog)
		self.groupBox.setGeometry(QtCore.QRect(10, 35, 281, 100))
		self.groupBox.setObjectName("groupBox")
		self.fpnamerbtn = QtWidgets.QRadioButton(self.groupBox)
		self.fpnamerbtn.setGeometry(QtCore.QRect(10, 20, 50, 17))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.fpnamerbtn.setFont(font)
		self.fpnamerbtn.setObjectName("fpnamerbtn")
		self.fpcoderbtn = QtWidgets.QRadioButton(self.groupBox)
		self.fpcoderbtn.setGeometry(QtCore.QRect(73, 21, 70, 17))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.fpcoderbtn.setFont(font)
		self.fpcoderbtn.setObjectName("fpcoderbtn")
		self.label_3 = QtWidgets.QLabel(self.groupBox)
		self.label_3.setGeometry(QtCore.QRect(7, 45, 90, 13))
		self.label_3.setObjectName("label_3")
		self.searchled = QtWidgets.QLineEdit(self.groupBox)
		self.searchled.setGeometry(QtCore.QRect(10, 64, 180, 20))
		self.searchled.setObjectName("searchled")
		self.searchbtn = QtWidgets.QPushButton(self.groupBox)
		self.searchbtn.setGeometry(QtCore.QRect(203, 59, 60, 30))
		self.searchbtn.setObjectName("searchbtn")
		self.groupBox_2 = QtWidgets.QGroupBox(searchFPDialog)
		self.groupBox_2.setGeometry(QtCore.QRect(10, 136, 330, 431))
		self.groupBox_2.setObjectName("groupBox_2")
		self.searchResultlistWidget = QtWidgets.QListWidget(self.groupBox_2)
		self.searchResultlistWidget.setGeometry(QtCore.QRect(4, 14, 320, 410))
		self.searchResultlistWidget.setObjectName("searchResultlistWidget")
		self.groupBox_3 = QtWidgets.QGroupBox(searchFPDialog)
		self.groupBox_3.setGeometry(QtCore.QRect(360, 40, 341, 161))
		self.groupBox_3.setObjectName("groupBox_3")
		self.label_4 = QtWidgets.QLabel(self.groupBox_3)
		self.label_4.setGeometry(QtCore.QRect(13, 32, 70, 13))
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(self.groupBox_3)
		self.label_5.setGeometry(QtCore.QRect(13, 64, 40, 13))
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(self.groupBox_3)
		self.label_6.setGeometry(QtCore.QRect(14, 96, 40, 13))
		self.label_6.setObjectName("label_6")
		self.label_8 = QtWidgets.QLabel(self.groupBox_3)
		self.label_8.setGeometry(QtCore.QRect(14, 128, 30, 13))
		self.label_8.setObjectName("label_8")
		self.label_9 = QtWidgets.QLabel(self.groupBox_3)
		self.label_9.setGeometry(QtCore.QRect(131, 128, 110, 13))
		self.label_9.setObjectName("label_9")
		self.codeled = QtWidgets.QLineEdit(self.groupBox_3)
		self.codeled.setEnabled(False)
		self.codeled.setGeometry(QtCore.QRect(76, 30, 130, 20))
		self.codeled.setObjectName("codeled")
		self.nameled = QtWidgets.QLineEdit(self.groupBox_3)
		self.nameled.setEnabled(False)
		self.nameled.setGeometry(QtCore.QRect(50, 60, 271, 20))
		self.nameled.setObjectName("nameled")
		self.strsizeled = QtWidgets.QLineEdit(self.groupBox_3)
		self.strsizeled.setEnabled(False)
		self.strsizeled.setGeometry(QtCore.QRect(51, 94, 180, 20))
		self.strsizeled.setObjectName("strsizeled")
		self.unitled = QtWidgets.QLineEdit(self.groupBox_3)
		self.unitled.setEnabled(False)
		self.unitled.setGeometry(QtCore.QRect(44, 126, 60, 20))
		self.unitled.setObjectName("unitled")
		self.invQtyled = QtWidgets.QLineEdit(self.groupBox_3)
		self.invQtyled.setEnabled(False)
		self.invQtyled.setGeometry(QtCore.QRect(235, 126, 90, 20))
		self.invQtyled.setObjectName("invQtyled")
		self.costled = QtWidgets.QLineEdit(self.groupBox_3)
		self.costled.setEnabled(False)
		self.costled.setGeometry(QtCore.QRect(249, 30, 70, 20))
		self.costled.setObjectName("costled")
		self.label_11 = QtWidgets.QLabel(self.groupBox_3)
		self.label_11.setGeometry(QtCore.QRect(218, 32, 30, 13))
		self.label_11.setObjectName("label_11")
		self.line_2 = QtWidgets.QFrame(searchFPDialog)
		self.line_2.setGeometry(QtCore.QRect(349, 43, 3, 530))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.label_10 = QtWidgets.QLabel(searchFPDialog)
		self.label_10.setGeometry(QtCore.QRect(361, 203, 330, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_10.setFont(font)
		self.label_10.setStyleSheet("color: rgb(255, 0, 0);")
		self.label_10.setText("")
		self.label_10.setAlignment(QtCore.Qt.AlignCenter)
		self.label_10.setObjectName("label_10")
		self.groupBox_4 = QtWidgets.QGroupBox(searchFPDialog)
		self.groupBox_4.setGeometry(QtCore.QRect(360, 247, 331, 60))
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
		self.searchbtn.clicked.connect(self.do_search)
		self.searchResultlistWidget.itemClicked.connect(self.Clicked)
		self.editbtn.clicked.connect(self.do_edit)
		self.deletebtn.clicked.connect(self.do_delete)
		self.closebtn.clicked.connect(self.close)

		self.retranslateUi(searchFPDialog)
		QtCore.QMetaObject.connectSlotsByName(searchFPDialog)

	def retranslateUi(self, searchFPDialog):
		_translate = QtCore.QCoreApplication.translate
		searchFPDialog.setWindowTitle(_translate("searchFPDialog", "Finish Product Search"))
		self.label.setText(_translate("searchFPDialog", "Welcome, "))
		self.groupBox.setTitle(_translate("searchFPDialog", "Please select search method and type !"))
		self.fpnamerbtn.setText(_translate("searchFPDialog", "Name"))
		self.fpcoderbtn.setText(_translate("searchFPDialog", "Code"))
		self.label_3.setText(_translate("searchFPDialog", "Search Keyword:"))
		self.searchbtn.setText(_translate("searchFPDialog", "Search"))
		self.groupBox_2.setTitle(_translate("searchFPDialog", "Search Results"))
		self.groupBox_3.setTitle(_translate("searchFPDialog", "Item Detailes"))
		self.label_4.setText(_translate("searchFPDialog", "Gen - Code :"))
		self.label_5.setText(_translate("searchFPDialog", "Name :"))
		self.label_6.setText(_translate("searchFPDialog", "Code :"))
		self.label_8.setText(_translate("searchFPDialog", "Unit :"))
		self.label_9.setText(_translate("searchFPDialog", "Inventory Quantity :"))
		self.label_11.setText(_translate("searchFPDialog", "Cost :"))
		self.deletebtn.setText(_translate("searchFPDialog", "Delete"))
		self.editbtn.setText(_translate("searchFPDialog", "Edit"))
		self.closebtn.setText(_translate("searchFPDialog", "Close"))

	def Clicked(self, item):
		role = getLoginDataPKL()['role']
		if int(role) == 1 or int(role) == 2 or int(role) == 3:
			self.deletebtn.setEnabled(False)
		self.editbtn.setEnabled(True)

		gencode = before(item.text(), ' -')
		if select_finish_product_by_gen_code(gencode):
			spart = select_finish_product_by_gen_code(gencode)
			print(gencode)
			self.nameled.setText(spart.name)
			self.unitled.setText(spart.source)
			self.strsizeled.setText(spart.code)
			self.codeled.setText(spart.gen_code)
			self.costled.setText(str(spart.price))
			self.invQtyled.setText(str(spart.inv_qty))
		return spart

	def do_search(self):
		self.searchResultlistWidget.clear()
		self.label_10.clear()
		if self.fpnamerbtn.isChecked():
			search_key = 'name'
		elif self.fpcoderbtn.isChecked():
			search_key = 'code'
		if self.fpnamerbtn.isChecked() or self.fpcoderbtn.isChecked():
			for item in select_finish_product(search_key, self.searchled.text()):
				self.searchResultlistWidget.addItem(item.gen_code + " - " + item.name + "(" + item.code + ")")
		else:
			self.label_10.setText("You must select one method for search !")

	def do_delete(self):
		code = self.codeled.text()
		if select_finish_product_by_gen_code(code):
			rawMat = select_finish_product_by_gen_code(code)
		reply = QMessageBox.question(QMessageBox(), "OOP'S",
									 'Are you sure to delete ?\n Finish Product \n Code : {}'.format(
										 rawMat.code) + '\n System Code : {}'.format(
										 rawMat.gen_code) + '\n Name : {}'.format(
										 rawMat.name) + '\n This Action Cant Undo',
									 QMessageBox.Yes | QMessageBox.No)
		if reply == QMessageBox.Yes:
			delete_finish_product(rawMat.id)

	def do_edit(self):
		from uiview.ui_updatereNewFP import Ui_editFPDialog
		spp = select_finish_product_by_gen_code(self.codeled.text())
		self.dd = Ui_editFPDialog(spp)
		self.dd.exec_()


def before(value, a):
	# Find first part and return slice before it.
	pos_a = value.find(a)
	if pos_a == -1: return ""
	return value[0:pos_a]


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myapp = Ui_searchFPDialog()
	myapp.show()
	myapp.exec_()
