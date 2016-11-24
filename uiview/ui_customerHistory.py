# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_customerHistory.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

from Control.maintenanceLogic import getMaintenanceForCustomer, getMaintenanceStatus
from models.cityModel import select_city_by_id
from models.customersModel import select_customer_by_id
from models.dbUtile import Maintenance
from models.maintenanceModel import select_maintenance_by_code
from uiview.uimodels.custMaintTableModel import CustomerMaintenanceTableModel


class Ui_historyDialog(QDialog):
    def __init__(self, customer, parent=None):
        super(Ui_historyDialog, self).__init__()
        self.customer = customer
        self.setupUi(self)
    def setupUi(self, historyDialog):
        historyDialog.setObjectName("historyDialog")
        historyDialog.resize(348, 569)
        self.label = QtWidgets.QLabel(historyDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 90, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(historyDialog)
        self.label_2.setGeometry(QtCore.QRect(9, 37, 130, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(historyDialog)
        self.label_3.setGeometry(QtCore.QRect(11, 63, 90, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(historyDialog)
        self.label_4.setGeometry(QtCore.QRect(167, 63, 80, 13))
        self.label_4.setObjectName("label_4")
        self.customerNamelbl = QtWidgets.QLineEdit(historyDialog)
        self.customerNamelbl.setEnabled(False)
        self.customerNamelbl.setGeometry(QtCore.QRect(95, 8, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.customerNamelbl.setFont(font)
        self.customerNamelbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.customerNamelbl.setObjectName("customerNamelbl")
        self.customerAgelbl = QtWidgets.QLineEdit(historyDialog)
        self.customerAgelbl.setEnabled(False)
        self.customerAgelbl.setGeometry(QtCore.QRect(88, 60, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.customerAgelbl.setFont(font)
        self.customerAgelbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.customerAgelbl.setObjectName("customerAgelbl")
        self.CustomerCitylbl = QtWidgets.QLineEdit(historyDialog)
        self.CustomerCitylbl.setEnabled(False)
        self.CustomerCitylbl.setGeometry(QtCore.QRect(244, 60, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.CustomerCitylbl.setFont(font)
        self.CustomerCitylbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.CustomerCitylbl.setObjectName("CustomerCitylbl")
        self.customerMobilelbl = QtWidgets.QLineEdit(historyDialog)
        self.customerMobilelbl.setEnabled(False)
        self.customerMobilelbl.setGeometry(QtCore.QRect(135, 34, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.customerMobilelbl.setFont(font)
        self.customerMobilelbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.customerMobilelbl.setObjectName("customerMobilelbl")
        self.line = QtWidgets.QFrame(historyDialog)
        self.line.setGeometry(QtCore.QRect(3, 87, 340, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableView = QtWidgets.QTableView(historyDialog)
        self.tableView.setGeometry(QtCore.QRect(8, 109, 330, 311))
        self.tableView.setObjectName("tableView")
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setTabKeyNavigation(False)
        self.tableView.setProperty("showDropIndicator", False)
        self.tableView.setDragDropOverwriteMode(False)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)



        self.label_5 = QtWidgets.QLabel(historyDialog)
        self.label_5.setGeometry(QtCore.QRect(12, 92, 140, 13))
        self.label_5.setObjectName("label_5")
        self.line_2 = QtWidgets.QFrame(historyDialog)
        self.line_2.setGeometry(QtCore.QRect(4, 426, 340, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.detailsbtn = QtWidgets.QPushButton(historyDialog)
        self.detailsbtn.setGeometry(QtCore.QRect(20, 524, 75, 40))
        self.detailsbtn.setObjectName("detailsbtn")
        self.detailsbtn.setEnabled(False)

        self.closebtn = QtWidgets.QPushButton(historyDialog)
        self.closebtn.setGeometry(QtCore.QRect(250, 524, 75, 40))
        self.closebtn.setObjectName("closebtn")
        self.line_3 = QtWidgets.QFrame(historyDialog)
        self.line_3.setGeometry(QtCore.QRect(3, 520, 340, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_6 = QtWidgets.QLabel(historyDialog)
        self.label_6.setGeometry(QtCore.QRect(6, 433, 100, 13))
        self.label_6.setObjectName("label_6")
        self.mainteCode = QtWidgets.QLineEdit(historyDialog)
        self.mainteCode.setEnabled(False)
        self.mainteCode.setGeometry(QtCore.QRect(105, 431, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.mainteCode.setFont(font)
        self.mainteCode.setStyleSheet("color: rgb(255, 0, 0);")
        self.mainteCode.setObjectName("mainteCode")
        self.label_7 = QtWidgets.QLabel(historyDialog)
        self.label_7.setGeometry(QtCore.QRect(6, 459, 110, 13))
        self.label_7.setObjectName("label_7")
        self.mainteProductlbl = QtWidgets.QLineEdit(historyDialog)
        self.mainteProductlbl.setEnabled(False)
        self.mainteProductlbl.setGeometry(QtCore.QRect(116, 457, 220, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.mainteProductlbl.setFont(font)
        self.mainteProductlbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.mainteProductlbl.setObjectName("mainteProductlbl")
        self.mainteStatuslbl = QtWidgets.QLineEdit(historyDialog)
        self.mainteStatuslbl.setEnabled(False)
        self.mainteStatuslbl.setGeometry(QtCore.QRect(109, 483, 230, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.mainteStatuslbl.setFont(font)
        self.mainteStatuslbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.mainteStatuslbl.setObjectName("mainteStatuslbl")
        self.label_8 = QtWidgets.QLabel(historyDialog)
        self.label_8.setGeometry(QtCore.QRect(6, 485, 110, 13))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(historyDialog)
        QtCore.QMetaObject.connectSlotsByName(historyDialog)
        # self.customer = select_customer_by_id(21)
        self.customerNamelbl.setText(self.customer.name)
        self.customerMobilelbl.setText(self.customer.mobile_number)
        self.customerAgelbl.setText(str(self.customer.age))
        city = select_city_by_id(self.customer.city_id)
        self.CustomerCitylbl.setText(city.name)

        self.tableData = CustomerMaintenanceTableModel()
        self.tableView.setModel(self.tableData)
        for idx, val in enumerate(getMaintenanceForCustomer(self.customer)):
            self.tableData.addMaintenance(Maintenance(getMaintenanceForCustomer(self.customer)[
                idx].m_code, None, None, None, None, None, None, None,
            getMaintenanceForCustomer(self.customer)[idx].product_of_maintenance, None, None,
                                                   None, None))

        self.tableView.setColumnWidth(0, 102)
        self.tableView.setColumnWidth(1, 210)
        self.tableView.clicked.connect(self.Clicked)
        self.detailsbtn.clicked.connect(self.detailsDia)
        self.closebtn.clicked.connect(self.close)

    def retranslateUi(self, historyDialog):
        _translate = QtCore.QCoreApplication.translate
        historyDialog.setWindowTitle(_translate("historyDialog", "Customer History"))
        self.label.setText(_translate("historyDialog", "Customer Name :"))
        self.label_2.setText(_translate("historyDialog", "Customer Mobile Number :"))
        self.label_3.setText(_translate("historyDialog", "Customer Age :"))
        self.label_4.setText(_translate("historyDialog", "Customer City :"))
        self.label_5.setText(_translate("historyDialog", "Maintenance of Customer :"))
        self.detailsbtn.setText(_translate("historyDialog", "Detalis"))
        self.closebtn.setText(_translate("historyDialog", "Close"))
        self.label_6.setText(_translate("historyDialog", "Maintenance Code :"))
        self.label_7.setText(_translate("historyDialog", "Maintenance Product :"))
        self.label_8.setText(_translate("historyDialog", "Maintenance Status :"))

    def Clicked(self, item):
        indexes = self.tableView.selectionModel().selectedRows(0)
        for ind in sorted(indexes):
            maint = select_maintenance_by_code(ind.data())
            self.mainteCode.setText(maint.m_code)
            self.mainteProductlbl.setText(maint.product_of_maintenance)
            self.mainteStatuslbl.setText(str(getMaintenanceStatus(maint)))
        self.detailsbtn.setEnabled(True)


    def detailsDia(self):
        indexes = self.tableView.selectionModel().selectedRows(0)
        for ind in sorted(indexes):
            maint = select_maintenance_by_code(ind.data())
        from uiview.ui_maintenanceDetails import Ui_maintenanceDetailsDialog
        self.md = Ui_maintenanceDetailsDialog(maint)
        self.md.exec_()