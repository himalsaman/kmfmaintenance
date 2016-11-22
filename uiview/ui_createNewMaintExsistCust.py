# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_createNewMaintExsistCust.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

from Control.customerControl import getAllcustomers
from Control.maintenanceLogic import creatMaintenanceWithNewCustomer, creatMaintenanceExtCustomer
from models.cityModel import select_city_by_id
from models.customersModel import select_all_customers, select_customer_by_mob_num
from models.dbUtile import Customers
from uiview.uimodels.NewCustomerTableModel import NewCustomerTableModel


class Ui_createNewMaintenanceForExistsCustDialog(QDialog):
    def __init__(self, parent=None):
        super(Ui_createNewMaintenanceForExistsCustDialog, self).__init__()
        self.setupUi(self)
    def setupUi(self, createNewMaintenanceForExistsCustDialog):
        createNewMaintenanceForExistsCustDialog.setObjectName("createNewMaintenanceForExistsCustDialog")
        createNewMaintenanceForExistsCustDialog.resize(726, 455)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(createNewMaintenanceForExistsCustDialog.sizePolicy().hasHeightForWidth())
        createNewMaintenanceForExistsCustDialog.setSizePolicy(sizePolicy)
        self.tableView = QtWidgets.QTableView(createNewMaintenanceForExistsCustDialog)
        self.tableView.setGeometry(QtCore.QRect(10, 50, 360, 400))
        self.tableView.setObjectName("tableView")
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setTabKeyNavigation(False)
        self.tableView.setProperty("showDropIndicator", False)
        self.tableView.setDragDropOverwriteMode(False)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)

        self.tableData = NewCustomerTableModel()
        self.tableView.setModel(self.tableData)
        self.tableView.setColumnWidth(0, 229)
        self.tableView.setColumnWidth(1, 90)

        for idx, val in enumerate(getAllcustomers()):
            self.tableData.addCustomer(Customers(
                getAllcustomers()[idx].name
                , getAllcustomers()[idx].mobile_number
                , None
                , None
                , None))

        self.tableView.clicked.connect(self.Clicked)

        self.line = QtWidgets.QFrame(createNewMaintenanceForExistsCustDialog)
        self.line.setGeometry(QtCore.QRect(8, 25, 710, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(createNewMaintenanceForExistsCustDialog)
        self.label.setGeometry(QtCore.QRect(13, 4, 50, 13))
        self.label.setObjectName("label")
        self.loggeduser = QtWidgets.QLabel(createNewMaintenanceForExistsCustDialog)
        self.loggeduser.setGeometry(QtCore.QRect(63, 4, 120, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.loggeduser.setFont(font)
        self.loggeduser.setText("")
        self.loggeduser.setObjectName("loggeduser")
        self.label_2 = QtWidgets.QLabel(createNewMaintenanceForExistsCustDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 29, 150, 13))
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(createNewMaintenanceForExistsCustDialog)
        self.line_2.setGeometry(QtCore.QRect(374, 30, 3, 420))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(createNewMaintenanceForExistsCustDialog)
        self.label_3.setGeometry(QtCore.QRect(378, 26, 170, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(createNewMaintenanceForExistsCustDialog)
        self.label_4.setGeometry(QtCore.QRect(381, 96, 130, 13))
        self.label_4.setObjectName("label_4")
        self.label_12 = QtWidgets.QLabel(createNewMaintenanceForExistsCustDialog)
        self.label_12.setGeometry(QtCore.QRect(381, 63, 90, 13))
        self.label_12.setObjectName("label_12")
        self.customerNamelbl = QtWidgets.QLineEdit(createNewMaintenanceForExistsCustDialog)
        self.customerNamelbl.setEnabled(False)
        self.customerNamelbl.setGeometry(QtCore.QRect(467, 60, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.customerNamelbl.setFont(font)
        self.customerNamelbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.customerNamelbl.setObjectName("customerNamelbl")
        self.customerMobilelbl = QtWidgets.QLineEdit(createNewMaintenanceForExistsCustDialog)
        self.customerMobilelbl.setEnabled(False)
        self.customerMobilelbl.setGeometry(QtCore.QRect(503, 93, 210, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.customerMobilelbl.setFont(font)
        self.customerMobilelbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.customerMobilelbl.setObjectName("customerMobilelbl")
        self.line_3 = QtWidgets.QFrame(createNewMaintenanceForExistsCustDialog)
        self.line_3.setGeometry(QtCore.QRect(379, 50, 340, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.customerAgelbl = QtWidgets.QLineEdit(createNewMaintenanceForExistsCustDialog)
        self.customerAgelbl.setEnabled(False)
        self.customerAgelbl.setGeometry(QtCore.QRect(460, 126, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.customerAgelbl.setFont(font)
        self.customerAgelbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.customerAgelbl.setObjectName("customerAgelbl")
        self.label_5 = QtWidgets.QLabel(createNewMaintenanceForExistsCustDialog)
        self.label_5.setGeometry(QtCore.QRect(381, 129, 130, 13))
        self.label_5.setObjectName("label_5")
        self.customerCitylbl = QtWidgets.QLineEdit(createNewMaintenanceForExistsCustDialog)
        self.customerCitylbl.setEnabled(False)
        self.customerCitylbl.setGeometry(QtCore.QRect(628, 126, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.customerCitylbl.setFont(font)
        self.customerCitylbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.customerCitylbl.setObjectName("customerCitylbl")
        self.label_6 = QtWidgets.QLabel(createNewMaintenanceForExistsCustDialog)
        self.label_6.setGeometry(QtCore.QRect(550, 129, 130, 13))
        self.label_6.setObjectName("label_6")
        self.line_4 = QtWidgets.QFrame(createNewMaintenanceForExistsCustDialog)
        self.line_4.setGeometry(QtCore.QRect(379, 157, 340, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.createbtn = QtWidgets.QPushButton(createNewMaintenanceForExistsCustDialog)
        self.createbtn.setGeometry(QtCore.QRect(400, 170, 140, 40))
        self.createbtn.setObjectName("createbtn")
        self.closebtn = QtWidgets.QPushButton(createNewMaintenanceForExistsCustDialog)
        self.closebtn.setGeometry(QtCore.QRect(631, 411, 90, 40))
        self.closebtn.setObjectName("closebtn")
        self.line_5 = QtWidgets.QFrame(createNewMaintenanceForExistsCustDialog)
        self.line_5.setGeometry(QtCore.QRect(381, 397, 340, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.createbtn.setEnabled(False)
        self.createbtn.clicked.connect(self.do_maint)
        self.retranslateUi(createNewMaintenanceForExistsCustDialog)
        QtCore.QMetaObject.connectSlotsByName(createNewMaintenanceForExistsCustDialog)

    def retranslateUi(self, createNewMaintenanceForExistsCustDialog):
        _translate = QtCore.QCoreApplication.translate
        createNewMaintenanceForExistsCustDialog.setWindowTitle(_translate("createNewMaintenanceForExistsCustDialog", "Create New Maintenance For Exsist Customer"))
        self.label.setText(_translate("createNewMaintenanceForExistsCustDialog", "Welcome, "))
        self.label_2.setText(_translate("createNewMaintenanceForExistsCustDialog", "Please Select One Customer :"))
        self.label_3.setText(_translate("createNewMaintenanceForExistsCustDialog", "Selected Customer Data :"))
        self.label_4.setText(_translate("createNewMaintenanceForExistsCustDialog", "Customer Mobile Phone :"))
        self.label_12.setText(_translate("createNewMaintenanceForExistsCustDialog", "Customer Name :"))
        self.label_5.setText(_translate("createNewMaintenanceForExistsCustDialog", "Customer Age :"))
        self.label_6.setText(_translate("createNewMaintenanceForExistsCustDialog", "Customer City :"))
        self.createbtn.setText(_translate("createNewMaintenanceForExistsCustDialog", "Create New Maintenance"))
        self.closebtn.setText(_translate("createNewMaintenanceForExistsCustDialog", "Close"))


    def Clicked(self, item):
        indexes = self.tableView.selectionModel().selectedRows(1)
        for ind in sorted(indexes):
            cst = select_customer_by_mob_num(ind.data())
            self.customerNamelbl.setText(cst.name)
            self.customerMobilelbl.setText(cst.mobile_number)
            self.customerAgelbl.setText(str(cst.age))
            cty = select_city_by_id(cst.city_id)
            self.customerCitylbl.setText(cty.name)
            self.createbtn.setEnabled(True)

    def do_maint(self):
        indexes = self.tableView.selectionModel().selectedRows(1)
        for ind in sorted(indexes):
            cst = select_customer_by_mob_num(ind.data())
            maint = creatMaintenanceExtCustomer(cst)
            from uiview.ui_createBOM import Ui_createBOMDialog
            self.cbom = Ui_createBOMDialog(maint)
            self.cbom.exec_()

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = Ui_createNewMaintenanceForExistsCustDialog()
	window.show()
	sys.exit(app.exec_())
