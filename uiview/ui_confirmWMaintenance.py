# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_confirmWMaintenance.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from reportlab.lib.styles import LineStyle

from Control.maintenanceLogic import getMaintenanceHolded
from Control.materialsControl import decreaseRawMaterialInvQty, decreaseSparePartsInvQty
from Control.userControl import getLoginDataPKL
from models.billOfMaterialItemModel import select_bill_of_material_item_for_BOM
from models.billOfMaterialModel import select_bill_of_material_for_maintenance
from models.dbUtile import Customers
from models.maintenanceModel import select_maintenance_by_code, delete_maintenance, update_maintenance_confirm
from reports.acconfReport import CreateAcConfReport
from reports.proconfReport import CreateProConfReport
from uiview.uimodels.MaintenanceTableModel import MaintenanceTableModel


def stylesheet():
	styles = {
		'default': LineStyle(

		)
	}


class Ui_confirmWMaintenanceDialog(QDialog):
	def __init__(self, parent=None):
		super(Ui_confirmWMaintenanceDialog, self).__init__()
		self.setupUi(self)

	def setupUi(self, confirmWMaintenanceDialog):
		self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

		confirmWMaintenanceDialog.setObjectName("confirmWMaintenanceDialog")
		confirmWMaintenanceDialog.resize(832, 470)
		self.label = QtWidgets.QLabel(confirmWMaintenanceDialog)
		self.label.setGeometry(QtCore.QRect(14, 3, 47, 20))
		self.label.setObjectName("label")
		self.loggeduser = QtWidgets.QLabel(confirmWMaintenanceDialog)
		self.loggeduser.setGeometry(QtCore.QRect(65, 3, 180, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggeduser.setFont(font)
		self.loggeduser.setText("")
		self.loggeduser.setObjectName("loggeduser")
		self.loggeduser.setText(getLoginDataPKL()['name'])
		self.line = QtWidgets.QFrame(confirmWMaintenanceDialog)
		self.line.setGeometry(QtCore.QRect(3, 28, 820, 3))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.label_3 = QtWidgets.QLabel(confirmWMaintenanceDialog)
		self.label_3.setGeometry(QtCore.QRect(14, 31, 150, 20))
		self.label_3.setObjectName("label_3")
		self.tableView = QtWidgets.QTableView(confirmWMaintenanceDialog)
		self.tableView.setGeometry(QtCore.QRect(10, 50, 390, 411))
		self.tableView.setObjectName("tableView")
		self.tableView = QtWidgets.QTableView(confirmWMaintenanceDialog)
		self.tableView.setGeometry(QtCore.QRect(10, 50, 390, 411))
		self.tableView.setObjectName("tableView")
		self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.tableView.setTabKeyNavigation(False)
		self.tableView.setProperty("showDropIndicator", False)
		self.tableView.setDragDropOverwriteMode(False)
		self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
		self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.tableView.horizontalHeader().setCascadingSectionResizes(True)
		self.tableData = MaintenanceTableModel()
		self.tableView.setModel(self.tableData)
		self.tableView.setColumnWidth(0, 100)
		self.tableView.setColumnWidth(1, 191)
		self.tableView.setColumnWidth(2, 82)
		for idx, val in enumerate(getMaintenanceHolded()):
			self.tableData.addCustomer(Customers(getMaintenanceHolded()[idx].customers.name
												 , getMaintenanceHolded()[
													 idx].customers.mobile_number
												 , None, None, None, None
												 , getMaintenanceHolded()[idx].m_code
												 , None, None))
		self.tableView.clicked.connect(self.Clicked)
		self.line_2 = QtWidgets.QFrame(confirmWMaintenanceDialog)
		self.line_2.setGeometry(QtCore.QRect(410, 35, 3, 430))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.label_4 = QtWidgets.QLabel(confirmWMaintenanceDialog)
		self.label_4.setGeometry(QtCore.QRect(420, 87, 100, 13))
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(confirmWMaintenanceDialog)
		self.label_5.setGeometry(QtCore.QRect(420, 109, 110, 20))
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(confirmWMaintenanceDialog)
		self.label_6.setGeometry(QtCore.QRect(420, 129, 130, 20))
		self.label_6.setObjectName("label_6")
		self.label_7 = QtWidgets.QLabel(confirmWMaintenanceDialog)
		self.label_7.setGeometry(QtCore.QRect(421, 34, 90, 20))
		self.label_7.setObjectName("label_7")
		self.label_8 = QtWidgets.QLabel(confirmWMaintenanceDialog)
		self.label_8.setGeometry(QtCore.QRect(420, 58, 120, 20))
		self.label_8.setObjectName("label_8")
		self.maintCodelbl = QtWidgets.QLineEdit(confirmWMaintenanceDialog)
		self.maintCodelbl.setEnabled(False)
		self.maintCodelbl.setGeometry(QtCore.QRect(519, 85, 120, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.maintCodelbl.setFont(font)
		self.maintCodelbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.maintCodelbl.setObjectName("maintCodelbl")
		self.maintProductlbl = QtWidgets.QLineEdit(confirmWMaintenanceDialog)
		self.maintProductlbl.setEnabled(False)
		self.maintProductlbl.setGeometry(QtCore.QRect(532, 110, 280, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.maintProductlbl.setFont(font)
		self.maintProductlbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.maintProductlbl.setObjectName("maintProductlbl")
		self.maintDesclbl = QtWidgets.QTextBrowser(confirmWMaintenanceDialog)
		self.maintDesclbl.setEnabled(False)
		self.maintDesclbl.setGeometry(QtCore.QRect(549, 136, 270, 80))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.maintDesclbl.setFont(font)
		self.maintDesclbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.maintDesclbl.setLineWidth(1)
		self.maintDesclbl.setObjectName("maintDesclbl")
		self.custNamelbl = QtWidgets.QLineEdit(confirmWMaintenanceDialog)
		self.custNamelbl.setEnabled(False)
		self.custNamelbl.setGeometry(QtCore.QRect(508, 35, 280, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.custNamelbl.setFont(font)
		self.custNamelbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.custNamelbl.setObjectName("custNamelbl")
		self.custMobilePhonelbl = QtWidgets.QLineEdit(confirmWMaintenanceDialog)
		self.custMobilePhonelbl.setEnabled(False)
		self.custMobilePhonelbl.setGeometry(QtCore.QRect(543, 60, 240, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.custMobilePhonelbl.setFont(font)
		self.custMobilePhonelbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.custMobilePhonelbl.setObjectName("custMobilePhonelbl")
		self.line_3 = QtWidgets.QFrame(confirmWMaintenanceDialog)
		self.line_3.setGeometry(QtCore.QRect(416, 220, 410, 3))
		self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.deletebtn = QtWidgets.QPushButton(confirmWMaintenanceDialog)
		self.deletebtn.setGeometry(QtCore.QRect(473, 415, 90, 40))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.deletebtn.setFont(font)
		self.deletebtn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
									 "color: rgb(255, 255, 255);")
		self.deletebtn.setObjectName("deletebtn")
		self.closebtn = QtWidgets.QPushButton(confirmWMaintenanceDialog)
		self.closebtn.setGeometry(QtCore.QRect(687, 414, 90, 40))
		self.closebtn.setObjectName("closebtn")
		self.closebtn.clicked.connect(self.close)
		self.line_4 = QtWidgets.QFrame(confirmWMaintenanceDialog)
		self.line_4.setGeometry(QtCore.QRect(416, 391, 410, 20))
		self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_4.setObjectName("line_4")
		self.label_2 = QtWidgets.QLabel(confirmWMaintenanceDialog)
		self.label_2.setGeometry(QtCore.QRect(421, 236, 100, 13))
		self.label_2.setObjectName("label_2")
		self.label_9 = QtWidgets.QLabel(confirmWMaintenanceDialog)
		self.label_9.setGeometry(QtCore.QRect(421, 273, 90, 13))
		self.label_9.setObjectName("label_9")
		self.label_10 = QtWidgets.QLabel(confirmWMaintenanceDialog)
		self.label_10.setGeometry(QtCore.QRect(421, 315, 100, 13))
		self.label_10.setObjectName("label_10")
		self.label_11 = QtWidgets.QLabel(confirmWMaintenanceDialog)
		self.label_11.setGeometry(QtCore.QRect(638, 232, 60, 20))
		self.label_11.setAlignment(QtCore.Qt.AlignCenter)
		self.label_11.setObjectName("label_11")
		self.rowCostlbl = QtWidgets.QLineEdit(confirmWMaintenanceDialog)
		self.rowCostlbl.setEnabled(False)
		self.rowCostlbl.setGeometry(QtCore.QRect(520, 227, 100, 30))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.rowCostlbl.setFont(font)
		self.rowCostlbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.rowCostlbl.setObjectName("rowCostlbl")
		self.spCostlbl = QtWidgets.QLineEdit(confirmWMaintenanceDialog)
		self.spCostlbl.setEnabled(False)
		self.spCostlbl.setGeometry(QtCore.QRect(520, 265, 100, 30))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.spCostlbl.setFont(font)
		self.spCostlbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.spCostlbl.setObjectName("spCostlbl")
		self.matTotalCostlbl = QtWidgets.QLineEdit(confirmWMaintenanceDialog)
		self.matTotalCostlbl.setEnabled(False)
		self.matTotalCostlbl.setGeometry(QtCore.QRect(520, 307, 100, 30))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.matTotalCostlbl.setFont(font)
		self.matTotalCostlbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.matTotalCostlbl.setObjectName("matTotalCostlbl")
		self.line_5 = QtWidgets.QFrame(confirmWMaintenanceDialog)
		self.line_5.setGeometry(QtCore.QRect(629, 228, 3, 110))
		self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_5.setObjectName("line_5")
		self.label_12 = QtWidgets.QLabel(confirmWMaintenanceDialog)
		self.label_12.setGeometry(QtCore.QRect(635, 312, 60, 20))
		self.label_12.setAlignment(QtCore.Qt.AlignCenter)
		self.label_12.setObjectName("label_12")
		self.laborled = QtWidgets.QLineEdit(confirmWMaintenanceDialog)
		self.laborled.setEnabled(False)
		self.laborled.setGeometry(QtCore.QRect(700, 229, 100, 30))
		self.laborled.setObjectName("laborled")
		self.laborled.setFont(font)
		self.laborled.setStyleSheet("color: rgb(255, 0, 0);")
		self.line_6 = QtWidgets.QFrame(confirmWMaintenanceDialog)
		self.line_6.setGeometry(QtCore.QRect(418, 343, 410, 3))
		self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_6.setObjectName("line_6")
		self.line_7 = QtWidgets.QFrame(confirmWMaintenanceDialog)
		self.line_7.setGeometry(QtCore.QRect(420, 300, 200, 3))
		self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_7.setObjectName("line_7")
		self.totalCostlbl = QtWidgets.QLineEdit(confirmWMaintenanceDialog)
		self.totalCostlbl.setEnabled(False)
		self.totalCostlbl.setGeometry(QtCore.QRect(702, 307, 100, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.totalCostlbl.setFont(font)
		self.totalCostlbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.totalCostlbl.setObjectName("totalCostlbl")
		self.line_8 = QtWidgets.QFrame(confirmWMaintenanceDialog)
		self.line_8.setGeometry(QtCore.QRect(629, 406, 3, 60))
		self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_8.setObjectName("line_8")
		self.line_9 = QtWidgets.QFrame(confirmWMaintenanceDialog)
		self.line_9.setGeometry(QtCore.QRect(635, 300, 190, 3))
		self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_9.setObjectName("line_9")
		self.confirmbtn = QtWidgets.QPushButton(confirmWMaintenanceDialog)
		self.confirmbtn.setGeometry(QtCore.QRect(670, 351, 140, 40))
		font = QtGui.QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.confirmbtn.setFont(font)
		self.confirmbtn.setStyleSheet("color: rgb(255, 255, 255);\n"
									  "background-color: rgb(0, 203, 0);")
		self.confirmbtn.setObjectName("confirmbtn")
		self.confirmbtn.setEnabled(False)
		self.detailesbtn = QtWidgets.QPushButton(confirmWMaintenanceDialog)
		self.detailesbtn.setGeometry(QtCore.QRect(420, 351, 100, 40))
		font = QtGui.QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.detailesbtn.setFont(font)
		self.detailesbtn.setObjectName("detailesbtn")
		self.detailesbtn.setEnabled(False)
		self.deletebtn.setEnabled(False)
		self.confirmbtn.clicked.connect(self.confirmMainte)
		self.deletebtn.clicked.connect(self.do_delete)
		self.retranslateUi(confirmWMaintenanceDialog)
		QtCore.QMetaObject.connectSlotsByName(confirmWMaintenanceDialog)

	def retranslateUi(self, confirmWMaintenanceDialog):
		_translate = QtCore.QCoreApplication.translate
		confirmWMaintenanceDialog.setWindowTitle(
			_translate("confirmWMaintenanceDialog", "Customer Confirm Waiting Maintenance"))
		self.label.setText(_translate("confirmWMaintenanceDialog", "Welcome,"))
		self.label_3.setText(_translate("confirmWMaintenanceDialog", "Select Maintenance from table :"))
		self.label_4.setText(_translate("confirmWMaintenanceDialog", "Maintenance Code :"))
		self.label_5.setText(_translate("confirmWMaintenanceDialog", "Maintenance Product :"))
		self.label_6.setText(_translate("confirmWMaintenanceDialog", "Maintenance Descreption :"))
		self.label_7.setText(_translate("confirmWMaintenanceDialog", "Customer Name :"))
		self.label_8.setText(_translate("confirmWMaintenanceDialog", "Customer Mobile Phone :"))
		self.deletebtn.setText(_translate("confirmWMaintenanceDialog", "Delete"))
		self.closebtn.setText(_translate("confirmWMaintenanceDialog", "Close"))
		self.label_2.setText(_translate("confirmWMaintenanceDialog", "Raw Material Cost :"))
		self.label_9.setText(_translate("confirmWMaintenanceDialog", "Spare Parts Cost :"))
		self.label_10.setText(_translate("confirmWMaintenanceDialog", "Total Material Cost :"))
		self.label_11.setText(_translate("confirmWMaintenanceDialog", "Labor Cost :"))
		self.label_12.setText(_translate("confirmWMaintenanceDialog", "Total Cost :"))
		self.confirmbtn.setText(_translate("confirmWMaintenanceDialog", "Confirm"))
		self.detailesbtn.setText(_translate("confirmWMaintenanceDialog", "Details"))

	def Clicked(self, item):
		indexes = self.tableView.selectionModel().selectedRows(0)
		for ind in sorted(indexes):
			maint = select_maintenance_by_code(ind.data())
			self.custNamelbl.setText(maint.customers.name)
			self.custMobilePhonelbl.setText(maint.customers.mobile_number)
			self.maintCodelbl.setText(maint.m_code)
			self.maintProductlbl.setText(maint.product_of_maintenance)
			self.maintDesclbl.setText(maint.maintenance_description)
			self.laborled.setText(str(maint.cost_of_labor))
			bom = select_bill_of_material_for_maintenance(maint.id)
			self.rowCostlbl.setText(str(bom.cost_of_raw_material))
			self.spCostlbl.setText(str(bom.cost_of_spare_parts))
			self.matTotalCostlbl.setText(str(maint.cost_of_bill_of_material))
			total = maint.cost_of_labor + maint.cost_of_bill_of_material
			self.totalCostlbl.setText(str(total))
			self.confirmbtn.setEnabled(True)
			self.detailesbtn.setEnabled(True)
			self.deletebtn.setEnabled(True)
			self.detailesbtn.clicked.connect(self.detailsDia)

	def confirmMainte(self):
		datetimestr = datetime.now()
		timestampstr = datetimestr.strftime('%Y-%m-%d %H:%M:%S')
		indexes = self.tableView.selectionModel().selectedRows(0)
		for ind in sorted(indexes):
			maint = select_maintenance_by_code(ind.data())
		bom = select_bill_of_material_for_maintenance(maint.id)
		bomitem = select_bill_of_material_item_for_BOM(bom.id)
		for item in bomitem:
			if item.rawMaterial != None:
				decreaseRawMaterialInvQty(item.rawMaterial, item.qty_of_material)
			if item.spareParts != None:
				decreaseSparePartsInvQty(item.spareParts, item.qty_of_material)
		update_maintenance_confirm(maint.id, timestampstr)
		CreateAcConfReport(maint).create_pdf()
		CreateProConfReport(maint).create_pdf()

		self.tableData = MaintenanceTableModel()
		self.tableView.setModel(self.tableData)
		for idx, val in enumerate(getMaintenanceHolded()):
			self.tableData.addCustomer(Customers(getMaintenanceHolded()[idx].customers.name
												 , getMaintenanceHolded()[
													 idx].customers.mobile_number
												 , None, None, None, None
												 , getMaintenanceHolded()[idx].m_code
												 , None, None))

	def do_delete(self):
		indexes = self.tableView.selectionModel().selectedRows(0)
		for ind in sorted(indexes):
			maint = select_maintenance_by_code(ind.data())
		reply = QMessageBox.question(QMessageBox(), "OOP'S",
									 'Are you sure to delete ?\n Maintenance \n Code : {}'.format(
										 maint.m_code) + '\n Customer Name : {}'.format(
										 maint.customers.name) + '\n This Action Cant Undo',
									 QMessageBox.Yes | QMessageBox.No)
		if reply == QMessageBox.Yes:
			delete_maintenance(maint.id)

		self.tableData = MaintenanceTableModel()
		self.tableView.setModel(self.tableData)
		for idx, val in enumerate(getMaintenanceHolded()):
			self.tableData.addCustomer(Customers(getMaintenanceHolded()[idx].customers.name
												 , getMaintenanceHolded()[
													 idx].customers.mobile_number
												 , None, None, None, None
												 , getMaintenanceHolded()[idx].m_code
												 , None, None))

	def detailsDia(self):
		indexes = self.tableView.selectionModel().selectedRows(0)
		for ind in sorted(indexes):
			maint = select_maintenance_by_code(ind.data())

		from uiview.ui_maintenanceDetails import Ui_maintenanceDetailsDialog
		self.md = Ui_maintenanceDetailsDialog(maint)
		self.md.exec_()


# if __name__ == "__main__":
# 	app = QtWidgets.QApplication(sys.argv)
# 	myapp = Ui_confirmWMaintenanceDialog()
# 	myapp.show()
# 	app.exec_()
