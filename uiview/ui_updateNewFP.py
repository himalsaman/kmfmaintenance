# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_updateNewFP.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox

from Control.materialsControl import upFinishProductCost, increaseFinishProductInvQty, decreaseFinishProductInvQty
from Control.userControl import getLoginDataPKL
from models.finishProductsModel import select_all_finish_product, select_finish_product_by_gen_code, \
    update_finish_product, update_finish_product_cost
from models.sparePartsModel import select_spare_parts_bygen_code


class Ui_editFPDialog(QDialog):
    def __init__(self):
        super(Ui_editFPDialog, self).__init__()
        self.setupUi(self)
    def setupUi(self, editFPDialog):
        editFPDialog.setObjectName("editFPDialog")
        editFPDialog.resize(818, 523)
        self.label = QtWidgets.QLabel(editFPDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 16))
        self.label.setObjectName("label")
        self.loggeduserlbl = QtWidgets.QLabel(editFPDialog)
        self.loggeduserlbl.setGeometry(QtCore.QRect(61, 11, 170, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.loggeduserlbl.setFont(font)
        self.loggeduserlbl.setText("")
        self.loggeduserlbl.setObjectName("loggeduserlbl")
        self.line = QtWidgets.QFrame(editFPDialog)
        self.line.setGeometry(QtCore.QRect(11, 28, 800, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutWidget = QtWidgets.QWidget(editFPDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(391, 50, 81, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.line_2 = QtWidgets.QFrame(editFPDialog)
        self.line_2.setGeometry(QtCore.QRect(372, 43, 20, 471))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.fpnamelbl = QtWidgets.QLabel(editFPDialog)
        self.fpnamelbl.setGeometry(QtCore.QRect(430, 54, 270, 20))
        self.fpnamelbl.setText("")
        self.fpnamelbl.setObjectName("fpnamelbl")
        self.fpcodelbl = QtWidgets.QLabel(editFPDialog)
        self.fpcodelbl.setGeometry(QtCore.QRect(435, 85, 130, 20))
        self.fpcodelbl.setText("")
        self.fpcodelbl.setObjectName("fpcodelbl")
        self.label_7 = QtWidgets.QLabel(editFPDialog)
        self.label_7.setGeometry(QtCore.QRect(662, 54, 50, 20))
        self.label_7.setObjectName("label_7")
        self.fpcostlbl = QtWidgets.QLabel(editFPDialog)
        self.fpcostlbl.setGeometry(QtCore.QRect(425, 116, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fpcostlbl.setFont(font)
        self.fpcostlbl.setText("")
        self.fpcostlbl.setObjectName("fpcostlbl")
        self.fpunitlbl = QtWidgets.QLabel(editFPDialog)
        self.fpunitlbl.setGeometry(QtCore.QRect(710, 54, 50, 20))
        self.fpunitlbl.setText("")
        self.fpunitlbl.setObjectName("fpunitlbl")
        self.label_4 = QtWidgets.QLabel(editFPDialog)
        self.label_4.setGeometry(QtCore.QRect(530, 114, 79, 25))
        self.label_4.setObjectName("label_4")
        self.fpinvqtylbl = QtWidgets.QLabel(editFPDialog)
        self.fpinvqtylbl.setGeometry(QtCore.QRect(610, 116, 81, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fpinvqtylbl.setFont(font)
        self.fpinvqtylbl.setText("")
        self.fpinvqtylbl.setObjectName("fpinvqtylbl")
        self.line_3 = QtWidgets.QFrame(editFPDialog)
        self.line_3.setGeometry(QtCore.QRect(390, 142, 420, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_15 = QtWidgets.QLabel(editFPDialog)
        self.label_15.setGeometry(QtCore.QRect(394, 174, 79, 26))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(editFPDialog)
        self.label_16.setGeometry(QtCore.QRect(646, 177, 50, 20))
        self.label_16.setObjectName("label_16")

        self.label_20 = QtWidgets.QLabel(editFPDialog)
        self.label_20.setGeometry(QtCore.QRect(394, 206, 50, 25))
        self.label_20.setObjectName("label_20")

        self.fpnameled = QtWidgets.QLineEdit(editFPDialog)
        self.fpnameled.setGeometry(QtCore.QRect(430, 179, 200, 20))
        self.fpnameled.setObjectName("fpnameled")

        self.fpsourled = QtWidgets.QLineEdit(editFPDialog)
        self.fpsourled.setGeometry(QtCore.QRect(690, 177, 110, 22))
        self.fpsourled.setObjectName("fpsourled")

        self.label_18 = QtWidgets.QLabel(editFPDialog)
        self.label_18.setGeometry(QtCore.QRect(393, 152, 400, 20))
        self.label_18.setObjectName("label_18")
        self.line_4 = QtWidgets.QFrame(editFPDialog)
        self.line_4.setGeometry(QtCore.QRect(389, 272, 420, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.dataupdatebtn = QtWidgets.QPushButton(editFPDialog)
        self.dataupdatebtn.setGeometry(QtCore.QRect(565, 242, 75, 30))
        self.dataupdatebtn.setObjectName("dataupdatebtn")
        self.label_19 = QtWidgets.QLabel(editFPDialog)
        self.label_19.setGeometry(QtCore.QRect(395, 282, 160, 20))
        self.label_19.setObjectName("label_19")
        self.label_21 = QtWidgets.QLabel(editFPDialog)
        self.label_21.setGeometry(QtCore.QRect(390, 351, 400, 20))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(editFPDialog)
        self.label_22.setGeometry(QtCore.QRect(394, 309, 50, 20))
        self.label_22.setObjectName("label_22")
        self.oldcostlbl = QtWidgets.QLabel(editFPDialog)
        self.oldcostlbl.setGeometry(QtCore.QRect(443, 310, 80, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.oldcostlbl.setFont(font)
        self.oldcostlbl.setText("")
        self.oldcostlbl.setObjectName("oldcostlbl")
        self.label_24 = QtWidgets.QLabel(editFPDialog)
        self.label_24.setGeometry(QtCore.QRect(548, 309, 60, 20))
        self.label_24.setObjectName("label_24")
        self.newcostled = QtWidgets.QLineEdit(editFPDialog)
        self.newcostled.setGeometry(QtCore.QRect(603, 311, 110, 20))
        self.newcostled.setObjectName("newcostled")
        self.updatecostbtn = QtWidgets.QPushButton(editFPDialog)
        self.updatecostbtn.setGeometry(QtCore.QRect(724, 309, 75, 23))
        self.updatecostbtn.setObjectName("updatecostbtn")
        self.line_5 = QtWidgets.QFrame(editFPDialog)
        self.line_5.setGeometry(QtCore.QRect(390, 340, 420, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.updateqtybtn = QtWidgets.QPushButton(editFPDialog)
        self.updateqtybtn.setGeometry(QtCore.QRect(723, 377, 80, 23))
        self.updateqtybtn.setObjectName("updateqtybtn")
        self.oldqtylbl = QtWidgets.QLabel(editFPDialog)
        self.oldqtylbl.setGeometry(QtCore.QRect(440, 377, 80, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.oldqtylbl.setFont(font)
        self.oldqtylbl.setText("")
        self.oldqtylbl.setObjectName("oldqtylbl")
        self.label_26 = QtWidgets.QLabel(editFPDialog)
        self.label_26.setGeometry(QtCore.QRect(537, 376, 70, 20))
        self.label_26.setObjectName("label_26")

        self.label_27 = QtWidgets.QLabel(editFPDialog)
        self.label_27.setGeometry(QtCore.QRect(391, 376, 50, 20))
        self.label_27.setObjectName("label_27")

        self.fpgencodelbl = QtWidgets.QLabel(editFPDialog)
        self.fpgencodelbl.setGeometry(QtCore.QRect(391, 376, 50, 20))
        self.fpgencodelbl.setObjectName("fpgencodelbl")
        self.fpgencodelbl.setVisible(False)

        self.newqtySpinBox = QtWidgets.QDoubleSpinBox(editFPDialog)
        self.newqtySpinBox.setGeometry(QtCore.QRect(600, 377, 110, 22))
        self.newqtySpinBox.setObjectName("newqtySpinBox")
        self.closebtn = QtWidgets.QPushButton(editFPDialog)
        self.closebtn.setGeometry(QtCore.QRect(548, 460, 90, 40))
        self.closebtn.setObjectName("closebtn")
        self.listWidget = QtWidgets.QListWidget(editFPDialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 361, 471))
        self.listWidget.setObjectName("listWidget")

        for item in select_all_finish_product():
            self.listWidget.addItem(item.gen_code + " - " + item.name)
        self.listWidget.itemClicked.connect(self.Clicked)

        self.fpcodeled = QtWidgets.QLineEdit(editFPDialog)
        self.fpcodeled.setGeometry(QtCore.QRect(430, 210, 151, 20))
        self.fpcodeled.setObjectName("fpcodeled")
        self.updateqtybtn_2 = QtWidgets.QPushButton(editFPDialog)
        self.updateqtybtn_2.setGeometry(QtCore.QRect(725, 412, 75, 23))
        self.updateqtybtn_2.setObjectName("updateqtybtn_2")
        self.label_28 = QtWidgets.QLabel(editFPDialog)
        self.label_28.setGeometry(QtCore.QRect(541, 411, 70, 20))
        self.label_28.setObjectName("label_28")
        self.newqtySpinBox_2 = QtWidgets.QDoubleSpinBox(editFPDialog)
        self.newqtySpinBox_2.setGeometry(QtCore.QRect(600, 412, 110, 22))
        self.newqtySpinBox_2.setObjectName("newqtySpinBox_2")
        self.statulbl = QtWidgets.QLabel(editFPDialog)
        self.statulbl.setGeometry(QtCore.QRect(390, 420, 410, 41))
        self.statulbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.statulbl.setAlignment(QtCore.Qt.AlignCenter)
        self.statulbl.setText("")
        self.statulbl.setAlignment(QtCore.Qt.AlignCenter)
        self.statulbl.setObjectName("statulbl")
        self.dataupdatebtn.clicked.connect(self.update_data)
        self.updatecostbtn.clicked.connect(self.update_cost)
        self.updateqtybtn.clicked.connect(self.plusupdate_inv)
        self.updateqtybtn_2.clicked.connect(self.minupdate_inv)
        self.closebtn.clicked.connect(self.close)

        self.retranslateUi(editFPDialog)
        QtCore.QMetaObject.connectSlotsByName(editFPDialog)

    def retranslateUi(self, editFPDialog):
        _translate = QtCore.QCoreApplication.translate
        editFPDialog.setWindowTitle(_translate("editFPDialog", "Edit Finish Product"))
        self.label.setText(_translate("editFPDialog", "Welcome, "))
        self.label_3.setText(_translate("editFPDialog", "Name :"))
        self.label_5.setText(_translate("editFPDialog", "Code :"))
        self.label_8.setText(_translate("editFPDialog", "Cost :"))
        self.label_7.setText(_translate("editFPDialog", "Source :"))
        self.label_4.setText(_translate("editFPDialog", "Inventory QYT :"))
        self.label_15.setText(_translate("editFPDialog", "Name :"))
        self.label_16.setText(_translate("editFPDialog", "Source :"))
        self.label_18.setText(_translate("editFPDialog", "This Data Just you can edit it for more security"))
        self.dataupdatebtn.setText(_translate("editFPDialog", "Update Data"))
        self.label_19.setText(_translate("editFPDialog", "If you want update cost"))
        self.label_20.setText(_translate("editFPDialog", "Code :"))
        self.label_21.setText(_translate("editFPDialog", "If you want update Inventory Quantity"))
        self.label_22.setText(_translate("editFPDialog", "Old Cost:"))
        self.label_24.setText(_translate("editFPDialog", "New Cost :"))
        self.updatecostbtn.setText(_translate("editFPDialog", "Update Cost"))
        self.updateqtybtn.setText(_translate("editFPDialog", "+ Update QTY"))
        self.label_26.setText(_translate("editFPDialog", "+ New QTY :"))
        self.label_27.setText(_translate("editFPDialog", "Old QTY:"))
        self.closebtn.setText(_translate("editFPDialog", "Close"))
        self.updateqtybtn_2.setText(_translate("editFPDialog", "- Update QTY"))
        self.label_28.setText(_translate("editFPDialog", "- New QTY :"))

    def Clicked(self, item):
        role = getLoginDataPKL()['role']
        if int(role) == 2 :
            self.updatecostbtn.setEnabled(False)
            self.updateqtybtn.setEnabled(False)
            self.dataupdatebtn.setEnabled(False)
        if int(role) == 3:
            # self.updatecostbtn.setEnabled(False)
            self.updateqtybtn.setEnabled(True)
            self.updateqtybtn_2.setEnabled(True)
            self.dataupdatebtn.setEnabled(True)
        if int(role) == 1 :
            self.updatecostbtn.setEnabled(True)
            self.updateqtybtn.setEnabled(False)
            self.dataupdatebtn.setEnabled(False)

        gencode = before(item.text(), '-')
        if select_finish_product_by_gen_code(gencode):
            fpor = select_finish_product_by_gen_code(gencode)
            print(fpor)
            self.fpnamelbl.setText(fpor.name)
            self.fpunitlbl.setText(fpor.source)
            self.fpcodelbl.setText(fpor.code)
            self.fpcostlbl.setText(str(fpor.price))
            self.fpinvqtylbl.setText(str(fpor.inv_qty))
            self.fpgencodelbl.setText(fpor.gen_code)
            self.fpnameled.setText(fpor.name)
            self.fpsourled.setText(fpor.source)
            self.fpcodeled.setText(fpor.code)
            # ## old (cost and inv_qty)
            self.oldcostlbl.setText(str(fpor.price))
            self.oldqtylbl.setText(str(fpor.inv_qty))
        return fpor

    def update_data(self):
        id_code = self.fpgencodelbl.text()
        upsp = select_finish_product_by_gen_code(id_code)
        xname = self.fpnameled.text()
        xsource = self.fpsourled.text()
        # # # spesial case
        xcode = self.fpcodeled.text()
        xcost = upsp.price
        xinv_qty = upsp.inv_qty
        xgen_code = upsp.gen_code
        #
        if xname == '':
            xname = upsp.name
        if xsource == '':
            xsource = upsp.source
        if xcode == '':
            xcode = upsp.code
        update_finish_product(upsp.id, xname, xcode, xcost, xinv_qty, xsource, xgen_code)
        self.statulbl.setText("Data updated successfully")

    def update_cost(self):
        if self.newcostled.text() == '':
            self.statulbl.setText('New Cost is Required ')
        else:
            reply = QMessageBox.question(QMessageBox(), 'Delete', "Are you sure to update cost ?\n"
                                                                  "This action you can't undo",
                                         QMessageBox.Yes | QMessageBox.No)
            id_code = self.fpgencodelbl.text()
            upsp = select_finish_product_by_gen_code(id_code)

            n_cost = self.newcostled.text()
            if n_cost == '':
                n_cost = upsp.price

            if reply == QMessageBox.Yes:
                upFinishProductCost(upsp, n_cost)
                self.statulbl.setText("Data updated successfully")
            else:
                self.statulbl.setText("Data not updated ")

    def plusupdate_inv(self):
        if self.newqtySpinBox.value() == 0:
            self.statulbl.setText("New Quantity is Required ")
        else:
            reply = QMessageBox.question(QMessageBox(), 'Delete', "Are you sure to update cost ?\n"
                                                                  "This action you can't undo",
                                         QMessageBox.Yes | QMessageBox.No)
            id_code = self.fpgencodelbl.text()
            upsp = select_finish_product_by_gen_code(id_code)

            n_inv = self.newqtySpinBox.value()

            if reply == QMessageBox.Yes:
                increaseFinishProductInvQty(upsp, n_inv)
                self.statulbl.setText("Data updated successfully")
            else:
                self.statulbl.setText("Data not updated ")

    def minupdate_inv(self):
        if self.newqtySpinBox_2.value() == 0:
            self.statulbl.setText("New Quantity is Required ")
        else:
            reply = QMessageBox.question(QMessageBox(), 'Delete', "Are you sure to update cost ?\n"
                                                                  "This action you can't undo",
                                         QMessageBox.Yes | QMessageBox.No)
            id_code = self.fpgencodelbl.text()
            upsp = select_finish_product_by_gen_code(id_code)

            n_inv = self.newqtySpinBox_2.value()

            if reply == QMessageBox.Yes:
                decreaseFinishProductInvQty(upsp, n_inv)
                self.statulbl.setText("Data updated successfully")
            else:
                self.statulbl.setText("Data not updated ")


def before(value, a):
	# Find first part and return slice before it.
	pos_a = value.find(a)
	if pos_a == -1: return ""
	return value[0:pos_a]

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_editFPDialog()
    myapp.show()
    myapp.exec_()
