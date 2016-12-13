# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_updateCustomer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QDialog

from Control.userControl import getLoginDataPKL
from models import cityModel
from models.cityModel import select_city_by_id
from models.customersModel import select_customer_by_mob_num, update_customer


class Ui_updateCustomer(QDialog):
	def __init__(self, parent=None):
		super(Ui_updateCustomer, self).__init__()
		self.setupUi(self)

	def setupUi(self, updateCustomer):
		self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

		updateCustomer.setObjectName("updateCustomer")
		updateCustomer.resize(683, 390)
		self.label = QtWidgets.QLabel(updateCustomer)
		self.label.setGeometry(QtCore.QRect(10, 10, 47, 16))
		self.label.setObjectName("label")
		self.loggeduserlbl = QtWidgets.QLabel(updateCustomer)
		self.loggeduserlbl.setGeometry(QtCore.QRect(60, 10, 191, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggeduserlbl.setFont(font)
		self.loggeduserlbl.setText("")
		self.loggeduserlbl.setObjectName("loggeduserlbl")
		self.loggeduserlbl.setText(getLoginDataPKL()['name'])
		self.line = QtWidgets.QFrame(updateCustomer)
		self.line.setGeometry(QtCore.QRect(5, 27, 671, 16))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.custnameled = QtWidgets.QLineEdit(updateCustomer)
		self.custnameled.setGeometry(QtCore.QRect(404, 44, 261, 20))
		self.custnameled.setObjectName("custnameled")

		self.mobcustled = QtWidgets.QLineEdit(updateCustomer)
		self.mobcustled.setGeometry(QtCore.QRect(404, 70, 191, 20))
		self.mobcustled.setObjectName("mobcustled")

		self.mobcustled91 = QtWidgets.QLineEdit(updateCustomer)
		self.mobcustled91.setGeometry(QtCore.QRect(404, 100, 191, 20))
		self.mobcustled91.setObjectName("mobcustled91")

		self.mobcustled92 = QtWidgets.QLineEdit(updateCustomer)
		self.mobcustled92.setGeometry(QtCore.QRect(404, 130, 191, 20))
		self.mobcustled92.setObjectName("mobcustled92")

		self.mobcustled93 = QtWidgets.QLineEdit(updateCustomer)
		self.mobcustled93.setGeometry(QtCore.QRect(404, 160, 191, 20))
		self.mobcustled93.setObjectName("mobcustled93")

		self.mobcustled94 = QtWidgets.QLineEdit(updateCustomer)
		self.mobcustled94.setGeometry(QtCore.QRect(404, 190, 191, 20))
		self.mobcustled94.setObjectName("mobcustled94")

		self.citycmbx = QtWidgets.QComboBox(updateCustomer)
		self.citycmbx.setGeometry(QtCore.QRect(401, 220, 171, 22))
		self.citycmbx.setObjectName("citycmbx")
		self.citycmbx.addItem("", 0)
		for city in cityModel.select_all_cities():
			self.citycmbx.addItem(city.name, city.id)
		self.agespin = QtWidgets.QSpinBox(updateCustomer)
		self.agespin.setGeometry(QtCore.QRect(404, 250, 81, 22))
		self.agespin.setObjectName("agespin")
		self.groupBox = QtWidgets.QGroupBox(updateCustomer)
		self.groupBox.setGeometry(QtCore.QRect(404, 280, 191, 41))
		self.groupBox.setTitle("")
		self.groupBox.setObjectName("groupBox")
		self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 2, 181, 31))
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
		self.updatebtn = QtWidgets.QPushButton(updateCustomer)
		self.updatebtn.setGeometry(QtCore.QRect(435, 350, 75, 31))
		self.updatebtn.setObjectName("updatebtn")
		self.updatebtn.clicked.connect(self.updateCustomer)
		self.cancelbtn = QtWidgets.QPushButton(updateCustomer)
		self.cancelbtn.setGeometry(QtCore.QRect(555, 350, 75, 31))
		self.cancelbtn.setObjectName("cancelbtn")
		self.cancelbtn.clicked.connect(self.close)
		self.statuslbl = QtWidgets.QLabel(updateCustomer)
		self.statuslbl.setGeometry(QtCore.QRect(10, 345, 331, 31))
		self.statuslbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.statuslbl.setText("")
		self.statuslbl.setAlignment(QtCore.Qt.AlignCenter)
		self.statuslbl.setObjectName("statuslbl")
		self.layoutWidget = QtWidgets.QWidget(updateCustomer)
		self.layoutWidget.setGeometry(QtCore.QRect(350, 38, 51, 265))
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

		self.label_41 = QtWidgets.QLabel(self.layoutWidget)
		self.label_41.setObjectName("label_41")
		self.verticalLayout.addWidget(self.label_41)

		self.label_42 = QtWidgets.QLabel(self.layoutWidget)
		self.label_42.setObjectName("label_42")
		self.verticalLayout.addWidget(self.label_42)

		self.label_43 = QtWidgets.QLabel(self.layoutWidget)
		self.label_43.setObjectName("label_43")
		self.verticalLayout.addWidget(self.label_43)

		self.label_44 = QtWidgets.QLabel(self.layoutWidget)
		self.label_44.setObjectName("label_44")
		self.verticalLayout.addWidget(self.label_44)

		self.label_7 = QtWidgets.QLabel(self.layoutWidget)
		self.label_7.setObjectName("label_7")
		self.verticalLayout.addWidget(self.label_7)
		self.label_6 = QtWidgets.QLabel(self.layoutWidget)
		self.label_6.setObjectName("label_6")
		self.verticalLayout.addWidget(self.label_6)
		self.label_5 = QtWidgets.QLabel(self.layoutWidget)
		self.label_5.setObjectName("label_5")
		self.verticalLayout.addWidget(self.label_5)
		self.line_2 = QtWidgets.QFrame(updateCustomer)
		self.line_2.setGeometry(QtCore.QRect(333, 40, 20, 340))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.layoutWidget_2 = QtWidgets.QWidget(updateCustomer)
		self.layoutWidget_2.setGeometry(QtCore.QRect(10, 88, 70, 251))
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

		self.label_91 = QtWidgets.QLabel(self.layoutWidget_2)
		self.label_91.setObjectName("label_91")
		self.verticalLayout_2.addWidget(self.label_91)

		self.label_92 = QtWidgets.QLabel(self.layoutWidget_2)
		self.label_92.setObjectName("label_92")
		self.verticalLayout_2.addWidget(self.label_92)

		self.label_93 = QtWidgets.QLabel(self.layoutWidget_2)
		self.label_93.setObjectName("label_93")
		self.verticalLayout_2.addWidget(self.label_93)

		self.label_94 = QtWidgets.QLabel(self.layoutWidget_2)
		self.label_94.setObjectName("label_94")
		self.verticalLayout_2.addWidget(self.label_94)

		self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
		self.label_10.setObjectName("label_10")
		self.verticalLayout_2.addWidget(self.label_10)
		self.label_11 = QtWidgets.QLabel(self.layoutWidget_2)
		self.label_11.setObjectName("label_11")
		self.verticalLayout_2.addWidget(self.label_11)
		self.label_12 = QtWidgets.QLabel(self.layoutWidget_2)
		self.label_12.setObjectName("label_12")
		self.verticalLayout_2.addWidget(self.label_12)
		self.layoutWidget_3 = QtWidgets.QWidget(updateCustomer)
		self.layoutWidget_3.setGeometry(QtCore.QRect(90, 88, 271, 251))
		self.layoutWidget_3.setObjectName("layoutWidget_3")
		self.layoutWidget_3.setStyleSheet("color: rgb(255, 0, 0);")
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

		self.remobilenumlbl91 = QtWidgets.QLabel(self.layoutWidget_3)
		self.remobilenumlbl91.setText("")
		self.remobilenumlbl91.setObjectName("remobilenumlbl91")
		self.verticalLayout_3.addWidget(self.remobilenumlbl91)

		self.remobilenumlbl92 = QtWidgets.QLabel(self.layoutWidget_3)
		self.remobilenumlbl92.setText("")
		self.remobilenumlbl92.setObjectName("remobilenumlbl92")
		self.verticalLayout_3.addWidget(self.remobilenumlbl92)

		self.remobilenumlbl93 = QtWidgets.QLabel(self.layoutWidget_3)
		self.remobilenumlbl93.setText("")
		self.remobilenumlbl93.setObjectName("remobilenumlbl93")
		self.verticalLayout_3.addWidget(self.remobilenumlbl93)

		self.remobilenumlbl94 = QtWidgets.QLabel(self.layoutWidget_3)
		self.remobilenumlbl94.setText("")
		self.remobilenumlbl94.setObjectName("remobilenumlbl94")
		self.verticalLayout_3.addWidget(self.remobilenumlbl94)

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
		self.searchButton = QtWidgets.QPushButton(updateCustomer)
		self.searchButton.setGeometry(QtCore.QRect(272, 45, 61, 31))
		self.searchButton.setObjectName("searchButton")
		self.mobcustled.setValidator(QIntValidator())
		self.searchButton.clicked.connect(self.searchCustomer)
		self.searchled = QtWidgets.QLineEdit(updateCustomer)
		self.searchled.setGeometry(QtCore.QRect(74, 51, 191, 20))
		self.searchled.setObjectName("searchled")
		self.label_2 = QtWidgets.QLabel(updateCustomer)
		self.label_2.setGeometry(QtCore.QRect(20, 54, 47, 13))
		self.label_2.setObjectName("label_2")
		self.retranslateUi(updateCustomer)
		QtCore.QMetaObject.connectSlotsByName(updateCustomer)

	def retranslateUi(self, updateCustomer):
		_translate = QtCore.QCoreApplication.translate
		updateCustomer.setWindowTitle(_translate("updateCustomer", "Update Customer"))
		self.label.setText(_translate("updateCustomer", "Welcome, "))
		self.malebtn.setText(_translate("updateCustomer", "Male"))
		self.femalerbtn.setText(_translate("updateCustomer", "Female"))
		self.updatebtn.setText(_translate("updateCustomer", "Save"))
		self.cancelbtn.setText(_translate("updateCustomer", "Cancel"))
		self.label_3.setText(_translate("updateCustomer", "Name:"))
		self.label_4.setText(_translate("updateCustomer", "Mobile # :"))
		self.label_41.setText(_translate("updateCustomer", "Mobile 1 # :"))
		self.label_42.setText(_translate("updateCustomer", "Mobile 2 # :"))
		self.label_43.setText(_translate("updateCustomer", "Mobile 3 # :"))
		self.label_44.setText(_translate("updateCustomer", "Mobile 4 # :"))
		self.label_7.setText(_translate("updateCustomer", "City :"))
		self.label_6.setText(_translate("updateCustomer", "Age :"))
		self.label_5.setText(_translate("updateCustomer", "Gender :"))
		self.label_8.setText(_translate("updateCustomer", "Name:"))
		self.label_9.setText(_translate("updateCustomer", "M. Mobile # :"))
		self.label_91.setText(_translate("updateCustomer", "M. Mobile 1 # :"))
		self.label_92.setText(_translate("updateCustomer", "M. Mobile 2 # :"))
		self.label_93.setText(_translate("updateCustomer", "M. Mobile 3 # :"))
		self.label_94.setText(_translate("updateCustomer", "M. Mobile 4 # :"))
		self.label_10.setText(_translate("updateCustomer", "City :"))
		self.label_11.setText(_translate("updateCustomer", "Age :"))
		self.label_12.setText(_translate("updateCustomer", "Gender :"))
		self.searchButton.setText(_translate("updateCustomer", "Search"))
		self.label_2.setText(_translate("updateCustomer", "Mobile #"))

	def searchCustomer(self):
		mob_num = self.searchled.text()
		if mob_num == '':
			self.statuslbl.setText('Must enter mobilephone to start search')
		elif select_customer_by_mob_num(mob_num):
			selectedCust = select_customer_by_mob_num(mob_num)
			self.renamelbl.setText(selectedCust.name)
			self.custnameled.setText(selectedCust.name)
			self.remobilenumlbl.setText(selectedCust.mobile_number)
			self.remobilenumlbl91.setText(selectedCust.mobile_number_1)
			self.remobilenumlbl92.setText(selectedCust.mobile_number_2)
			self.remobilenumlbl93.setText(selectedCust.mobile_number_3)
			self.remobilenumlbl94.setText(selectedCust.mobile_number_4)
			self.mobcustled.setText(selectedCust.mobile_number)
			self.mobcustled91.setText(selectedCust.mobile_number_1)
			self.mobcustled92.setText(selectedCust.mobile_number_2)
			self.mobcustled93.setText(selectedCust.mobile_number_3)
			self.mobcustled94.setText(selectedCust.mobile_number_4)
			city = select_city_by_id(selectedCust.city_id)
			self.recitylbl.setText(city.name)
			self.citycmbx.setCurrentText(city.name)
			self.reagelbl.setText(str(selectedCust.age))
			self.agespin.setValue(selectedCust.age)
			self.regenderlbl.setText(selectedCust.gender.capitalize())
			if selectedCust.gender == 'male':
				self.malebtn.setChecked(True)
			else:
				self.femalerbtn.setChecked(True)
			self.statuslbl.setText('')
		else:
			self.statuslbl.setText("Can't found customer")

	def updateCustomer(self):
		if select_customer_by_mob_num(self.searchled.text()) and self.mobcustled.text() != '' or \
						self.remobilenumlbl.text() != '':
			selectedCust = select_customer_by_mob_num(self.searchled.text())
			custname = self.custnameled.text()
			custmobnum = self.mobcustled.text()
			custmobnum1 = self.mobcustled91.text()
			custmobnum2 = self.mobcustled92.text()
			custmobnum3 = self.mobcustled93.text()
			custmobnum4 = self.mobcustled94.text()
			custcity_id = self.citycmbx.currentIndex()
			custage = self.agespin.text()
			if self.malebtn.isChecked():
				gndr = 'male'
			elif self.femalerbtn.isChecked():
				gndr = 'female'
			if custname:
				custname = self.renamelbl.text()
			if not custmobnum:
				custmobnum = self.remobilenumlbl.text()
			if self.citycmbx.currentIndex() == 0:
				custcity_id = selectedCust.city_id
			if self.agespin.value() == 0:
				custage = self.reagelbl.text()
			if not self.malebtn.isChecked() | self.femalerbtn.isChecked():
				gndr = self.regenderlbl.text()
			update_customer(selectedCust.id, custname, custmobnum, custmobnum1, custmobnum2, custmobnum3,
							custmobnum4, gndr, custage, custcity_id)
			self.close()
		else:
			self.statuslbl.setText("No Customer To Update")


# if __name__ == "__main__":
# 	app = QtWidgets.QApplication(sys.argv)
# 	myapp = Ui_updateCustomer()
# 	myapp.show()
# 	app.exec_()
