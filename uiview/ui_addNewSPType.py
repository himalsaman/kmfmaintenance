# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addNewSPType.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import random
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QDialog

from Control.userControl import getLoginDataPKL
from models.sparePartsModel import add_spare_parts


class Ui_addNewSPTypeDialog(QDialog):
	def __init__(self, parent=None):
		super(Ui_addNewSPTypeDialog, self).__init__()
		self.setupUi(self)


	def setupUi(self, addNewSPTypeDialog):
		addNewSPTypeDialog.setObjectName("addNewSPTypeDialog")
		addNewSPTypeDialog.resize(479, 276)
		self.label = QtWidgets.QLabel(addNewSPTypeDialog)
		self.label.setGeometry(QtCore.QRect(10, 5, 51, 21))
		self.label.setObjectName("label")
		self.loggeduserlbl = QtWidgets.QLabel(addNewSPTypeDialog)
		self.loggeduserlbl.setGeometry(QtCore.QRect(62, 6, 171, 21))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggeduserlbl.setFont(font)
		self.loggeduserlbl.setObjectName("loggeduserlbl")
		self.loggeduserlbl.setText(getLoginDataPKL()['name'])
		self.line = QtWidgets.QFrame(addNewSPTypeDialog)
		self.line.setGeometry(QtCore.QRect(7, 25, 491, 16))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.verticalLayoutWidget = QtWidgets.QWidget(addNewSPTypeDialog)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(14, 40, 111, 131))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_3.setObjectName("label_3")
		self.verticalLayout.addWidget(self.label_3)
		self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_4.setObjectName("label_4")
		self.verticalLayout.addWidget(self.label_4)
		self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_6.setObjectName("label_6")
		self.verticalLayout.addWidget(self.label_6)
		self.spNameled = QtWidgets.QLineEdit(addNewSPTypeDialog)
		self.spNameled.setGeometry(QtCore.QRect(56, 52, 370, 20))
		self.spNameled.setObjectName("spNameled")
		self.invQTYSpinBox = QtWidgets.QDoubleSpinBox(addNewSPTypeDialog)
		self.invQTYSpinBox.setGeometry(QtCore.QRect(125, 141, 131, 22))
		self.invQTYSpinBox.setDecimals(6)
		self.invQTYSpinBox.setMaximum(1000.0)
		self.invQTYSpinBox.setSingleStep(0.0001)
		self.invQTYSpinBox.setObjectName("invQTYSpinBox")
		self.label_7 = QtWidgets.QLabel(addNewSPTypeDialog)
		self.label_7.setGeometry(QtCore.QRect(240, 99, 41, 16))
		self.label_7.setObjectName("label_7")
		self.spunitcomboBox = QtWidgets.QComboBox(addNewSPTypeDialog)
		self.spunitcomboBox.setGeometry(QtCore.QRect(272, 97, 161, 22))
		self.spunitcomboBox.setObjectName("spunitcomboBox")
		self.spunitcomboBox.addItem("")
		self.spunitcomboBox.addItem("")
		self.label_8 = QtWidgets.QLabel(addNewSPTypeDialog)
		self.label_8.setGeometry(QtCore.QRect(280, 145, 60, 13))
		self.label_8.setObjectName("label_8")
		self.spcostled = QtWidgets.QLineEdit(addNewSPTypeDialog)
		self.spcostled.setGeometry(QtCore.QRect(311, 143, 140, 20))
		self.spcostled.setObjectName("spcostled")
		self.spcostled.setValidator(QDoubleValidator())
		self.savebtn = QtWidgets.QPushButton(addNewSPTypeDialog)
		self.savebtn.setGeometry(QtCore.QRect(148, 223, 72, 41))
		self.savebtn.setObjectName("savebtn")

		self.savebtn.clicked.connect(self.doAdd)

		self.cancelbtn = QtWidgets.QPushButton(addNewSPTypeDialog)
		self.cancelbtn.setGeometry(QtCore.QRect(256, 223, 72, 41))
		self.cancelbtn.setObjectName("cancelbtn")

		self.cancelbtn.clicked.connect(self.close)

		self.statulbl = QtWidgets.QLabel(addNewSPTypeDialog)
		self.statulbl.setGeometry(QtCore.QRect(16, 177, 461, 41))
		self.statulbl.setText("")
		self.statulbl.setAlignment(QtCore.Qt.AlignCenter)
		self.statulbl.setObjectName("statulbl")
		self.label_2 = QtWidgets.QLabel(addNewSPTypeDialog)
		self.label_2.setGeometry(QtCore.QRect(454, 147, 47, 13))
		self.label_2.setObjectName("label_2")
		self.spcodeled = QtWidgets.QLineEdit(addNewSPTypeDialog)
		self.spcodeled.setGeometry(QtCore.QRect(50, 97, 171, 20))
		self.spcodeled.setObjectName("spcodeled")
		self.statulbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.retranslateUi(addNewSPTypeDialog)
		self.spunitcomboBox.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(addNewSPTypeDialog)


	def retranslateUi(self, addNewSPTypeDialog):
		_translate = QtCore.QCoreApplication.translate
		addNewSPTypeDialog.setWindowTitle(_translate("addNewSPTypeDialog", "Add New Spare Parts Type"))
		self.label.setText(_translate("addNewSPTypeDialog", "Welcome,"))
		self.label_3.setText(_translate("addNewSPTypeDialog", "Name :"))
		self.label_4.setText(_translate("addNewSPTypeDialog", "Code:"))
		self.label_6.setText(_translate("addNewSPTypeDialog", "Initial Inventory QTY :"))
		self.label_7.setText(_translate("addNewSPTypeDialog", "Unit :"))
		self.spunitcomboBox.setItemText(0, _translate("addNewSPTypeDialog", ""))
		self.spunitcomboBox.setItemText(1, _translate("addNewSPTypeDialog", "Each ( EA )"))
		self.label_8.setText(_translate("addNewSPTypeDialog", "Cost :"))
		self.savebtn.setText(_translate("addNewSPTypeDialog", "Add"))
		self.cancelbtn.setText(_translate("addNewSPTypeDialog", "Cancel"))
		self.label_2.setText(_translate("addNewSPTypeDialog", "SAR"))


	def doAdd(self):
		if self.spNameled.text() == '' or \
						self.spunitcomboBox.currentIndex() == 0 or\
						self.spcostled.text() == '' or \
						self.invQTYSpinBox.value() == 0:
			self.statulbl.setText('All fields is required')
		else:
			self.statulbl.setText('ok')
			name = self.spNameled.text()
			if self.spunitcomboBox.currentIndex() == 1:
				unit = 'ea'
			if self.spcodeled.text() == '':
				code = '0'
			else:
				code = self.spcodeled.text()
			cost = self.spcostled.text()
			invqty = self.invQTYSpinBox.value()
			gencode = 'sp {}'.format(random.randrange(10, 10000, 2))
			add_spare_parts(name, code, gencode, cost, invqty, unit)
			self.statulbl.setText(name + ", added successfully")


