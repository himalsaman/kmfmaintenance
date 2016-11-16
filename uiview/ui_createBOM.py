# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_createBOM.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

from Control.BOMControl import getAllItemForBOM
from Control.maintenanceLogic import claculateBOMItemRMCost, claculateBOMItemSPCost
from Control.userControl import getLoginDataPKL
from models.billOfMaterialModel import select_bill_of_material_by_id
from models.dbUtile import BillOfMaterialItem

from uiview.uimodels.bomItemTableModel import BomItemTableModel


class Ui_createBOMDialog(QDialog):
	def __init__(self):
		super(Ui_createBOMDialog, self).__init__()
		self.setupUi(self)

	def setupUi(self, createBOMDialog):
		createBOMDialog.setObjectName("createBOMDialog")
		createBOMDialog.resize(763, 492)
		self.label = QtWidgets.QLabel(createBOMDialog)
		self.label.setGeometry(QtCore.QRect(10, 10, 47, 20))
		self.label.setObjectName("label")
		self.loggedUserlbl = QtWidgets.QLabel(createBOMDialog)
		self.loggedUserlbl.setGeometry(QtCore.QRect(61, 11, 180, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggedUserlbl.setFont(font)
		self.loggedUserlbl.setText("")
		self.loggedUserlbl.setObjectName("loggedUserlbl")
		self.loggedUserlbl.setText(getLoginDataPKL()['name'])
		self.line = QtWidgets.QFrame(createBOMDialog)
		self.line.setGeometry(QtCore.QRect(12, 36, 740, 3))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.label_3 = QtWidgets.QLabel(createBOMDialog)
		self.label_3.setGeometry(QtCore.QRect(10, 47, 90, 13))
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(createBOMDialog)
		self.label_4.setGeometry(QtCore.QRect(253, 47, 130, 13))
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(createBOMDialog)
		self.label_5.setGeometry(QtCore.QRect(11, 82, 130, 13))
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(createBOMDialog)
		self.label_6.setGeometry(QtCore.QRect(12, 108, 130, 13))
		self.label_6.setObjectName("label_6")
		self.customerNamelbl = QtWidgets.QLabel(createBOMDialog)
		self.customerNamelbl.setGeometry(QtCore.QRect(96, 48, 151, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.customerNamelbl.setFont(font)
		self.customerNamelbl.setText("")
		self.customerNamelbl.setObjectName("customerNamelbl")
		self.customerMPhonelbl = QtWidgets.QLabel(createBOMDialog)
		self.customerMPhonelbl.setGeometry(QtCore.QRect(376, 47, 121, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.customerMPhonelbl.setFont(font)
		self.customerMPhonelbl.setText("")
		self.customerMPhonelbl.setObjectName("customerMPhonelbl")
		self.line_2 = QtWidgets.QFrame(createBOMDialog)
		self.line_2.setGeometry(QtCore.QRect(10, 199, 740, 3))
		self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.label_10 = QtWidgets.QLabel(createBOMDialog)
		self.label_10.setGeometry(QtCore.QRect(340, 16, 100, 13))
		self.label_10.setObjectName("label_10")
		self.maintenanceCodelbl = QtWidgets.QLabel(createBOMDialog)
		self.maintenanceCodelbl.setGeometry(QtCore.QRect(440, 16, 100, 13))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.maintenanceCodelbl.setFont(font)
		self.maintenanceCodelbl.setText("")
		self.maintenanceCodelbl.setObjectName("maintenanceCodelbl")
		self.label_12 = QtWidgets.QLabel(createBOMDialog)
		self.label_12.setGeometry(QtCore.QRect(537, 17, 47, 10))
		self.label_12.setObjectName("label_12")
		self.bomCodelbl = QtWidgets.QLabel(createBOMDialog)
		self.bomCodelbl.setGeometry(QtCore.QRect(585, 13, 100, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.bomCodelbl.setFont(font)
		self.bomCodelbl.setText("")
		self.bomCodelbl.setObjectName("bomCodelbl")
		self.label_14 = QtWidgets.QLabel(createBOMDialog)
		self.label_14.setGeometry(QtCore.QRect(524, 51, 120, 13))
		self.label_14.setObjectName("label_14")
		self.label_15 = QtWidgets.QLabel(createBOMDialog)
		self.label_15.setGeometry(QtCore.QRect(524, 81, 120, 13))
		self.label_15.setObjectName("label_15")
		self.label_16 = QtWidgets.QLabel(createBOMDialog)
		self.label_16.setGeometry(QtCore.QRect(524, 111, 100, 13))
		self.label_16.setObjectName("label_16")
		self.totalRMCled = QtWidgets.QLineEdit(createBOMDialog)
		self.totalRMCled.setEnabled(False)
		self.totalRMCled.setGeometry(QtCore.QRect(653, 48, 100, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.totalRMCled.setFont(font)
		self.totalRMCled.setStyleSheet("color: rgb(255, 0, 0);")
		self.totalRMCled.setAlignment(QtCore.Qt.AlignCenter)
		self.totalRMCled.setObjectName("totalRMCled")
		self.totalSPCled = QtWidgets.QLineEdit(createBOMDialog)
		self.totalSPCled.setEnabled(False)
		self.totalSPCled.setGeometry(QtCore.QRect(653, 76, 100, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.totalSPCled.setFont(font)
		self.totalSPCled.setStyleSheet("color: rgb(255, 0, 0);")
		self.totalSPCled.setAlignment(QtCore.Qt.AlignCenter)
		self.totalSPCled.setObjectName("totalSPCled")
		self.totalRMSPCled = QtWidgets.QLineEdit(createBOMDialog)
		self.totalRMSPCled.setEnabled(False)
		self.totalRMSPCled.setGeometry(QtCore.QRect(653, 108, 100, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.totalRMSPCled.setFont(font)
		self.totalRMSPCled.setStyleSheet("color: rgb(255, 0, 0);")
		self.totalRMSPCled.setAlignment(QtCore.Qt.AlignCenter)
		self.totalRMSPCled.setObjectName("totalRMSPCled")
		self.addNewRMbtn = QtWidgets.QPushButton(createBOMDialog)
		self.addNewRMbtn.setGeometry(QtCore.QRect(10, 211, 100, 40))
		self.addNewRMbtn.setObjectName("addNewRMbtn")

		self.addNewRMbtn.clicked.connect(self.addRMAction)

		self.addNewSPbtn = QtWidgets.QPushButton(createBOMDialog)
		self.addNewSPbtn.setGeometry(QtCore.QRect(9, 266, 100, 40))
		self.addNewSPbtn.setObjectName("addNewSPbtn")

		self.addNewSPbtn.clicked.connect(self.addSpAction)

		self.calcinibtn = QtWidgets.QPushButton(createBOMDialog)
		self.calcinibtn.setGeometry(QtCore.QRect(8, 319, 100, 40))
		self.calcinibtn.setStyleSheet("color: rgb(255, 0, 0);")
		self.calcinibtn.setObjectName("calcinibtn")
		self.line_7 = QtWidgets.QFrame(createBOMDialog)
		self.line_7.setGeometry(QtCore.QRect(118, 210, 3, 270))
		self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_7.setObjectName("line_7")
		self.closebtn = QtWidgets.QPushButton(createBOMDialog)
		self.closebtn.setGeometry(QtCore.QRect(10, 430, 100, 40))
		self.closebtn.setObjectName("closebtn")
		self.line_8 = QtWidgets.QFrame(createBOMDialog)
		self.line_8.setGeometry(QtCore.QRect(510, 41, 3, 150))
		self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_8.setObjectName("line_8")
		self.line_9 = QtWidgets.QFrame(createBOMDialog)
		self.line_9.setGeometry(QtCore.QRect(647, 209, 3, 270))
		self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_9.setObjectName("line_9")
		self.label_17 = QtWidgets.QLabel(createBOMDialog)
		self.label_17.setGeometry(QtCore.QRect(676, 210, 60, 13))
		self.label_17.setObjectName("label_17")
		self.laborCostled = QtWidgets.QLineEdit(createBOMDialog)
		self.laborCostled.setGeometry(QtCore.QRect(655, 230, 100, 20))
		self.laborCostled.setAlignment(QtCore.Qt.AlignCenter)
		self.laborCostled.setObjectName("laborCostled")
		self.label_18 = QtWidgets.QLabel(createBOMDialog)
		self.label_18.setGeometry(QtCore.QRect(675, 264, 60, 13))
		self.label_18.setObjectName("label_18")
		self.otherCostlbl = QtWidgets.QLineEdit(createBOMDialog)
		self.otherCostlbl.setGeometry(QtCore.QRect(655, 284, 100, 20))
		self.otherCostlbl.setAlignment(QtCore.Qt.AlignCenter)
		self.otherCostlbl.setObjectName("otherCostlbl")
		self.label_19 = QtWidgets.QLabel(createBOMDialog)
		self.label_19.setGeometry(QtCore.QRect(675, 390, 60, 13))
		self.label_19.setObjectName("label_19")
		self.totalCostled = QtWidgets.QLineEdit(createBOMDialog)
		self.totalCostled.setEnabled(False)
		self.totalCostled.setGeometry(QtCore.QRect(655, 410, 100, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.totalCostled.setFont(font)
		self.totalCostled.setStyleSheet("color: rgb(255, 0, 0);")
		self.totalCostled.setAlignment(QtCore.Qt.AlignCenter)
		self.totalCostled.setObjectName("totalCostled")
		self.calcfinbtn = QtWidgets.QPushButton(createBOMDialog)
		self.calcfinbtn.setGeometry(QtCore.QRect(664, 327, 80, 40))
		self.calcfinbtn.setObjectName("calcfinbtn")
		self.tableView = QtWidgets.QTableView(createBOMDialog)
		self.tableView.setGeometry(QtCore.QRect(130, 212, 510, 270))
		self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.tableView.setTabKeyNavigation(False)
		self.tableView.setProperty("showDropIndicator", False)
		self.tableView.setDragDropOverwriteMode(False)
		self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
		self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.tableView.setObjectName("tableView")
		self.tableData = BomItemTableModel()
		self.tableView.setModel(self.tableData)

		self.tableView.setColumnWidth(0, 263)
		self.tableView.setColumnWidth(1, 90)
		self.tableView.setColumnWidth(2, 70)
		self.tableView.setColumnWidth(3, 70)

		self.line_3 = QtWidgets.QFrame(createBOMDialog)
		self.line_3.setGeometry(QtCore.QRect(11, 70, 490, 3))
		self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.productMaintled = QtWidgets.QLineEdit(createBOMDialog)
		self.productMaintled.setGeometry(QtCore.QRect(140, 80, 201, 20))
		self.productMaintled.setObjectName("productMaintled")
		self.maintdesled = QtWidgets.QPlainTextEdit(createBOMDialog)
		self.maintdesled.setGeometry(QtCore.QRect(143, 111, 291, 80))
		self.maintdesled.setObjectName("maintdesled")

		self.upbtn = QtWidgets.QPushButton(createBOMDialog)
		self.upbtn.setGeometry(QtCore.QRect(520, 160, 90, 30))
		self.upbtn.setObjectName("savebtn")
		self.upbtn.clicked.connect(self.refre)

		self.savebtn = QtWidgets.QPushButton(createBOMDialog)
		self.savebtn.setGeometry(QtCore.QRect(10, 370, 100, 40))
		self.savebtn.setObjectName("savebtn")
		# self.savebtn.clicked.connect()
		self.show_table_date()

		self.show_data()
		self.retranslateUi(createBOMDialog)
		QtCore.QMetaObject.connectSlotsByName(createBOMDialog)

	def retranslateUi(self, createBOMDialog):
		_translate = QtCore.QCoreApplication.translate
		createBOMDialog.setWindowTitle(_translate("createBOMDialog", "Create BOM"))
		self.label.setText(_translate("createBOMDialog", "Welcome, "))
		self.label_3.setText(_translate("createBOMDialog", "Customer Name :"))
		self.label_4.setText(_translate("createBOMDialog", "Customer Mobile Phone :"))
		self.label_5.setText(_translate("createBOMDialog", "Product for Maintenance :"))
		self.label_6.setText(_translate("createBOMDialog", "Maintenance Descreption :"))
		self.label_10.setText(_translate("createBOMDialog", "Maintenance Code :"))
		self.label_12.setText(_translate("createBOMDialog", "BOM ID :"))
		self.label_14.setText(_translate("createBOMDialog", "Total Raw Material Cost :"))
		self.label_15.setText(_translate("createBOMDialog", "Total Spare Parts Cost :"))
		self.label_16.setText(_translate("createBOMDialog", "Total RM & SP Cost :"))
		self.addNewRMbtn.setText(_translate("createBOMDialog", "Add Raw Material"))
		self.addNewSPbtn.setText(_translate("createBOMDialog", "Add Spare Part"))
		self.calcinibtn.setText(_translate("createBOMDialog", "Claculate Cost"))
		self.closebtn.setText(_translate("createBOMDialog", "Close"))
		self.label_17.setText(_translate("createBOMDialog", "Labor Cost"))
		self.label_18.setText(_translate("createBOMDialog", "Other Cost"))
		self.label_19.setText(_translate("createBOMDialog", "Total Cost"))
		self.calcfinbtn.setText(_translate("createBOMDialog", "Add Cost  \n"
															  " Re-Calculate"))
		self.savebtn.setText(_translate("createBOMDialog", "Save"))
		self.upbtn.setText(_translate("createBOMDialog", "Refresh"))

	def show_table_date(self):
		for idx, val in enumerate(getAllItemForBOM()):
			self.tableData.addItems(BillOfMaterialItem(getAllItemForBOM()[idx].raw_material_id
													   , getAllItemForBOM()[idx].spare_part_id
													   , None, getAllItemForBOM()[idx].cost_of_material,
													   getAllItemForBOM()[idx].qty_of_material))

	def show_data(self):
		bomid = getAllItemForBOM()[1].bill_of_material_id
		bom = select_bill_of_material_by_id(bomid)
		maintenanceCode = bom.maintenance.m_code
		bomCode = bom.gen_code
		custName = bom.maintenance.customers.name
		custMobile = bom.maintenance.customers.mobile_number
		rwcost = claculateBOMItemRMCost()
		spcost = claculateBOMItemSPCost()

		self.maintenanceCodelbl.setText(maintenanceCode)
		self.bomCodelbl.setText(bomCode)
		self.customerNamelbl.setText(custName)
		self.customerMPhonelbl.setText(custMobile)
		self.totalRMCled.setText(str(rwcost))
		self.totalSPCled.setText(str(spcost))
		self.totalRMSPCled.setText(str(rwcost + spcost))

	# def set_data(self):

	def addRMAction(self):
		from uiview.ui_addRMBOMItem import Ui_addRMBOMItemDialog
		self.addrmdiloag = Ui_addRMBOMItemDialog()
		self.addrmdiloag.exec_()

	def addSpAction(self):
		from uiview.ui_addSPBOMItem import Ui_addSPBOMItemDialog
		self.addspdiloag = Ui_addSPBOMItemDialog()
		self.addspdiloag.exec_()


	def refre(self):
		self.deleteLater()
		self.d = Ui_createBOMDialog()
		self.d.show()
		self.show_table_date()
if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	cnc_dialog = Ui_createBOMDialog()
	cnc_dialog.show()
	sys.exit(app.exec_())

