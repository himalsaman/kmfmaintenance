# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_reporting.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

from Control.maintenanceLogic import getMaintenanceWaitingDelevary, getMaintenanceBTWDate
from Control.userControl import getLoginDataPKL
from models.customersModel import select_customer, select_customer_exact
from reports.allcustoms import CreateAllCustomsReport
from reports.allrawmaterial import CreateAllRMReport
from reports.allspareparts import CreateAllSPReport
from reports.mainAmounted import CreateMaintAmountdReport
from reports.mainBTWDates import CreateMainBTWDatesReport
from reports.mainFinish import CreateMaintFinishReport
from reports.mainFinishWitDelv import CreateMaintFinishWaitDelvReport
from reports.mainUnderProc import CreateMaintUnderProcReport
from reports.mainWaitCustConf import CreateWaitCustConfReport
from reports.mainWaitLaborCost import CreateMainWaitLaborCostReport
from reports.maintOfCust import CreateMaintOfCustReport


class Ui_reportDialog(QDialog):
    def __init__(self):
        super(Ui_reportDialog, self).__init__()
        self.setupUi(self)
    def setupUi(self, reportDialog):
        reportDialog.setObjectName("reportDialog")
        reportDialog.resize(282, 75)

        self.label = QtWidgets.QLabel(reportDialog)
        self.label.setGeometry(QtCore.QRect(8, 4, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(reportDialog)
        self.label_2.setGeometry(QtCore.QRect(60, 5, 200, 13))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(reportDialog)
        self.line.setGeometry(QtCore.QRect(5, 23, 270, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.methodcomboBox = QtWidgets.QComboBox(reportDialog)
        self.methodcomboBox.setGeometry(QtCore.QRect(5, 50, 270, 22))
        self.methodcomboBox.setObjectName("methodcomboBox")
        self.methodcomboBox.addItem("")
        self.methodcomboBox.setItemText(0, "")
        self.methodcomboBox.addItem("")
        self.methodcomboBox.setItemText(1, "Maintenance\'s For Customer")
        self.methodcomboBox.addItem("")
        self.methodcomboBox.setItemText(2, "Maintenance\'s By Status")
        self.methodcomboBox.addItem("")
        self.methodcomboBox.setItemText(3, "Maintenance\'s Amounted")
        self.methodcomboBox.addItem("")
        self.methodcomboBox.setItemText(4, "Maintenance\'s By Date")
        self.methodcomboBox.addItem("")
        self.methodcomboBox.setItemText(5, "Row Material")
        self.methodcomboBox.addItem("")
        self.methodcomboBox.setItemText(6, "Spare Parts")
        self.methodcomboBox.addItem("")
        self.methodcomboBox.setItemText(7, "Customers")

        self.label_3 = QtWidgets.QLabel(reportDialog)
        self.label_3.setGeometry(QtCore.QRect(8, 26, 150, 13))
        self.label_3.setObjectName("label_3")

        # reports for maintenance by customer
        # (search)
        self.custsearchgbox = QtWidgets.QGroupBox(reportDialog)
        # self.custsearchgbox.setGeometry(QtCore.QRect(5, 75, 270, 120))
        self.custsearchgbox.setObjectName("custsearchgbox")
        self.custNamerbtn = QtWidgets.QRadioButton(self.custsearchgbox)
        self.custNamerbtn.setGeometry(QtCore.QRect(36, 20, 50, 17))
        self.custNamerbtn.setObjectName("custNamerbtn")
        self.custMobNumrbtn = QtWidgets.QRadioButton(self.custsearchgbox)
        self.custMobNumrbtn.setGeometry(QtCore.QRect(100, 20, 120, 17))
        self.custMobNumrbtn.setObjectName("custMobNumrbtn")
        self.line_2 = QtWidgets.QFrame(self.custsearchgbox)
        self.line_2.setGeometry(QtCore.QRect(5, 75, 260, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.custsearchled = QtWidgets.QLineEdit(self.custsearchgbox)
        self.custsearchled.setGeometry(QtCore.QRect(3, 44, 190, 20))
        self.custsearchled.setObjectName("custsearchled")
        self.custsearchbtn = QtWidgets.QPushButton(self.custsearchgbox)
        self.custsearchbtn.setGeometry(QtCore.QRect(196, 40, 60, 30))
        self.custsearchbtn.setObjectName("custsearchbtn")
        self.line_3 = QtWidgets.QFrame(self.custsearchgbox)
        self.line_3.setGeometry(QtCore.QRect(5, 110, 260, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.custstatuclbl = QtWidgets.QLabel(self.custsearchgbox)
        self.custstatuclbl.setGeometry(QtCore.QRect(5, 78, 260, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.custstatuclbl.setFont(font)
        self.custstatuclbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.custstatuclbl.setText("")
        self.custstatuclbl.setAlignment(QtCore.Qt.AlignCenter)
        self.custstatuclbl.setObjectName("custstatuclbl")

        # (result)
        self.custSreachResultgbox = QtWidgets.QGroupBox(reportDialog)
        # self.custSreachResultgbox.setGeometry(QtCore.QRect(5, 195, 270, 101))
        self.custSreachResultgbox.setTitle("")
        self.custSreachResultgbox.setFlat(False)
        self.custSreachResultgbox.setObjectName("custSreachResultgbox")
        self.label_5 = QtWidgets.QLabel(self.custSreachResultgbox)
        self.label_5.setGeometry(QtCore.QRect(5, 7, 30, 13))
        self.label_5.setObjectName("label_5")
        self.custnamelbl = QtWidgets.QLineEdit(self.custSreachResultgbox)
        self.custnamelbl.setEnabled(False)
        self.custnamelbl.setGeometry(QtCore.QRect(39, 5, 220, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.custnamelbl.setFont(font)
        self.custnamelbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.custnamelbl.setObjectName("custnamelbl")
        self.label_6 = QtWidgets.QLabel(self.custSreachResultgbox)
        self.label_6.setGeometry(QtCore.QRect(5, 30, 47, 13))
        self.label_6.setObjectName("label_6")
        self.custmobnumlbl = QtWidgets.QLineEdit(self.custSreachResultgbox)
        self.custmobnumlbl.setEnabled(False)
        self.custmobnumlbl.setGeometry(QtCore.QRect(53, 28, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.custmobnumlbl.setFont(font)
        self.custmobnumlbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.custmobnumlbl.setObjectName("custmobnumlbl")
        self.custagelbl = QtWidgets.QLineEdit(self.custSreachResultgbox)
        self.custagelbl.setEnabled(False)
        self.custagelbl.setGeometry(QtCore.QRect(32, 51, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.custagelbl.setFont(font)
        self.custagelbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.custagelbl.setObjectName("custagelbl")
        self.label_7 = QtWidgets.QLabel(self.custSreachResultgbox)
        self.label_7.setGeometry(QtCore.QRect(6, 54, 30, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.custSreachResultgbox)
        self.label_8.setGeometry(QtCore.QRect(5, 78, 30, 13))
        self.label_8.setObjectName("label_8")
        self.custcitylbl = QtWidgets.QLineEdit(self.custSreachResultgbox)
        self.custcitylbl.setEnabled(False)
        self.custcitylbl.setGeometry(QtCore.QRect(30, 75, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.custcitylbl.setFont(font)
        self.custcitylbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.custcitylbl.setObjectName("custcitylbl")





        # report by maintenance status
        self.maintStatusgbox = QtWidgets.QGroupBox(reportDialog)
        # self.maintStatusgbox.setGeometry(QtCore.QRect(288, 3, 270, 140))
        self.maintStatusgbox.setObjectName("maintStatusgbox")
        self.waitingLaborCostrbtn = QtWidgets.QRadioButton(self.maintStatusgbox)
        self.waitingLaborCostrbtn.setGeometry(QtCore.QRect(10, 20, 120, 17))
        self.waitingLaborCostrbtn.setObjectName("waitingLaborCostrbtn")
        self.watingCustomerConfirmrbtn = QtWidgets.QRadioButton(self.maintStatusgbox)
        self.watingCustomerConfirmrbtn.setGeometry(QtCore.QRect(10, 40, 170, 17))
        self.watingCustomerConfirmrbtn.setObjectName("watingCustomerConfirmrbtn")
        self.underProcessingrbtn = QtWidgets.QRadioButton(self.maintStatusgbox)
        self.underProcessingrbtn.setGeometry(QtCore.QRect(130, 20, 110, 17))
        self.underProcessingrbtn.setObjectName("underProcessingrbtn")
        self.finishandwaitdelrbtn = QtWidgets.QRadioButton(self.maintStatusgbox)
        self.finishandwaitdelrbtn.setGeometry(QtCore.QRect(10, 60, 150, 17))
        self.finishandwaitdelrbtn.setObjectName("finishandwaitdelrbtn")
        self.finishrbtn = QtWidgets.QRadioButton(self.maintStatusgbox)
        self.finishrbtn.setGeometry(QtCore.QRect(10, 80, 82, 17))
        self.finishrbtn.setObjectName("finishrbtn")
        self.line_5 = QtWidgets.QFrame(self.maintStatusgbox)
        self.line_5.setGeometry(QtCore.QRect(5, 100, 260, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.maintstatuslbl = QtWidgets.QLabel(self.maintStatusgbox)
        self.maintstatuslbl.setGeometry(QtCore.QRect(4, 105, 260, 20))
        self.maintstatuslbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.maintstatuslbl.setText("")
        self.maintstatuslbl.setAlignment(QtCore.Qt.AlignCenter)
        self.maintstatuslbl.setObjectName("maintstatuslbl")
        self.line_6 = QtWidgets.QFrame(self.maintStatusgbox)
        self.line_6.setGeometry(QtCore.QRect(5, 130, 260, 3))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")


        #report by date
        self.dategbox = QtWidgets.QGroupBox(reportDialog)
        # self.dategbox.setGeometry(QtCore.QRect(288, 143, 270, 80))
        self.dategbox.setObjectName("dategbox")
        self.label_4 = QtWidgets.QLabel(self.dategbox)
        self.label_4.setGeometry(QtCore.QRect(6, 23, 40, 13))
        self.label_4.setObjectName("label_4")
        self.fromdateEdit = QtWidgets.QDateEdit(self.dategbox)
        self.fromdateEdit.setGeometry(QtCore.QRect(39, 19, 110, 22))
        self.fromdateEdit.setObjectName("fromdateEdit")
        self.label_9 = QtWidgets.QLabel(self.dategbox)
        self.label_9.setGeometry(QtCore.QRect(6, 48, 40, 13))
        self.label_9.setObjectName("label_9")
        self.todateEdit = QtWidgets.QDateEdit(self.dategbox)
        self.todateEdit.setGeometry(QtCore.QRect(39, 44, 110, 22))
        self.todateEdit.setObjectName("todateEdit")


        # report Action buton and line
        self.repotbtn = QtWidgets.QPushButton(reportDialog)
        self.repotbtn.setObjectName("repotbtn")
        self.repoline = QtWidgets.QFrame(reportDialog)
        self.repoline.setFrameShape(QtWidgets.QFrame.HLine)
        self.repoline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.repoline.setObjectName("repoline")
        self.line_4 = QtWidgets.QFrame(reportDialog)
        self.line_4.setGeometry(QtCore.QRect(282, 5, 3, 350))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.custsearchgbox.setVisible(False)
        self.custSreachResultgbox.setVisible(False)
        self.maintStatusgbox.setVisible(False)
        self.repoline.setVisible(False)
        self.repotbtn.setVisible(False)
        self.dategbox.setVisible(False)


        #role
        role = getLoginDataPKL()['role']
        if int(role) == 2 :
            self.methodcomboBox.model().item(1).setEnabled(False)
            self.methodcomboBox.model().item(2).setEnabled(False)
            self.methodcomboBox.model().item(3).setEnabled(False)
            self.methodcomboBox.model().item(4).setEnabled(False)
            self.methodcomboBox.model().item(5).setEnabled(False)
            self.methodcomboBox.model().item(6).setEnabled(False)
            self.methodcomboBox.model().item(7).setEnabled(False)


        if int(role) == 3:
            self.methodcomboBox.model().item(1).setEnabled(False)
            self.methodcomboBox.model().item(3).setEnabled(False)
            self.methodcomboBox.model().item(4).setEnabled(False)

            self.finishandwaitdelrbtn.setEnabled(False)
            self.finishrbtn.setEnabled(False)
            self.waitingLaborCostrbtn.setEnabled(False)
            self.watingCustomerConfirmrbtn.setEnabled(False)

        self.retranslateUi(reportDialog)
        QtCore.QMetaObject.connectSlotsByName(reportDialog)

        self.methodcomboBox.currentIndexChanged.connect(self.setGromity)



    def retranslateUi(self, reportDialog):
        _translate = QtCore.QCoreApplication.translate
        reportDialog.setWindowTitle(_translate("reportDialog", "Reporting"))
        self.label.setText(_translate("reportDialog", "Welcome,"))
        self.label_3.setText(_translate("reportDialog", "Please Select Report Method:"))
        self.custsearchgbox.setTitle(_translate("reportDialog", "Select method of customer search"))
        self.custNamerbtn.setText(_translate("reportDialog", "Name"))
        self.custMobNumrbtn.setText(_translate("reportDialog", "Main Mobile Number"))
        self.custsearchbtn.setText(_translate("reportDialog", "Search"))
        self.label_5.setText(_translate("reportDialog", "Name:"))
        self.label_6.setText(_translate("reportDialog", "Mobile #:"))
        self.label_7.setText(_translate("reportDialog", "Age:"))
        self.label_8.setText(_translate("reportDialog", "City:"))
        self.repotbtn.setText(_translate("reportDialog", "Report"))
        self.maintStatusgbox.setTitle(_translate("reportDialog", "Select Maintenance Status"))
        self.waitingLaborCostrbtn.setText(_translate("reportDialog", "Waiting Labor Cost"))
        self.watingCustomerConfirmrbtn.setText(_translate("reportDialog", "Waiting Customer Confirmation"))
        self.underProcessingrbtn.setText(_translate("reportDialog", "Under Processing"))
        self.finishandwaitdelrbtn.setText(_translate("reportDialog", "Finish and Waiting Delivery"))
        self.finishrbtn.setText(_translate("reportDialog", "Finished"))
        self.dategbox.setTitle(_translate("reportDialog", "Enter From - To Date"))
        self.label_4.setText(_translate("reportDialog", "From :"))
        self.label_9.setText(_translate("reportDialog", "To :"))

    def setGromity(self):
        if self.methodcomboBox.currentIndex() == 1:
            self.resize(282, 359)
            self.repoline.setGeometry(QtCore.QRect(4, 300, 270, 3))
            self.repotbtn.setGeometry(QtCore.QRect(96, 305, 80, 40))
            self.repoline.setVisible(True)
            self.repotbtn.setVisible(True)
            self.maintStatusgbox.setVisible(False)
            self.dategbox.setVisible(False)
            self.custsearchgbox.setGeometry(QtCore.QRect(5, 75, 270, 120))
            self.custsearchgbox.setVisible(True)
            self.custsearchbtn.clicked.connect(self.customerHandel)
            self.repotbtn.clicked.connect(self.openMaintenanceByCustomerReport)

        if self.methodcomboBox.currentIndex() == 2:
            self.resize(282, 260)
            self.repoline.setGeometry(QtCore.QRect(4, 30, 270, 3))
            self.repotbtn.setGeometry(QtCore.QRect(96, 215, 80, 40))
            self.repoline.setVisible(False)
            self.repotbtn.setVisible(True)
            self.custsearchgbox.setVisible(False)
            self.custSreachResultgbox.setVisible(False)
            self.maintStatusgbox.setVisible(True)
            self.maintStatusgbox.setGeometry(QtCore.QRect(5, 77, 270, 180))
            self.repotbtn.clicked.connect(self.maintStatusHandel)

        if self.methodcomboBox.currentIndex() == 3:
            self.resize(282, 75)
            self.repoline.setVisible(False)
            self.repotbtn.setVisible(False)
            self.maintStatusgbox.setVisible(False)
            self.dategbox.setVisible(False)
            self.openMaintAmountedReport()

        if self.methodcomboBox.currentIndex() == 4:
            self.resize(282, 215)
            self.repoline.setVisible(True)
            self.repotbtn.setVisible(True)
            self.repoline.setGeometry(QtCore.QRect(4, 165, 270, 3))
            self.repotbtn.setGeometry(QtCore.QRect(96, 170, 80, 40))
            self.maintStatusgbox.setVisible(False)
            self.dategbox.setVisible(True)
            self.fromdateEdit.setDateTime(datetime.now())
            self.todateEdit.setDateTime(datetime.now())
            self.dategbox.setGeometry(QtCore.QRect(6, 75, 270, 80))
            self.repotbtn.clicked.connect(self.dateHandel)

        if self.methodcomboBox.currentIndex() == 5:
            self.resize(282, 75)
            self.repoline.setVisible(False)
            self.repotbtn.setVisible(False)
            self.maintStatusgbox.setVisible(False)
            self.dategbox.setVisible(False)
            CreateAllRMReport().create_pdf()

        if self.methodcomboBox.currentIndex() == 6:
            self.resize(282, 75)
            self.repoline.setVisible(False)
            self.repotbtn.setVisible(False)
            self.maintStatusgbox.setVisible(False)
            self.dategbox.setVisible(False)
            CreateAllSPReport().create_pdf()

        if self.methodcomboBox.currentIndex() == 7:
            self.resize(282, 75)
            self.repoline.setVisible(False)
            self.repotbtn.setVisible(False)
            self.maintStatusgbox.setVisible(False)
            self.dategbox.setVisible(False)
            CreateAllCustomsReport().create_pdf()


    def customerHandel(self):
        if self.custNamerbtn.isChecked():
            key = "name"
            self.custstatuclbl.setText('')
        elif self.custMobNumrbtn.isChecked():
            key = "mobile_number"
            self.custstatuclbl.setText('')
        else:
            self.custstatuclbl.setText('Please Select Search Method')
        if self.custsearchled.text() != '':
            value = self.custsearchled.text()
            if select_customer_exact(key, value):
                cust = select_customer_exact(key, value)
                self.custSreachResultgbox.setGeometry(QtCore.QRect(5, 196, 270, 161))
                self.custSreachResultgbox.setVisible(True)
                self.custnamelbl.setText(cust.name)
                self.custmobnumlbl.setText(cust.mobile_number)
                self.custagelbl.setText(str(cust.age))
                self.custcitylbl.setText(cust.city.name)
                return cust
            else:
                self.custstatuclbl.setText('No search Result')
        else:
            self.custstatuclbl.setText('Enter Search Keyword')

    def maintStatusHandel(self):
        if not self.finishandwaitdelrbtn.isChecked()\
            and not self.finishrbtn.isChecked()\
            and not self.underProcessingrbtn.isChecked()\
            and not self.waitingLaborCostrbtn.isChecked()\
            and not self.watingCustomerConfirmrbtn.isChecked():
            self.maintstatuslbl.setText("You Must Select One Status")
        if self.finishandwaitdelrbtn.isChecked():
            self.openMaintFinishWaitDelvReport()
        if self.waitingLaborCostrbtn.isChecked():
            self.openMainWaitLaborCostReport()
        if self.underProcessingrbtn.isChecked():
            self.openMaintUnderProcReport()
        if self.watingCustomerConfirmrbtn.isChecked():
            self.openWaitCustConfReport()
        if self.finishrbtn.isChecked():
            self.openMaintFinishedReport()

    def dateHandel(self):
        if not self.fromdateEdit.dateTime() == None or not self.todateEdit.dateTime() == None:
            fromdate = self.fromdateEdit.dateTime()
            toDate = self.todateEdit.dateTime()
            CreateMainBTWDatesReport(fromdate.toPyDateTime(), toDate.toPyDateTime()).create_pdf()
            # '%Y-%m-%d %H:%M:%S'
            # print(fromdate.toPyDateTime())
            # print(toDate.toPyDateTime())
            # print(getMaintenanceBTWDate(fromdate.toPyDateTime(), toDate.toPyDateTime()))


    def openMaintenanceByCustomerReport(self):
        CreateMaintOfCustReport(self.customerHandel()).create_pdf()

    def openMaintFinishWaitDelvReport(self):
        CreateMaintFinishWaitDelvReport().create_pdf()

    def openMainWaitLaborCostReport(self):
        CreateMainWaitLaborCostReport().create_pdf()

    def openMaintUnderProcReport(self):
        CreateMaintUnderProcReport().create_pdf()

    def openWaitCustConfReport(self):
        CreateWaitCustConfReport().create_pdf()

    def openMaintFinishedReport(self):
        CreateMaintFinishReport().create_pdf()

    def openMaintAmountedReport(self):
        CreateMaintAmountdReport().create_pdf()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_reportDialog()
    myapp.show()
    sys.exit(app.exec_())
