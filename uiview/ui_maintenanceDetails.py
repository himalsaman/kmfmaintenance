# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_maintenanceDetails.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

from Control.BOMControl import getAllItemForBOM
from models.billOfMaterialModel import select_bill_of_material_for_maintenance
from models.dbUtile import BillOfMaterialItem
from uiview.uimodels.bomItemTableModel import BomItemTableModel


class Ui_maintenanceDetailsDialog(QDialog):
	def __init__(self, mainte):
		super(Ui_maintenanceDetailsDialog, self).__init__()
		self.mainte = mainte
		self.setupUi(self)

	def setupUi(self, maintenanceDetailsDialog):
		maintenanceDetailsDialog.setObjectName("maintenanceDetailsDialog")
		maintenanceDetailsDialog.resize(696, 588)
		self.label = QtWidgets.QLabel(maintenanceDetailsDialog)
		self.label.setGeometry(QtCore.QRect(8, 5, 50, 13))
		self.label.setObjectName("label")
		self.loggeduserlbl = QtWidgets.QLabel(maintenanceDetailsDialog)
		self.loggeduserlbl.setGeometry(QtCore.QRect(58, 5, 201, 16))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.loggeduserlbl.setFont(font)
		self.loggeduserlbl.setText("")
		self.loggeduserlbl.setObjectName("loggeduserlbl")
		self.label_3 = QtWidgets.QLabel(maintenanceDetailsDialog)
		self.label_3.setGeometry(QtCore.QRect(10, 33, 90, 13))
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(maintenanceDetailsDialog)
		self.label_4.setGeometry(QtCore.QRect(12, 60, 130, 13))
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(maintenanceDetailsDialog)
		self.label_5.setGeometry(QtCore.QRect(10, 96, 120, 20))
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(maintenanceDetailsDialog)
		self.label_6.setGeometry(QtCore.QRect(350, 60, 60, 13))
		self.label_6.setObjectName("label_6")
		self.label_7 = QtWidgets.QLabel(maintenanceDetailsDialog)
		self.label_7.setGeometry(QtCore.QRect(350, 34, 100, 13))
		self.label_7.setObjectName("label_7")
		self.line = QtWidgets.QFrame(maintenanceDetailsDialog)
		self.line.setGeometry(QtCore.QRect(7, 25, 680, 3))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.customerNamelbl = QtWidgets.QLineEdit(maintenanceDetailsDialog)
		self.customerNamelbl.setEnabled(False)
		self.customerNamelbl.setGeometry(QtCore.QRect(96, 31, 240, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.customerNamelbl.setFont(font)
		self.customerNamelbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.customerNamelbl.setObjectName("customerNamelbl")
		self.maintenanceCodelbl = QtWidgets.QLineEdit(maintenanceDetailsDialog)
		self.maintenanceCodelbl.setEnabled(False)
		self.maintenanceCodelbl.setGeometry(QtCore.QRect(449, 31, 160, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.maintenanceCodelbl.setFont(font)
		self.maintenanceCodelbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.maintenanceCodelbl.setObjectName("maintenanceCodelbl")
		self.maintenanceProductlbl = QtWidgets.QLineEdit(maintenanceDetailsDialog)
		self.maintenanceProductlbl.setEnabled(False)
		self.maintenanceProductlbl.setGeometry(QtCore.QRect(133, 92, 290, 30))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.maintenanceProductlbl.setFont(font)
		self.maintenanceProductlbl.setObjectName("maintenanceProductlbl")
		self.bomCodelbl = QtWidgets.QLineEdit(maintenanceDetailsDialog)
		self.bomCodelbl.setEnabled(False)
		self.bomCodelbl.setGeometry(QtCore.QRect(409, 57, 170, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.bomCodelbl.setFont(font)
		self.bomCodelbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.bomCodelbl.setObjectName("bomCodelbl")
		self.customerMobilelbl = QtWidgets.QLineEdit(maintenanceDetailsDialog)
		self.customerMobilelbl.setEnabled(False)
		self.customerMobilelbl.setGeometry(QtCore.QRect(144, 57, 190, 20))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.customerMobilelbl.setFont(font)
		self.customerMobilelbl.setStyleSheet("color: rgb(255, 0, 0);")
		self.customerMobilelbl.setObjectName("customerMobilelbl")
		self.line_2 = QtWidgets.QFrame(maintenanceDetailsDialog)
		self.line_2.setGeometry(QtCore.QRect(7, 82, 680, 3))
		self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.line_3 = QtWidgets.QFrame(maintenanceDetailsDialog)
		self.line_3.setGeometry(QtCore.QRect(344, 30, 3, 50))
		self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.label_11 = QtWidgets.QLabel(maintenanceDetailsDialog)
		self.label_11.setGeometry(QtCore.QRect(11, 136, 130, 13))
		self.label_11.setObjectName("label_11")
		self.label_12 = QtWidgets.QLabel(maintenanceDetailsDialog)
		self.label_12.setGeometry(QtCore.QRect(10, 222, 60, 13))
		self.label_12.setObjectName("label_12")
		self.maintenanceDescriplbl = QtWidgets.QTextEdit(maintenanceDetailsDialog)
		self.maintenanceDescriplbl.setEnabled(False)
		self.maintenanceDescriplbl.setGeometry(QtCore.QRect(141, 132, 380, 80))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.maintenanceDescriplbl.setFont(font)
		self.maintenanceDescriplbl.setObjectName("maintenanceDescriplbl")
		self.tableView = QtWidgets.QTableView(maintenanceDetailsDialog)
		self.tableView.setEnabled(False)
		self.tableView.setGeometry(QtCore.QRect(71, 221, 520, 360))
		self.tableView.setObjectName("tableView")
		self.closebtn = QtWidgets.QPushButton(maintenanceDetailsDialog)
		self.closebtn.setGeometry(QtCore.QRect(609, 536, 80, 40))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.closebtn.setFont(font)
		self.closebtn.setObjectName("closebtn")
		self.editbtn = QtWidgets.QPushButton(maintenanceDetailsDialog)
		self.editbtn.setGeometry(QtCore.QRect(609, 483, 80, 40))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setBold(True)
		font.setWeight(75)
		self.editbtn.setFont(font)
		self.editbtn.setObjectName("editbtn")
		self.line_4 = QtWidgets.QFrame(maintenanceDetailsDialog)
		self.line_4.setGeometry(QtCore.QRect(600, 89, 3, 490))
		self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_4.setObjectName("line_4")

		self.retranslateUi(maintenanceDetailsDialog)
		QtCore.QMetaObject.connectSlotsByName(maintenanceDetailsDialog)
		self.maintedata()
		self.editbtn.clicked.connect(self.openEdit)
		self.closebtn.clicked.connect(self.close)

	def retranslateUi(self, maintenanceDetailsDialog):
		_translate = QtCore.QCoreApplication.translate
		maintenanceDetailsDialog.setWindowTitle(_translate("maintenanceDetailsDialog", "Maintenance Details Dialog"))
		self.label.setText(_translate("maintenanceDetailsDialog", "Welcome, "))
		self.label_3.setText(_translate("maintenanceDetailsDialog", "Customer Name :"))
		self.label_4.setText(_translate("maintenanceDetailsDialog", "Customer Mobile Number :"))
		self.label_5.setText(_translate("maintenanceDetailsDialog", "Product of Maintenance :"))
		self.label_6.setText(_translate("maintenanceDetailsDialog", "BOM Code :"))
		self.label_7.setText(_translate("maintenanceDetailsDialog", "Maintenance Code :"))
		self.label_11.setText(_translate("maintenanceDetailsDialog", "Maintenance descreption :"))
		self.label_12.setText(_translate("maintenanceDetailsDialog", "BOM Table :"))
		self.closebtn.setText(_translate("maintenanceDetailsDialog", "Close"))
		self.editbtn.setText(_translate("maintenanceDetailsDialog", "Edit"))

	def maintedata(self):
		bom = select_bill_of_material_for_maintenance(self.mainte.id)
		self.maintenanceCodelbl.setText(self.mainte.m_code)
		self.bomCodelbl.setText(bom.gen_code)
		self.customerNamelbl.setText(self.mainte.customers.name)
		self.customerMobilelbl.setText(self.mainte.customers.mobile_number)
		self.maintenanceProductlbl.setText(self.mainte.product_of_maintenance)
		self.maintenanceDescriplbl.setText(self.mainte.maintenance_description)
		self.tableDataShow()
	def tableDataShow(self):
		self.tableData = BomItemTableModel()
		self.tableView.setModel(self.tableData)
		bom = select_bill_of_material_for_maintenance(self.mainte.id)
		for idx, val in enumerate(getAllItemForBOM(bom.id)):
			self.tableData.addItems(BillOfMaterialItem(getAllItemForBOM(bom.id)[
														   idx].raw_material_id
													   , getAllItemForBOM(bom.id)[
														   idx].spare_part_id
													   , None, getAllItemForBOM(bom.id)[
														   idx].cost_of_material,
													   getAllItemForBOM(bom.id)[
														   idx].qty_of_material,
													   getAllItemForBOM(bom.id)[idx].gen_code))

	def openEdit(self):
		from uiview.ui_editBOM import Ui_editBOMDialog
		self.ed = Ui_editBOMDialog(self.mainte)
		self.ed.exec_()
