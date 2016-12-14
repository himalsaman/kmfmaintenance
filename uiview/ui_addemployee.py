# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addemployee.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

from models.employeeModel import add_employee


class Ui_addemplDialog(QDialog):
    def __init__(self):
        super(Ui_addemplDialog, self).__init__()
        self.setupUi(self)
    def setupUi(self, addemplDialog):
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        addemplDialog.setObjectName("addemplDialog")
        addemplDialog.resize(319, 266)
        self.label = QtWidgets.QLabel(addemplDialog)
        self.label.setGeometry(QtCore.QRect(9, 13, 47, 13))
        self.label.setObjectName("label")
        self.nameled = QtWidgets.QLineEdit(addemplDialog)
        self.nameled.setGeometry(QtCore.QRect(49, 11, 260, 20))
        self.nameled.setObjectName("nameled")
        self.label_2 = QtWidgets.QLabel(addemplDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 41, 47, 13))
        self.label_2.setObjectName("label_2")
        self.mobled = QtWidgets.QLineEdit(addemplDialog)
        self.mobled.setGeometry(QtCore.QRect(62, 39, 180, 20))
        self.mobled.setObjectName("mobled")
        self.label_3 = QtWidgets.QLabel(addemplDialog)
        self.label_3.setGeometry(QtCore.QRect(10, 69, 47, 13))
        self.label_3.setObjectName("label_3")
        self.jobled = QtWidgets.QLineEdit(addemplDialog)
        self.jobled.setGeometry(QtCore.QRect(62, 67, 250, 20))
        self.jobled.setObjectName("jobled")
        self.label_4 = QtWidgets.QLabel(addemplDialog)
        self.label_4.setGeometry(QtCore.QRect(10, 99, 70, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(addemplDialog)
        self.label_5.setGeometry(QtCore.QRect(10, 158, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(addemplDialog)
        self.label_6.setGeometry(QtCore.QRect(10, 127, 47, 13))
        self.label_6.setObjectName("label_6")
        self.natidled = QtWidgets.QLineEdit(addemplDialog)
        self.natidled.setGeometry(QtCore.QRect(50, 125, 180, 20))
        self.natidled.setObjectName("natidled")
        self.natiocomboBox = QtWidgets.QComboBox(addemplDialog)
        self.natiocomboBox.setGeometry(QtCore.QRect(70, 95, 190, 22))
        self.natiocomboBox.setObjectName("natiocomboBox")
        self.natiocomboBox.addItem("")
        self.natiocomboBox.setItemText(0, "")
        self.natiocomboBox.addItem("")
        self.natiocomboBox.addItem("")
        self.natiocomboBox.addItem("")
        self.natiocomboBox.addItem("")
        self.natiocomboBox.addItem("")
        self.natiocomboBox.addItem("")
        self.natiocomboBox.addItem("")
        self.natiocomboBox.addItem("")
        self.natiocomboBox.addItem("")
        self.natiocomboBox.addItem("")
        self.natiocomboBox.addItem("")
        self.natiocomboBox.addItem("")
        self.natiocomboBox.addItem("")
        self.gendercomboBox = QtWidgets.QComboBox(addemplDialog)
        self.gendercomboBox.setGeometry(QtCore.QRect(54, 155, 100, 22))
        self.gendercomboBox.setObjectName("gendercomboBox")
        self.gendercomboBox.addItem("")
        self.gendercomboBox.setItemText(0, "")
        self.gendercomboBox.addItem("")
        self.gendercomboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(addemplDialog)
        self.label_7.setGeometry(QtCore.QRect(11, 186, 47, 13))
        self.label_7.setObjectName("label_7")
        self.agespinBox = QtWidgets.QSpinBox(addemplDialog)
        self.agespinBox.setGeometry(QtCore.QRect(41, 183, 70, 22))
        self.agespinBox.setObjectName("agespinBox")
        self.line = QtWidgets.QFrame(addemplDialog)
        self.line.setGeometry(QtCore.QRect(4, 212, 310, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.savebtn = QtWidgets.QPushButton(addemplDialog)
        self.savebtn.setGeometry(QtCore.QRect(60, 220, 75, 40))
        self.savebtn.setObjectName("savebtn")
        self.closebtn = QtWidgets.QPushButton(addemplDialog)
        self.closebtn.setGeometry(QtCore.QRect(154, 220, 75, 40))
        self.closebtn.setObjectName("closebtn")

        self.savebtn.clicked.connect(self.do_add)
        self.closebtn.clicked.connect(self.close)

        self.retranslateUi(addemplDialog)
        QtCore.QMetaObject.connectSlotsByName(addemplDialog)

    def retranslateUi(self, addemplDialog):
        _translate = QtCore.QCoreApplication.translate
        addemplDialog.setWindowTitle(_translate("addemplDialog", "Add Employee"))
        self.label.setText(_translate("addemplDialog", "Name :"))
        self.label_2.setText(_translate("addemplDialog", "Mobile # :"))
        self.label_3.setText(_translate("addemplDialog", "Job Title :"))
        self.label_4.setText(_translate("addemplDialog", "Nationality :"))
        self.label_5.setText(_translate("addemplDialog", "Gender :"))
        self.label_6.setText(_translate("addemplDialog", "Na. ID :"))
        self.natiocomboBox.setItemText(1, _translate("addemplDialog", "Afghanistan"))
        self.natiocomboBox.setItemText(2, _translate("addemplDialog", "Algeria"))
        self.natiocomboBox.setItemText(3, _translate("addemplDialog", "Bangladesh"))
        self.natiocomboBox.setItemText(4, _translate("addemplDialog", "Egypt"))
        self.natiocomboBox.setItemText(5, _translate("addemplDialog", "India"))
        self.natiocomboBox.setItemText(6, _translate("addemplDialog", "Indonesia"))
        self.natiocomboBox.setItemText(7, _translate("addemplDialog", "Jordan"))
        self.natiocomboBox.setItemText(8, _translate("addemplDialog", "Pakistan"))
        self.natiocomboBox.setItemText(9, _translate("addemplDialog", "Philippines"))
        self.natiocomboBox.setItemText(10, _translate("addemplDialog", "Saudi Arabia"))
        self.natiocomboBox.setItemText(11, _translate("addemplDialog", "Sudan"))
        self.natiocomboBox.setItemText(12, _translate("addemplDialog", "Syria"))
        self.natiocomboBox.setItemText(13, _translate("addemplDialog", "Yemen"))
        self.gendercomboBox.setItemText(1, _translate("addemplDialog", "Male"))
        self.gendercomboBox.setItemText(2, _translate("addemplDialog", "Female"))
        self.label_7.setText(_translate("addemplDialog", "Age :"))
        self.savebtn.setText(_translate("addemplDialog", "Save"))
        self.closebtn.setText(_translate("addemplDialog", "Close"))

    def do_add(self):
        if self.nameled.text() == '' and self.jobled.text() == '':
            pass
        else:
            name = self.nameled.text()
            mobile = self.mobled.text()
            job = self.jobled.text()
            natio = self.natiocomboBox.currentText()
            natid = self.natidled.text()
            gender = self.gendercomboBox.currentText()
            age = self.agespinBox.value()
            add_employee(name, mobile, job, natio, natid, gender, age)


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     myapp = Ui_addemplDialog()
#     myapp.exec_()