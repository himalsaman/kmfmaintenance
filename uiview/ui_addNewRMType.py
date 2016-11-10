# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addNewRMType.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import random
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

from models.rawMaterialModel import add_raw_material


class Ui_addNewRMTypeDialog(QDialog):
	def __init__(self, parent=None):
		super(Ui_addNewRMTypeDialog, self).__init__()
		self.setupUi(self)

	def setupUi(self, addNewRMTypeDialog):
		addNewRMTypeDialog.setObjectName("addNewRMTypeDialog")
		addNewRMTypeDialog.resize(506, 310)
		self.label = QtWidgets.QLabel(addNewRMTypeDialog)
		self.label.setGeometry(QtCore.QRect(10, 5, 51, 21))
		self.label.setObjectName("label")
		self.loggeduserlbl = QtWidgets.QLabel(addNewRMTypeDialog)
		self.loggeduserlbl.setGeometry(QtCore.QRect(62, 6, 171, 21))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggeduserlbl.setFont(font)
		self.loggeduserlbl.setText("")
		self.loggeduserlbl.setObjectName("loggeduserlbl")
		self.line = QtWidgets.QFrame(addNewRMTypeDialog)
		self.line.setGeometry(QtCore.QRect(7, 25, 491, 16))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.verticalLayoutWidget = QtWidgets.QWidget(addNewRMTypeDialog)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(14, 40, 111, 171))
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
		self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_5.setObjectName("label_5")
		self.verticalLayout.addWidget(self.label_5)
		self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_6.setObjectName("label_6")
		self.verticalLayout.addWidget(self.label_6)
		self.rmNameled = QtWidgets.QLineEdit(addNewRMTypeDialog)
		self.rmNameled.setGeometry(QtCore.QRect(56, 52, 370, 20))
		self.rmNameled.setObjectName("rmNameled")
		self.srtingSizeled = QtWidgets.QLineEdit(addNewRMTypeDialog)
		self.srtingSizeled.setGeometry(QtCore.QRect(77, 139, 190, 20))
		self.srtingSizeled.setObjectName("srtingSizeled")
		self.invQTYSpinBox = QtWidgets.QDoubleSpinBox(addNewRMTypeDialog)
		self.invQTYSpinBox.setGeometry(QtCore.QRect(127, 181, 131, 22))
		self.invQTYSpinBox.setDecimals(6)
		self.invQTYSpinBox.setMaximum(100000000.0)
		self.invQTYSpinBox.setSingleStep(0.0001)
		self.invQTYSpinBox.setObjectName("invQTYSpinBox")
		self.label_7 = QtWidgets.QLabel(addNewRMTypeDialog)
		self.label_7.setGeometry(QtCore.QRect(240, 99, 41, 16))
		self.label_7.setObjectName("label_7")
		self.rmDefualtSizeSpinBox = QtWidgets.QDoubleSpinBox(addNewRMTypeDialog)
		self.rmDefualtSizeSpinBox.setGeometry(QtCore.QRect(86, 95, 131, 22))
		self.rmDefualtSizeSpinBox.setDecimals(6)
		self.rmDefualtSizeSpinBox.setMaximum(1000000.0)
		self.rmDefualtSizeSpinBox.setSingleStep(0.0001)
		self.rmDefualtSizeSpinBox.setObjectName("rmDefualtSizeSpinBox")
		self.rmunitcomboBox = QtWidgets.QComboBox(addNewRMTypeDialog)
		self.rmunitcomboBox.setGeometry(QtCore.QRect(272, 97, 161, 22))
		self.rmunitcomboBox.setObjectName("rmunitcomboBox")
		self.rmunitcomboBox.addItem("","")
		self.rmunitcomboBox.addItem("m", "")
		self.rmunitcomboBox.addItem("cm","")
		self.rmunitcomboBox.addItem("m","")
		self.rmunitcomboBox.addItem("g","")
		self.rmunitcomboBox.addItem("kg","")
		self.rmunitcomboBox.addItem("ea","")
		self.rmunitcomboBox.addItem("l","")
		self.label_8 = QtWidgets.QLabel(addNewRMTypeDialog)
		self.label_8.setGeometry(QtCore.QRect(280, 141, 60, 13))
		self.label_8.setObjectName("label_8")
		self.rmcostled = QtWidgets.QLineEdit(addNewRMTypeDialog)
		self.rmcostled.setGeometry(QtCore.QRect(334, 139, 140, 20))
		self.rmcostled.setObjectName("rmcostled")
		self.savebtn = QtWidgets.QPushButton(addNewRMTypeDialog)
		self.savebtn.setGeometry(QtCore.QRect(148, 260, 72, 41))
		self.savebtn.setObjectName("savebtn")

		self.savebtn.clicked.connect(self.doAdd)

		self.cancelbtn = QtWidgets.QPushButton(addNewRMTypeDialog)
		self.cancelbtn.setGeometry(QtCore.QRect(256, 260, 72, 41))
		self.cancelbtn.setObjectName("cancelbtn")

		self.cancelbtn.clicked.connect(self.close)

		self.statulbl = QtWidgets.QLabel(addNewRMTypeDialog)
		self.statulbl.setGeometry(QtCore.QRect(16, 214, 461, 41))
		self.statulbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.statulbl.setAlignment(QtCore.Qt.AlignCenter)
		self.statulbl.setText("")
		self.statulbl.setAlignment(QtCore.Qt.AlignCenter)
		self.statulbl.setObjectName("statulbl")
		self.label_2 = QtWidgets.QLabel(addNewRMTypeDialog)
		self.label_2.setGeometry(QtCore.QRect(477, 143, 47, 13))
		self.label_2.setObjectName("label_2")

		self.retranslateUi(addNewRMTypeDialog)
		self.rmunitcomboBox.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(addNewRMTypeDialog)

	def retranslateUi(self, addNewRMTypeDialog):
		_translate = QtCore.QCoreApplication.translate
		addNewRMTypeDialog.setWindowTitle(_translate("addNewRMTypeDialog", "Add New Raw Material Type"))
		self.label.setText(_translate("addNewRMTypeDialog", "Welcome,"))
		self.label_3.setText(_translate("addNewRMTypeDialog", "Name :"))
		self.label_4.setText(_translate("addNewRMTypeDialog", "Default Size :"))
		self.label_5.setText(_translate("addNewRMTypeDialog", "String Size :"))
		self.label_6.setText(_translate("addNewRMTypeDialog", "Initial Inventory QTY :"))
		self.label_7.setText(_translate("addNewRMTypeDialog", "Unit :"))
		self.rmunitcomboBox.setItemText(0, _translate("addNewRMTypeDialog", ""))
		self.rmunitcomboBox.setItemText(1, _translate("addNewRMTypeDialog", "Millimetre ( MM )"))
		self.rmunitcomboBox.setItemText(2, _translate("addNewRMTypeDialog", "Centimeter ( CM )"))
		self.rmunitcomboBox.setItemText(3, _translate("addNewRMTypeDialog", "Metre ( M )"))
		self.rmunitcomboBox.setItemText(4, _translate("addNewRMTypeDialog", "Gram ( G )"))
		self.rmunitcomboBox.setItemText(5, _translate("addNewRMTypeDialog", "Kilogram ( KG )"))
		self.rmunitcomboBox.setItemText(6, _translate("addNewRMTypeDialog", "Each ( EA )"))
		self.rmunitcomboBox.setItemText(7, _translate("addNewRMTypeDialog", "Litre ( L )"))
		self.label_8.setText(_translate("addNewRMTypeDialog", "Cost / ds :"))
		self.savebtn.setText(_translate("addNewRMTypeDialog", "Add"))
		self.cancelbtn.setText(_translate("addNewRMTypeDialog", "Cancel"))
		self.label_2.setText(_translate("addNewRMTypeDialog", "SAR"))

	def doAdd(self):
		if self.rmNameled.text() == '' or\
						self.rmDefualtSizeSpinBox.value() == 0.000000 or \
						self.rmunitcomboBox.currentIndex() == 0 or \
						self.srtingSizeled.text() == '' or \
						self.rmcostled.text() == '' or \
						self.invQTYSpinBox.value() == 0.000000:
			self.statulbl.setText('All fields is required')
		else:
			self.statulbl.setText('ok')
			name = self.rmNameled.text()
			defsize = self.rmDefualtSizeSpinBox.value()
			if self.rmunitcomboBox.currentIndex() == 1:
				unit = 'mm'
			if self.rmunitcomboBox.currentIndex() == 2:
				unit = 'cm'
			if self.rmunitcomboBox.currentIndex() == 3:
				unit = 'm'
			if self.rmunitcomboBox.currentIndex() == 4:
				unit = 'g'
			if self.rmunitcomboBox.currentIndex() == 5:
				unit = 'kg'
			if self.rmunitcomboBox.currentIndex() == 6:
				unit = 'ea'
			if self.rmunitcomboBox.currentIndex() == 7:
				unit = 'l'
			strsize = self.srtingSizeled.text()
			cost = self.rmcostled.text()
			invqty = self.invQTYSpinBox.value()
			gencode = 'rw{}'.format(random.randrange(10, 10000, 2))
			add_raw_material(name, gencode, defsize, strsize, unit, cost, invqty)
			self.statulbl.setText(name + ", added successfully")


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	cnc_dialog = Ui_addNewRMTypeDialog()
	cnc_dialog.show()
	sys.exit(app.exec_())
