# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pusedMaintenance.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox

from Control.maintenanceLogic import getMaintenancePused
from Control.userControl import getLoginDataPKL
from models.dbUtile import Customers
from models.maintenanceModel import select_maintenance_by_code, delete_maintenance
from uiview.uimodels.customerTableModel import CustomerTableModel


class Ui_pusedMaintenanceDialog(QDialog):
	def __init__(self, parent=None):
		super(Ui_pusedMaintenanceDialog, self).__init__()
		self.setupUi(self)

	def setupUi(self, pusedMaintenanceDialog):
		pusedMaintenanceDialog.setObjectName("pusedMaintenanceDialog")
		pusedMaintenanceDialog.resize(832, 470)
		self.label = QtWidgets.QLabel(pusedMaintenanceDialog)
		self.label.setGeometry(QtCore.QRect(14, 3, 47, 20))
		self.label.setObjectName("label")
		self.loggeduser = QtWidgets.QLabel(pusedMaintenanceDialog)
		self.loggeduser.setGeometry(QtCore.QRect(65, 3, 180, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggeduser.setFont(font)
		self.loggeduser.setText("")
		self.loggeduser.setObjectName("loggeduser")
		self.line = QtWidgets.QFrame(pusedMaintenanceDialog)
		self.line.setGeometry(QtCore.QRect(3, 28, 820, 3))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.label_3 = QtWidgets.QLabel(pusedMaintenanceDialog)
		self.label_3.setGeometry(QtCore.QRect(14, 31, 150, 20))
		self.label_3.setObjectName("label_3")
		self.tableView = QtWidgets.QTableView(pusedMaintenanceDialog)
		self.tableView.setGeometry(QtCore.QRect(10, 50, 390, 411))
		self.tableView.setObjectName("tableView")
		self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.tableView.setTabKeyNavigation(False)
		self.tableView.setProperty("showDropIndicator", False)
		self.tableView.setDragDropOverwriteMode(False)
		self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
		self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.tableView.horizontalHeader().setCascadingSectionResizes(True)
		self.tableData = CustomerTableModel()
		self.tableView.setModel(self.tableData)
		for idx, val in enumerate(getMaintenancePused()):
			self.tableData.addCustomer(Customers(getMaintenancePused()[idx].customers.name
												 , getMaintenancePused()[
													 idx].customers.mobile_number
												 , None, None, None, None
												 , getMaintenancePused()[idx].m_code
												 , None, None))
		self.tableView.clicked.connect(self.Clicked)
		self.tableView.setColumnWidth(0, 261)
		self.tableView.setColumnWidth(1, 88)
		self.line_2 = QtWidgets.QFrame(pusedMaintenanceDialog)
		self.line_2.setGeometry(QtCore.QRect(410, 35, 3, 430))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.label_4 = QtWidgets.QLabel(pusedMaintenanceDialog)
		self.label_4.setGeometry(QtCore.QRect(420, 97, 100, 13))
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(pusedMaintenanceDialog)
		self.label_5.setGeometry(QtCore.QRect(420, 126, 110, 20))
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(pusedMaintenanceDialog)
		self.label_6.setGeometry(QtCore.QRect(420, 150, 130, 20))
		self.label_6.setObjectName("label_6")
		self.label_7 = QtWidgets.QLabel(pusedMaintenanceDialog)
		self.label_7.setGeometry(QtCore.QRect(423, 34, 90, 20))
		self.label_7.setObjectName("label_7")
		self.label_8 = QtWidgets.QLabel(pusedMaintenanceDialog)
		self.label_8.setGeometry(QtCore.QRect(422, 64, 120, 20))
		self.label_8.setObjectName("label_8")
		self.maintCodelbl = QtWidgets.QLineEdit(pusedMaintenanceDialog)
		self.maintCodelbl.setEnabled(False)
		self.maintCodelbl.setGeometry(QtCore.QRect(519, 95, 120, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.maintCodelbl.setFont(font)
		self.maintCodelbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.maintCodelbl.setObjectName("maintCodelbl")
		self.maintProductlbl = QtWidgets.QLineEdit(pusedMaintenanceDialog)
		self.maintProductlbl.setEnabled(False)
		self.maintProductlbl.setGeometry(QtCore.QRect(532, 127, 280, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.maintProductlbl.setFont(font)
		self.maintProductlbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.maintProductlbl.setObjectName("maintProductlbl")
		self.maintDesclbl = QtWidgets.QTextBrowser(pusedMaintenanceDialog)
		self.maintDesclbl.setEnabled(False)
		self.maintDesclbl.setGeometry(QtCore.QRect(549, 157, 270, 80))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.maintDesclbl.setFont(font)
		self.maintDesclbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.maintDesclbl.setLineWidth(1)
		self.maintDesclbl.setObjectName("maintDesclbl")
		self.custNamelbl = QtWidgets.QLineEdit(pusedMaintenanceDialog)
		self.custNamelbl.setEnabled(False)
		self.custNamelbl.setGeometry(QtCore.QRect(510, 35, 280, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.custNamelbl.setFont(font)
		self.custNamelbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.custNamelbl.setObjectName("custNamelbl")
		self.custMobilePhonelbl = QtWidgets.QLineEdit(pusedMaintenanceDialog)
		self.custMobilePhonelbl.setEnabled(False)
		self.custMobilePhonelbl.setGeometry(QtCore.QRect(545, 66, 240, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.custMobilePhonelbl.setFont(font)
		self.custMobilePhonelbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.custMobilePhonelbl.setObjectName("custMobilePhonelbl")
		self.line_3 = QtWidgets.QFrame(pusedMaintenanceDialog)
		self.line_3.setGeometry(QtCore.QRect(416, 249, 410, 3))
		self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.createBOMbtn = QtWidgets.QPushButton(pusedMaintenanceDialog)
		self.createBOMbtn.setGeometry(QtCore.QRect(520, 259, 80, 40))
		self.createBOMbtn.setEnabled(False)
		self.createBOMbtn.setObjectName("createBOMbtn")
		self.deletebtn = QtWidgets.QPushButton(pusedMaintenanceDialog)
		self.deletebtn.setGeometry(QtCore.QRect(630, 259, 80, 40))
		self.deletebtn.setObjectName("deletebtn")
		self.deletebtn.setEnabled(False)
		self.closebtn = QtWidgets.QPushButton(pusedMaintenanceDialog)
		self.closebtn.setGeometry(QtCore.QRect(740, 258, 80, 40))
		self.closebtn.setObjectName("closebtn")
		# maintenance data
		self.loggeduser.setText(getLoginDataPKL()['name'])
		# Buttons Action
		self.closebtn.clicked.connect(self.close)
		self.createBOMbtn.clicked.connect(self.openCreateBom)
		self.deletebtn.clicked.connect(self.do_delete)
		self.retranslateUi(pusedMaintenanceDialog)
		QtCore.QMetaObject.connectSlotsByName(pusedMaintenanceDialog)

	def retranslateUi(self, pusedMaintenanceDialog):
		_translate = QtCore.QCoreApplication.translate
		pusedMaintenanceDialog.setWindowTitle(_translate("pusedMaintenanceDialog", "Pused Maintenance"))
		self.label.setText(_translate("pusedMaintenanceDialog", "Welcome,"))
		self.label_3.setText(_translate("pusedMaintenanceDialog", "Select Maintenance from table :"))
		self.label_4.setText(_translate("pusedMaintenanceDialog", "Maintenance Code :"))
		self.label_5.setText(_translate("pusedMaintenanceDialog", "Maintenance Product :"))
		self.label_6.setText(_translate("pusedMaintenanceDialog", "Maintenance Descreption :"))
		self.label_7.setText(_translate("pusedMaintenanceDialog", "Customer Name :"))
		self.label_8.setText(_translate("pusedMaintenanceDialog", "Customer Mobile Phone :"))
		self.createBOMbtn.setText(_translate("pusedMaintenanceDialog", "Create BOM"))
		self.deletebtn.setText(_translate("pusedMaintenanceDialog", "Delete"))
		self.closebtn.setText(_translate("pusedMaintenanceDialog", "Close"))

	def Clicked(self, item):
		indexes = self.tableView.selectionModel().selectedRows(2)
		for ind in sorted(indexes):
			maint = select_maintenance_by_code(ind.data())
			self.custNamelbl.setText(maint.customers.name)
			self.custMobilePhonelbl.setText(maint.customers.mobile_number)
			self.maintCodelbl.setText(maint.m_code)
			self.maintProductlbl.setText(maint.product_of_maintenance)
			self.maintDesclbl.setText(maint.maintenance_description)
		self.createBOMbtn.setEnabled(True)
		self.deletebtn.setEnabled(True)
		role = getLoginDataPKL()['role']
		if int(role) == 2 or int(role) == 3 or int(role) == 1:
			self.deletebtn.setEnabled(False)

	def openCreateBom(self):
		indexes = self.tableView.selectionModel().selectedRows(2)
		for ind in sorted(indexes):
			maint = select_maintenance_by_code(ind.data())

		from uiview.ui_createBOM import Ui_createBOMDialog
		self.cbom = Ui_createBOMDialog(maint)
		self.cbom.exec_()

	def do_delete(self):
		indexes = self.tableView.selectionModel().selectedRows(2)
		for ind in sorted(indexes):
			maint = select_maintenance_by_code(ind.data())
		# print(maint)
		reply = QMessageBox.question(QMessageBox(), "OOP'S",
									 'Are you sure to delete ?\n Maintenance \n Code : {}'.format(
										 maint.m_code) + '\n Customer Name : {}'.format(
										 maint.customers.name) + '\n This Action Cant Undo',
									 QMessageBox.Yes | QMessageBox.No)
		if reply == QMessageBox.Yes:
			delete_maintenance(maint.id)
		self.tableData = CustomerTableModel()
		self.tableView.setModel(self.tableData)
		for idx, val in enumerate(getMaintenancePused()):
			self.tableData.addCustomer(Customers(getMaintenancePused()[idx].customers.name
												 , getMaintenancePused()[
													 idx].customers.mobile_number
												 , None, None, None, None
												 , getMaintenancePused()[idx].m_code
												 , None, None))

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	myapp = Ui_pusedMaintenanceDialog()
	myapp.show()
	app.exec_()
