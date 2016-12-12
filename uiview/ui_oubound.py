# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_oubound.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import datetime
import sys
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox

from Control.materialsControl import increaseToolsInvQty, increaseRawMaterialInvQty, increaseSparePartsInvQty, \
    increaseFinishProductInvQty
from Control.ouboundControl import getOutbounEmployeeRow, getOutbounCustomerRow, getOutbounOneCustomerRow
from models.cityModel import select_city_by_id
from models.customersModel import select_customer_key, select_customer_by_id, select_customer_by_mob_num
from models.dbUtile import Outbound, Customers, Employees
from models.employeeModel import select_employee, select_employee_by_id
from models.ouboundModel import select_outbound_by_code, delete_outbound, update_oubound_status
from models.toolsModel import select_tools_by_id
from reports.outboundCustReport import CreateOutboundCustReport
from reports.outboundReport import CreateOutboundReport
from uiview.uimodels.outboundModel import OutboundTableModel


class Ui_createOBDialog(QDialog):
    def __init__(self):
        super(Ui_createOBDialog, self).__init__()
        self.setupUi(self)
    def setupUi(self, createOBDialog):
        createOBDialog.setObjectName("createOBDialog")
        createOBDialog.resize(858, 590)
        self.label = QtWidgets.QLabel(createOBDialog)
        self.label.setGeometry(QtCore.QRect(7, 3, 47, 20))
        self.label.setObjectName("label")
        self.loggedUserlbl = QtWidgets.QLabel(createOBDialog)
        self.loggedUserlbl.setGeometry(QtCore.QRect(58, 4, 180, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.loggedUserlbl.setFont(font)
        self.loggedUserlbl.setText("")
        self.loggedUserlbl.setObjectName("loggedUserlbl")
        self.line = QtWidgets.QFrame(createOBDialog)
        self.line.setGeometry(QtCore.QRect(3, 28, 850, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.bomgroupbox = QtWidgets.QGroupBox(createOBDialog)
        self.bomgroupbox.setEnabled(True)
        self.bomgroupbox.setGeometry(QtCore.QRect(350, 132, 501, 391))
        self.bomgroupbox.setTitle("")
        self.bomgroupbox.setObjectName("bomgroupbox")
        self.addNewRMbtn = QtWidgets.QPushButton(self.bomgroupbox)
        self.addNewRMbtn.setGeometry(QtCore.QRect(5, 14, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.addNewRMbtn.setFont(font)
        self.addNewRMbtn.setObjectName("addNewRMbtn")
        self.addNewSPbtn = QtWidgets.QPushButton(self.bomgroupbox)
        self.addNewSPbtn.setGeometry(QtCore.QRect(115, 14, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.addNewSPbtn.setFont(font)
        self.addNewSPbtn.setObjectName("addNewSPbtn")
        self.protableView = QtWidgets.QTableView(self.bomgroupbox)
        self.protableView.setGeometry(QtCore.QRect(5, 71, 491, 311))
        self.protableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.protableView.setTabKeyNavigation(False)
        self.protableView.setProperty("showDropIndicator", False)
        self.protableView.setDragDropOverwriteMode(False)
        self.protableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.protableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.protableView.setObjectName("protableView")

        # self.protableView.setModel(self.tableData)


        self.protableView.setColumnWidth(1, 150)
        self.protableView.setColumnWidth(2, 150)
        self.protableView.setColumnWidth(3, 90)
        self.protableView.setColumnWidth(4, 50)
        self.addNewTObtn = QtWidgets.QPushButton(self.bomgroupbox)
        self.addNewTObtn.setGeometry(QtCore.QRect(216, 14, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.addNewTObtn.setFont(font)
        self.addNewTObtn.setObjectName("addNewTObtn")
        self.addNewFPbtn = QtWidgets.QPushButton(self.bomgroupbox)
        self.addNewFPbtn.setGeometry(QtCore.QRect(296, 14, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.addNewFPbtn.setFont(font)
        self.addNewFPbtn.setObjectName("addNewFPbtn")
        self.line_2 = QtWidgets.QFrame(self.bomgroupbox)
        self.line_2.setGeometry(QtCore.QRect(109, 20, 3, 30))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.bomgroupbox)
        self.line_4.setGeometry(QtCore.QRect(210, 20, 3, 30))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.bomgroupbox)
        self.line_5.setGeometry(QtCore.QRect(290, 20, 3, 30))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.refreshbtn = QtWidgets.QPushButton(self.bomgroupbox)
        self.refreshbtn.setGeometry(QtCore.QRect(425, 5, 70, 60))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.refreshbtn.setFont(font)
        self.refreshbtn.setStyleSheet("background-color: rgb(0, 108, 0);\n"
"color: rgb(255, 255, 255);")
        self.refreshbtn.setObjectName("refreshbtn")
        self.label_2 = QtWidgets.QLabel(createOBDialog)
        self.label_2.setGeometry(QtCore.QRect(392, 4, 30, 20))
        self.label_2.setObjectName("label_2")
        self.nowdatelbl = QtWidgets.QLabel(createOBDialog)
        self.nowdatelbl.setGeometry(QtCore.QRect(424, 4, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nowdatelbl.setFont(font)
        self.nowdatelbl.setText("")
        self.nowdatelbl.setObjectName("nowdatelbl")
        self.outboundnumlbl = QtWidgets.QLabel(createOBDialog)
        self.outboundnumlbl.setGeometry(QtCore.QRect(605, 4, 100, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.outboundnumlbl.setFont(font)
        self.outboundnumlbl.setText("")
        self.outboundnumlbl.setObjectName("outboundnumlbl")
        self.label_5 = QtWidgets.QLabel(createOBDialog)
        self.label_5.setGeometry(QtCore.QRect(539, 4, 70, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(createOBDialog)
        self.label_6.setGeometry(QtCore.QRect(708, 4, 40, 20))
        self.label_6.setObjectName("label_6")
        self.outboundstatuslbl = QtWidgets.QLabel(createOBDialog)
        self.outboundstatuslbl.setGeometry(QtCore.QRect(746, 4, 101, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.outboundstatuslbl.setFont(font)
        self.outboundstatuslbl.setText("")
        self.outboundstatuslbl.setObjectName("outboundstatuslbl")
        self.line_7 = QtWidgets.QFrame(createOBDialog)
        self.line_7.setGeometry(QtCore.QRect(3, 540, 850, 3))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.savebtn = QtWidgets.QPushButton(createOBDialog)
        self.savebtn.setGeometry(QtCore.QRect(350, 546, 90, 40))
        self.savebtn.setObjectName("savebtn")
        self.closebtn = QtWidgets.QPushButton(createOBDialog)
        self.closebtn.setGeometry(QtCore.QRect(450, 546, 90, 40))
        self.closebtn.setObjectName("closebtn")

        self.closeOutbtn = QtWidgets.QPushButton(createOBDialog)
        self.closeOutbtn.setGeometry(QtCore.QRect(750, 546, 90, 40))
        self.closeOutbtn.setObjectName("closebtn")

        self.searchresultgbox = QtWidgets.QGroupBox(createOBDialog)
        self.searchresultgbox.setGeometry(QtCore.QRect(350, 29, 401, 101))
        self.searchresultgbox.setObjectName("searchresultgbox")
        self.label_8 = QtWidgets.QLabel(self.searchresultgbox)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 47, 20))
        self.label_8.setObjectName("label_8")
        self.nameled = QtWidgets.QLineEdit(self.searchresultgbox)
        self.nameled.setEnabled(False)
        self.nameled.setGeometry(QtCore.QRect(48, 20, 230, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.nameled.setFont(font)
        self.nameled.setStyleSheet("color: rgb(255, 0, 0);")
        self.nameled.setObjectName("nameled")
        self.mobnumled = QtWidgets.QLineEdit(self.searchresultgbox)
        self.mobnumled.setEnabled(False)
        self.mobnumled.setGeometry(QtCore.QRect(61, 47, 170, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.mobnumled.setFont(font)
        self.mobnumled.setStyleSheet("color: rgb(255, 0, 0);")
        self.mobnumled.setObjectName("mobnumled")
        self.label_9 = QtWidgets.QLabel(self.searchresultgbox)
        self.label_9.setGeometry(QtCore.QRect(10, 46, 47, 20))
        self.label_9.setObjectName("label_9")
        self.cityled = QtWidgets.QLineEdit(self.searchresultgbox)
        self.cityled.setEnabled(False)
        self.cityled.setGeometry(QtCore.QRect(295, 50, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.cityled.setFont(font)
        self.cityled.setStyleSheet("color: rgb(255, 0, 0);")
        self.cityled.setObjectName("cityled")
        self.citylbl = QtWidgets.QLabel(self.searchresultgbox)
        self.citylbl.setGeometry(QtCore.QRect(241, 49, 61, 20))
        self.citylbl.setObjectName("citylbl")
        self.joblbl = QtWidgets.QLabel(self.searchresultgbox)
        self.joblbl.setGeometry(QtCore.QRect(11, 75, 30, 20))
        self.joblbl.setObjectName("joblbl")
        self.jobled = QtWidgets.QLineEdit(self.searchresultgbox)
        self.jobled.setEnabled(False)
        self.jobled.setGeometry(QtCore.QRect(44, 76, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.jobled.setFont(font)
        self.jobled.setStyleSheet("color: rgb(255, 0, 0);")
        self.jobled.setObjectName("jobled")
        self.ageled = QtWidgets.QLineEdit(self.searchresultgbox)
        self.ageled.setEnabled(False)
        self.ageled.setGeometry(QtCore.QRect(325, 20, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ageled.setFont(font)
        self.ageled.setStyleSheet("color: rgb(255, 0, 0);")
        self.ageled.setObjectName("ageled")
        self.label_12 = QtWidgets.QLabel(self.searchresultgbox)
        self.label_12.setGeometry(QtCore.QRect(296, 19, 30, 20))
        self.label_12.setObjectName("label_12")
        self.groupBox_2 = QtWidgets.QGroupBox(createOBDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(5, 30, 330, 70))
        self.groupBox_2.setObjectName("groupBox_2")
        self.reqTypecomboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.reqTypecomboBox.setGeometry(QtCore.QRect(7, 26, 210, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.reqTypecomboBox.setFont(font)
        self.reqTypecomboBox.setStyleSheet("color: rgb(255, 0, 0);")
        self.reqTypecomboBox.setObjectName("reqTypecomboBox")
        self.reqTypecomboBox.addItem("")
        self.reqTypecomboBox.setItemText(0, "")
        self.reqTypecomboBox.addItem("")
        self.reqTypecomboBox.addItem("")
        self.newCustbtn = QtWidgets.QPushButton(self.groupBox_2)
        self.newCustbtn.setGeometry(QtCore.QRect(234, 22, 90, 40))
        self.newCustbtn.setObjectName("newCustbtn")
        self.line_6 = QtWidgets.QFrame(createOBDialog)
        self.line_6.setGeometry(QtCore.QRect(342, 33, 3, 500))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_8 = QtWidgets.QFrame(createOBDialog)
        self.line_8.setGeometry(QtCore.QRect(5, 100, 330, 10))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.groupBox_3 = QtWidgets.QGroupBox(createOBDialog)
        self.groupBox_3.setGeometry(QtCore.QRect(5, 107, 330, 50))
        self.groupBox_3.setObjectName("groupBox_3")
        self.searchled = QtWidgets.QLineEdit(self.groupBox_3)
        self.searchled.setGeometry(QtCore.QRect(10, 20, 220, 21))
        self.searchled.setObjectName("searchled")
        self.searchbtn = QtWidgets.QPushButton(self.groupBox_3)
        self.searchbtn.setGeometry(QtCore.QRect(245, 15, 70, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.searchbtn.setFont(font)
        self.searchbtn.setObjectName("searchbtn")
        self.line_9 = QtWidgets.QFrame(createOBDialog)
        self.line_9.setGeometry(QtCore.QRect(4, 156, 330, 10))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.rqulistWidget = QtWidgets.QListWidget(createOBDialog)
        self.rqulistWidget.setGeometry(QtCore.QRect(5, 167, 330, 351))
        self.rqulistWidget.setObjectName("rqulistWidget")

        self.addNewRMbtn.setEnabled(False)
        self.addNewSPbtn.setEnabled(False)
        self.addNewTObtn.setEnabled(False)
        self.addNewFPbtn.setEnabled(False)
        self.nowdatelbl.setText(str(datetime.now().date()))


        self.refreshbtn.clicked.connect(self.refresheddata)
        self.searchbtn.clicked.connect(self.requTypeHandel)
        self.rqulistWidget.itemClicked.connect(self.Clicked)
        self.addNewRMbtn.clicked.connect(self.openRMDialog)
        self.addNewSPbtn.clicked.connect(self.openSPDialog)
        self.addNewTObtn.clicked.connect(self.openTODialog)
        self.addNewFPbtn.clicked.connect(self.openFPDialog)
        self.closeOutbtn.clicked.connect(self.openOutReport)
        self.closebtn.clicked.connect(self.close)
        self.closeOutbtn.setEnabled(False)
        self.refreshbtn.setEnabled(False)
        self.savebtn.setVisible(False)

        self.tableDataShow()
        self.newCustbtn.setVisible(False)
        self.retranslateUi(createOBDialog)
        QtCore.QMetaObject.connectSlotsByName(createOBDialog)


    def retranslateUi(self, createOBDialog):
        _translate = QtCore.QCoreApplication.translate
        createOBDialog.setWindowTitle(_translate("createOBDialog", "Create Outbound"))
        self.label.setText(_translate("createOBDialog", "Welcome, "))
        self.addNewRMbtn.setText(_translate("createOBDialog", "Add \n"
                                                              "Raw Material"))
        self.addNewSPbtn.setText(_translate("createOBDialog", "Add \n"
                                                              "Spare Part"))
        self.addNewTObtn.setText(_translate("createOBDialog", "Add Tool"))
        self.addNewFPbtn.setText(_translate("createOBDialog", "Add \n"
                                                              "Finish Product"))
        self.refreshbtn.setText(_translate("createOBDialog", "Refresh"))
        self.label_2.setText(_translate("createOBDialog", "Date:"))
        self.label_5.setText(_translate("createOBDialog", "outbound # :"))
        self.label_6.setText(_translate("createOBDialog", "Status :"))
        self.savebtn.setText(_translate("createOBDialog", "Save"))
        self.closebtn.setText(_translate("createOBDialog", "Close"))
        self.closeOutbtn.setText(_translate("createOBDialog", "Close Outbound"))
        self.searchresultgbox.setTitle(_translate("createOBDialog", "Selected "))
        self.label_8.setText(_translate("createOBDialog", "Name :"))
        self.label_9.setText(_translate("createOBDialog", "Mobile # :"))
        self.citylbl.setText(_translate("createOBDialog", "City :"))
        self.joblbl.setText(_translate("createOBDialog", "Job:"))
        self.label_12.setText(_translate("createOBDialog", "Age :"))
        self.groupBox_2.setTitle(_translate("createOBDialog", "Select Requester Type :"))
        self.reqTypecomboBox.setItemText(1, _translate("createOBDialog", "Employee"))
        self.reqTypecomboBox.setItemText(2, _translate("createOBDialog", "Customer"))
        self.newCustbtn.setText(_translate("createOBDialog", "New\n"
                                                             " Customer"))
        self.groupBox_3.setTitle(_translate("createOBDialog", "Search keyword"))
        self.searchbtn.setText(_translate("createOBDialog", "Search"))


    def requTypeHandel(self):
        if self.reqTypecomboBox.currentIndex() == 0:
            self.rqulistWidget.clear()
            pass
        if self.reqTypecomboBox.currentIndex() == 1:
            self.rqulistWidget.clear()
            for item in select_employee('name', self.searchled.text()):
                self.rqulistWidget.addItem(str(item.id) + ' - ' + item.name)
        if self.reqTypecomboBox.currentIndex() == 2:
            self.rqulistWidget.clear()
            for item in select_customer_key('name', self.searchled.text()):
                self.rqulistWidget.addItem(str(item.id) + ' - ' + item.name)


    def Clicked(self, item):
        id = before(item.text(), '-')
        if self.reqTypecomboBox.currentIndex() == 1:
            retitem = select_employee_by_id(id)
        if self.reqTypecomboBox.currentIndex() == 2:
            retitem = select_customer_by_id(id)
        self.addNewRMbtn.setEnabled(True)
        self.addNewSPbtn.setEnabled(True)
        self.addNewTObtn.setEnabled(True)
        self.addNewFPbtn.setEnabled(True)
        self.closeOutbtn.setEnabled(True)
        self.refreshbtn.setEnabled(True)

        self.setData(retitem)
        return retitem


    def setData(self, obj):
        self.nameled.setText(obj.name)
        self.ageled.setText(str(obj.age))
        self.mobnumled.setText(obj.mobile_number)
        if self.reqTypecomboBox.currentIndex() == 1:
            self.joblbl.setVisible(False)
            self.jobled.setVisible(False)
            self.jobled.setText(obj.job_title)
            self.citylbl.setText('Country :')

            self.reqTypecomboBox.model().item(2).setEnabled(False)
            city = obj.nationality
        elif self.reqTypecomboBox.currentIndex() == 2:
            self.reqTypecomboBox.model().item(1).setEnabled(False)

            self.citylbl.setText('City :')
            city = select_city_by_id(obj.city_id).name
        self.cityled.setText(city)


    def tableDataShow(self):
        mylist =[]
        if self.reqTypecomboBox.currentIndex() == 1:
            mylist = getOutbounEmployeeRow()
            self.tableData = OutboundTableModel()
            self.protableView.setModel(self.tableData)
        if self.reqTypecomboBox.currentIndex() == 2:
            cust = select_customer_by_mob_num(self.mobnumled.text())
            mylist = getOutbounOneCustomerRow(cust)
            self.tableData = OutboundTableModel()
            self.protableView.setModel(self.tableData)
        self.protableView.setColumnWidth(0, 100)
        self.protableView.setColumnWidth(1, 130)
        self.protableView.setColumnWidth(2, 132)
        self.protableView.setColumnWidth(3, 70)
        self.protableView.setColumnWidth(4, 40)

        for idx, val in enumerate(mylist):
            self.tableData.addItems(Outbound(val.code,
                                             None,
                                             None,
                                             val.customer_id,
                                             val.employee_id,
                                             val.raw_material_id,  # raw
                                             val.spare_part_id,  # spare
                                             val.tools_id,  # tools
                                             val.product_id,  # product
                                             val.req_qty,  # qty
                                             None))

    def openRMDialog(self):
        from uiview.ui_addRMOB import Ui_addRMOBDialog
        id = before(self.rqulistWidget.currentItem().text(), '-')
        if self.reqTypecomboBox.currentIndex() == 1:
            retitem = select_employee_by_id(id)
        if self.reqTypecomboBox.currentIndex() == 2:
            retitem = select_customer_by_id(id)
        self.di = Ui_addRMOBDialog(retitem)
        self.di.exec_()

    def openSPDialog(self):
        from uiview.ui_addSPOB import Ui_addSPOBDialog
        id = before(self.rqulistWidget.currentItem().text(), '-')
        if self.reqTypecomboBox.currentIndex() == 1:
            retitem = select_employee_by_id(id)
        if self.reqTypecomboBox.currentIndex() == 2:
            retitem = select_customer_by_id(id)
        self.di = Ui_addSPOBDialog(retitem)
        self.di.exec_()

    def openTODialog(self):
        from uiview.ui_addTOOB import Ui_addTOOBDialog
        id = before(self.rqulistWidget.currentItem().text(), '-')
        if self.reqTypecomboBox.currentIndex() == 1:
            retitem = select_employee_by_id(id)
        if self.reqTypecomboBox.currentIndex() == 2:
            retitem = select_customer_by_id(id)
        self.di = Ui_addTOOBDialog(retitem)
        self.di.exec_()

    def openFPDialog(self):
        from uiview.ui_addFPOB import Ui_addFPOBDialog
        id = before(self.rqulistWidget.currentItem().text(), '-')
        if self.reqTypecomboBox.currentIndex() == 1:
            retitem = select_employee_by_id(id)
        if self.reqTypecomboBox.currentIndex() == 2:
            retitem = select_customer_by_id(id)
        self.di = Ui_addFPOBDialog(retitem)
        self.di.exec_()

    def refresheddata(self):
        self.tableData = OutboundTableModel()
        self.protableView.setModel(self.tableData)
        self.tableDataShow()

    def contextMenuEvent(self, event):
        self.menu = QtWidgets.QMenu(self)
        renameAction = QtWidgets.QAction('Delete', self)
        renameAction.triggered.connect(self.renameSlot)
        self.menu.addAction(renameAction)
        # add other required actions
        self.menu.popup(QtGui.QCursor.pos())

    def renameSlot(self):
        indexes = self.protableView.selectionModel().selectedRows(0)
        for ind in sorted(indexes):
            outitem = select_outbound_by_code(ind.data())
            if outitem.customer_id != None:
                pers  = select_customer_by_id(outitem.customer_id)
            if outitem.employee_id != None:
                pers = select_employee_by_id(outitem.employee_id)
        replay = QMessageBox.warning(QMessageBox(), "Oop's", 'You want delete\n {} : '.format(
            outitem.code) + '\n{}'.format(pers.name) +'\n Are you sure?',
                                     QMessageBox.Yes | QMessageBox.Cancel)
        if replay == QMessageBox.Yes:
            if  outitem.tools :
                if outitem.tools.back == 0:
                    increaseToolsInvQty(outitem.tools, outitem.req_qty)
            if outitem.rawMaterial:
                increaseRawMaterialInvQty(outitem.raw_material, outitem.req_qty)
            if outitem.spareParts:
                increaseSparePartsInvQty(outitem.spareParts, outitem.req_qty)
            if outitem.finishProducts:
                increaseFinishProductInvQty(outitem.finishProducts, outitem.req_qty)
            delete_outbound(outitem.id)
            self.refresheddata()
    def openOutReport(self):
        if self.reqTypecomboBox.currentIndex() == 1:
            CreateOutboundReport().create_pdf()
            mylist = getOutbounEmployeeRow()
            for idx, val in enumerate(mylist):
                update_oubound_status(val.id, 0)
                # print(val.id)
        if self.reqTypecomboBox.currentIndex() == 2 :
            cust = select_customer_by_mob_num(self.mobnumled.text())
            CreateOutboundCustReport(cust).create_pdf()
            mylist = getOutbounOneCustomerRow(cust)
            for idx, val in enumerate(mylist):
                update_oubound_status(val.id, 0)


def before(value, a):
    # Find first part and return slice before it.
    pos_a = value.find(a)
    if pos_a == -1: return ""
    return value[0:pos_a]


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_createOBDialog()
    myapp.show()
    myapp.exec_()