# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addUser.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

from Control.userControl import checkUsernameExsist
from models.usersModel import add_user


class Ui_adduserDialog(QDialog):
    def __init__(self, parent=None):
        super(Ui_adduserDialog, self).__init__()
        self.setupUi(self)
    def setupUi(self, adduserDialog):
        adduserDialog.setObjectName("adduserDialog")
        adduserDialog.resize(318, 264)
        self.label = QtWidgets.QLabel(adduserDialog)
        self.label.setGeometry(QtCore.QRect(8, 8, 150, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(adduserDialog)
        self.label_2.setGeometry(QtCore.QRect(7, 62, 60, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(adduserDialog)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 30, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(adduserDialog)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 70, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(adduserDialog)
        self.label_5.setGeometry(QtCore.QRect(9, 91, 60, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(adduserDialog)
        self.label_6.setGeometry(QtCore.QRect(9, 35, 40, 13))
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(adduserDialog)
        self.line.setGeometry(QtCore.QRect(3, 26, 310, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.nameled = QtWidgets.QLineEdit(adduserDialog)
        self.nameled.setGeometry(QtCore.QRect(46, 32, 260, 20))
        self.nameled.setObjectName("nameled")
        self.usernameled = QtWidgets.QLineEdit(adduserDialog)
        self.usernameled.setGeometry(QtCore.QRect(65, 60, 180, 20))
        self.usernameled.setObjectName("usernameled")
        self.passled = QtWidgets.QLineEdit(adduserDialog)
        self.passled.setGeometry(QtCore.QRect(68, 89, 190, 20))
        self.passled.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.passled.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passled.setObjectName("passled")
        self.repassled = QtWidgets.QLineEdit(adduserDialog)
        self.repassled.setGeometry(QtCore.QRect(80, 117, 180, 20))
        self.repassled.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repassled.setObjectName("repassled")
        self.rolecbx = QtWidgets.QComboBox(adduserDialog)
        self.rolecbx.setGeometry(QtCore.QRect(40, 146, 140, 22))
        self.rolecbx.setObjectName("rolecbx")
        self.rolecbx.addItem("")
        self.rolecbx.setItemText(0, "")
        self.rolecbx.addItem("")
        self.rolecbx.addItem("")
        self.rolecbx.addItem("")
        self.line_2 = QtWidgets.QFrame(adduserDialog)
        self.line_2.setGeometry(QtCore.QRect(3, 170, 310, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.statuslbl = QtWidgets.QLabel(adduserDialog)
        self.statuslbl.setGeometry(QtCore.QRect(8, 170, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.statuslbl.setFont(font)
        self.statuslbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.statuslbl.setText("")
        self.statuslbl.setAlignment(QtCore.Qt.AlignCenter)
        self.statuslbl.setObjectName("statuslbl")
        self.line_3 = QtWidgets.QFrame(adduserDialog)
        self.line_3.setGeometry(QtCore.QRect(3, 207, 310, 10))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.savebtn = QtWidgets.QPushButton(adduserDialog)
        self.savebtn.setGeometry(QtCore.QRect(70, 215, 75, 40))
        self.savebtn.setObjectName("savebtn")
        self.cancelbtn = QtWidgets.QPushButton(adduserDialog)
        self.cancelbtn.setGeometry(QtCore.QRect(170, 215, 75, 40))
        self.cancelbtn.setObjectName("cancelbtn")
        self.savebtn.clicked.connect(self.do_add)
        self.cancelbtn.clicked.connect(self.close)

        self.retranslateUi(adduserDialog)
        QtCore.QMetaObject.connectSlotsByName(adduserDialog)

    def retranslateUi(self, adduserDialog):
        _translate = QtCore.QCoreApplication.translate
        adduserDialog.setWindowTitle(_translate("adduserDialog", "Add User"))
        self.label.setText(_translate("adduserDialog", "Welcome to User Registration :"))
        self.label_2.setText(_translate("adduserDialog", "Username :"))
        self.label_3.setText(_translate("adduserDialog", "Role :"))
        self.label_4.setText(_translate("adduserDialog", "Re-Password :"))
        self.label_5.setText(_translate("adduserDialog", "Password :"))
        self.label_6.setText(_translate("adduserDialog", "Name :"))
        self.rolecbx.setItemText(1, _translate("adduserDialog", "Accountant"))
        self.rolecbx.setItemText(2, _translate("adduserDialog", "Production Manager"))
        self.rolecbx.setItemText(3, _translate("adduserDialog", "Warehous Keeper"))
        self.savebtn.setText(_translate("adduserDialog", "Save"))
        self.cancelbtn.setText(_translate("adduserDialog", "Cancel"))

    def do_add(self):
        name = self.nameled.text()
        username = self.usernameled.text()
        password = self.passled.text()
        repassword = self.repassled.text()
        role = self.rolecbx.currentIndex()
        if name == '' or username == '' or password == '' or repassword == ''or role == 0:
            self.statuslbl.setText('Al fields is required ')
        elif password != repassword:
            self.statuslbl.setText('Password and Re-Password not matched')

        elif checkUsernameExsist(username):
            self.statuslbl.setText('{}'.format(username + " Is Already Exsist \n Please enter "
                                                          "another one"))
        else:
            datetimestr = datetime.now()
            timestampstr = datetimestr.strftime('%Y-%m-%d %H:%M:%S')
            add_user(name, username, password, timestampstr, role)
            self.statuslbl.setText('{}'.format(username + "Is Added successfully"))




if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	myapp = Ui_adduserDialog()
	myapp.show()
	app.exec_()
