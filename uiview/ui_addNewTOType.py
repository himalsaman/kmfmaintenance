# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addNewTOType.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import random
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QDialog

from models.toolsModel import add_tools


class Ui_addNewTOTypeDialog(QDialog):
	def __init__(self):
		super(Ui_addNewTOTypeDialog, self).__init__()
		self.setupUi(self)

	def setupUi(self, addNewTOTypeDialog):
		self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

		addNewTOTypeDialog.setObjectName("addNewTOTypeDialog")
		addNewTOTypeDialog.resize(436, 269)
		self.label = QtWidgets.QLabel(addNewTOTypeDialog)
		self.label.setGeometry(QtCore.QRect(10, 5, 51, 21))
		self.label.setObjectName("label")
		self.loggeduserlbl = QtWidgets.QLabel(addNewTOTypeDialog)
		self.loggeduserlbl.setGeometry(QtCore.QRect(62, 6, 171, 21))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggeduserlbl.setFont(font)
		self.loggeduserlbl.setText("")
		self.loggeduserlbl.setObjectName("loggeduserlbl")
		self.line = QtWidgets.QFrame(addNewTOTypeDialog)
		self.line.setGeometry(QtCore.QRect(7, 25, 491, 16))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.verticalLayoutWidget = QtWidgets.QWidget(addNewTOTypeDialog)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(8, 40, 111, 121))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_3.setObjectName("label_3")
		self.verticalLayout.addWidget(self.label_3)
		self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_8.setObjectName("label_8")
		self.verticalLayout.addWidget(self.label_8)
		self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_6.setObjectName("label_6")
		self.verticalLayout.addWidget(self.label_6)
		self.toNameled = QtWidgets.QLineEdit(addNewTOTypeDialog)
		self.toNameled.setGeometry(QtCore.QRect(48, 50, 370, 20))
		self.toNameled.setObjectName("toNameled")
		self.invQTYSpinBox = QtWidgets.QDoubleSpinBox(addNewTOTypeDialog)
		self.invQTYSpinBox.setGeometry(QtCore.QRect(121, 133, 131, 22))
		self.invQTYSpinBox.setDecimals(6)
		self.invQTYSpinBox.setMaximum(1000.0)
		self.invQTYSpinBox.setSingleStep(0.0001)
		self.invQTYSpinBox.setObjectName("invQTYSpinBox")
		self.label_7 = QtWidgets.QLabel(addNewTOTypeDialog)
		self.label_7.setGeometry(QtCore.QRect(237, 95, 41, 16))
		self.label_7.setObjectName("label_7")
		self.tounitcomboBox = QtWidgets.QComboBox(addNewTOTypeDialog)
		self.tounitcomboBox.setGeometry(QtCore.QRect(269, 93, 161, 22))
		self.tounitcomboBox.setObjectName("tounitcomboBox")
		self.tounitcomboBox.addItem("")
		self.tounitcomboBox.addItem("")
		self.rmcostled = QtWidgets.QLineEdit(addNewTOTypeDialog)
		self.rmcostled.setGeometry(QtCore.QRect(62, 92, 140, 20))
		self.rmcostled.setObjectName("rmcostled")
		self.rmcostled.setValidator(QDoubleValidator())
		self.savebtn = QtWidgets.QPushButton(addNewTOTypeDialog)
		self.savebtn.setGeometry(QtCore.QRect(148, 215, 72, 41))
		self.savebtn.setObjectName("savebtn")
		self.cancelbtn = QtWidgets.QPushButton(addNewTOTypeDialog)
		self.cancelbtn.setGeometry(QtCore.QRect(256, 215, 72, 41))
		self.cancelbtn.setObjectName("cancelbtn")
		self.statulbl = QtWidgets.QLabel(addNewTOTypeDialog)
		self.statulbl.setGeometry(QtCore.QRect(6, 167, 461, 41))
		self.statulbl.setText("")
		self.statulbl.setAlignment(QtCore.Qt.AlignCenter)
		self.statulbl.setObjectName("statulbl")
		self.statulbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.label_2 = QtWidgets.QLabel(addNewTOTypeDialog)
		self.label_2.setGeometry(QtCore.QRect(205, 96, 47, 13))
		self.label_2.setObjectName("label_2")
		self.checkBox = QtWidgets.QCheckBox(addNewTOTypeDialog)
		self.checkBox.setGeometry(QtCore.QRect(280, 140, 70, 17))
		self.checkBox.setObjectName("checkBox")

		self.savebtn.clicked.connect(self.doAdd)
		self.cancelbtn.clicked.connect(self.close)

		self.retranslateUi(addNewTOTypeDialog)
		self.tounitcomboBox.setCurrentIndex(1)
		QtCore.QMetaObject.connectSlotsByName(addNewTOTypeDialog)

	def retranslateUi(self, addNewTOTypeDialog):
		_translate = QtCore.QCoreApplication.translate
		addNewTOTypeDialog.setWindowTitle(_translate("addNewTOTypeDialog", "Add New Tools Type"))
		self.label.setText(_translate("addNewTOTypeDialog", "Welcome,"))
		self.label_3.setText(_translate("addNewTOTypeDialog", "Name :"))
		self.label_8.setText(_translate("addNewTOTypeDialog", "Cost / ds :"))
		self.label_6.setText(_translate("addNewTOTypeDialog", "Initial Inventory QTY :"))
		self.label_7.setText(_translate("addNewTOTypeDialog", "Unit :"))
		self.tounitcomboBox.setItemText(1, _translate("addNewTOTypeDialog", "Each ( EA )"))
		self.savebtn.setText(_translate("addNewTOTypeDialog", "Add"))
		self.cancelbtn.setText(_translate("addNewTOTypeDialog", "Cancel"))
		self.label_2.setText(_translate("addNewTOTypeDialog", "SAR"))
		self.checkBox.setText(_translate("addNewTOTypeDialog", "Backable"))

	def doAdd(self):
		if self.toNameled.text() == '' or \
						self.tounitcomboBox.currentIndex() == 0 or \
						self.rmcostled.text() == '':
			self.statulbl.setText('All fields is required')
		else:
			self.statulbl.setText('ok')
			name = self.toNameled.text()
			if self.tounitcomboBox.currentIndex() == 1:
				unit = 'ea'
			cost = self.rmcostled.text()
			invqty = self.invQTYSpinBox.value()
			gencode = 'to {}'.format(random.randrange(10, 10000, 2))
			if self.checkBox.isChecked():
				back = 1
			else:
				back = 0
			add_tools(name, cost, invqty, unit, gencode, back)
			self.statulbl.setText(name + ", added successfully")
			self.close()


# if __name__ == '__main__':
# 	app = QtWidgets.QApplication(sys.argv)
# 	myapp = Ui_addNewTOTypeDialog()
# 	myapp.show()
# 	myapp.exec_()
