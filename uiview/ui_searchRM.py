# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_searchRM.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox

from models.rawMaterialModel import select_row_material, select_row_material_bycode, delete_raw_material


class Ui_searchRMDialog(QDialog):
	def __init__(self, parent=None):
		super(Ui_searchRMDialog, self).__init__()
		self.setupUi(self)

	def setupUi(self, searchRMDialog):
		searchRMDialog.setObjectName("searchRMDialog")

		searchRMDialog.resize(711, 580)
		self.label = QtWidgets.QLabel(searchRMDialog)
		self.label.setGeometry(QtCore.QRect(13, 10, 50, 13))
		self.label.setObjectName("label")
		self.loggeduserlbl = QtWidgets.QLabel(searchRMDialog)
		self.loggeduserlbl.setGeometry(QtCore.QRect(64, 11, 230, 13))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggeduserlbl.setFont(font)
		self.loggeduserlbl.setText("")
		self.loggeduserlbl.setObjectName("loggeduserlbl")
		self.line = QtWidgets.QFrame(searchRMDialog)
		self.line.setGeometry(QtCore.QRect(6, 29, 700, 3))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.groupBox = QtWidgets.QGroupBox(searchRMDialog)
		self.groupBox.setGeometry(QtCore.QRect(10, 35, 281, 100))
		self.groupBox.setObjectName("groupBox")
		self.srnamerbtn = QtWidgets.QRadioButton(self.groupBox)
		self.srnamerbtn.setGeometry(QtCore.QRect(10, 20, 55, 17))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.srnamerbtn.setFont(font)
		self.srnamerbtn.setObjectName("srnamerbtn")
		self.srunitrbtn = QtWidgets.QRadioButton(self.groupBox)
		self.srunitrbtn.setGeometry(QtCore.QRect(80, 20, 45, 17))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.srunitrbtn.setFont(font)
		self.srunitrbtn.setObjectName("srunitrbtn")
		self.srsizerbtn = QtWidgets.QRadioButton(self.groupBox)
		self.srsizerbtn.setGeometry(QtCore.QRect(140, 20, 45, 17))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.srsizerbtn.setFont(font)
		self.srsizerbtn.setObjectName("srsizerbtn")
		self.srcoderbtn = QtWidgets.QRadioButton(self.groupBox)
		self.srcoderbtn.setGeometry(QtCore.QRect(200, 20, 110, 17))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.srcoderbtn.setFont(font)
		self.srcoderbtn.setObjectName("srcoderbtn")
		self.label_3 = QtWidgets.QLabel(self.groupBox)
		self.label_3.setGeometry(QtCore.QRect(7, 45, 90, 13))
		self.label_3.setObjectName("label_3")
		self.searchled = QtWidgets.QLineEdit(self.groupBox)
		self.searchled.setGeometry(QtCore.QRect(10, 64, 180, 20))
		self.searchled.setObjectName("searchled")
		self.searchbtn = QtWidgets.QPushButton(self.groupBox)
		self.searchbtn.setGeometry(QtCore.QRect(203, 59, 60, 30))
		self.searchbtn.setObjectName("searchbtn")

		self.searchbtn.clicked.connect(self.do_search)

		self.groupBox_2 = QtWidgets.QGroupBox(searchRMDialog)
		self.groupBox_2.setGeometry(QtCore.QRect(10, 136, 330, 431))
		self.groupBox_2.setObjectName("groupBox_2")
		self.searchResultlistWidget = QtWidgets.QListWidget(self.groupBox_2)
		self.searchResultlistWidget.setGeometry(QtCore.QRect(4, 14, 320, 410))
		self.searchResultlistWidget.setObjectName("searchResultlistWidget")

		self.searchResultlistWidget.itemClicked.connect(self.Clicked)

		self.groupBox_3 = QtWidgets.QGroupBox(searchRMDialog)
		self.groupBox_3.setGeometry(QtCore.QRect(360, 40, 330, 201))
		self.groupBox_3.setObjectName("groupBox_3")
		self.label_4 = QtWidgets.QLabel(self.groupBox_3)
		self.label_4.setGeometry(QtCore.QRect(13, 32, 40, 13))
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(self.groupBox_3)
		self.label_5.setGeometry(QtCore.QRect(13, 64, 40, 13))
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(self.groupBox_3)
		self.label_6.setGeometry(QtCore.QRect(14, 96, 60, 13))
		self.label_6.setObjectName("label_6")
		self.label_7 = QtWidgets.QLabel(self.groupBox_3)
		self.label_7.setGeometry(QtCore.QRect(14, 129, 90, 13))
		self.label_7.setObjectName("label_7")
		self.label_8 = QtWidgets.QLabel(self.groupBox_3)
		self.label_8.setGeometry(QtCore.QRect(10, 160, 30, 13))
		self.label_8.setObjectName("label_8")

		self.label_9 = QtWidgets.QLabel(self.groupBox_3)
		self.label_9.setGeometry(QtCore.QRect(127, 160, 110, 13))
		self.label_9.setObjectName("label_9")

		self.codeled = QtWidgets.QLabel(self.groupBox_3)
		self.codeled.setGeometry(QtCore.QRect(50, 28, 150, 20))
		self.codeled.setObjectName("codeled")
		self.codeled.setFont(font)
		self.codeled.setStyleSheet("color: rgb(255, 0, 0);")

		self.nameled = QtWidgets.QLabel(self.groupBox_3)
		self.nameled.setGeometry(QtCore.QRect(50, 58, 271, 20))
		self.nameled.setObjectName("nameled")
		self.nameled.setFont(font)
		self.nameled.setStyleSheet("color: rgb(255, 0, 0);")

		self.strsizeled = QtWidgets.QLabel(self.groupBox_3)
		self.strsizeled.setGeometry(QtCore.QRect(77, 92, 241, 20))
		self.strsizeled.setObjectName("strsizeled")
		self.strsizeled.setFont(font)
		self.strsizeled.setStyleSheet("color: rgb(255, 0, 0);")

		self.numsizeled = QtWidgets.QLabel(self.groupBox_3)
		self.numsizeled.setGeometry(QtCore.QRect(98, 125, 180, 20))
		self.numsizeled.setObjectName("numsizeled")
		self.numsizeled.setFont(font)
		self.numsizeled.setStyleSheet("color: rgb(255, 0, 0);")

		self.unitled = QtWidgets.QLabel(self.groupBox_3)
		self.unitled.setGeometry(QtCore.QRect(40, 155, 60, 20))
		self.unitled.setObjectName("unitled")
		self.unitled.setFont(font)
		self.unitled.setStyleSheet("color: rgb(255, 0, 0);")

		self.invQtyled = QtWidgets.QLabel(self.groupBox_3)
		self.invQtyled.setGeometry(QtCore.QRect(231, 156, 90, 20))
		self.invQtyled.setObjectName("invQtyled")
		self.invQtyled.setFont(font)
		self.invQtyled.setStyleSheet("color: rgb(255, 0, 0);")

		self.costled = QtWidgets.QLabel(self.groupBox_3)
		self.costled.setGeometry(QtCore.QRect(241, 28, 80, 20))
		self.costled.setObjectName("costled")
		self.costled.setFont(font)
		self.costled.setStyleSheet("color: rgb(255, 0, 0);")

		self.label_11 = QtWidgets.QLabel(self.groupBox_3)
		self.label_11.setGeometry(QtCore.QRect(210, 32, 30, 13))
		self.label_11.setObjectName("label_11")
		self.line_2 = QtWidgets.QFrame(searchRMDialog)
		self.line_2.setGeometry(QtCore.QRect(349, 43, 3, 530))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.label_10 = QtWidgets.QLabel(searchRMDialog)
		self.label_10.setGeometry(QtCore.QRect(361, 245, 330, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_10.setFont(font)
		self.label_10.setStyleSheet("color: rgb(255, 0, 0);")
		self.label_10.setText("")
		self.label_10.setAlignment(QtCore.Qt.AlignCenter)
		self.label_10.setObjectName("label_10")
		self.groupBox_4 = QtWidgets.QGroupBox(searchRMDialog)
		self.groupBox_4.setGeometry(QtCore.QRect(360, 285, 331, 60))
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
		self.closebtn.clicked.connect(self.close)
		self.deletebtn.clicked.connect(self.do_delete)
		# self.editbtn.clicked.connect(self.openEditeNewRawMaterial)
		self.editbtn.setVisible(False)
		self.deletebtn.setEnabled(False)

		self.retranslateUi(searchRMDialog)
		QtCore.QMetaObject.connectSlotsByName(searchRMDialog)


	def retranslateUi(self, searchRMDialog):
		_translate = QtCore.QCoreApplication.translate
		searchRMDialog.setWindowTitle(_translate("searchRMDialog", "Raw Material Search"))
		self.label.setText(_translate("searchRMDialog", "Welcome, "))
		self.groupBox.setTitle(_translate("searchRMDialog", "Please select search method and type !"))
		self.srnamerbtn.setText(_translate("searchRMDialog", "Name"))
		self.srunitrbtn.setText(_translate("searchRMDialog", "Unit"))
		self.srsizerbtn.setText(_translate("searchRMDialog", "Size"))
		self.srcoderbtn.setText(_translate("searchRMDialog", "Code"))
		self.label_3.setText(_translate("searchRMDialog", "Search Keyword:"))
		self.searchbtn.setText(_translate("searchRMDialog", "Search"))
		self.groupBox_2.setTitle(_translate("searchRMDialog", "Search Results"))
		self.groupBox_3.setTitle(_translate("searchRMDialog", "Item Detailes"))
		self.label_4.setText(_translate("searchRMDialog", "Code :"))
		self.label_5.setText(_translate("searchRMDialog", "Name :"))
		self.label_6.setText(_translate("searchRMDialog", "String Size :"))
		self.label_7.setText(_translate("searchRMDialog", "Size ( Number ) :"))
		self.label_8.setText(_translate("searchRMDialog", "Unit :"))
		self.label_9.setText(_translate("searchRMDialog", "Inventory Quantity :"))
		self.label_11.setText(_translate("searchRMDialog", "Cost :"))
		self.deletebtn.setText(_translate("searchRMDialog", "Delete"))
		self.editbtn.setText(_translate("searchRMDialog", "Edit"))
		self.closebtn.setText(_translate("searchRMDialog", "Close"))

	def do_search(self):
		self.searchResultlistWidget.clear()
		self.label_10.clear()
		if self.srnamerbtn.isChecked():
			search_key = 'name'
		elif self.srunitrbtn.isChecked():
			search_key = 'unit'
		elif self.srsizerbtn.isChecked():
			search_key = 'string_size'
		elif self.srcoderbtn.isChecked():
			search_key = 'code'
		if self.srnamerbtn.isChecked()or self.srunitrbtn.isChecked() or self.srsizerbtn.isChecked(
			) or self.srcoderbtn.isChecked():
			for item in select_row_material(search_key, self.searchled.text()):
				self.searchResultlistWidget.addItem(item.code + " - " + item.name)
		else :
			self.label_10.setText("You must select one method for search !")

	def Clicked(self, item):
		self.deletebtn.setEnabled(True)
		self.editbtn.setEnabled(True)
		code = before(item.text(), '-')
		if select_row_material_bycode(code):
			rawMat = select_row_material_bycode(code)
			self.codeled.setText(rawMat.code)
			self.nameled.setText(rawMat.name)
			self.unitled.setText(rawMat.unit)
			self.numsizeled.setText(str(rawMat.default_size))
			self.strsizeled.setText(rawMat.string_size)
			self.costled.setText(str(rawMat.cost_per_default_size))
			self.invQtyled.setText(str(rawMat.inv_qty))
		return rawMat

	def do_delete(self):
		code = self.codeled.text()
		if not code == '':
			if select_row_material_bycode(code):
				rawMat = select_row_material_bycode(code)
			reply = QMessageBox.question(QMessageBox(), "OOP'S", 'Are you sure to delete ?\n Raw '
																 'Material \n Code : {}'.format(
				rawMat.code)+'\n Name : {}'.format(rawMat.name)+'\n This Action Cant Undo',
										 QMessageBox.Yes | QMessageBox.No)
			if reply == QMessageBox.Yes:
				delete_raw_material(rawMat.id)

	def openEditeNewRawMaterial(self):
		from uiview.ui_updateNewRM import Ui_editRWDialog
		self.di = Ui_editRWDialog()
		self.di.exec_()

def before(value, a):
	# Find first part and return slice before it.
	pos_a = value.find(a)
	if pos_a == -1: return ""
	return value[0:pos_a]

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	myapp = Ui_searchRMDialog()
	myapp.show()
	app.exec_()

