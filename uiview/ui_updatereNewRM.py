# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_updateNewRM.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox

from Control.materialsControl import increaseRawMaterialInvQty, upRawMaterialCost, decreaseRawMaterialInvQty
from Control.userControl import getLoginDataPKL
from models.rawMaterialModel import update_raw_material


class Ui_editRWDialog(QDialog):
	def __init__(self, rawm, parent=None):
		super(Ui_editRWDialog, self).__init__()
		self.rawm = rawm
		self.setupUi(self)

	def setupUi(self, editRWDialog):
		self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

		editRWDialog.setObjectName("editRWDialog")
		editRWDialog.resize(819, 523)
		self.label = QtWidgets.QLabel(editRWDialog)
		self.label.setGeometry(QtCore.QRect(10, 10, 47, 16))
		self.label.setObjectName("label")
		self.loggeduserlbl = QtWidgets.QLabel(editRWDialog)
		self.loggeduserlbl.setGeometry(QtCore.QRect(61, 11, 170, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggeduserlbl.setFont(font)
		self.loggeduserlbl.setText("")
		self.loggeduserlbl.setObjectName("loggeduserlbl")
		self.loggeduserlbl.setText(getLoginDataPKL()['name'])
		self.line = QtWidgets.QFrame(editRWDialog)
		self.line.setGeometry(QtCore.QRect(11, 28, 800, 16))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.verticalLayoutWidget = QtWidgets.QWidget(editRWDialog)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(391, 50, 81, 91))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_3.setObjectName("label_3")
		self.verticalLayout.addWidget(self.label_3)
		self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_5.setObjectName("label_5")
		self.verticalLayout.addWidget(self.label_5)
		self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_8.setObjectName("label_8")
		self.verticalLayout.addWidget(self.label_8)
		self.line_2 = QtWidgets.QFrame(editRWDialog)
		self.line_2.setGeometry(QtCore.QRect(372, 43, 20, 471))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.rwnamelbl = QtWidgets.QLabel(editRWDialog)
		self.rwnamelbl.setGeometry(QtCore.QRect(430, 54, 270, 20))
		self.rwnamelbl.setText("")
		self.rwnamelbl.setObjectName("rwnamelbl")
		self.rwcodelbl = QtWidgets.QLabel(editRWDialog)
		self.rwcodelbl.setGeometry(QtCore.QRect(430, 54, 270, 20))
		self.rwcodelbl.setVisible(False)
		self.rwcodelbl.setText("")
		self.rwcodelbl.setObjectName("rwcodelbl")
		self.rwdefaultsize = QtWidgets.QLabel(editRWDialog)
		self.rwdefaultsize.setGeometry(QtCore.QRect(460, 85, 130, 20))
		self.rwdefaultsize.setText("")
		self.rwdefaultsize.setObjectName("rwdefaultsize")
		self.label_6 = QtWidgets.QLabel(editRWDialog)
		self.label_6.setGeometry(QtCore.QRect(608, 85, 79, 21))
		self.label_6.setObjectName("label_6")
		self.label_7 = QtWidgets.QLabel(editRWDialog)
		self.label_7.setGeometry(QtCore.QRect(722, 54, 30, 20))
		self.label_7.setObjectName("label_7")
		self.rwstrsize = QtWidgets.QLabel(editRWDialog)
		self.rwstrsize.setGeometry(QtCore.QRect(667, 86, 170, 20))
		self.rwstrsize.setText("")
		self.rwstrsize.setObjectName("rwstrsize")
		self.rwcostlbl = QtWidgets.QLabel(editRWDialog)
		self.rwcostlbl.setGeometry(QtCore.QRect(425, 116, 131, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.rwcostlbl.setFont(font)
		self.rwcostlbl.setText("")
		self.rwcostlbl.setObjectName("rwcostlbl")
		self.rwunitlbl = QtWidgets.QLabel(editRWDialog)
		self.rwunitlbl.setGeometry(QtCore.QRect(750, 54, 50, 20))
		self.rwunitlbl.setText("")
		self.rwunitlbl.setObjectName("rwunitlbl")
		self.label_4 = QtWidgets.QLabel(editRWDialog)
		self.label_4.setGeometry(QtCore.QRect(530, 113, 79, 25))
		self.label_4.setObjectName("label_4")
		self.rwinvqtylbl = QtWidgets.QLabel(editRWDialog)
		self.rwinvqtylbl.setGeometry(QtCore.QRect(610, 115, 81, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.rwinvqtylbl.setFont(font)
		self.rwinvqtylbl.setText("")
		self.rwinvqtylbl.setObjectName("rwinvqtylbl")
		self.line_3 = QtWidgets.QFrame(editRWDialog)
		self.line_3.setGeometry(QtCore.QRect(390, 142, 420, 16))
		self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.label_15 = QtWidgets.QLabel(editRWDialog)
		self.label_15.setGeometry(QtCore.QRect(394, 174, 79, 26))
		self.label_15.setObjectName("label_15")
		self.label_16 = QtWidgets.QLabel(editRWDialog)
		self.label_16.setGeometry(QtCore.QRect(676, 177, 30, 20))
		self.label_16.setObjectName("label_16")
		self.label_17 = QtWidgets.QLabel(editRWDialog)
		self.label_17.setGeometry(QtCore.QRect(585, 209, 79, 21))
		self.label_17.setObjectName("label_17")
		self.label_20 = QtWidgets.QLabel(editRWDialog)
		self.label_20.setGeometry(QtCore.QRect(394, 206, 79, 25))
		self.label_20.setObjectName("label_20")
		self.rwnameled = QtWidgets.QLineEdit(editRWDialog)
		self.rwnameled.setGeometry(QtCore.QRect(430, 179, 240, 20))
		self.rwnameled.setObjectName("rwnameled")
		self.unitcomboBox = QtWidgets.QComboBox(editRWDialog)
		self.unitcomboBox.setGeometry(QtCore.QRect(704, 177, 100, 22))
		self.unitcomboBox.setObjectName("unitcomboBox")
		self.unitcomboBox.addItem("")
		self.unitcomboBox.setItemText(0, "")
		self.unitcomboBox.addItem("")
		self.unitcomboBox.addItem("")
		self.unitcomboBox.addItem("")
		self.unitcomboBox.addItem("")
		self.unitcomboBox.addItem("")
		self.unitcomboBox.addItem("")
		self.unitcomboBox.addItem("")
		self.strsizeled = QtWidgets.QLineEdit(editRWDialog)
		self.strsizeled.setGeometry(QtCore.QRect(642, 209, 170, 20))
		self.strsizeled.setObjectName("strsizeled")
		self.defaultsizSpinBox = QtWidgets.QDoubleSpinBox(editRWDialog)
		self.defaultsizSpinBox.setGeometry(QtCore.QRect(461, 208, 120, 22))
		self.defaultsizSpinBox.setObjectName("defaultsizSpinBox")
		self.defaultsizSpinBox.setMaximum(100000000.0)
		self.label_18 = QtWidgets.QLabel(editRWDialog)
		self.label_18.setGeometry(QtCore.QRect(393, 152, 400, 20))
		self.label_18.setObjectName("label_18")
		self.line_4 = QtWidgets.QFrame(editRWDialog)
		self.line_4.setGeometry(QtCore.QRect(389, 272, 420, 16))
		self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_4.setObjectName("line_4")
		self.dataupdatebtn = QtWidgets.QPushButton(editRWDialog)
		self.dataupdatebtn.setGeometry(QtCore.QRect(565, 242, 75, 30))
		self.dataupdatebtn.setObjectName("dataupdatebtn")
		self.dataupdatebtn.clicked.connect(self.update_data)  ###################
		self.label_19 = QtWidgets.QLabel(editRWDialog)
		self.label_19.setGeometry(QtCore.QRect(395, 282, 160, 20))
		self.label_19.setObjectName("label_19")
		self.label_21 = QtWidgets.QLabel(editRWDialog)
		self.label_21.setGeometry(QtCore.QRect(390, 351, 400, 20))
		self.label_21.setObjectName("label_21")
		self.label_22 = QtWidgets.QLabel(editRWDialog)
		self.label_22.setGeometry(QtCore.QRect(394, 309, 50, 20))
		self.label_22.setObjectName("label_22")
		self.oldcostlbl = QtWidgets.QLabel(editRWDialog)
		self.oldcostlbl.setGeometry(QtCore.QRect(443, 310, 80, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.oldcostlbl.setFont(font)
		self.oldcostlbl.setText("")
		self.oldcostlbl.setObjectName("oldcostlbl")
		self.label_24 = QtWidgets.QLabel(editRWDialog)
		self.label_24.setGeometry(QtCore.QRect(548, 309, 60, 20))
		self.label_24.setObjectName("label_24")
		self.newcostled = QtWidgets.QLineEdit(editRWDialog)
		self.newcostled.setGeometry(QtCore.QRect(603, 311, 110, 20))
		self.newcostled.setObjectName("newcostled")
		self.newcostled.setValidator(QDoubleValidator())
		self.updatecostbtn = QtWidgets.QPushButton(editRWDialog)
		self.updatecostbtn.setGeometry(QtCore.QRect(724, 309, 75, 23))
		self.updatecostbtn.setObjectName("updatecostbtn")
		self.updatecostbtn.clicked.connect(self.update_cost)  ########################
		self.line_5 = QtWidgets.QFrame(editRWDialog)
		self.line_5.setGeometry(QtCore.QRect(390, 340, 420, 16))
		self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_5.setObjectName("line_5")
		self.updateqtybtn = QtWidgets.QPushButton(editRWDialog)
		self.updateqtybtn.setGeometry(QtCore.QRect(725, 377, 75, 23))
		self.updateqtybtn.setObjectName("updateqtybtn")
		self.updateqtybtn.clicked.connect(self.update_inv)  ###########################
		self.oldqtylbl = QtWidgets.QLabel(editRWDialog)
		self.oldqtylbl.setGeometry(QtCore.QRect(440, 377, 80, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.oldqtylbl.setFont(font)
		self.oldqtylbl.setText("")
		self.oldqtylbl.setObjectName("oldqtylbl")
		self.label_26 = QtWidgets.QLabel(editRWDialog)
		self.label_26.setGeometry(QtCore.QRect(545, 376, 60, 20))
		self.label_26.setObjectName("label_26")
		self.label_27 = QtWidgets.QLabel(editRWDialog)
		self.label_27.setGeometry(QtCore.QRect(391, 376, 50, 20))
		self.label_27.setObjectName("label_27")
		self.newqtySpinBox = QtWidgets.QDoubleSpinBox(editRWDialog)
		self.newqtySpinBox.setGeometry(QtCore.QRect(600, 377, 110, 22))
		self.newqtySpinBox.setObjectName("newqtySpinBox")
		self.newqtySpinBox.setMaximum(100000000.0)
		self.closebtn = QtWidgets.QPushButton(editRWDialog)
		self.closebtn.setGeometry(QtCore.QRect(548, 460, 90, 40))
		self.closebtn.setObjectName("closebtn")
		self.closebtn.clicked.connect(self.close)
		self.rawmateriallist = QtWidgets.QListWidget(editRWDialog)
		self.rawmateriallist.setGeometry(QtCore.QRect(10, 40, 361, 471))
		self.rawmateriallist.setObjectName("rawmateriallist")
		self.rawmateriallist.addItem(self.rawm.code + " - " + self.rawm.name)
		self.rawmateriallist.itemClicked.connect(self.Clicked)
		self.statulbl = QtWidgets.QLabel(editRWDialog)
		self.statulbl.setGeometry(QtCore.QRect(390, 425, 410, 41))
		self.statulbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.statulbl.setAlignment(QtCore.Qt.AlignCenter)
		self.statulbl.setText("")
		self.statulbl.setAlignment(QtCore.Qt.AlignCenter)
		self.statulbl.setObjectName("statulbl")
		self.updateqtybtn_2 = QtWidgets.QPushButton(editRWDialog)
		self.updateqtybtn_2.setGeometry(QtCore.QRect(725, 412, 75, 23))
		self.updateqtybtn_2.setObjectName("updateqtybtn_2")
		self.label_28 = QtWidgets.QLabel(editRWDialog)
		self.label_28.setGeometry(QtCore.QRect(541, 411, 70, 20))
		self.label_28.setObjectName("label_28")
		self.newqtySpinBox_2 = QtWidgets.QDoubleSpinBox(editRWDialog)
		self.newqtySpinBox_2.setGeometry(QtCore.QRect(600, 412, 110, 22))
		self.newqtySpinBox_2.setObjectName("newqtySpinBox_2")

		self.updateqtybtn_2.clicked.connect(self.minupdate_inv)

		self.dataupdatebtn.setEnabled(False)
		self.updatecostbtn.setEnabled(False)
		self.updateqtybtn.setEnabled(False)
		self.updateqtybtn_2.setEnabled(False)

		self.retranslateUi(editRWDialog)
		QtCore.QMetaObject.connectSlotsByName(editRWDialog)

	def retranslateUi(self, editRWDialog):
		_translate = QtCore.QCoreApplication.translate
		editRWDialog.setWindowTitle(_translate("editRWDialog", "Edit Raw Material"))
		self.label.setText(_translate("editRWDialog", "Welcome, "))
		self.label_3.setText(_translate("editRWDialog", "Name :"))
		self.label_5.setText(_translate("editRWDialog", "Default Size :"))
		self.label_8.setText(_translate("editRWDialog", "Cost :"))
		self.label_6.setText(_translate("editRWDialog", "String Size :"))
		self.label_7.setText(_translate("editRWDialog", "Unit :"))
		self.label_4.setText(_translate("editRWDialog", "Inventory QYT :"))
		self.label_15.setText(_translate("editRWDialog", "Name :"))
		self.label_16.setText(_translate("editRWDialog", "Unit :"))
		self.label_17.setText(_translate("editRWDialog", "String Size :"))
		self.label_20.setText(_translate("editRWDialog", "Default Size :"))
		self.unitcomboBox.setItemText(1, _translate("editRWDialog", "Millimetre ( MM )"))
		self.unitcomboBox.setItemText(2, _translate("editRWDialog", "Centimeter ( CM )"))
		self.unitcomboBox.setItemText(3, _translate("editRWDialog", "Metre ( M )"))
		self.unitcomboBox.setItemText(4, _translate("editRWDialog", "Gram ( G )"))
		self.unitcomboBox.setItemText(5, _translate("editRWDialog", "Kilogram ( KG )"))
		self.unitcomboBox.setItemText(6, _translate("editRWDialog", "Each ( EA )"))
		self.unitcomboBox.setItemText(7, _translate("editRWDialog", "Litre ( L )"))
		self.label_18.setText(_translate("editRWDialog", "This Data Just you can edit it for more security"))
		self.dataupdatebtn.setText(_translate("editRWDialog", "Update Data"))
		self.label_19.setText(_translate("editRWDialog", "If you want update cost"))
		self.label_21.setText(_translate("editRWDialog", "If you want update Inventory Quantity"))
		self.label_22.setText(_translate("editRWDialog", "Old Cost:"))
		self.label_24.setText(_translate("editRWDialog", "New Cost :"))
		self.updatecostbtn.setText(_translate("editRWDialog", "Update Cost"))
		self.updateqtybtn.setText(_translate("editRWDialog", "+ Update QTY"))
		self.updateqtybtn_2.setText(_translate("editRWDialog", "- Update QTY"))
		self.label_26.setText(_translate("editRWDialog", "+ New QTY :"))
		self.label_27.setText(_translate("editRWDialog", "Old QTY:"))
		self.closebtn.setText(_translate("editRWDialog", "Close"))
		self.label_28.setText(_translate("editFPDialog", "- New QTY :"))

	unitdict = {'': 0, 'mm': 1, 'cm': 2, 'm': 3, 'g': 4, 'kg': 5, 'ea': 6, 'l': 7}

	def Clicked(self, item):
		self.dataupdatebtn.setEnabled(True)
		self.updatecostbtn.setEnabled(True)
		self.updateqtybtn.setEnabled(True)
		self.updateqtybtn_2.setEnabled(True)
		role = getLoginDataPKL()['role']
		if int(role) == 2:
			self.updatecostbtn.setEnabled(False)
			self.updateqtybtn.setEnabled(False)
			self.updateqtybtn_2.setEnabled(False)
			self.dataupdatebtn.setEnabled(False)
		if int(role) == 3:
			self.dataupdatebtn.setEnabled(True)
			self.updatecostbtn.setEnabled(False)
			self.updateqtybtn_2.setEnabled(True)
			self.updateqtybtn.setEnabled(True)
		if int(role) == 1:
			self.updatecostbtn.setEnabled(True)
			self.updateqtybtn.setEnabled(False)
			self.updateqtybtn_2.setEnabled(False)
			self.dataupdatebtn.setEnabled(False)

		code = before(item.text(), '-')
		rawMat = self.rawm
		self.rwcodelbl.setText(rawMat.code)
		self.rwnamelbl.setText(rawMat.name)
		self.rwunitlbl.setText(rawMat.unit)
		self.rwdefaultsize.setText(str(rawMat.default_size))
		self.rwstrsize.setText(rawMat.string_size)
		self.rwcostlbl.setText(str(rawMat.cost_per_default_size))
		self.rwinvqtylbl.setText(str(rawMat.inv_qty))
		self.rwnameled.setText(rawMat.name)
		self.unitcomboBox.setCurrentIndex(self.unitdict[rawMat.unit])
		self.defaultsizSpinBox.setValue(rawMat.default_size)
		self.strsizeled.setText(rawMat.string_size)
		## old (cost and inv_qty)
		self.oldcostlbl.setText(str(rawMat.cost_per_default_size))
		self.oldqtylbl.setText(str(rawMat.inv_qty))
		return rawMat

	def update_data(self):
		uprm = self.rawm
		xname = self.rwnameled.text()
		idx = self.unitcomboBox.currentIndex()
		xunit = list(self.unitdict.keys())[list(self.unitdict.values()).index(idx)]
		xdefault_size = self.defaultsizSpinBox.value()
		xstr_size = self.strsizeled.text()
		# # spesial case
		xcode = uprm.code
		xcost = uprm.cost_per_default_size
		xinv_qty = uprm.inv_qty
		#
		if xname == '':
			xname = uprm.name
		if xunit == uprm.unit:
			xunit = uprm.unit
		if xdefault_size == uprm.default_size:
			xdefault_size = uprm.default_size
		if xstr_size == '':
			xstr_size = uprm.string_size
		update_raw_material(uprm.id, xcode, xname, xdefault_size, xstr_size, xunit, xcost, xinv_qty)
		self.statulbl.setText("Data updated successfully")

	def update_cost(self):
		if self.newcostled.text() == '':
			self.statulbl.setText('The New Cost is Required')
		else:
			reply = QMessageBox.question(QMessageBox(), 'Delete', "Are you sure to update cost ?\n"
																  "This action you can't undo",
										 QMessageBox.Yes | QMessageBox.No)
			uprm = self.rawm

			n_cost = self.newcostled.text()
			if n_cost == '':
				n_cost = uprm.cost_per_default_size
			if reply == QMessageBox.Yes:
				upRawMaterialCost(uprm, n_cost)
				self.statulbl.setText("Data updated successfully")
			else:
				self.statulbl.setText("Data not updated ")

	def update_inv(self):
		if self.newqtySpinBox.value() == 0:
			self.statulbl.setText('New Quantity is required ')
		else:
			reply = QMessageBox.question(QMessageBox(), 'Delete', "Are you sure to update "
																  "inventory quantity ?\n"
																  "This action you can't undo",
										 QMessageBox.Yes | QMessageBox.No)

			uprm = self.rawm

			n_inv = self.newqtySpinBox.value()
			if reply == QMessageBox.Yes:
				increaseRawMaterialInvQty(uprm, n_inv)
				self.statulbl.setText("Data updated successfully")
			else:
				self.statulbl.setText("Data not updated ")

	def minupdate_inv(self):
		if self.newqtySpinBox_2.value() == 0:
			self.statulbl.setText('New Quantity is required ')
		else:
			reply = QMessageBox.question(QMessageBox(), 'Delete', "Are you sure to update "
																  "inventory quantity ?\n"
																  "This action you can't undo",
										 QMessageBox.Yes | QMessageBox.No)

			uprm = self.rawm

			n_inv = self.newqtySpinBox_2.value()
			if reply == QMessageBox.Yes:
				decreaseRawMaterialInvQty(uprm, n_inv)
				self.statulbl.setText("Data updated successfully")
			else:
				self.statulbl.setText("Data not updated ")


def before(value, a):
	# Find first part and return slice before it.
	pos_a = value.find(a)
	if pos_a == -1: return ""
	return value[0:pos_a]


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	myapp = Ui_editRWDialog()
	myapp.show()
	app.exec_()
