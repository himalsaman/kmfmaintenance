# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addNewFPType.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import random
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

from models.finishProductsModel import add_finish_product


class Ui_addNewFPTypeDialog(QDialog):
    def __init__(self):
        super(Ui_addNewFPTypeDialog, self).__init__()
        self.setupUi(self)

    def setupUi(self, addNewFPTypeDialog):
        addNewFPTypeDialog.setObjectName("addNewFPTypeDialog")
        addNewFPTypeDialog.resize(479, 300)
        self.label = QtWidgets.QLabel(addNewFPTypeDialog)
        self.label.setGeometry(QtCore.QRect(10, 5, 51, 21))
        self.label.setObjectName("label")
        self.loggeduserlbl = QtWidgets.QLabel(addNewFPTypeDialog)
        self.loggeduserlbl.setGeometry(QtCore.QRect(62, 6, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.loggeduserlbl.setFont(font)
        self.loggeduserlbl.setText("")
        self.loggeduserlbl.setObjectName("loggeduserlbl")
        self.line = QtWidgets.QFrame(addNewFPTypeDialog)
        self.line.setGeometry(QtCore.QRect(7, 25, 491, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutWidget = QtWidgets.QWidget(addNewFPTypeDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(14, 40, 111, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.fpNameled = QtWidgets.QLineEdit(addNewFPTypeDialog)
        self.fpNameled.setGeometry(QtCore.QRect(56, 52, 370, 20))
        self.fpNameled.setObjectName("fpNameled")
        self.invQTYSpinBox = QtWidgets.QDoubleSpinBox(addNewFPTypeDialog)
        self.invQTYSpinBox.setGeometry(QtCore.QRect(125, 141, 131, 22))
        self.invQTYSpinBox.setDecimals(6)
        self.invQTYSpinBox.setMaximum(1000.0)
        self.invQTYSpinBox.setSingleStep(0.0001)
        self.invQTYSpinBox.setObjectName("invQTYSpinBox")
        self.label_7 = QtWidgets.QLabel(addNewFPTypeDialog)
        self.label_7.setGeometry(QtCore.QRect(240, 99, 41, 16))
        self.label_7.setObjectName("label_7")
        self.fpunitcomboBox = QtWidgets.QComboBox(addNewFPTypeDialog)
        self.fpunitcomboBox.setGeometry(QtCore.QRect(272, 97, 161, 22))
        self.fpunitcomboBox.setObjectName("fpunitcomboBox")
        self.fpunitcomboBox.addItem("")

        self.label_88 = QtWidgets.QLabel(addNewFPTypeDialog)
        self.label_88.setGeometry(QtCore.QRect(14, 180, 161, 22))
        self.label_88.setObjectName("label_88")

        self.fpsrcled = QtWidgets.QLineEdit(addNewFPTypeDialog)
        self.fpsrcled.setGeometry(QtCore.QRect(60, 182, 140, 20))
        self.fpsrcled.setObjectName("fpsrctled")

        self.label_8 = QtWidgets.QLabel(addNewFPTypeDialog)
        self.label_8.setGeometry(QtCore.QRect(280, 145, 60, 13))
        self.label_8.setObjectName("label_8")

        self.fpcostled = QtWidgets.QLineEdit(addNewFPTypeDialog)
        self.fpcostled.setGeometry(QtCore.QRect(311, 143, 140, 20))
        self.fpcostled.setObjectName("fpcostled")
        self.savebtn = QtWidgets.QPushButton(addNewFPTypeDialog)
        self.savebtn.setGeometry(QtCore.QRect(148, 250, 72, 41))
        self.savebtn.setObjectName("savebtn")
        self.cancelbtn = QtWidgets.QPushButton(addNewFPTypeDialog)
        self.cancelbtn.setGeometry(QtCore.QRect(256, 250, 72, 41))
        self.cancelbtn.setObjectName("cancelbtn")
        self.statulbl = QtWidgets.QLabel(addNewFPTypeDialog)
        self.statulbl.setGeometry(QtCore.QRect(16, 205, 461, 41))
        self.statulbl.setText("")
        self.statulbl.setAlignment(QtCore.Qt.AlignCenter)
        self.statulbl.setObjectName("statulbl")
        self.statulbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2 = QtWidgets.QLabel(addNewFPTypeDialog)
        self.label_2.setGeometry(QtCore.QRect(454, 147, 47, 13))
        self.label_2.setObjectName("label_2")
        self.fpcodeled = QtWidgets.QLineEdit(addNewFPTypeDialog)
        self.fpcodeled.setGeometry(QtCore.QRect(50, 97, 171, 20))
        self.fpcodeled.setObjectName("fpcodeled")

        self.retranslateUi(addNewFPTypeDialog)
        self.savebtn.clicked.connect(self.do_Add)
        self.cancelbtn.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(addNewFPTypeDialog)

    def retranslateUi(self, addNewFPTypeDialog):
        _translate = QtCore.QCoreApplication.translate
        addNewFPTypeDialog.setWindowTitle(_translate("addNewFPTypeDialog", "Add New Finish Product Type"))
        self.label.setText(_translate("addNewFPTypeDialog", "Welcome,"))
        self.label_3.setText(_translate("addNewFPTypeDialog", "Name :"))
        self.label_4.setText(_translate("addNewFPTypeDialog", "Code:"))
        self.label_6.setText(_translate("addNewFPTypeDialog", "Initial Inventory QTY :"))
        self.label_7.setText(_translate("addNewFPTypeDialog", "Unit :"))
        self.fpunitcomboBox.setItemText(0, _translate("addNewFPTypeDialog", "Each ( EA )"))
        self.label_8.setText(_translate("addNewFPTypeDialog", "Cost :"))
        self.label_88.setText(_translate("addNewFPTypeDialog", "Source :"))
        self.savebtn.setText(_translate("addNewFPTypeDialog", "Add"))
        self.cancelbtn.setText(_translate("addNewFPTypeDialog", "Cancel"))
        self.label_2.setText(_translate("addNewFPTypeDialog", "SAR"))

    def do_Add(self):
        if self.fpNameled.text() == '' or \
                        self.fpcostled.text() == '':
            self.statulbl.setText('All fields is required')
        else:
            self.statulbl.setText('ok')
            name = self.fpNameled.text()
            if self.fpunitcomboBox.currentIndex() == 1:
                unit = 'ea'
            if self.fpcodeled.text() == '':
                code = '0'
            else:
                code = self.fpcodeled.text()
            cost = self.fpcostled.text()
            invqty = self.invQTYSpinBox.value()
            gencode = 'fp{}'.format(random.randrange(10, 10000, 2))
            source = self.fpsrcled.text()
            add_finish_product(name, code, cost, invqty, gencode, source)
            self.statulbl.setText(name + ", added successfully")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_addNewFPTypeDialog()
    myapp.show()
    app.exec_()
