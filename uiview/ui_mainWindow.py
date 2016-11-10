# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from Control.userControl import getLoginDataPKL, deleteLoginDataPKL


class Ui_MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(Ui_MainWindow, self).__init__()
		self.setupUi(self)

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(787, 609)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
		MainWindow.setSizePolicy(sizePolicy)
		MainWindow.setMinimumSize(QtCore.QSize(787, 609))
		MainWindow.setMaximumSize(QtCore.QSize(787, 609))
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(10, 0, 51, 41))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(10, 50, 182, 13))
		self.label_2.setObjectName("label_2")
		self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
		self.tableWidget.setGeometry(QtCore.QRect(10, 70, 351, 481))
		self.tableWidget.setLineWidth(1)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setColumnCount(2)
		self.tableWidget.setRowCount(0)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, item)
		self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
		self.tableWidget.horizontalHeader().setDefaultSectionSize(174)
		self.line = QtWidgets.QFrame(self.centralwidget)
		self.line.setGeometry(QtCore.QRect(10, 30, 771, 16))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.line_2 = QtWidgets.QFrame(self.centralwidget)
		self.line_2.setGeometry(QtCore.QRect(370, 50, 20, 511))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(400, 50, 134, 13))
		self.label_3.setObjectName("label_3")
		self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
		self.tableWidget_2.setGeometry(QtCore.QRect(400, 70, 371, 481))
		self.tableWidget_2.setObjectName("tableWidget_2")
		self.tableWidget_2.setColumnCount(2)
		self.tableWidget_2.setRowCount(0)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_2.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget_2.setHorizontalHeaderItem(1, item)
		self.tableWidget_2.horizontalHeader().setDefaultSectionSize(184)
		self.loggedUserName = QtWidgets.QLabel(self.centralwidget)
		self.loggedUserName.setGeometry(QtCore.QRect(60, 0, 171, 41))

		self.loggedUserName.setText(getLoginDataPKL()['name'])

		self.loggedUserName.setObjectName("loggedUserName")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 21))
		self.menubar.setObjectName("menubar")
		self.menuFile = QtWidgets.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		self.menuCustomer = QtWidgets.QMenu(self.menubar)
		self.menuCustomer.setObjectName("menuCustomer")
		self.menuMaintenance = QtWidgets.QMenu(self.menubar)
		self.menuMaintenance.setObjectName("menuMaintenance")
		self.menuRaw_Material = QtWidgets.QMenu(self.menubar)
		self.menuRaw_Material.setObjectName("menuRaw_Material")
		self.menuSpare_Parts = QtWidgets.QMenu(self.menubar)
		self.menuSpare_Parts.setObjectName("menuSpare_Parts")
		self.menuAccounting = QtWidgets.QMenu(self.menubar)
		self.menuAccounting.setObjectName("menuAccounting")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.actionLogout = QtWidgets.QAction(MainWindow)
		self.actionLogout.setObjectName("actionLogout")

		self.actionLogout.triggered.connect(self.doLogout)

		self.actionChange_Password = QtWidgets.QAction(MainWindow)
		self.actionChange_Password.setObjectName("actionChange_Password")

		self.actionChange_Password.triggered.connect(self.openChangePasswordDialog)

		self.actionExit = QtWidgets.QAction(MainWindow)
		self.actionExit.setObjectName("actionExit")

		self.actionExit.triggered.connect(self.doExit)

		self.actionAdd_New = QtWidgets.QAction(MainWindow)
		self.actionAdd_New.setObjectName("actionAdd_New")

		self.actionAdd_New.triggered.connect(self.openCreateNewCustomerDialog)

		self.actionEdit = QtWidgets.QAction(MainWindow)
		self.actionEdit.setObjectName("actionEdit")

		self.actionEdit.triggered.connect(self.openEditCustomerDialog)

		self.actionSearch = QtWidgets.QAction(MainWindow)
		self.actionSearch.setObjectName("actionSearch")

		self.actionSearch.triggered.connect(self.openSearchCustomerDialog)

		self.actionRports = QtWidgets.QAction(MainWindow)
		self.actionRports.setObjectName("actionRports")
		self.actionAdd_New_2 = QtWidgets.QAction(MainWindow)
		self.actionAdd_New_2.setObjectName("actionAdd_New_2")
		self.actionEdit_2 = QtWidgets.QAction(MainWindow)
		self.actionEdit_2.setObjectName("actionEdit_2")
		self.actionSearch_2 = QtWidgets.QAction(MainWindow)
		self.actionSearch_2.setObjectName("actionSearch_2")
		self.actionReports = QtWidgets.QAction(MainWindow)
		self.actionReports.setObjectName("actionReports")
		self.actionAdd_New_3 = QtWidgets.QAction(MainWindow)
		self.actionAdd_New_3.setObjectName("actionAdd_New_3")
		self.actionEdit_3 = QtWidgets.QAction(MainWindow)
		self.actionEdit_3.setObjectName("actionEdit_3")
		self.actionSearch_3 = QtWidgets.QAction(MainWindow)
		self.actionSearch_3.setObjectName("actionSearch_3")
		self.actionReports_2 = QtWidgets.QAction(MainWindow)
		self.actionReports_2.setObjectName("actionReports_2")
		self.actionAdd_New_4 = QtWidgets.QAction(MainWindow)
		self.actionAdd_New_4.setObjectName("actionAdd_New_4")
		self.actionEdit_4 = QtWidgets.QAction(MainWindow)
		self.actionEdit_4.setObjectName("actionEdit_4")
		self.actionSearch_4 = QtWidgets.QAction(MainWindow)
		self.actionSearch_4.setObjectName("actionSearch_4")
		self.actionReports_3 = QtWidgets.QAction(MainWindow)
		self.actionReports_3.setObjectName("actionReports_3")
		self.menuFile.addAction(self.actionLogout)
		self.menuFile.addAction(self.actionChange_Password)
		self.menuFile.addAction(self.actionExit)
		self.menuCustomer.addAction(self.actionAdd_New)
		self.menuCustomer.addAction(self.actionEdit)
		self.menuCustomer.addAction(self.actionSearch)
		self.menuCustomer.addAction(self.actionRports)
		self.menuMaintenance.addAction(self.actionAdd_New_2)
		self.menuMaintenance.addAction(self.actionEdit_2)
		self.menuMaintenance.addAction(self.actionSearch_2)
		self.menuMaintenance.addAction(self.actionReports)
		self.menuRaw_Material.addAction(self.actionAdd_New_3)
		self.menuRaw_Material.addAction(self.actionEdit_3)
		self.menuRaw_Material.addAction(self.actionSearch_3)
		self.menuRaw_Material.addAction(self.actionReports_2)
		self.menuSpare_Parts.addAction(self.actionAdd_New_4)
		self.menuSpare_Parts.addAction(self.actionEdit_4)
		self.menuSpare_Parts.addAction(self.actionSearch_4)
		self.menuSpare_Parts.addAction(self.actionReports_3)
		self.menubar.addAction(self.menuFile.menuAction())
		self.menubar.addAction(self.menuCustomer.menuAction())
		self.menubar.addAction(self.menuMaintenance.menuAction())
		self.menubar.addAction(self.menuRaw_Material.menuAction())
		self.menubar.addAction(self.menuSpare_Parts.menuAction())
		self.menubar.addAction(self.menuAccounting.menuAction())

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow", "Welcome, "))
		self.label_2.setText(_translate("MainWindow", "Customers Not Have Maintenance yet"))
		item = self.tableWidget.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Customer Name"))
		item = self.tableWidget.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Add Date"))
		self.label_3.setText(_translate("MainWindow", "Maintenance Not Have BOM"))
		item = self.tableWidget_2.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Maintenance Code"))
		item = self.tableWidget_2.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Customer Name"))
		self.menuFile.setTitle(_translate("MainWindow", "File"))
		self.menuCustomer.setTitle(_translate("MainWindow", "Customer"))
		self.menuMaintenance.setTitle(_translate("MainWindow", "Maintenance"))
		self.menuRaw_Material.setTitle(_translate("MainWindow", "Raw Material"))
		self.menuSpare_Parts.setTitle(_translate("MainWindow", "Spare Parts"))
		self.menuAccounting.setTitle(_translate("MainWindow", "Accounting"))
		self.actionLogout.setText(_translate("MainWindow", "Logout"))
		self.actionChange_Password.setText(_translate("MainWindow", "Change Password"))
		self.actionExit.setText(_translate("MainWindow", "Exit"))
		self.actionAdd_New.setText(_translate("MainWindow", "Add New"))
		self.actionEdit.setText(_translate("MainWindow", "Edit"))
		self.actionSearch.setText(_translate("MainWindow", "Search"))
		self.actionRports.setText(_translate("MainWindow", "Reports"))
		self.actionAdd_New_2.setText(_translate("MainWindow", "Add New"))
		self.actionEdit_2.setText(_translate("MainWindow", "Edit"))
		self.actionSearch_2.setText(_translate("MainWindow", "Search"))
		self.actionReports.setText(_translate("MainWindow", "Reports"))
		self.actionAdd_New_3.setText(_translate("MainWindow", "Add New"))
		self.actionEdit_3.setText(_translate("MainWindow", "Edit"))
		self.actionSearch_3.setText(_translate("MainWindow", "Search"))
		self.actionReports_2.setText(_translate("MainWindow", "Reports"))
		self.actionAdd_New_4.setText(_translate("MainWindow", "Add New"))
		self.actionEdit_4.setText(_translate("MainWindow", "Edit"))
		self.actionSearch_4.setText(_translate("MainWindow", "Search"))
		self.actionReports_3.setText(_translate("MainWindow", "Reports"))

	def doLogout(self):
		reply = QMessageBox.question(QMessageBox(), 'Logout', 'Are you sure to logout ?',
									 QMessageBox.Yes | QMessageBox.No)
		if reply == QMessageBox.Yes:
			from uiview.ui_loginDialog import Ui_loginDialog
			deleteLoginDataPKL()
			self.close()
			self.login_dialog = Ui_loginDialog()
			self.login_dialog.show()

	def doExit(self):
		reply = QMessageBox.question(QMessageBox(), 'Logout', 'Are you sure to quit ?',
									 QMessageBox.Yes | QMessageBox.No)
		if reply == QMessageBox.Yes:
			deleteLoginDataPKL()
			sys.exit()

	def openChangePasswordDialog(self):
		from uiview.ui_changePassword import Ui_changePasswordDilaod
		self.chPass_dialog = Ui_changePasswordDilaod()
		self.chPass_dialog.show()

	def openCreateNewCustomerDialog(self):
		from uiview.ui_createNewCustomer import Ui_createNewCustomer
		self.cnc_dialog = Ui_createNewCustomer()
		self.cnc_dialog.show()

	def openEditCustomerDialog(self):
		from uiview.ui_updateCustomer import Ui_updateCustomer
		self.upc_dialog = Ui_updateCustomer()
		self.upc_dialog.show()

	def openSearchCustomerDialog(self):
		from uiview.ui_deleteCustomer import Ui_deleteCustomer
		self.cnc_dialog = Ui_deleteCustomer()
		self.cnc_dialog.show()


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = Ui_MainWindow()
	window.show()
	sys.exit(app.exec_())