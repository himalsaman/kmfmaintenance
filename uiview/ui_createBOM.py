# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_createBOM.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from datetime import datetime

from PyQt5 import Qt

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox, qApp
from PyQt5.QtWidgets import QMenu

from Control import BOMControl
from Control.BOMControl import getAllItemForBOM, claculateBOMItemRMCost, claculateBOMItemSPCost, creatBOMWithNewMAint
from Control.userControl import getLoginDataPKL
from models.billOfMaterialItemModel import  select_bill_of_material_item_by_code, \
	delete_bill_of_material_item, select_bill_of_material_item_for_BOM
from models.billOfMaterialModel import select_bill_of_material_for_maintenance, update_bill_of_material
from models.dbUtile import BillOfMaterialItem
from models.maintenanceModel import  update_maintenance, update_maintenance_from_BOM, update_maintenance_product
from models.rawMaterialModel import  select_row_material_by_id
from models.sparePartsModel import select_spare_parts_by_id
from uiview.uimodels.bomItemTableModel import BomItemTableModel

datetimestr = datetime.now()
timestampstr = datetimestr.strftime('%Y-%m-%d %H:%M:%S')


class Ui_createBOMDialog(QDialog):
	def __init__(self, mainte):
		super(Ui_createBOMDialog, self).__init__()
		self.mainte = mainte
		self.setupUi(self)

	def setupUi(self, createBOMDialog):
		createBOMDialog.setObjectName("createBOMDialog")
		createBOMDialog.resize(763, 510)
		self.label = QtWidgets.QLabel(createBOMDialog)
		self.label.setGeometry(QtCore.QRect(10, -1, 47, 20))
		self.label.setObjectName("label")
		self.loggedUserlbl = QtWidgets.QLabel(createBOMDialog)
		self.loggedUserlbl.setGeometry(QtCore.QRect(61, 0, 180, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggedUserlbl.setFont(font)
		self.loggedUserlbl.setText("")
		self.loggedUserlbl.setObjectName("loggedUserlbl")
		self.line = QtWidgets.QFrame(createBOMDialog)
		self.line.setGeometry(QtCore.QRect(12, 20, 740, 3))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.label_3 = QtWidgets.QLabel(createBOMDialog)
		self.label_3.setGeometry(QtCore.QRect(10, 31, 90, 13))
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(createBOMDialog)
		self.label_4.setGeometry(QtCore.QRect(253, 31, 130, 13))
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(createBOMDialog)
		self.label_5.setGeometry(QtCore.QRect(11, 61, 130, 13))
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(createBOMDialog)
		self.label_6.setGeometry(QtCore.QRect(12, 78, 130, 13))
		self.label_6.setObjectName("label_6")
		self.customerNamelbl = QtWidgets.QLabel(createBOMDialog)
		self.customerNamelbl.setGeometry(QtCore.QRect(96, 32, 151, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.customerNamelbl.setFont(font)
		self.customerNamelbl.setText("")
		self.customerNamelbl.setObjectName("customerNamelbl")
		self.customerMPhonelbl = QtWidgets.QLabel(createBOMDialog)
		self.customerMPhonelbl.setGeometry(QtCore.QRect(376, 31, 121, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.customerMPhonelbl.setFont(font)
		self.customerMPhonelbl.setText("")
		self.customerMPhonelbl.setObjectName("customerMPhonelbl")
		self.line_2 = QtWidgets.QFrame(createBOMDialog)
		self.line_2.setGeometry(QtCore.QRect(6, 201, 750, 3))
		self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.label_10 = QtWidgets.QLabel(createBOMDialog)
		self.label_10.setGeometry(QtCore.QRect(405, 5, 100, 13))
		self.label_10.setObjectName("label_10")
		self.maintenanceCodelbl = QtWidgets.QLabel(createBOMDialog)
		self.maintenanceCodelbl.setGeometry(QtCore.QRect(505, 5, 100, 13))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.maintenanceCodelbl.setFont(font)
		self.maintenanceCodelbl.setText("")
		self.maintenanceCodelbl.setObjectName("maintenanceCodelbl")
		self.label_12 = QtWidgets.QLabel(createBOMDialog)
		self.label_12.setGeometry(QtCore.QRect(602, 6, 47, 10))
		self.label_12.setObjectName("label_12")
		self.bomCodelbl = QtWidgets.QLabel(createBOMDialog)
		self.bomCodelbl.setGeometry(QtCore.QRect(650, 2, 100, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.bomCodelbl.setFont(font)
		self.bomCodelbl.setText("")
		self.bomCodelbl.setObjectName("bomCodelbl")
		self.label_14 = QtWidgets.QLabel(createBOMDialog)
		self.label_14.setGeometry(QtCore.QRect(524, 30, 120, 13))
		self.label_14.setObjectName("label_14")
		self.label_15 = QtWidgets.QLabel(createBOMDialog)
		self.label_15.setGeometry(QtCore.QRect(524, 60, 120, 13))
		self.label_15.setObjectName("label_15")
		self.label_16 = QtWidgets.QLabel(createBOMDialog)
		self.label_16.setGeometry(QtCore.QRect(524, 90, 100, 13))
		self.label_16.setObjectName("label_16")
		self.totalRMCled = QtWidgets.QLineEdit(createBOMDialog)
		self.totalRMCled.setEnabled(False)
		self.totalRMCled.setGeometry(QtCore.QRect(653, 27, 100, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.totalRMCled.setFont(font)
		self.totalRMCled.setStyleSheet("color: rgb(255, 0, 0);")
		self.totalRMCled.setAlignment(QtCore.Qt.AlignCenter)
		self.totalRMCled.setObjectName("totalRMCled")
		self.totalSPCled = QtWidgets.QLineEdit(createBOMDialog)
		self.totalSPCled.setEnabled(False)
		self.totalSPCled.setGeometry(QtCore.QRect(653, 55, 100, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.totalSPCled.setFont(font)
		self.totalSPCled.setStyleSheet("color: rgb(255, 0, 0);")
		self.totalSPCled.setAlignment(QtCore.Qt.AlignCenter)
		self.totalSPCled.setObjectName("totalSPCled")
		self.totalRMSPCled = QtWidgets.QLineEdit(createBOMDialog)
		self.totalRMSPCled.setEnabled(False)
		self.totalRMSPCled.setGeometry(QtCore.QRect(653, 87, 100, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.totalRMSPCled.setFont(font)
		self.totalRMSPCled.setStyleSheet("color: rgb(255, 0, 0);")
		self.totalRMSPCled.setAlignment(QtCore.Qt.AlignCenter)
		self.totalRMSPCled.setObjectName("totalRMSPCled")
		self.line_8 = QtWidgets.QFrame(createBOMDialog)
		self.line_8.setGeometry(QtCore.QRect(510, 36, 3, 150))
		self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_8.setObjectName("line_8")
		self.line_3 = QtWidgets.QFrame(createBOMDialog)
		self.line_3.setGeometry(QtCore.QRect(11, 50, 490, 3))
		self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.productMaintled = QtWidgets.QLineEdit(createBOMDialog)
		self.productMaintled.setGeometry(QtCore.QRect(140, 59, 201, 20))
		self.productMaintled.setObjectName("productMaintled")
		self.maintdesled = QtWidgets.QTextEdit(createBOMDialog)
		self.maintdesled.setGeometry(QtCore.QRect(143, 86, 291, 80))
		self.maintdesled.setObjectName("maintdesled")
		self.bomgroupbox = QtWidgets.QGroupBox(createBOMDialog)
		self.bomgroupbox.setGeometry(QtCore.QRect(8, 211, 750, 290))
		self.bomgroupbox.setTitle("")
		self.bomgroupbox.setObjectName("bomgroupbox")
		self.savebtn = QtWidgets.QPushButton(self.bomgroupbox)
		self.savebtn.setGeometry(QtCore.QRect(7, 179, 90, 40))
		self.savebtn.setObjectName("savebtn")
		self.laborCostled = QtWidgets.QLineEdit(self.bomgroupbox)
		self.laborCostled.setGeometry(QtCore.QRect(645, 29, 100, 20))
		self.laborCostled.setAlignment(QtCore.Qt.AlignCenter)
		self.laborCostled.setObjectName("laborCostled")
		self.otherCostlbl = QtWidgets.QLineEdit(self.bomgroupbox)
		self.otherCostlbl.setGeometry(QtCore.QRect(645, 83, 100, 20))
		self.otherCostlbl.setAlignment(QtCore.Qt.AlignCenter)
		self.otherCostlbl.setObjectName("otherCostlbl")
		self.label_19 = QtWidgets.QLabel(self.bomgroupbox)
		self.label_19.setGeometry(QtCore.QRect(665, 189, 60, 13))
		self.label_19.setObjectName("label_19")
		self.addNewRMbtn = QtWidgets.QPushButton(self.bomgroupbox)
		self.addNewRMbtn.setGeometry(QtCore.QRect(5, 15, 100, 40))
		self.addNewRMbtn.setObjectName("addNewRMbtn")
		self.label_18 = QtWidgets.QLabel(self.bomgroupbox)
		self.label_18.setGeometry(QtCore.QRect(665, 63, 60, 13))
		self.label_18.setObjectName("label_18")
		self.totalCostled = QtWidgets.QLineEdit(self.bomgroupbox)
		self.totalCostled.setEnabled(False)
		self.totalCostled.setGeometry(QtCore.QRect(645, 209, 100, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.totalCostled.setFont(font)
		self.totalCostled.setStyleSheet("color: rgb(255, 0, 0);")
		self.totalCostled.setAlignment(QtCore.Qt.AlignCenter)
		self.totalCostled.setObjectName("totalCostled")
		self.line_7 = QtWidgets.QFrame(self.bomgroupbox)
		self.line_7.setGeometry(QtCore.QRect(106, 12, 10, 280))
		self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_7.setObjectName("line_7")
		self.label_17 = QtWidgets.QLabel(self.bomgroupbox)
		self.label_17.setGeometry(QtCore.QRect(666, 9, 60, 13))
		self.label_17.setObjectName("label_17")
		self.closebtn = QtWidgets.QPushButton(self.bomgroupbox)
		self.closebtn.setGeometry(QtCore.QRect(7, 239, 90, 40))

		self.closebtn.clicked.connect(self.close)

		self.closebtn.setObjectName("closebtn")
		self.calcfinbtn = QtWidgets.QPushButton(self.bomgroupbox)
		self.calcfinbtn.setGeometry(QtCore.QRect(654, 126, 80, 40))
		self.calcfinbtn.setObjectName("calcfinbtn")
		self.addNewSPbtn = QtWidgets.QPushButton(self.bomgroupbox)
		self.addNewSPbtn.setGeometry(QtCore.QRect(5, 69, 100, 40))
		self.addNewSPbtn.setObjectName("addNewSPbtn")
		self.line_9 = QtWidgets.QFrame(self.bomgroupbox)
		self.line_9.setGeometry(QtCore.QRect(637, 8, 3, 280))
		self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_9.setObjectName("line_9")
		self.tableView = QtWidgets.QTableView(self.bomgroupbox)
		self.tableView.setGeometry(QtCore.QRect(119, 15, 510, 270))
		self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.tableView.setTabKeyNavigation(False)
		self.tableView.setProperty("showDropIndicator", False)
		self.tableView.setDragDropOverwriteMode(False)
		self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
		self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.tableView.setObjectName("tableView")
		self.tableData = BomItemTableModel()
		self.tableView.setModel(self.tableData)
		self.tableView.setColumnWidth(1, 210)
		self.tableView.setColumnWidth(2, 80)
		self.tableView.setColumnWidth(3, 40)
		self.tableView.setColumnWidth(4, 60)
		self.calcinibtn = QtWidgets.QPushButton(createBOMDialog)
		self.calcinibtn.setGeometry(QtCore.QRect(668, 165, 90, 30))
		self.calcinibtn.setStyleSheet("color: rgb(255, 0, 0);")
		self.calcinibtn.setObjectName("calcinibtn")
		self.savereqdatabtn = QtWidgets.QPushButton(createBOMDialog)
		self.savereqdatabtn.setGeometry(QtCore.QRect(346, 171, 160, 23))
		self.savereqdatabtn.setObjectName("savereqdatabtn")
		self.label.raise_()
		self.loggedUserlbl.raise_()
		self.line.raise_()
		self.label_3.raise_()
		self.label_4.raise_()
		self.label_5.raise_()
		self.label_6.raise_()
		self.customerNamelbl.raise_()
		self.customerMPhonelbl.raise_()
		self.line_2.raise_()
		self.label_10.raise_()
		self.maintenanceCodelbl.raise_()
		self.label_12.raise_()
		self.bomCodelbl.raise_()
		self.label_14.raise_()
		self.label_15.raise_()
		self.label_16.raise_()
		self.totalRMCled.raise_()
		self.totalSPCled.raise_()
		self.totalRMSPCled.raise_()
		self.line_8.raise_()
		self.line_3.raise_()
		self.productMaintled.raise_()
		self.maintdesled.raise_()
		self.bomgroupbox.raise_()
		self.calcinibtn.raise_()
		self.addNewRMbtn.raise_()
		self.addNewSPbtn.raise_()
		self.calcinibtn.raise_()
		self.bomgroupbox.setEnabled(False)
		self.calcinibtn.setEnabled(False)
		# set Maintenance Data
		self.loggedUserlbl.setText(getLoginDataPKL()['name'])
		self.maintenanceCodelbl.setText(self.mainte.m_code)
		if self.mainte.billOfMaterial == None:
			self.bomCodelbl.setText(BOMControl.BOMCode())
		# else:
		# self.bomCodelbl.setText(self.createBOM.gen_code)
		self.customerNamelbl.setText(self.mainte.customers.name)
		self.customerMPhonelbl.setText(self.mainte.customers.mobile_number)
		if not self.mainte.product_of_maintenance == None:
			self.productMaintled.setText(self.mainte.product_of_maintenance)
			self.productMaintled.setEnabled(False)
			if not self.mainte.maintenance_description == None:
				self.maintdesled.setText(self.mainte.maintenance_description)
				self.maintdesled.setEnabled(False)
			# self.createBOMFun()
			self.bomgroupbox.setEnabled(True)
			self.calcinibtn.setEnabled(True)
		else:
			self.setRequData()
		self.savereqdatabtn.raise_()
		self.savereqdatabtn.clicked.connect(self.setRequData)
		self.calcinibtn.clicked.connect(self.refresheddata)
		self.addNewRMbtn.clicked.connect(self.addRMAction)
		self.addNewSPbtn.clicked.connect(self.addSpAction)
		self.savebtn.clicked.connect(self.saveBOM)
		self.label_17.setVisible(False)
		self.label_18.setVisible(False)
		self.label_19.setVisible(False)
		self.laborCostled.setVisible(False)
		self.otherCostlbl.setVisible(False)
		self.calcfinbtn.setVisible(False)
		self.totalCostled.setVisible(False)
		self.line_9.setVisible(False)

		self.retranslateUi(createBOMDialog)
		QtCore.QMetaObject.connectSlotsByName(createBOMDialog)
		self.tableDataShow()
		self.lablesData()


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
		self.savebtn.setText(_translate("createBOMDialog", "Save"))
		self.label_19.setText(_translate("createBOMDialog", "Total Cost"))
		self.addNewRMbtn.setText(_translate("createBOMDialog", "Add Raw Material"))
		self.label_18.setText(_translate("createBOMDialog", "Other Cost"))
		self.label_17.setText(_translate("createBOMDialog", "Labor Cost"))
		self.closebtn.setText(_translate("createBOMDialog", "Close"))
		self.calcfinbtn.setText(_translate("createBOMDialog", "Add Cost  \n"
															  " Re-Calculate"))
		self.addNewSPbtn.setText(_translate("createBOMDialog", "Add Spare Part"))
		self.calcinibtn.setText(_translate("createBOMDialog", "Refresh"))
		self.savereqdatabtn.setText(_translate("createBOMDialog", "Save Product & Descreption"))

	def createBOMFun(self):
		if select_bill_of_material_for_maintenance(self.mainte.id):
			bom = select_bill_of_material_for_maintenance(self.mainte.id)
		else:
			bom = creatBOMWithNewMAint(self.mainte.id)
		return bom

	def setRequData(self):
		if self.productMaintled.text() == '' or self.maintdesled.toPlainText() == '':
			QMessageBox.warning(QMessageBox(), "Oop's", 'Product and Description is required',
								QMessageBox.Ok)
		else:
			# maint = self.mainte
			maint_id = self.mainte.id
			update_maintenance_product(self.mainte.id
									   , self.productMaintled.text()
									   , self.maintdesled.toPlainText())
			self.createBOMFun()
			self.bomgroupbox.setEnabled(True)
			self.calcinibtn.setEnabled(True)
			self.productMaintled.setEnabled(False)
			self.maintdesled.setEnabled(False)
			self.savereqdatabtn.setEnabled(False)

	def tableDataShow(self):
		if select_bill_of_material_for_maintenance(self.mainte.id):
			bom = select_bill_of_material_for_maintenance(self.mainte.id)
			for idx, val in enumerate(getAllItemForBOM(bom.id)):
				self.tableData.addItems(BillOfMaterialItem(getAllItemForBOM(bom.id)[
															   idx].raw_material_id
										, getAllItemForBOM(bom.id)[idx].spare_part_id
										, None, getAllItemForBOM(bom.id)[idx].cost_of_material,
										getAllItemForBOM(bom.id)[idx].qty_of_material,
										getAllItemForBOM(bom.id)[idx].gen_code))

	def contextMenuEvent(self, event):
		self.menu = QtWidgets.QMenu(self)
		renameAction = QtWidgets.QAction('Delete', self)
		renameAction.triggered.connect(self.renameSlot)
		self.menu.addAction(renameAction)
		# add other required actions
		self.menu.popup(QtGui.QCursor.pos())

	def renameSlot(self):
		indexes = self.tableView.selectionModel().selectedRows(0)
		for ind in sorted(indexes):
			bomitem = select_bill_of_material_item_by_code(ind.data())
			if bomitem.raw_material_id != None:
				mat = select_row_material_by_id(bomitem.raw_material_id)
				matname = mat.name
				matcode = mat.code
				mattype = 'Raw Material'
			if bomitem.spare_part_id != None:
				mat = select_spare_parts_by_id(bomitem.spare_part_id)
				matname = mat.name
				matcode = mat.gen_code
				mattype = 'Spare Parts'
		replay = QMessageBox.warning(QMessageBox(), "Oop's", 'You want delete\n {} : '.format(mattype)+'{}'.format(matcode)+' - {}'.format(matname)+'\n Are you sure?',
							QMessageBox.Yes | QMessageBox.Cancel)
		if replay == QMessageBox.Yes :
			delete_bill_of_material_item(bomitem.id)

	# get the selected cell and perform renaming
	def refresheddata(self):
		bom = select_bill_of_material_for_maintenance(self.mainte.id)
		self.tableData = BomItemTableModel()
		self.tableView.setModel(self.tableData)
		self.tableDataShow()
		self.lablesData()

	def lablesData(self):
		if select_bill_of_material_for_maintenance(self.mainte.id):
			bom = select_bill_of_material_for_maintenance(self.mainte.id)
			if claculateBOMItemRMCost(bom.id) == 0:
				rwcost = 0
			else:
				rwcost = claculateBOMItemRMCost(bom.id)
			if claculateBOMItemSPCost(bom.id) == 0:
				spcost = 0
			else:
				spcost = claculateBOMItemSPCost(bom.id)
			self.totalRMCled.setText(str(rwcost))
			self.totalSPCled.setText(str(spcost))
			self.totalRMSPCled.setText(str(rwcost + spcost))

	def addRMAction(self):
		bomo = select_bill_of_material_for_maintenance(self.mainte.id)
		from uiview.ui_addRMBOMItem import Ui_addRMBOMItemDialog
		self.addrmdiloag = Ui_addRMBOMItemDialog(bomo)
		self.addrmdiloag.exec_()

	def addSpAction(self):
		bomo = select_bill_of_material_for_maintenance(self.mainte.id)
		from uiview.ui_addSPBOMItem import Ui_addSPBOMItemDialog
		self.addspdiloag = Ui_addSPBOMItemDialog(bomo)
		self.addspdiloag.exec_()

	def saveBOM(self):
		if select_bill_of_material_for_maintenance(self.mainte.id):
			bom = select_bill_of_material_for_maintenance(self.mainte.id)
			rwmatcost = claculateBOMItemRMCost(bom.id)
			spmatcost = claculateBOMItemSPCost(bom.id)
			mattotalcost =  rwmatcost + spmatcost
			update_bill_of_material(bom.id, spmatcost, rwmatcost, mattotalcost)
			self.saveMainte()

	def saveMainte(self):
		totalCost = self.totalRMSPCled.text()
		update_maintenance_from_BOM(
			self.mainte.id
			, totalCost
			, timestampstr
			  )

