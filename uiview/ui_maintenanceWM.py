# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_maintenanceWM.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from Control.maintenanceLogic import getAllMaintenanceNotCreated
from models.customersModel import select_customer_by_id, select_customer_by_mob_num
from models.dbUtile import Customers
from uiview.ui_createNewCustomerWithMaintenance import Ui_createNewCustomerWithMaintenance
from uiview.uimodels.customerTableModel import CustomerTableModel


class Ui_maintenanceMW(QMainWindow):
    def __init__(self):
        super(Ui_maintenanceMW, self).__init__()
        self.setupUi(self)

    def setupUi(self, maintenanceMW):
        maintenanceMW.setObjectName("maintenanceMW")
        maintenanceMW.resize(695, 633)
        self.centralwidget = QtWidgets.QWidget(maintenanceMW)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.label.setObjectName("label")
        self.loggedUserlbl = QtWidgets.QLabel(self.centralwidget)
        self.loggedUserlbl.setGeometry(QtCore.QRect(62, 11, 150, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.loggedUserlbl.setFont(font)
        self.loggedUserlbl.setText("")
        self.loggedUserlbl.setObjectName("loggedUserlbl")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 33, 680, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 45, 140, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(360, 50, 3, 560))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(370, 163, 311, 110))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 23, 47, 13))
        self.label_5.setObjectName("label_5")
        self.cusNamelbl = QtWidgets.QLineEdit(self.groupBox_2)
        self.cusNamelbl.setEnabled(False)
        self.cusNamelbl.setGeometry(QtCore.QRect(46, 21, 250, 20))
        self.cusNamelbl.setObjectName("cusNamelbl")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 52, 80, 13))
        self.label_6.setObjectName("label_6")
        self.custMobled = QtWidgets.QLineEdit(self.groupBox_2)
        self.custMobled.setEnabled(False)
        self.custMobled.setGeometry(QtCore.QRect(90, 49, 201, 20))
        self.custMobled.setObjectName("custMobled")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 80, 13))
        self.label_7.setObjectName("label_7")
        self.custGendled = QtWidgets.QLineEdit(self.groupBox_2)
        self.custGendled.setEnabled(False)
        self.custGendled.setGeometry(QtCore.QRect(55, 77, 100, 20))
        self.custGendled.setObjectName("custGendled")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(164, 81, 80, 13))
        self.label_8.setObjectName("label_8")
        self.custCityled = QtWidgets.QLineEdit(self.groupBox_2)
        self.custCityled.setEnabled(False)
        self.custCityled.setGeometry(QtCore.QRect(194, 78, 100, 20))
        self.custCityled.setObjectName("custCityled")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(370, 283, 310, 80))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.editOneForSelectedCustbtn = QtWidgets.QPushButton(self.groupBox_3)
        self.editOneForSelectedCustbtn.setGeometry(QtCore.QRect(180, 9, 120, 60))
        self.editOneForSelectedCustbtn.setObjectName("editOneForSelectedCustbtn")
        self.createNewForSelectedCustbtn = QtWidgets.QPushButton(self.groupBox_3)
        self.createNewForSelectedCustbtn.setGeometry(QtCore.QRect(10, 9, 140, 60))
        self.createNewForSelectedCustbtn.setObjectName("createNewForSelectedCustbtn")
        self.statuslbl = QtWidgets.QLabel(self.centralwidget)
        self.statuslbl.setGeometry(QtCore.QRect(371, 367, 310, 50))
        self.statuslbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.statuslbl.setText("")
        self.statuslbl.setAlignment(QtCore.Qt.AlignCenter)
        self.statuslbl.setObjectName("statuslbl")
        self.createNewForNewCustbtn = QtWidgets.QPushButton(self.centralwidget)
        self.createNewForNewCustbtn.setGeometry(QtCore.QRect(425, 67, 200, 60))
        self.createNewForNewCustbtn.setObjectName("createNewForNewCustbtn")
        self.createNewForNewCustbtn.clicked.connect(self.do_addNewCustomerAndMaintenanceAction)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(9, 75, 341, 520))
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setTabKeyNavigation(False)
        self.tableView.setProperty("showDropIndicator", False)
        self.tableView.setDragDropOverwriteMode(False)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableData = CustomerTableModel()
        self.tableView.setModel(self.tableData)
        self.tableView.setColumnWidth(0,220)
        self.tableView.setColumnWidth(1, 97)

        for idx, val in enumerate(getAllMaintenanceNotCreated()):
            self.tableData.addCustomer(Customers(getAllMaintenanceNotCreated()[idx].name
                                                 , getAllMaintenanceNotCreated()[idx].mobile_number
                                                 , None, None, None))

        self.tableView.clicked.connect(self.Clicked)

        maintenanceMW.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(maintenanceMW)
        self.statusbar.setObjectName("statusbar")
        maintenanceMW.setStatusBar(self.statusbar)

        self.retranslateUi(maintenanceMW)
        QtCore.QMetaObject.connectSlotsByName(maintenanceMW)

    def retranslateUi(self, maintenanceMW):
        _translate = QtCore.QCoreApplication.translate
        maintenanceMW.setWindowTitle(_translate("maintenanceMW", "Maintenance"))
        self.label.setText(_translate("maintenanceMW", "Welcome,"))
        self.label_4.setText(_translate("maintenanceMW", "Select Customer from table"))
        self.groupBox_2.setTitle(_translate("maintenanceMW", "Selected Customer Information"))
        self.label_5.setText(_translate("maintenanceMW", "Name :"))
        self.label_6.setText(_translate("maintenanceMW", "Mobile Number :"))
        self.label_7.setText(_translate("maintenanceMW", "Gender :"))
        self.label_8.setText(_translate("maintenanceMW", "City :"))
        self.editOneForSelectedCustbtn.setText(_translate("maintenanceMW", "Edit One \n"
" for selected customer"))
        self.createNewForSelectedCustbtn.setText(_translate("maintenanceMW", "Create New Maintenance \n"
" for selected customer"))
        self.createNewForNewCustbtn.setText(_translate("maintenanceMW", "Create New Maintenance \n"
" with new customer"))


    def Clicked(self, item):
        indexes = self.tableView.selectionModel().selectedRows(1)
        for ind in sorted(indexes):
            cust = select_customer_by_mob_num(ind.data())
            self.cusNamelbl.setText(cust.name)
            self.custMobled.setText(cust.mobile_number)
            self.custGendled.setText(cust.gender)
            self.custCityled.setText(cust.city.name)

    def do_addNewCustomerAndMaintenanceAction(self):
        self.target = Ui_createNewCustomerWithMaintenance()
        self.target.exec_()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    cnc_dialog = Ui_maintenanceMW()
    cnc_dialog.show()
    sys.exit(app.exec_())