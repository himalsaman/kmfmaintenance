# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_finishMaintenance.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox

from Control.maintenanceLogic import getMaintenanceUnderProccessing
from Control.userControl import getLoginDataPKL
from models.billOfMaterialModel import select_bill_of_material_for_maintenance
from models.dbUtile import Customers
from models.maintenanceModel import select_maintenance_by_code, update_maintenance_finish, \
	delete_maintenance
from uiview.uimodels.MaintenanceTableModel import MaintenanceTableModel


class Ui_finishMaintenanceDialog(QDialog):
	def __init__(self, parent=None):
		super(Ui_finishMaintenanceDialog, self).__init__()
		self.setupUi(self)

	def setupUi(self, finishMaintenanceDialog):
		self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

		finishMaintenanceDialog.setObjectName("finishMaintenanceDialog")
		finishMaintenanceDialog.resize(832, 508)
		self.label = QtWidgets.QLabel(finishMaintenanceDialog)
		self.label.setGeometry(QtCore.QRect(14, 3, 47, 20))
		self.label.setObjectName("label")
		self.loggeduser = QtWidgets.QLabel(finishMaintenanceDialog)
		self.loggeduser.setGeometry(QtCore.QRect(65, 3, 180, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggeduser.setFont(font)
		self.loggeduser.setText("")
		self.loggeduser.setObjectName("loggeduser")
		self.loggeduser.setText(getLoginDataPKL()['name'])
		self.line = QtWidgets.QFrame(finishMaintenanceDialog)
		self.line.setGeometry(QtCore.QRect(3, 28, 820, 3))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.label_3 = QtWidgets.QLabel(finishMaintenanceDialog)
		self.label_3.setGeometry(QtCore.QRect(14, 31, 150, 20))
		self.label_3.setObjectName("label_3")
		self.tableView = QtWidgets.QTableView(finishMaintenanceDialog)
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
		for idx, val in enumerate(getMaintenanceUnderProccessing()):
			self.tableData.addCustomer(Customers(getMaintenanceUnderProccessing()[idx].customers.name
												 , getMaintenanceUnderProccessing()[
													 idx].customers.mobile_number
												 , None, None, None, None
												 , getMaintenanceUnderProccessing()[idx].m_code
												 , None, None))
		self.tableView.clicked.connect(self.Clicked)
		self.line_2 = QtWidgets.QFrame(finishMaintenanceDialog)
		self.line_2.setGeometry(QtCore.QRect(410, 35, 3, 470))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.label_4 = QtWidgets.QLabel(finishMaintenanceDialog)
		self.label_4.setGeometry(QtCore.QRect(420, 83, 100, 13))
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(finishMaintenanceDialog)
		self.label_5.setGeometry(QtCore.QRect(420, 103, 110, 20))
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(finishMaintenanceDialog)
		self.label_6.setGeometry(QtCore.QRect(420, 124, 130, 20))
		self.label_6.setObjectName("label_6")
		self.label_7 = QtWidgets.QLabel(finishMaintenanceDialog)
		self.label_7.setGeometry(QtCore.QRect(421, 34, 90, 20))
		self.label_7.setObjectName("label_7")
		self.label_8 = QtWidgets.QLabel(finishMaintenanceDialog)
		self.label_8.setGeometry(QtCore.QRect(420, 56, 120, 20))
		self.label_8.setObjectName("label_8")
		self.maintCodelbl = QtWidgets.QLineEdit(finishMaintenanceDialog)
		self.maintCodelbl.setEnabled(False)
		self.maintCodelbl.setGeometry(QtCore.QRect(519, 81, 120, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.maintCodelbl.setFont(font)
		self.maintCodelbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.maintCodelbl.setObjectName("maintCodelbl")
		self.maintProductlbl = QtWidgets.QLineEdit(finishMaintenanceDialog)
		self.maintProductlbl.setEnabled(False)
		self.maintProductlbl.setGeometry(QtCore.QRect(532, 104, 280, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.maintProductlbl.setFont(font)
		self.maintProductlbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.maintProductlbl.setObjectName("maintProductlbl")
		self.maintDesclbl = QtWidgets.QTextBrowser(finishMaintenanceDialog)
		self.maintDesclbl.setEnabled(False)
		self.maintDesclbl.setGeometry(QtCore.QRect(549, 128, 270, 80))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.maintDesclbl.setFont(font)
		self.maintDesclbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.maintDesclbl.setLineWidth(1)
		self.maintDesclbl.setObjectName("maintDesclbl")
		self.custNamelbl = QtWidgets.QLineEdit(finishMaintenanceDialog)
		self.custNamelbl.setEnabled(False)
		self.custNamelbl.setGeometry(QtCore.QRect(508, 35, 280, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.custNamelbl.setFont(font)
		self.custNamelbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.custNamelbl.setObjectName("custNamelbl")
		self.custMobilePhonelbl = QtWidgets.QLineEdit(finishMaintenanceDialog)
		self.custMobilePhonelbl.setEnabled(False)
		self.custMobilePhonelbl.setGeometry(QtCore.QRect(543, 58, 240, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.custMobilePhonelbl.setFont(font)
		self.custMobilePhonelbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.custMobilePhonelbl.setObjectName("custMobilePhonelbl")
		self.line_3 = QtWidgets.QFrame(finishMaintenanceDialog)
		self.line_3.setGeometry(QtCore.QRect(416, 211, 410, 3))
		self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.deletebtn = QtWidgets.QPushButton(finishMaintenanceDialog)
		self.deletebtn.setGeometry(QtCore.QRect(473, 462, 90, 40))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.deletebtn.setFont(font)
		self.deletebtn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
									 "color: rgb(255, 255, 255);")
		self.deletebtn.setObjectName("deletebtn")
		self.closebtn = QtWidgets.QPushButton(finishMaintenanceDialog)
		self.closebtn.setGeometry(QtCore.QRect(687, 462, 90, 40))
		self.closebtn.setObjectName("closebtn")
		self.closebtn.clicked.connect(self.close)
		self.detailsbtn = QtWidgets.QPushButton(finishMaintenanceDialog)
		self.detailsbtn.setGeometry(QtCore.QRect(430, 413, 90, 40))
		self.detailsbtn.setObjectName("detailsbtn")
		self.detailsbtn.setEnabled(False)
		self.line_4 = QtWidgets.QFrame(finishMaintenanceDialog)
		self.line_4.setGeometry(QtCore.QRect(416, 448, 410, 20))
		self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_4.setObjectName("line_4")
		self.label_2 = QtWidgets.QLabel(finishMaintenanceDialog)
		self.label_2.setGeometry(QtCore.QRect(421, 301, 100, 13))
		self.label_2.setObjectName("label_2")
		self.label_9 = QtWidgets.QLabel(finishMaintenanceDialog)
		self.label_9.setGeometry(QtCore.QRect(421, 338, 90, 13))
		self.label_9.setObjectName("label_9")
		self.label_10 = QtWidgets.QLabel(finishMaintenanceDialog)
		self.label_10.setGeometry(QtCore.QRect(421, 380, 100, 13))
		self.label_10.setObjectName("label_10")
		self.label_11 = QtWidgets.QLabel(finishMaintenanceDialog)
		self.label_11.setGeometry(QtCore.QRect(638, 297, 60, 20))
		self.label_11.setAlignment(QtCore.Qt.AlignCenter)
		self.label_11.setObjectName("label_11")
		self.rowCostlbl = QtWidgets.QLineEdit(finishMaintenanceDialog)
		self.rowCostlbl.setEnabled(False)
		self.rowCostlbl.setGeometry(QtCore.QRect(520, 292, 100, 30))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.rowCostlbl.setFont(font)
		self.rowCostlbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.rowCostlbl.setObjectName("rowCostlbl")
		self.spCostlbl = QtWidgets.QLineEdit(finishMaintenanceDialog)
		self.spCostlbl.setEnabled(False)
		self.spCostlbl.setGeometry(QtCore.QRect(520, 330, 100, 30))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.spCostlbl.setFont(font)
		self.spCostlbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.spCostlbl.setObjectName("spCostlbl")
		self.matTotalCostlbl = QtWidgets.QLineEdit(finishMaintenanceDialog)
		self.matTotalCostlbl.setEnabled(False)
		self.matTotalCostlbl.setGeometry(QtCore.QRect(520, 372, 100, 30))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.matTotalCostlbl.setFont(font)
		self.matTotalCostlbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.matTotalCostlbl.setObjectName("matTotalCostlbl")
		self.line_5 = QtWidgets.QFrame(finishMaintenanceDialog)
		self.line_5.setGeometry(QtCore.QRect(629, 293, 3, 110))
		self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_5.setObjectName("line_5")
		self.label_12 = QtWidgets.QLabel(finishMaintenanceDialog)
		self.label_12.setGeometry(QtCore.QRect(635, 377, 60, 20))
		self.label_12.setAlignment(QtCore.Qt.AlignCenter)
		self.label_12.setObjectName("label_12")
		self.laborled = QtWidgets.QLineEdit(finishMaintenanceDialog)
		self.laborled.setEnabled(False)
		self.laborled.setGeometry(QtCore.QRect(700, 294, 100, 30))
		self.laborled.setObjectName("laborled")
		self.line_6 = QtWidgets.QFrame(finishMaintenanceDialog)
		self.line_6.setGeometry(QtCore.QRect(418, 408, 410, 3))
		self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_6.setObjectName("line_6")
		self.line_7 = QtWidgets.QFrame(finishMaintenanceDialog)
		self.line_7.setGeometry(QtCore.QRect(420, 365, 200, 3))
		self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_7.setObjectName("line_7")
		self.totalCostlbl = QtWidgets.QLineEdit(finishMaintenanceDialog)
		self.totalCostlbl.setEnabled(False)
		self.totalCostlbl.setGeometry(QtCore.QRect(702, 372, 100, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.totalCostlbl.setFont(font)
		self.totalCostlbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.totalCostlbl.setObjectName("totalCostlbl")
		self.line_8 = QtWidgets.QFrame(finishMaintenanceDialog)
		self.line_8.setGeometry(QtCore.QRect(630, 462, 3, 40))
		self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_8.setObjectName("line_8")
		self.line_9 = QtWidgets.QFrame(finishMaintenanceDialog)
		self.line_9.setGeometry(QtCore.QRect(635, 365, 190, 3))
		self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_9.setObjectName("line_9")
		self.finishbtn = QtWidgets.QPushButton(finishMaintenanceDialog)
		self.finishbtn.setGeometry(QtCore.QRect(670, 413, 130, 40))
		font = QtGui.QFont()
		font.setPointSize(11)
		font.setBold(True)
		font.setWeight(75)
		self.finishbtn.setFont(font)
		self.finishbtn.setStyleSheet("color: rgb(255, 255, 255);\n"
									 "background-color: rgb(0, 203, 0);")
		self.finishbtn.setObjectName("finishbtn")
		self.line_10 = QtWidgets.QFrame(finishMaintenanceDialog)
		self.line_10.setGeometry(QtCore.QRect(415, 287, 410, 3))
		self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_10.setObjectName("line_10")
		self.label_13 = QtWidgets.QLabel(finishMaintenanceDialog)
		self.label_13.setGeometry(QtCore.QRect(422, 219, 80, 13))
		self.label_13.setObjectName("label_13")
		self.label_14 = QtWidgets.QLabel(finishMaintenanceDialog)
		self.label_14.setGeometry(QtCore.QRect(423, 243, 80, 13))
		self.label_14.setObjectName("label_14")
		self.label_15 = QtWidgets.QLabel(finishMaintenanceDialog)
		self.label_15.setGeometry(QtCore.QRect(423, 265, 80, 13))
		self.label_15.setObjectName("label_15")
		self.createdlbl = QtWidgets.QLineEdit(finishMaintenanceDialog)
		self.createdlbl.setEnabled(False)
		self.createdlbl.setGeometry(QtCore.QRect(498, 216, 180, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.createdlbl.setFont(font)
		self.createdlbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.createdlbl.setObjectName("createdlbl")
		self.startlbl = QtWidgets.QLineEdit(finishMaintenanceDialog)
		self.startlbl.setEnabled(False)
		self.startlbl.setGeometry(QtCore.QRect(483, 240, 191, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.startlbl.setFont(font)
		self.startlbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.startlbl.setObjectName("startlbl")
		self.finishlbl = QtWidgets.QLineEdit(finishMaintenanceDialog)
		self.finishlbl.setEnabled(False)
		self.finishlbl.setGeometry(QtCore.QRect(486, 263, 190, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.finishlbl.setFont(font)
		self.finishlbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.finishlbl.setObjectName("finishlbl")
		self.finishlbl.setVisible(False)
		self.label_15.setVisible(False)
		self.finishbtn.setEnabled(False)
		self.finishbtn.clicked.connect(self.do_finish)
		self.deletebtn.clicked.connect(self.do_delete)
		self.detailsbtn.clicked.connect(self.detailsDia)
		self.retranslateUi(finishMaintenanceDialog)
		QtCore.QMetaObject.connectSlotsByName(finishMaintenanceDialog)
		role = getLoginDataPKL()['role']
		if int(role) == 2 or int(role) == 3:
			self.label_11.setVisible(False)
			self.label_12.setVisible(False)
			self.laborled.setVisible(False)
			self.totalCostlbl.setVisible(False)
			self.deletebtn.setEnabled(False)

	def retranslateUi(self, finishMaintenanceDialog):
		_translate = QtCore.QCoreApplication.translate
		finishMaintenanceDialog.setWindowTitle(_translate("finishMaintenanceDialog", "Finish Maintenance"))
		self.label.setText(_translate("finishMaintenanceDialog", "Welcome,"))
		self.label_3.setText(_translate("finishMaintenanceDialog", "Select Maintenance from table :"))
		self.label_4.setText(_translate("finishMaintenanceDialog", "Maintenance Code :"))
		self.label_5.setText(_translate("finishMaintenanceDialog", "Maintenance Product :"))
		self.label_6.setText(_translate("finishMaintenanceDialog", "Maintenance Descreption :"))
		self.label_7.setText(_translate("finishMaintenanceDialog", "Customer Name :"))
		self.label_8.setText(_translate("finishMaintenanceDialog", "Customer Mobile Phone :"))
		self.deletebtn.setText(_translate("finishMaintenanceDialog", "Delete"))
		self.closebtn.setText(_translate("finishMaintenanceDialog", "Close"))
		self.label_2.setText(_translate("finishMaintenanceDialog", "Raw Material Cost :"))
		self.label_9.setText(_translate("finishMaintenanceDialog", "Spare Parts Cost :"))
		self.label_10.setText(_translate("finishMaintenanceDialog", "Total Material Cost :"))
		self.label_11.setText(_translate("finishMaintenanceDialog", "Labor Cost :"))
		self.label_12.setText(_translate("finishMaintenanceDialog", "Total Cost :"))
		self.finishbtn.setText(_translate("finishMaintenanceDialog", "Finish"))
		self.label_13.setText(_translate("finishMaintenanceDialog", "Created Date :"))
		self.label_14.setText(_translate("finishMaintenanceDialog", "Start Date :"))
		self.label_15.setText(_translate("finishMaintenanceDialog", "Finish Date :"))
		self.detailsbtn.setText(_translate("finishMaintenanceDialog", "Details"))

	def Clicked(self, item):
		indexes = self.tableView.selectionModel().selectedRows(0)
		for ind in sorted(indexes):
			maint = select_maintenance_by_code(ind.data())
			self.custNamelbl.setText(maint.customers.name)
			self.custMobilePhonelbl.setText(maint.customers.mobile_number)
			self.maintCodelbl.setText(maint.m_code)
			self.maintProductlbl.setText(maint.product_of_maintenance)
			self.maintDesclbl.setText(maint.maintenance_description)
			self.createdlbl.setText(str(maint.created_at))
			self.laborled.setText(str(maint.cost_of_labor))
			self.startlbl.setText(str(maint.start_date))
			bom = select_bill_of_material_for_maintenance(maint.id)
			self.rowCostlbl.setText(str(bom.cost_of_raw_material))
			self.spCostlbl.setText(str(bom.cost_of_spare_parts))
			self.matTotalCostlbl.setText(str(maint.cost_of_bill_of_material))
			self.totalCostlbl.setText(str(maint.cost_of_bill_of_material + maint.cost_of_labor))
			self.finishbtn.setEnabled(True)
			self.detailsbtn.setEnabled(True)

	def do_finish(self):
		datetimestr = datetime.now()
		timestampstr = datetimestr.strftime('%Y-%m-%d %H:%M:%S')
		indexes = self.tableView.selectionModel().selectedRows(0)
		for ind in sorted(indexes):
			maint = select_maintenance_by_code(ind.data())
			update_maintenance_finish(maint.id, timestampstr)
		self.tableData = MaintenanceTableModel()
		self.tableView.setModel(self.tableData)
		for idx, val in enumerate(getMaintenanceUnderProccessing()):
			self.tableData.addCustomer(Customers(getMaintenanceUnderProccessing()[idx].customers.name
												 , getMaintenanceUnderProccessing()[
													 idx].customers.mobile_number
												 , None, None, None, None
												 , getMaintenanceUnderProccessing()[idx].m_code
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
		for idx, val in enumerate(getMaintenanceUnderProccessing()):
			self.tableData.addCustomer(Customers(getMaintenanceUnderProccessing()[idx].customers.name
												 , getMaintenanceUnderProccessing()[
													 idx].customers.mobile_number
												 , None, None, None, None
												 , getMaintenanceUnderProccessing()[idx].m_code
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
# 	myapp = Ui_finishMaintenanceDialog()
# 	myapp.show()
# 	app.exec_()
