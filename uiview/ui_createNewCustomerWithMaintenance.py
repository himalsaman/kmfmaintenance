# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_createNewCustomer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QDialog

from Control.customerControl import validCustomer
# from Control.maintenanceLogic import creatMaintenanceWithNewCustomer
from Control.maintenanceLogic import creatMaintenanceWithNewCustomer
from Control.userControl import getLoginDataPKL
from models import cityModel
from models import customersModel


class Ui_createNewCustomerWithMaintenance(QDialog):
	def __init__(self, parent=None):
		super(Ui_createNewCustomerWithMaintenance, self).__init__()
		self.setupUi(self)

	def setupUi(self, createNewCustomer):
		createNewCustomer.setObjectName("createNewCustomer")
		createNewCustomer.resize(391, 312)
		self.label = QtWidgets.QLabel(createNewCustomer)
		self.label.setGeometry(QtCore.QRect(10, 10, 47, 16))
		self.label.setObjectName("label")
		self.loggeduserlbl = QtWidgets.QLabel(createNewCustomer)
		self.loggeduserlbl.setGeometry(QtCore.QRect(60, 10, 191, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggeduserlbl.setFont(font)
		self.loggeduserlbl.setText("")
		self.loggeduserlbl.setObjectName("loggeduserlbl")
		self.loggeduserlbl.setText(getLoginDataPKL()['name'])
		self.line = QtWidgets.QFrame(createNewCustomer)
		self.line.setGeometry(QtCore.QRect(5, 27, 381, 16))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.custnameled = QtWidgets.QLineEdit(createNewCustomer)
		self.custnameled.setGeometry(QtCore.QRect(63, 43, 261, 20))
		self.custnameled.setObjectName("custnameled")
		self.mobcustled = QtWidgets.QLineEdit(createNewCustomer)
		self.mobcustled.setGeometry(QtCore.QRect(63, 79, 191, 20))
		self.mobcustled.setObjectName("mobcustled")
		self.mobcustled.setValidator(QIntValidator())
		self.citycmbx = QtWidgets.QComboBox(createNewCustomer)
		self.citycmbx.setGeometry(QtCore.QRect(60, 110, 171, 22))
		self.citycmbx.setObjectName("citycmbx")

		self.citycmbx.addItem("", 0)
		for city in cityModel.select_all_cities():
			self.citycmbx.addItem(city.name, city.id)

		self.agespin = QtWidgets.QSpinBox(createNewCustomer)
		self.agespin.setGeometry(QtCore.QRect(63, 149, 81, 22))
		self.agespin.setObjectName("agespin")
		self.groupBox = QtWidgets.QGroupBox(createNewCustomer)
		self.groupBox.setGeometry(QtCore.QRect(63, 180, 191, 41))
		self.groupBox.setTitle("")
		self.groupBox.setObjectName("groupBox")
		self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(3, 1, 181, 31))
		self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.malebtn = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
		self.malebtn.setObjectName("malebtn")
		self.horizontalLayout.addWidget(self.malebtn)
		self.femalerbtn = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
		self.femalerbtn.setObjectName("femalerbtn")
		self.horizontalLayout.addWidget(self.femalerbtn)
		self.savebtn = QtWidgets.QPushButton(createNewCustomer)
		self.savebtn.setGeometry(QtCore.QRect(85, 269, 75, 31))
		self.savebtn.setObjectName("savebtn")

		self.savebtn.clicked.connect(self.do_createNewCustomer)

		self.cancelbtn = QtWidgets.QPushButton(createNewCustomer)
		self.cancelbtn.setGeometry(QtCore.QRect(205, 269, 75, 31))
		self.cancelbtn.setObjectName("cancelbtn")

		self.cancelbtn.clicked.connect(self.close)

		self.statuslbl = QtWidgets.QLabel(createNewCustomer)
		self.statuslbl.setGeometry(QtCore.QRect(5, 228, 381, 31))
		self.statuslbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.statuslbl.setText("")
		self.statuslbl.setAlignment(QtCore.Qt.AlignCenter)
		self.statuslbl.setObjectName("statuslbl")
		self.layoutWidget = QtWidgets.QWidget(createNewCustomer)
		self.layoutWidget.setGeometry(QtCore.QRect(9, 37, 51, 171))
		self.layoutWidget.setObjectName("layoutWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.label_3 = QtWidgets.QLabel(self.layoutWidget)
		self.label_3.setObjectName("label_3")
		self.verticalLayout.addWidget(self.label_3)
		self.label_4 = QtWidgets.QLabel(self.layoutWidget)
		self.label_4.setObjectName("label_4")
		self.verticalLayout.addWidget(self.label_4)
		self.label_7 = QtWidgets.QLabel(self.layoutWidget)
		self.label_7.setObjectName("label_7")
		self.verticalLayout.addWidget(self.label_7)
		self.label_6 = QtWidgets.QLabel(self.layoutWidget)
		self.label_6.setObjectName("label_6")
		self.verticalLayout.addWidget(self.label_6)
		self.label_5 = QtWidgets.QLabel(self.layoutWidget)
		self.label_5.setObjectName("label_5")
		self.verticalLayout.addWidget(self.label_5)

		self.retranslateUi(createNewCustomer)
		QtCore.QMetaObject.connectSlotsByName(createNewCustomer)

	def retranslateUi(self, createNewCustomer):
		_translate = QtCore.QCoreApplication.translate
		createNewCustomer.setWindowTitle(_translate("createNewCustomer", "Create New Customer"))
		self.label.setText(_translate("createNewCustomer", "Welcome, "))
		self.malebtn.setText(_translate("createNewCustomer", "Male"))
		self.femalerbtn.setText(_translate("createNewCustomer", "Female"))
		self.savebtn.setText(_translate("createNewCustomer", "Save"))
		self.cancelbtn.setText(_translate("createNewCustomer", "Cancel"))
		self.label_3.setText(_translate("createNewCustomer", "Name:"))
		self.label_4.setText(_translate("createNewCustomer", "Mobile # :"))
		self.label_7.setText(_translate("createNewCustomer", "City :"))
		self.label_6.setText(_translate("createNewCustomer", "Age :"))
		self.label_5.setText(_translate("createNewCustomer", "Gender :"))

	def do_createNewCustomer(self):
		if not self.custnameled.text() or\
				not self.mobcustled.text() or\
				self.citycmbx.currentIndex() == 0 or\
				self.agespin.value() == 0 or\
				not self.malebtn.isChecked() and\
				not self.femalerbtn.isChecked():
			self.statuslbl.setText('All fields is required ')
		else :
			if not customersModel.select_customer_by_mob_num(self.mobcustled.text()):
				name = self.custnameled.text()
				mobileNumber = self.mobcustled.text()
				if self.malebtn.isChecked():
					gndr = 'male'
				elif self.femalerbtn.isChecked():
					gndr = 'female'
				age = self.agespin.text()
				city_id = self.citycmbx.currentIndex()
				mainte = creatMaintenanceWithNewCustomer(name, mobileNumber, gndr, age, city_id)
				self.statuslbl.setText('A new customer added successfully ')
				# print(mainte)
				from uiview.ui_createBOM import Ui_createBOMDialog
				self.b = Ui_createBOMDialog(mainte)
				self.b.exec_()
				self.close()
			else:
				self.statuslbl.setText('This customer is already exists ')

# if __name__ == "__main__":
# 	app = QtWidgets.QApplication(sys.argv)
# 	myapp = Ui_createNewCustomerWithMaintenance()
# 	myapp.show()
# 	app.exec_()