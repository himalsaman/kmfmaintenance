# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_updateNewTO.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox

from Control.materialsControl import increaseToolsInvQty, decreaseToolsInvQty, updateToolsCost
from Control.userControl import getLoginDataPKL
from models.toolsModel import select_all_tools, select_tools_by_gen_code, update_tools


class Ui_editTODialog(QDialog):
	def __init__(self):
		super(Ui_editTODialog, self).__init__()
		self.setupUi(self)

	def setupUi(self, editTODialog):
		self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

		editTODialog.setObjectName("editTODialog")
		editTODialog.resize(818, 523)
		self.label = QtWidgets.QLabel(editTODialog)
		self.label.setGeometry(QtCore.QRect(10, 10, 47, 16))
		self.label.setObjectName("label")
		self.loggeduserlbl = QtWidgets.QLabel(editTODialog)
		self.loggeduserlbl.setGeometry(QtCore.QRect(61, 11, 170, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggeduserlbl.setFont(font)
		self.loggeduserlbl.setText("")
		self.loggeduserlbl.setObjectName("loggeduserlbl")
		self.line = QtWidgets.QFrame(editTODialog)
		self.line.setGeometry(QtCore.QRect(11, 28, 800, 16))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.verticalLayoutWidget = QtWidgets.QWidget(editTODialog)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(391, 50, 81, 91))
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
		self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_8.setObjectName("label_8")
		self.verticalLayout.addWidget(self.label_8)
		self.line_2 = QtWidgets.QFrame(editTODialog)
		self.line_2.setGeometry(QtCore.QRect(372, 43, 20, 471))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.tonamelbl = QtWidgets.QLabel(editTODialog)
		self.tonamelbl.setGeometry(QtCore.QRect(430, 56, 270, 20))
		self.tonamelbl.setText("")
		self.tonamelbl.setObjectName("tonamelbl")
		self.label_7 = QtWidgets.QLabel(editTODialog)
		self.label_7.setGeometry(QtCore.QRect(722, 54, 30, 20))
		self.label_7.setObjectName("label_7")
		self.tocostlbl = QtWidgets.QLabel(editTODialog)
		self.tocostlbl.setGeometry(QtCore.QRect(425, 116, 131, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.tocostlbl.setFont(font)
		self.tocostlbl.setText("")
		self.tocostlbl.setObjectName("tocostlbl")
		self.tounitlbl = QtWidgets.QLabel(editTODialog)
		self.tounitlbl.setGeometry(QtCore.QRect(750, 54, 50, 20))
		self.tounitlbl.setText("")
		self.tounitlbl.setObjectName("tounitlbl")
		self.line_3 = QtWidgets.QFrame(editTODialog)
		self.line_3.setGeometry(QtCore.QRect(390, 142, 420, 16))
		self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.label_15 = QtWidgets.QLabel(editTODialog)
		self.label_15.setGeometry(QtCore.QRect(394, 174, 79, 26))
		self.label_15.setObjectName("label_15")
		self.label_16 = QtWidgets.QLabel(editTODialog)
		self.label_16.setGeometry(QtCore.QRect(676, 177, 30, 20))
		self.label_16.setObjectName("label_16")
		self.tonameled = QtWidgets.QLineEdit(editTODialog)
		self.tonameled.setGeometry(QtCore.QRect(430, 179, 240, 20))
		self.tonameled.setObjectName("tonameled")
		self.unitcomboBox = QtWidgets.QComboBox(editTODialog)
		self.unitcomboBox.setGeometry(QtCore.QRect(704, 177, 100, 22))
		self.unitcomboBox.setObjectName("unitcomboBox")
		self.unitcomboBox.addItem("")
		self.unitcomboBox.setItemText(0, "")
		self.unitcomboBox.addItem("")
		self.label_18 = QtWidgets.QLabel(editTODialog)
		self.label_18.setGeometry(QtCore.QRect(393, 152, 400, 20))
		self.label_18.setObjectName("label_18")
		self.line_4 = QtWidgets.QFrame(editTODialog)
		self.line_4.setGeometry(QtCore.QRect(389, 247, 420, 16))
		self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_4.setObjectName("line_4")
		self.dataupdatebtn = QtWidgets.QPushButton(editTODialog)
		self.dataupdatebtn.setGeometry(QtCore.QRect(565, 217, 75, 30))
		self.dataupdatebtn.setObjectName("dataupdatebtn")
		self.label_19 = QtWidgets.QLabel(editTODialog)
		self.label_19.setGeometry(QtCore.QRect(395, 257, 160, 20))
		self.label_19.setObjectName("label_19")
		self.label_21 = QtWidgets.QLabel(editTODialog)
		self.label_21.setGeometry(QtCore.QRect(390, 326, 400, 20))
		self.label_21.setObjectName("label_21")
		self.label_22 = QtWidgets.QLabel(editTODialog)
		self.label_22.setGeometry(QtCore.QRect(394, 284, 50, 20))
		self.label_22.setObjectName("label_22")
		self.oldcostlbl = QtWidgets.QLabel(editTODialog)
		self.oldcostlbl.setGeometry(QtCore.QRect(443, 285, 80, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.oldcostlbl.setFont(font)
		self.oldcostlbl.setText("")
		self.oldcostlbl.setObjectName("oldcostlbl")
		self.label_24 = QtWidgets.QLabel(editTODialog)
		self.label_24.setGeometry(QtCore.QRect(548, 284, 60, 20))
		self.label_24.setObjectName("label_24")
		self.newcostled = QtWidgets.QLineEdit(editTODialog)
		self.newcostled.setGeometry(QtCore.QRect(603, 286, 110, 20))
		self.newcostled.setObjectName("newcostled")
		self.updatecostbtn = QtWidgets.QPushButton(editTODialog)
		self.updatecostbtn.setGeometry(QtCore.QRect(724, 284, 75, 23))
		self.updatecostbtn.setObjectName("updatecostbtn")
		self.line_5 = QtWidgets.QFrame(editTODialog)
		self.line_5.setGeometry(QtCore.QRect(390, 315, 420, 16))
		self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_5.setObjectName("line_5")
		self.updateqtybtn = QtWidgets.QPushButton(editTODialog)
		self.updateqtybtn.setGeometry(QtCore.QRect(720, 352, 80, 23))
		self.updateqtybtn.setObjectName("updateqtybtn")
		self.oldqtylbl = QtWidgets.QLabel(editTODialog)
		self.oldqtylbl.setGeometry(QtCore.QRect(440, 352, 80, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.oldqtylbl.setFont(font)
		self.oldqtylbl.setText("")
		self.oldqtylbl.setObjectName("oldqtylbl")
		self.label_26 = QtWidgets.QLabel(editTODialog)
		self.label_26.setGeometry(QtCore.QRect(538, 352, 70, 20))
		self.label_26.setObjectName("label_26")
		self.label_27 = QtWidgets.QLabel(editTODialog)
		self.label_27.setGeometry(QtCore.QRect(391, 351, 50, 20))
		self.label_27.setObjectName("label_27")
		self.newqtySpinBox = QtWidgets.QDoubleSpinBox(editTODialog)
		self.newqtySpinBox.setGeometry(QtCore.QRect(600, 352, 110, 22))
		self.newqtySpinBox.setObjectName("newqtySpinBox")
		self.closebtn = QtWidgets.QPushButton(editTODialog)
		self.closebtn.setGeometry(QtCore.QRect(548, 470, 90, 40))
		self.closebtn.setObjectName("closebtn")
		self.listWidget = QtWidgets.QListWidget(editTODialog)
		self.listWidget.setGeometry(QtCore.QRect(10, 40, 361, 471))
		self.listWidget.setObjectName("listWidget")

		for item in select_all_tools():
			self.listWidget.addItem(item.gen_code + " - " + item.name)

		self.toinvqtylbl = QtWidgets.QLabel(editTODialog)
		self.toinvqtylbl.setGeometry(QtCore.QRect(475, 88, 79, 17))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.toinvqtylbl.setFont(font)
		self.toinvqtylbl.setText("")
		self.toinvqtylbl.setObjectName("toinvqtylbl")
		self.minupdateqtybtn = QtWidgets.QPushButton(editTODialog)
		self.minupdateqtybtn.setGeometry(QtCore.QRect(720, 390, 80, 23))
		self.minupdateqtybtn.setObjectName("minupdateqtybtn")
		self.label_28 = QtWidgets.QLabel(editTODialog)
		self.label_28.setGeometry(QtCore.QRect(541, 390, 70, 20))
		self.label_28.setObjectName("label_28")
		self.minnewqtySpinBox_2 = QtWidgets.QDoubleSpinBox(editTODialog)
		self.minnewqtySpinBox_2.setGeometry(QtCore.QRect(600, 390, 110, 22))
		self.minnewqtySpinBox_2.setObjectName("minnewqtySpinBox_2")
		self.togencodelbl = QtWidgets.QLabel(editTODialog)
		self.togencodelbl.setGeometry(QtCore.QRect(430, 54, 270, 20))
		self.togencodelbl.setVisible(False)
		self.togencodelbl.setObjectName("tonamelbl")
		self.retranslateUi(editTODialog)
		self.statulbl = QtWidgets.QLabel(editTODialog)
		self.statulbl.setGeometry(QtCore.QRect(390, 425, 410, 41))
		self.statulbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.statulbl.setAlignment(QtCore.Qt.AlignCenter)
		self.statulbl.setText("")
		self.statulbl.setAlignment(QtCore.Qt.AlignCenter)
		self.statulbl.setObjectName("statulbl")

		self.dataupdatebtn.clicked.connect(self.update_data)
		self.updatecostbtn.clicked.connect(self.update_cost)
		self.updateqtybtn.clicked.connect(self.update_inv)
		self.minupdateqtybtn.clicked.connect(self.minupdate_inv)
		self.closebtn.clicked.connect(self.close)

		self.dataupdatebtn.setEnabled(False)
		self.updatecostbtn.setEnabled(False)
		self.updateqtybtn.setEnabled(False)
		self.minupdateqtybtn.setEnabled(False)

		self.listWidget.itemClicked.connect(self.Clicked)
		QtCore.QMetaObject.connectSlotsByName(editTODialog)

	def retranslateUi(self, editTODialog):
		_translate = QtCore.QCoreApplication.translate
		editTODialog.setWindowTitle(_translate("editTODialog", "Edit Tools"))
		self.label.setText(_translate("editTODialog", "Welcome, "))
		self.label_3.setText(_translate("editTODialog", "Name :"))
		self.label_4.setText(_translate("editTODialog", "Inventory QYT :"))
		self.label_8.setText(_translate("editTODialog", "Cost :"))
		self.label_7.setText(_translate("editTODialog", "Unit :"))
		self.label_15.setText(_translate("editTODialog", "Name :"))
		self.label_16.setText(_translate("editTODialog", "Unit :"))

		self.unitcomboBox.setItemText(1, _translate("editTODialog", "Each ( EA )"))

		self.label_18.setText(_translate("editTODialog", "This Data Just you can edit it for more security"))
		self.dataupdatebtn.setText(_translate("editTODialog", "Update Data"))
		self.label_19.setText(_translate("editTODialog", "If you want update cost"))
		self.label_21.setText(_translate("editTODialog", "If you want update Inventory Quantity"))
		self.label_22.setText(_translate("editTODialog", "Old Cost:"))
		self.label_24.setText(_translate("editTODialog", "New Cost :"))
		self.updatecostbtn.setText(_translate("editTODialog", "Update Cost"))
		self.updateqtybtn.setText(_translate("editTODialog", " + Update QTY"))
		self.label_26.setText(_translate("editTODialog", "+ New QTY :"))
		self.label_27.setText(_translate("editTODialog", "Old QTY:"))
		self.closebtn.setText(_translate("editTODialog", "Close"))
		self.minupdateqtybtn.setText(_translate("editTODialog", "- Update QTY"))
		self.label_28.setText(_translate("editTODialog", "- New QTY :"))

	unitdict = {" ": 0, 'ea': 1}

	def Clicked(self, item):
		self.dataupdatebtn.setEnabled(True)
		self.updatecostbtn.setEnabled(True)
		self.updateqtybtn.setEnabled(True)
		self.minupdateqtybtn.setEnabled(True)

		role = getLoginDataPKL()['role']
		if int(role) == 2:
			self.updatecostbtn.setEnabled(False)
			self.updateqtybtn.setEnabled(False)
			self.dataupdatebtn.setEnabled(False)
		if int(role) == 3:
			self.updatecostbtn.setEnabled(False)
			self.updateqtybtn.setEnabled(True)
			self.dataupdatebtn.setEnabled(True)
		if int(role) == 1:
			self.updatecostbtn.setEnabled(True)
			self.updateqtybtn.setEnabled(False)
			self.dataupdatebtn.setEnabled(False)

		gencode = before(item.text(), '-')
		if select_tools_by_gen_code(gencode):
			tool = select_tools_by_gen_code(gencode)
			print(tool)
			self.tonamelbl.setText(tool.name)
			self.tounitlbl.setText(tool.unit)
			self.togencodelbl.setText(tool.gen_code)
			self.tocostlbl.setText(str(tool.price))
			self.toinvqtylbl.setText(str(tool.inv_qty))

			self.tonameled.setText(tool.name)
			self.unitcomboBox.setCurrentIndex(self.unitdict[tool.unit])
			## old (cost and inv_qty)
			self.oldcostlbl.setText(str(tool.price))
			self.oldqtylbl.setText(str(tool.inv_qty))
		return tool

	def update_data(self):
		id_code = self.togencodelbl.text()
		upsp = select_tools_by_gen_code(id_code)
		xname = self.tonameled.text()
		idx = self.unitcomboBox.currentIndex()
		xunit = list(self.unitdict.keys())[list(self.unitdict.values()).index(idx)]
		# # spesial case
		xcost = upsp.price
		xinv_qty = upsp.inv_qty
		xgen_code = upsp.gen_code
		#
		if xname == '':
			xname = upsp.name
		if xunit == upsp.unit:
			xunit = upsp.unit
		update_tools(upsp.id, xname, xcost, xinv_qty, xunit, xgen_code)
		self.statulbl.setText("Data updated successfully")

	def update_cost(self):
		if self.newcostled.text() == '':
			self.statulbl.setText('New Cost is Required ')
		else:
			reply = QMessageBox.question(QMessageBox(), 'Delete', "Are you sure to update cost ?\n"
																  "This action you can't undo",
										 QMessageBox.Yes | QMessageBox.No)
			id_code = self.togencodelbl.text()
			upsp = select_tools_by_gen_code(id_code)

			n_cost = self.newcostled.text()
			if n_cost == '':
				n_cost = upsp.price

			if reply == QMessageBox.Yes:
				updateToolsCost(upsp, n_cost)
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
			id_code = self.togencodelbl.text()
			upsp = select_tools_by_gen_code(id_code)

			n_inv = self.newqtySpinBox.value()

			if reply == QMessageBox.Yes:
				increaseToolsInvQty(upsp, n_inv)
				self.statulbl.setText("Data updated successfully")
			else:
				self.statulbl.setText("Data not updated ")

	def minupdate_inv(self):
		if self.minnewqtySpinBox_2.value() == 0:
			self.statulbl.setText("New Quantity is Required ")
		else:
			reply = QMessageBox.question(QMessageBox(), 'Delete', "Are you sure to update cost ?\n"
																  "This action you can't undo",
										 QMessageBox.Yes | QMessageBox.No)
			id_code = self.togencodelbl.text()
			upsp = select_tools_by_gen_code(id_code)

			n_inv = self.minnewqtySpinBox_2.value()

			if reply == QMessageBox.Yes:
				decreaseToolsInvQty(upsp, n_inv)
				self.statulbl.setText("Data updated successfully")
			else:
				self.statulbl.setText("Data not updated ")


def before(value, a):
	# Find first part and return slice before it.
	pos_a = value.find(a)
	if pos_a == -1: return ""
	return value[0:pos_a]


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myapp = Ui_editTODialog()
	myapp.show()
	myapp.exec_()
