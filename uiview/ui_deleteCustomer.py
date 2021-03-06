# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_deleteCustomer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox

from Control.userControl import getLoginDataPKL
from models.cityModel import select_city_by_id
from models.customersModel import select_customer_by_mob_num, delete_customer
from models.maintenanceModel import select_maintenance_customer


class Ui_deleteCustomer(QDialog):
	def __init__(self, parent=None):
		super(Ui_deleteCustomer, self).__init__()
		self.setupUi(self)

	def setupUi(self, deleteCustomer):
		self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

		deleteCustomer.setObjectName("deleteCustomer")
		deleteCustomer.resize(345, 410)
		self.label = QtWidgets.QLabel(deleteCustomer)
		self.label.setGeometry(QtCore.QRect(10, 10, 47, 16))
		self.label.setObjectName("label")
		self.loggeduserlbl = QtWidgets.QLabel(deleteCustomer)
		self.loggeduserlbl.setGeometry(QtCore.QRect(60, 10, 191, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggeduserlbl.setFont(font)
		self.loggeduserlbl.setText("")
		self.loggeduserlbl.setObjectName("loggeduserlbl")
		self.loggeduserlbl.setText(getLoginDataPKL()['name'])
		self.line = QtWidgets.QFrame(deleteCustomer)
		self.line.setGeometry(QtCore.QRect(5, 27, 331, 16))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.updatebtn = QtWidgets.QPushButton(deleteCustomer)
		self.updatebtn.setGeometry(QtCore.QRect(130, 370, 75, 31))
		self.updatebtn.setObjectName("updatebtn")
		self.updatebtn.clicked.connect(self.deleteCustomer)
		self.cancelbtn = QtWidgets.QPushButton(deleteCustomer)
		self.cancelbtn.setGeometry(QtCore.QRect(230, 370, 75, 31))
		self.cancelbtn.setObjectName("cancelbtn")
		self.cancelbtn.clicked.connect(self.close)
		self.detailsbtn = QtWidgets.QPushButton(deleteCustomer)
		self.detailsbtn.setGeometry(QtCore.QRect(30, 370, 75, 31))
		self.detailsbtn.setObjectName("updatebtn")
		self.statuslbl = QtWidgets.QLabel(deleteCustomer)
		self.statuslbl.setGeometry(QtCore.QRect(10, 335, 331, 31))
		self.statuslbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.statuslbl.setText("")
		self.statuslbl.setAlignment(QtCore.Qt.AlignCenter)
		self.statuslbl.setObjectName("statuslbl")
		self.layoutWidget_2 = QtWidgets.QWidget(deleteCustomer)
		self.layoutWidget_2.setGeometry(QtCore.QRect(10, 88, 51, 251))
		self.layoutWidget_2.setObjectName("layoutWidget_2")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.label_8 = QtWidgets.QLabel(self.layoutWidget_2)
		self.label_8.setObjectName("label_8")
		self.verticalLayout_2.addWidget(self.label_8)

		self.label_9 = QtWidgets.QLabel(self.layoutWidget_2)
		self.label_9.setObjectName("label_9")
		self.verticalLayout_2.addWidget(self.label_9)

		self.label_19 = QtWidgets.QLabel(self.layoutWidget_2)
		self.label_19.setObjectName("label_19")
		self.verticalLayout_2.addWidget(self.label_19)

		self.label_20 = QtWidgets.QLabel(self.layoutWidget_2)
		self.label_20.setObjectName("label_20")
		self.verticalLayout_2.addWidget(self.label_20)

		self.label_21 = QtWidgets.QLabel(self.layoutWidget_2)
		self.label_21.setObjectName("label_21")
		self.verticalLayout_2.addWidget(self.label_21)

		self.label_22 = QtWidgets.QLabel(self.layoutWidget_2)
		self.label_22.setObjectName("label_22")
		self.verticalLayout_2.addWidget(self.label_22)

		self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
		self.label_10.setObjectName("label_10")
		self.verticalLayout_2.addWidget(self.label_10)
		self.label_11 = QtWidgets.QLabel(self.layoutWidget_2)
		self.label_11.setObjectName("label_11")
		self.verticalLayout_2.addWidget(self.label_11)
		self.label_12 = QtWidgets.QLabel(self.layoutWidget_2)
		self.label_12.setObjectName("label_12")
		self.verticalLayout_2.addWidget(self.label_12)
		self.layoutWidget_3 = QtWidgets.QWidget(deleteCustomer)
		self.layoutWidget_3.setGeometry(QtCore.QRect(60, 88, 271, 251))
		self.layoutWidget_3.setObjectName("layoutWidget_3")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
		self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_3.setObjectName("verticalLayout_3")

		self.renamelbl = QtWidgets.QLabel(self.layoutWidget_3)
		self.renamelbl.setText("")
		self.renamelbl.setObjectName("renamelbl")
		self.verticalLayout_3.addWidget(self.renamelbl)

		self.remobilenumlbl = QtWidgets.QLabel(self.layoutWidget_3)
		self.remobilenumlbl.setText("")
		self.remobilenumlbl.setObjectName("remobilenumlbl")
		self.verticalLayout_3.addWidget(self.remobilenumlbl)

		self.remobilenumlbl1 = QtWidgets.QLabel(self.layoutWidget_3)
		self.remobilenumlbl1.setText("")
		self.remobilenumlbl1.setObjectName("remobilenumlbl1")
		self.verticalLayout_3.addWidget(self.remobilenumlbl1)

		self.remobilenumlbl2 = QtWidgets.QLabel(self.layoutWidget_3)
		self.remobilenumlbl2.setText("")
		self.remobilenumlbl2.setObjectName("remobilenumlbl2")
		self.verticalLayout_3.addWidget(self.remobilenumlbl2)

		self.remobilenumlbl3 = QtWidgets.QLabel(self.layoutWidget_3)
		self.remobilenumlbl3.setText("")
		self.remobilenumlbl3.setObjectName("remobilenumlbl3")
		self.verticalLayout_3.addWidget(self.remobilenumlbl3)

		self.remobilenumlbl4 = QtWidgets.QLabel(self.layoutWidget_3)
		self.remobilenumlbl4.setText("")
		self.remobilenumlbl4.setObjectName("remobilenumlbl4")
		self.verticalLayout_3.addWidget(self.remobilenumlbl4)

		self.recitylbl = QtWidgets.QLabel(self.layoutWidget_3)
		self.recitylbl.setText("")
		self.recitylbl.setObjectName("recitylbl")
		self.verticalLayout_3.addWidget(self.recitylbl)
		self.reagelbl = QtWidgets.QLabel(self.layoutWidget_3)
		self.reagelbl.setText("")
		self.reagelbl.setObjectName("reagelbl")
		self.verticalLayout_3.addWidget(self.reagelbl)
		self.regenderlbl = QtWidgets.QLabel(self.layoutWidget_3)
		self.regenderlbl.setText("")
		self.regenderlbl.setObjectName("regenderlbl")
		self.verticalLayout_3.addWidget(self.regenderlbl)
		self.searchButton = QtWidgets.QPushButton(deleteCustomer)
		self.searchButton.setGeometry(QtCore.QRect(272, 45, 61, 31))
		self.searchButton.setObjectName("searchButton")
		self.searchButton.clicked.connect(self.searchCustomer)
		self.searchled = QtWidgets.QLineEdit(deleteCustomer)
		self.searchled.setGeometry(QtCore.QRect(74, 51, 191, 20))
		self.searchled.setObjectName("searchled")
		self.label_2 = QtWidgets.QLabel(deleteCustomer)
		self.label_2.setGeometry(QtCore.QRect(20, 54, 47, 13))
		self.label_2.setObjectName("label_2")
		self.retranslateUi(deleteCustomer)
		QtCore.QMetaObject.connectSlotsByName(deleteCustomer)
		self.detailsbtn.clicked.connect(self.openHistory)
		self.updatebtn.setEnabled(False)
		self.detailsbtn.setEnabled(False)

	def retranslateUi(self, deleteCustomer):
		_translate = QtCore.QCoreApplication.translate
		deleteCustomer.setWindowTitle(_translate("deleteCustomer", "Search Customer"))
		self.label.setText(_translate("deleteCustomer", "Welcome, "))
		self.updatebtn.setText(_translate("deleteCustomer", "Delete"))
		self.cancelbtn.setText(_translate("deleteCustomer", "Cancel"))
		self.label_8.setText(_translate("deleteCustomer", "Name:"))
		self.label_9.setText(_translate("deleteCustomer", "Mobile # :"))
		self.label_10.setText(_translate("deleteCustomer", "City :"))
		self.label_11.setText(_translate("deleteCustomer", "Age :"))
		self.label_12.setText(_translate("deleteCustomer", "Gender :"))
		self.searchButton.setText(_translate("deleteCustomer", "Search"))
		self.label_2.setText(_translate("deleteCustomer", "Mobile #"))
		self.label_19.setText(_translate("deleteCustomer", "Mobile #1"))
		self.label_20.setText(_translate("deleteCustomer", "Mobile #2"))
		self.label_21.setText(_translate("deleteCustomer", "Mobile #3"))
		self.label_22.setText(_translate("deleteCustomer", "Mobile #4"))
		self.detailsbtn.setText(_translate("deleteCustomer", "Details"))

	def searchCustomer(self):
		mob_num = self.searchled.text()
		if mob_num == '':
			self.statuslbl.setText('Must enter mobilephone to start search')
		elif select_customer_by_mob_num(mob_num):
			selectedCust = select_customer_by_mob_num(mob_num)
			self.renamelbl.setText(selectedCust.name)
			self.remobilenumlbl.setText(selectedCust.mobile_number)
			self.remobilenumlbl1.setText(selectedCust.mobile_number_1)
			self.remobilenumlbl2.setText(selectedCust.mobile_number_2)
			self.remobilenumlbl3.setText(selectedCust.mobile_number_3)
			self.remobilenumlbl4.setText(selectedCust.mobile_number_4)
			city_name = select_city_by_id(selectedCust.city_id).name
			self.recitylbl.setText(city_name)
			self.reagelbl.setText(str(selectedCust.age))
			self.regenderlbl.setText(selectedCust.gender.capitalize())
			self.statuslbl.setText('')
			self.detailsbtn.setEnabled(True)
			# role handel
			role = getLoginDataPKL()['role']
			if int(role) == 1 or int(role) == 2 or int(role) == 3:
				self.updatebtn.setEnabled(False)
			else:
				self.updatebtn.setEnabled(True)

			if select_maintenance_customer(selectedCust.id):
				self.statuslbl.setText("Can't delete, this customer have maintenance")
			else:
				return False
		else:
			self.statuslbl.setText("Can't found customer")

	def deleteCustomer(self):
		mob_num = self.searchled.text()
		selectedCust = select_customer_by_mob_num(mob_num)
		if select_maintenance_customer(selectedCust.id):
			self.statuslbl.setText("Can't delete customer")
		else:
			reply = QMessageBox.question(QMessageBox(), 'Delete', "Are you sure to delete this customer ?\n"
																  "This action you can't undo",
										 QMessageBox.Yes | QMessageBox.No)
			if reply == QMessageBox.Yes:
				delete_customer(selectedCust.id)
				self.close()

	def openHistory(self):
		from uiview.ui_customerHistory import Ui_historyDialog
		mob_num = self.searchled.text()
		selectedCust = select_customer_by_mob_num(mob_num)
		self.hd = Ui_historyDialog(selectedCust)
		self.hd.exec_()


# if __name__ == "__main__":
# 	app = QtWidgets.QApplication(sys.argv)
# 	myapp = Ui_deleteCustomer()
# 	myapp.show()
# 	app.exec_()
