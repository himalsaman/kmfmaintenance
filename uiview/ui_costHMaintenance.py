# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_costHMaintenance.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox

from Control.maintenanceLogic import getMaintenanceWaitLaborCost
from Control.userControl import getLoginDataPKL
from models.billOfMaterialModel import select_bill_of_material_for_maintenance
from models.dbUtile import Customers
from models.maintenanceModel import select_maintenance_by_code, update_maintenance, delete_maintenance
from uiview.uimodels.MaintenanceTableModel import MaintenanceTableModel


class Ui_costHoldedMaintenanceDialog(QDialog):
	def __init__(self, parent=None):
		super(Ui_costHoldedMaintenanceDialog, self).__init__()
		self.setupUi(self)

	def setupUi(self, costHoldedMaintenanceDialog):
		self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

		costHoldedMaintenanceDialog.setObjectName("costHoldedMaintenanceDialog")
		costHoldedMaintenanceDialog.resize(832, 470)
		self.label = QtWidgets.QLabel(costHoldedMaintenanceDialog)
		self.label.setGeometry(QtCore.QRect(14, 3, 47, 20))
		self.label.setObjectName("label")
		self.loggeduser = QtWidgets.QLabel(costHoldedMaintenanceDialog)
		self.loggeduser.setGeometry(QtCore.QRect(65, 3, 180, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggeduser.setFont(font)
		self.loggeduser.setText("")
		self.loggeduser.setObjectName("loggeduser")
		self.loggeduser.setText(getLoginDataPKL()['name'])
		self.line = QtWidgets.QFrame(costHoldedMaintenanceDialog)
		self.line.setGeometry(QtCore.QRect(3, 28, 820, 3))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.label_3 = QtWidgets.QLabel(costHoldedMaintenanceDialog)
		self.label_3.setGeometry(QtCore.QRect(14, 31, 150, 20))
		self.label_3.setObjectName("label_3")
		self.tableView = QtWidgets.QTableView(costHoldedMaintenanceDialog)
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
		for idx, val in enumerate(getMaintenanceWaitLaborCost()):
			self.tableData.addCustomer(Customers(
				getMaintenanceWaitLaborCost()[idx].customers.name
				, getMaintenanceWaitLaborCost()[
					idx].customers.mobile_number
				, None, None, None, None
				, getMaintenanceWaitLaborCost()[idx].m_code
				, None, None))
		self.tableView.clicked.connect(self.Clicked)
		self.line_2 = QtWidgets.QFrame(costHoldedMaintenanceDialog)
		self.line_2.setGeometry(QtCore.QRect(410, 35, 3, 430))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.label_4 = QtWidgets.QLabel(costHoldedMaintenanceDialog)
		self.label_4.setGeometry(QtCore.QRect(420, 87, 100, 13))
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(costHoldedMaintenanceDialog)
		self.label_5.setGeometry(QtCore.QRect(420, 109, 110, 20))
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(costHoldedMaintenanceDialog)
		self.label_6.setGeometry(QtCore.QRect(420, 129, 130, 20))
		self.label_6.setObjectName("label_6")
		self.label_7 = QtWidgets.QLabel(costHoldedMaintenanceDialog)
		self.label_7.setGeometry(QtCore.QRect(421, 34, 90, 20))
		self.label_7.setObjectName("label_7")
		self.label_8 = QtWidgets.QLabel(costHoldedMaintenanceDialog)
		self.label_8.setGeometry(QtCore.QRect(420, 58, 120, 20))
		self.label_8.setObjectName("label_8")
		self.maintCodelbl = QtWidgets.QLineEdit(costHoldedMaintenanceDialog)
		self.maintCodelbl.setEnabled(False)
		self.maintCodelbl.setGeometry(QtCore.QRect(519, 85, 120, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.maintCodelbl.setFont(font)
		self.maintCodelbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.maintCodelbl.setObjectName("maintCodelbl")
		self.maintProductlbl = QtWidgets.QLineEdit(costHoldedMaintenanceDialog)
		self.maintProductlbl.setEnabled(False)
		self.maintProductlbl.setGeometry(QtCore.QRect(532, 110, 280, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.maintProductlbl.setFont(font)
		self.maintProductlbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.maintProductlbl.setObjectName("maintProductlbl")
		self.maintDesclbl = QtWidgets.QTextBrowser(costHoldedMaintenanceDialog)
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
		self.custNamelbl = QtWidgets.QLineEdit(costHoldedMaintenanceDialog)
		self.custNamelbl.setEnabled(False)
		self.custNamelbl.setGeometry(QtCore.QRect(508, 35, 280, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.custNamelbl.setFont(font)
		self.custNamelbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.custNamelbl.setObjectName("custNamelbl")
		self.custMobilePhonelbl = QtWidgets.QLineEdit(costHoldedMaintenanceDialog)
		self.custMobilePhonelbl.setEnabled(False)
		self.custMobilePhonelbl.setGeometry(QtCore.QRect(543, 60, 240, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.custMobilePhonelbl.setFont(font)
		self.custMobilePhonelbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.custMobilePhonelbl.setObjectName("custMobilePhonelbl")
		self.line_3 = QtWidgets.QFrame(costHoldedMaintenanceDialog)
		self.line_3.setGeometry(QtCore.QRect(416, 220, 410, 3))
		self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.calcbtn = QtWidgets.QPushButton(costHoldedMaintenanceDialog)
		self.calcbtn.setGeometry(QtCore.QRect(694, 292, 80, 40))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.calcbtn.setFont(font)
		self.calcbtn.setObjectName("calcbtn")
		self.deletebtn = QtWidgets.QPushButton(costHoldedMaintenanceDialog)
		self.deletebtn.setGeometry(QtCore.QRect(573, 415, 90, 40))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.deletebtn.setFont(font)
		self.deletebtn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
									 "color: rgb(255, 255, 255);")
		self.deletebtn.setObjectName("deletebtn")
		self.closebtn = QtWidgets.QPushButton(costHoldedMaintenanceDialog)
		self.closebtn.setGeometry(QtCore.QRect(730, 414, 90, 40))
		self.closebtn.setObjectName("closebtn")
		self.closebtn.clicked.connect(self.close)
		self.detailsbtn = QtWidgets.QPushButton(costHoldedMaintenanceDialog)
		self.detailsbtn.setGeometry(QtCore.QRect(420, 414, 90, 40))
		self.detailsbtn.setObjectName("detailsbtn")
		self.line_4 = QtWidgets.QFrame(costHoldedMaintenanceDialog)
		self.line_4.setGeometry(QtCore.QRect(416, 391, 410, 20))
		self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_4.setObjectName("line_4")
		self.label_2 = QtWidgets.QLabel(costHoldedMaintenanceDialog)
		self.label_2.setGeometry(QtCore.QRect(421, 236, 100, 13))
		self.label_2.setObjectName("label_2")
		self.label_9 = QtWidgets.QLabel(costHoldedMaintenanceDialog)
		self.label_9.setGeometry(QtCore.QRect(421, 273, 90, 13))
		self.label_9.setObjectName("label_9")
		self.label_10 = QtWidgets.QLabel(costHoldedMaintenanceDialog)
		self.label_10.setGeometry(QtCore.QRect(421, 315, 100, 13))
		self.label_10.setObjectName("label_10")
		self.label_11 = QtWidgets.QLabel(costHoldedMaintenanceDialog)
		self.label_11.setGeometry(QtCore.QRect(639, 222, 181, 20))
		self.label_11.setAlignment(QtCore.Qt.AlignCenter)
		self.label_11.setObjectName("label_11")
		self.rowCostlbl = QtWidgets.QLineEdit(costHoldedMaintenanceDialog)
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
		self.spCostlbl = QtWidgets.QLineEdit(costHoldedMaintenanceDialog)
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
		self.matTotalCostlbl = QtWidgets.QLineEdit(costHoldedMaintenanceDialog)
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
		self.line_5 = QtWidgets.QFrame(costHoldedMaintenanceDialog)
		self.line_5.setGeometry(QtCore.QRect(629, 228, 3, 110))
		self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_5.setObjectName("line_5")
		self.label_12 = QtWidgets.QLabel(costHoldedMaintenanceDialog)
		self.label_12.setGeometry(QtCore.QRect(536, 344, 190, 20))
		self.label_12.setAlignment(QtCore.Qt.AlignCenter)
		self.label_12.setObjectName("label_12")
		self.laborled = QtWidgets.QLineEdit(costHoldedMaintenanceDialog)
		self.laborled.setGeometry(QtCore.QRect(682, 242, 100, 30))
		self.laborled.setObjectName("laborled")
		self.laborled.setValidator(QDoubleValidator())
		self.line_6 = QtWidgets.QFrame(costHoldedMaintenanceDialog)
		self.line_6.setGeometry(QtCore.QRect(418, 343, 410, 3))
		self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_6.setObjectName("line_6")
		self.line_7 = QtWidgets.QFrame(costHoldedMaintenanceDialog)
		self.line_7.setGeometry(QtCore.QRect(420, 300, 200, 3))
		self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_7.setObjectName("line_7")
		self.totalCostlbl = QtWidgets.QLineEdit(costHoldedMaintenanceDialog)
		self.totalCostlbl.setEnabled(False)
		self.totalCostlbl.setGeometry(QtCore.QRect(582, 365, 100, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.totalCostlbl.setFont(font)
		self.totalCostlbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.totalCostlbl.setObjectName("totalCostlbl")
		self.line_8 = QtWidgets.QFrame(costHoldedMaintenanceDialog)
		self.line_8.setGeometry(QtCore.QRect(720, 406, 3, 60))
		self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_8.setObjectName("line_8")
		self.calcbtn.setEnabled(False)
		self.calcbtn.clicked.connect(self.do_addLaborCost)
		self.deletebtn.clicked.connect(self.do_delete)
		self.retranslateUi(costHoldedMaintenanceDialog)
		self.deletebtn.setEnabled(False)
		QtCore.QMetaObject.connectSlotsByName(costHoldedMaintenanceDialog)
		self.detailsbtn.clicked.connect(self.detailsDia)
		self.detailsbtn.setEnabled(False)

	def retranslateUi(self, costHoldedMaintenanceDialog):
		_translate = QtCore.QCoreApplication.translate
		costHoldedMaintenanceDialog.setWindowTitle(
			_translate("costHoldedMaintenanceDialog", "Labor Cost Holded Maintenance"))
		self.label.setText(_translate("costHoldedMaintenanceDialog", "Welcome,"))
		self.label_3.setText(_translate("costHoldedMaintenanceDialog", "Select Maintenance from table :"))
		self.label_4.setText(_translate("costHoldedMaintenanceDialog", "Maintenance Code :"))
		self.label_5.setText(_translate("costHoldedMaintenanceDialog", "Maintenance Product :"))
		self.label_6.setText(_translate("costHoldedMaintenanceDialog", "Maintenance Descreption :"))
		self.label_7.setText(_translate("costHoldedMaintenanceDialog", "Customer Name :"))
		self.label_8.setText(_translate("costHoldedMaintenanceDialog", "Customer Mobile Phone :"))
		self.calcbtn.setText(_translate("costHoldedMaintenanceDialog", "Calculate"))
		self.deletebtn.setText(_translate("costHoldedMaintenanceDialog", "Delete"))
		self.closebtn.setText(_translate("costHoldedMaintenanceDialog", "Close"))
		self.label_2.setText(_translate("costHoldedMaintenanceDialog", "Raw Material Cost :"))
		self.label_9.setText(_translate("costHoldedMaintenanceDialog", "Spare Parts Cost :"))
		self.label_10.setText(_translate("costHoldedMaintenanceDialog", "Total Material Cost :"))
		self.label_11.setText(_translate("costHoldedMaintenanceDialog", "Enter Labor Cost"))
		self.label_12.setText(_translate("costHoldedMaintenanceDialog", "Total Cost "))
		self.detailsbtn.setText(_translate("costHoldedMaintenanceDialog", "Details"))

	def Clicked(self, item):
		indexes = self.tableView.selectionModel().selectedRows(0)
		for ind in sorted(indexes):
			maint = select_maintenance_by_code(ind.data())
			self.custNamelbl.setText(maint.customers.name)
			self.custMobilePhonelbl.setText(maint.customers.mobile_number)
			self.maintCodelbl.setText(maint.m_code)
			self.maintProductlbl.setText(maint.product_of_maintenance)
			self.maintDesclbl.setText(maint.maintenance_description)
			bom = select_bill_of_material_for_maintenance(maint.id)
			self.rowCostlbl.setText(str(bom.cost_of_raw_material))
			self.spCostlbl.setText(str(bom.cost_of_spare_parts))
			self.matTotalCostlbl.setText(str(maint.cost_of_bill_of_material))
			self.calcbtn.setEnabled(True)
			self.detailsbtn.setEnabled(True)
			self.deletebtn.setEnabled(True)
			role = getLoginDataPKL()['role']
			if int(role) == 1:
				self.deletebtn.setEnabled(False)

	def do_addLaborCost(self):
		indexes = self.tableView.selectionModel().selectedRows(0)
		for ind in sorted(indexes):
			maint = select_maintenance_by_code(ind.data())
			laborCost = self.laborled.text()
			update_maintenance(maint.id, maint.cost_of_bill_of_material,
							   laborCost,
							   None, None,
							   maint.created_at, maint.close_at,
							   maint.product_of_maintenance, maint.maintenance_description,
							   maint.start_date, maint.done_date)
			self.totalCostlbl.setText(str(maint.cost_of_bill_of_material + maint.cost_of_labor))
			self.tableData = MaintenanceTableModel()
			self.tableView.setModel(self.tableData)
			for idx, val in enumerate(getMaintenanceWaitLaborCost()):
				self.tableData.addCustomer(Customers(getMaintenanceWaitLaborCost()[idx].customers.name
													 , getMaintenanceWaitLaborCost()[
														 idx].customers.mobile_number
													 , None, None, None, None
													 , getMaintenanceWaitLaborCost()[idx].m_code
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
		for idx, val in enumerate(getMaintenanceWaitLaborCost()):
			self.tableData.addCustomer(Customers(
				getMaintenanceWaitLaborCost()[idx].customers.name
				, getMaintenanceWaitLaborCost()[
					idx].customers.mobile_number
				, None, None, None, None
				, getMaintenanceWaitLaborCost()[idx].m_code
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
# 	myapp = Ui_costHoldedMaintenanceDialog()
# 	myapp.show()
# 	app.exec_()
