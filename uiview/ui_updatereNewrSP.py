# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_updateNewSP.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox

from Control.materialsControl import increaseSparePartsInvQty, upSparePartsCost, decreaseSparePartsInvQty
from Control.userControl import getLoginDataPKL
from models.sparePartsModel import select_spare_parts_bygen_code, select_all_spare_parts, update_spare_parts


class Ui_editSPDialog(QDialog):
	def __init__(self,sparep,parent=None):
		super(Ui_editSPDialog, self).__init__()
		self.sparep = sparep
		self.setupUi(self)

	def setupUi(self, editSPDialog):
		editSPDialog.setObjectName("editSPDialog")
		editSPDialog.resize(818, 523)
		self.label = QtWidgets.QLabel(editSPDialog)
		self.label.setGeometry(QtCore.QRect(10, 10, 47, 16))
		self.label.setObjectName("label")
		self.loggeduserlbl = QtWidgets.QLabel(editSPDialog)
		self.loggeduserlbl.setGeometry(QtCore.QRect(61, 11, 170, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggeduserlbl.setFont(font)
		self.loggeduserlbl.setText("")
		self.loggeduserlbl.setObjectName("loggeduserlbl")
		self.loggeduserlbl.setText(getLoginDataPKL()['name'])
		self.line = QtWidgets.QFrame(editSPDialog)
		self.line.setGeometry(QtCore.QRect(11, 28, 800, 16))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.verticalLayoutWidget = QtWidgets.QWidget(editSPDialog)
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
		self.line_2 = QtWidgets.QFrame(editSPDialog)
		self.line_2.setGeometry(QtCore.QRect(372, 43, 20, 471))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.spnamelbl = QtWidgets.QLabel(editSPDialog)
		self.spnamelbl.setGeometry(QtCore.QRect(430, 54, 270, 20))
		self.spnamelbl.setText("")
		self.spnamelbl.setObjectName("spnamelbl")
		self.spgencodelbl = QtWidgets.QLabel(editSPDialog)
		self.spgencodelbl.setGeometry(QtCore.QRect(430, 54, 270, 20))
		self.spgencodelbl.setVisible(False)
		self.spgencodelbl.setObjectName("spnamelbl")
		self.spcodelbl = QtWidgets.QLabel(editSPDialog)
		self.spcodelbl.setGeometry(QtCore.QRect(435, 85, 130, 20))
		self.spcodelbl.setText("")
		self.spcodelbl.setObjectName("spcodelbl")
		self.label_7 = QtWidgets.QLabel(editSPDialog)
		self.label_7.setGeometry(QtCore.QRect(722, 54, 30, 20))
		self.label_7.setObjectName("label_7")
		self.spcostlbl = QtWidgets.QLabel(editSPDialog)
		self.spcostlbl.setGeometry(QtCore.QRect(425, 116, 131, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.spcostlbl.setFont(font)
		self.spcostlbl.setText("")
		self.spcostlbl.setObjectName("spcostlbl")
		self.spunitlbl = QtWidgets.QLabel(editSPDialog)
		self.spunitlbl.setGeometry(QtCore.QRect(750, 54, 50, 20))
		self.spunitlbl.setText("")
		self.spunitlbl.setObjectName("spunitlbl")
		self.label_4 = QtWidgets.QLabel(editSPDialog)
		self.label_4.setGeometry(QtCore.QRect(530, 114, 79, 25))
		self.label_4.setObjectName("label_4")
		self.spinvqtylbl = QtWidgets.QLabel(editSPDialog)
		self.spinvqtylbl.setGeometry(QtCore.QRect(610, 116, 81, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.spinvqtylbl.setFont(font)
		self.spinvqtylbl.setText("")
		self.spinvqtylbl.setObjectName("spinvqtylbl")
		self.line_3 = QtWidgets.QFrame(editSPDialog)
		self.line_3.setGeometry(QtCore.QRect(390, 142, 420, 16))
		self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.label_15 = QtWidgets.QLabel(editSPDialog)
		self.label_15.setGeometry(QtCore.QRect(394, 174, 79, 26))
		self.label_15.setObjectName("label_15")
		self.label_16 = QtWidgets.QLabel(editSPDialog)
		self.label_16.setGeometry(QtCore.QRect(676, 177, 30, 20))
		self.label_16.setObjectName("label_16")
		self.label_20 = QtWidgets.QLabel(editSPDialog)
		self.label_20.setGeometry(QtCore.QRect(394, 206, 50, 25))
		self.label_20.setObjectName("label_20")
		self.spnameled = QtWidgets.QLineEdit(editSPDialog)
		self.spnameled.setGeometry(QtCore.QRect(430, 179, 240, 20))
		self.spnameled.setObjectName("spnameled")
		self.unitcomboBox = QtWidgets.QComboBox(editSPDialog)
		self.unitcomboBox.setGeometry(QtCore.QRect(704, 177, 100, 22))
		self.unitcomboBox.setObjectName("unitcomboBox")
		self.unitcomboBox.addItem("")
		self.unitcomboBox.addItem("")
		self.label_18 = QtWidgets.QLabel(editSPDialog)
		self.label_18.setGeometry(QtCore.QRect(393, 152, 400, 20))
		self.label_18.setObjectName("label_18")
		self.line_4 = QtWidgets.QFrame(editSPDialog)
		self.line_4.setGeometry(QtCore.QRect(389, 272, 420, 16))
		self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_4.setObjectName("line_4")
		self.dataupdatebtn = QtWidgets.QPushButton(editSPDialog)
		self.dataupdatebtn.setGeometry(QtCore.QRect(565, 242, 75, 30))
		self.dataupdatebtn.setObjectName("dataupdatebtn")
		self.dataupdatebtn.clicked.connect(self.update_data)
		self.label_19 = QtWidgets.QLabel(editSPDialog)
		self.label_19.setGeometry(QtCore.QRect(395, 282, 160, 20))
		self.label_19.setObjectName("label_19")
		self.label_21 = QtWidgets.QLabel(editSPDialog)
		self.label_21.setGeometry(QtCore.QRect(390, 351, 400, 20))
		self.label_21.setObjectName("label_21")
		self.label_22 = QtWidgets.QLabel(editSPDialog)
		self.label_22.setGeometry(QtCore.QRect(394, 309, 50, 20))
		self.label_22.setObjectName("label_22")
		self.oldcostlbl = QtWidgets.QLabel(editSPDialog)
		self.oldcostlbl.setGeometry(QtCore.QRect(443, 310, 80, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.oldcostlbl.setFont(font)
		self.oldcostlbl.setText("")
		self.oldcostlbl.setObjectName("oldcostlbl")
		self.label_24 = QtWidgets.QLabel(editSPDialog)
		self.label_24.setGeometry(QtCore.QRect(548, 309, 60, 20))
		self.label_24.setObjectName("label_24")
		self.newcostled = QtWidgets.QLineEdit(editSPDialog)
		self.newcostled.setGeometry(QtCore.QRect(603, 311, 110, 20))
		self.newcostled.setObjectName("newcostled")
		self.newcostled.setValidator(QDoubleValidator())
		self.updatecostbtn = QtWidgets.QPushButton(editSPDialog)
		self.updatecostbtn.setGeometry(QtCore.QRect(724, 309, 75, 23))
		self.updatecostbtn.setObjectName("updatecostbtn")
		self.updatecostbtn.clicked.connect(self.update_cost)
		self.line_5 = QtWidgets.QFrame(editSPDialog)
		self.line_5.setGeometry(QtCore.QRect(390, 340, 420, 16))
		self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_5.setObjectName("line_5")
		self.updateqtybtn = QtWidgets.QPushButton(editSPDialog)
		self.updateqtybtn.setGeometry(QtCore.QRect(725, 377, 75, 23))
		self.updateqtybtn.setObjectName("updateqtybtn")
		self.updateqtybtn.clicked.connect(self.update_inv)
		self.oldqtylbl = QtWidgets.QLabel(editSPDialog)
		self.oldqtylbl.setGeometry(QtCore.QRect(440, 377, 80, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.oldqtylbl.setFont(font)
		self.oldqtylbl.setText("")
		self.oldqtylbl.setObjectName("oldqtylbl")
		self.label_26 = QtWidgets.QLabel(editSPDialog)
		self.label_26.setGeometry(QtCore.QRect(545, 376, 60, 20))
		self.label_26.setObjectName("label_26")
		self.label_27 = QtWidgets.QLabel(editSPDialog)
		self.label_27.setGeometry(QtCore.QRect(391, 376, 50, 20))
		self.label_27.setObjectName("label_27")
		self.newqtySpinBox = QtWidgets.QDoubleSpinBox(editSPDialog)
		self.newqtySpinBox.setGeometry(QtCore.QRect(600, 377, 110, 22))
		self.newqtySpinBox.setObjectName("newqtySpinBox")
		self.closebtn = QtWidgets.QPushButton(editSPDialog)
		self.closebtn.setGeometry(QtCore.QRect(548, 450, 90, 40))
		self.closebtn.setObjectName("closebtn")
		self.closebtn.clicked.connect(self.close)
		# self.dataupdatebtn.setEnabled(False)
		# self.updatecostbtn.setEnabled(False)
		# self.updateqtybtn.setEnabled(False)
		self.listWidget = QtWidgets.QListWidget(editSPDialog)
		self.listWidget.setGeometry(QtCore.QRect(10, 40, 361, 471))
		self.listWidget.setObjectName("listWidget")
		self.selitem = self.listWidget.addItem(self.sparep.gen_code + " - " + self.sparep.name + "(" + self.sparep.code + ")")
		self.listWidget.itemClicked.connect(self.Clicked)
		self.spcodeled = QtWidgets.QLineEdit(editSPDialog)
		self.spcodeled.setGeometry(QtCore.QRect(430, 210, 151, 20))
		self.spcodeled.setObjectName("spcodeled")
		self.statulbl = QtWidgets.QLabel(editSPDialog)
		self.statulbl.setGeometry(QtCore.QRect(390, 425, 410, 41))
		self.statulbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.statulbl.setAlignment(QtCore.Qt.AlignCenter)
		self.statulbl.setText("")
		self.statulbl.setAlignment(QtCore.Qt.AlignCenter)
		self.statulbl.setObjectName("statulbl")
		self.updateqtybtn_2 = QtWidgets.QPushButton(editSPDialog)
		self.updateqtybtn_2.setGeometry(QtCore.QRect(725, 412, 75, 23))
		self.updateqtybtn_2.setObjectName("updateqtybtn_2")
		self.label_28 = QtWidgets.QLabel(editSPDialog)
		self.label_28.setGeometry(QtCore.QRect(541, 411, 70, 20))
		self.label_28.setObjectName("label_28")
		self.newqtySpinBox_2 = QtWidgets.QDoubleSpinBox(editSPDialog)
		self.newqtySpinBox_2.setGeometry(QtCore.QRect(600, 412, 110, 22))
		self.newqtySpinBox_2.setObjectName("newqtySpinBox_2")
		self.updateqtybtn_2.clicked.connect(self.minupdate_inv)
		self.retranslateUi(editSPDialog)
		QtCore.QMetaObject.connectSlotsByName(editSPDialog)

	def retranslateUi(self, editSPDialog):
		_translate = QtCore.QCoreApplication.translate
		editSPDialog.setWindowTitle(_translate("editSPDialog", "Edit Spare Parts"))
		self.label.setText(_translate("editSPDialog", "Welcome, "))
		self.label_3.setText(_translate("editSPDialog", "Name :"))
		self.label_5.setText(_translate("editSPDialog", "Code :"))
		self.label_8.setText(_translate("editSPDialog", "Cost :"))
		self.label_7.setText(_translate("editSPDialog", "Unit :"))
		self.label_4.setText(_translate("editSPDialog", "Inventory QYT :"))
		self.label_15.setText(_translate("editSPDialog", "Name :"))
		self.label_16.setText(_translate("editSPDialog", "Unit :"))
		self.label_20.setText(_translate("editSPDialog", "Code :"))
		self.unitcomboBox.setItemText(0, _translate("editSPDialog", ""))
		self.unitcomboBox.setItemText(1, _translate("editSPDialog", "Each ( EA )"))
		self.label_18.setText(_translate("editSPDialog", "This Data Just you can edit it for more security"))
		self.dataupdatebtn.setText(_translate("editSPDialog", "Update Data"))
		self.label_19.setText(_translate("editSPDialog", "If you want update cost"))
		self.label_21.setText(_translate("editSPDialog", "If you want update Inventory Quantity"))
		self.label_22.setText(_translate("editSPDialog", "Old Cost:"))
		self.label_24.setText(_translate("editSPDialog", "New Cost :"))
		self.updatecostbtn.setText(_translate("editSPDialog", "Update Cost"))
		self.updateqtybtn.setText(_translate("editSPDialog", "+ Update QTY"))
		self.updateqtybtn_2.setText(_translate("editSPDialog", "- Update QTY"))
		self.label_26.setText(_translate("editSPDialog", "+ New QTY :"))
		self.label_28.setText(_translate("editSPDialog", "- New QTY :"))
		self.label_27.setText(_translate("editSPDialog", "Old QTY:"))
		self.closebtn.setText(_translate("editSPDialog", "Close"))

	unitdict = {" ": 0, 'ea': 1}

	def Clicked(self, item):
		role = getLoginDataPKL()['role']
		if int(role) == 2 :
			self.updatecostbtn.setEnabled(False)
			self.updateqtybtn.setEnabled(False)
			self.dataupdatebtn.setEnabled(False)
		if int(role) == 3:
			self.updatecostbtn.setEnabled(False)
			self.updateqtybtn.setEnabled(True)
			self.dataupdatebtn.setEnabled(True)
		if int(role) == 1 :
			self.updatecostbtn.setEnabled(True)
			self.updateqtybtn.setEnabled(False)
			self.dataupdatebtn.setEnabled(False)

		gencode = before(item.text(), '-')
		# if select_spare_parts_bygen_code(gencode):
		spart = self.sparep
		print(spart)
		self.spnamelbl.setText(spart.name)
		self.spunitlbl.setText(spart.unit)
		self.spcodelbl.setText(spart.code)
		self.spgencodelbl.setText(spart.gen_code)
		self.spcostlbl.setText(str(spart.price))
		self.spinvqtylbl.setText(str(spart.inv_qty))

		self.spnameled.setText(spart.name)
		self.unitcomboBox.setCurrentIndex(self.unitdict[spart.unit])
		self.spcodeled.setText(spart.code)
		## old (cost and inv_qty)
		self.oldcostlbl.setText(str(spart.price))
		self.oldqtylbl.setText(str(spart.inv_qty))
		return spart

	def update_data(self):
		# id_code = self.spgencodelbl.text()
		upsp = self.sparep
		xname = self.spnameled.text()
		idx = self.unitcomboBox.currentIndex()
		xunit = list(self.unitdict.keys())[list(self.unitdict.values()).index(idx)]
		# # spesial case
		xcode = self.spcodeled.text()
		xcost = upsp.price
		xinv_qty = upsp.inv_qty
		xgen_code = upsp.gen_code
		#
		if xname == '':
			xname = upsp.name
		if xunit == upsp.unit:
			xunit = upsp.unit
		if xcode == '':
			xcode = upsp.code
		update_spare_parts(upsp.id, xname, xcode, xgen_code, xcost, xinv_qty, xunit)
		self.statulbl.setText("Data updated successfully")

	def update_cost(self):
		if self.newcostled.text() == '':
			self.statulbl.setText('New Cost is Required ')
		else:
			reply = QMessageBox.question(QMessageBox(), 'Delete', "Are you sure to update cost ?\n"
																  "This action you can't undo",
										 QMessageBox.Yes | QMessageBox.No)
			id_code = self.spgencodelbl.text()
			upsp = self.sparep

			n_cost = self.newcostled.text()
			if n_cost == '':
				n_cost = upsp.price

			if reply == QMessageBox.Yes:
				upSparePartsCost(upsp, n_cost)
				self.statulbl.setText("Data updated successfully")
			else:
				self.statulbl.setText("Data not updated ")

	def update_inv(self):
		if self.newqtySpinBox.value() == 0:
			self.statulbl.setText("New Quantity is Required ")
		else:
			reply = QMessageBox.question(QMessageBox(), 'Delete', "Are you sure to update cost ?\n"
																  "This action you can't undo",
										 QMessageBox.Yes | QMessageBox.No)
			id_code = self.spgencodelbl.text()
			upsp = self.sparep

			n_inv = self.newqtySpinBox.value()

			if reply == QMessageBox.Yes:
				increaseSparePartsInvQty(upsp, n_inv)
				self.statulbl.setText("Data updated successfully")
			else:
				self.statulbl.setText("Data not updated ")
	def minupdate_inv(self):
		if self.newqtySpinBox_2.value() == 0:
			self.statulbl.setText("New Quantity is Required ")
		else:
			reply = QMessageBox.question(QMessageBox(), 'Delete', "Are you sure to update cost ?\n"
																  "This action you can't undo",
										 QMessageBox.Yes | QMessageBox.No)
			id_code = self.spgencodelbl.text()
			upsp = self.sparep

			n_inv = self.newqtySpinBox_2.value()

			if reply == QMessageBox.Yes:
				decreaseSparePartsInvQty(upsp, n_inv)
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
	myapp = Ui_editSPDialog()
	myapp.show()
	app.exec_()
