# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_changePassword.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

from Control.userControl import getLoginDataPKL, changePassword


class Ui_changePasswordDilaod(QDialog):
    def __init__(self, parent=None):
        super(Ui_changePasswordDilaod, self).__init__()
        self.setupUi(self)

    def setupUi(self, changePasswordDilaod):
        changePasswordDilaod.setObjectName("changePasswordDilaod")
        changePasswordDilaod.resize(400, 331)
        self.label = QtWidgets.QLabel(changePasswordDilaod)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 16))
        self.label.setObjectName("label")
        self.usernameLabel = QtWidgets.QLabel(changePasswordDilaod)
        self.usernameLabel.setGeometry(QtCore.QRect(63, 10, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setText(getLoginDataPKL()['name'])
        self.usernameLabel.setObjectName("usernameLabel")
        self.line = QtWidgets.QFrame(changePasswordDilaod)
        self.line.setGeometry(QtCore.QRect(10, 30, 381, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(changePasswordDilaod)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 381, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(changePasswordDilaod)
        self.label_4.setGeometry(QtCore.QRect(10, 96, 381, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(changePasswordDilaod)
        self.label_5.setGeometry(QtCore.QRect(10, 139, 381, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(changePasswordDilaod)
        self.label_6.setGeometry(QtCore.QRect(10, 184, 381, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.usernameld = QtWidgets.QLineEdit(changePasswordDilaod)
        self.usernameld.setGeometry(QtCore.QRect(111, 71, 171, 20))
        self.usernameld.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameld.setObjectName("usernameld")
        self.usernameld.setEnabled(False)
        self.usernameld.setText(getLoginDataPKL()['username'])
        self.oldPasswordled = QtWidgets.QLineEdit(changePasswordDilaod)
        self.oldPasswordled.setGeometry(QtCore.QRect(113, 116, 171, 20))
        self.oldPasswordled.setAlignment(QtCore.Qt.AlignCenter)
        self.oldPasswordled.setObjectName("oldPasswordled")
        self.newPasswordled = QtWidgets.QLineEdit(changePasswordDilaod)
        self.newPasswordled.setGeometry(QtCore.QRect(112, 159, 171, 20))
        self.newPasswordled.setAlignment(QtCore.Qt.AlignCenter)
        self.newPasswordled.setObjectName("newPasswordled")
        self.renewpasswordled = QtWidgets.QLineEdit(changePasswordDilaod)
        self.renewpasswordled.setGeometry(QtCore.QRect(112, 203, 171, 20))
        self.renewpasswordled.setAlignment(QtCore.Qt.AlignCenter)
        self.renewpasswordled.setObjectName("renewpasswordled")
        self.savebtn = QtWidgets.QPushButton(changePasswordDilaod)
        self.savebtn.setGeometry(QtCore.QRect(110, 288, 75, 31))
        self.savebtn.setObjectName("savebtn")

        self.savebtn.clicked.connect(self.doChangePassword)

        self.cancelbtn = QtWidgets.QPushButton(changePasswordDilaod)
        self.cancelbtn.setGeometry(QtCore.QRect(210, 288, 75, 31))
        self.cancelbtn.setObjectName("cancelbtn")

        self.cancelbtn.clicked.connect(self.close)

        self.statuslbl = QtWidgets.QLabel(changePasswordDilaod)
        self.statuslbl.setGeometry(QtCore.QRect(6, 231, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.statuslbl.setFont(font)
        self.statuslbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.statuslbl.setText("")
        self.statuslbl.setAlignment(QtCore.Qt.AlignCenter)
        self.statuslbl.setObjectName("statuslbl")

        self.retranslateUi(changePasswordDilaod)
        QtCore.QMetaObject.connectSlotsByName(changePasswordDilaod)

    def retranslateUi(self, changePasswordDilaod):
        _translate = QtCore.QCoreApplication.translate
        changePasswordDilaod.setWindowTitle(_translate("changePasswordDilaod", "Change Password"))
        self.label.setText(_translate("changePasswordDilaod", "Welcome, "))
        self.label_3.setText(_translate("changePasswordDilaod", "Username"))
        self.label_4.setText(_translate("changePasswordDilaod", "Old Password"))
        self.label_5.setText(_translate("changePasswordDilaod", "New Password"))
        self.label_6.setText(_translate("changePasswordDilaod", "Re-new Password"))
        self.savebtn.setText(_translate("changePasswordDilaod", "Save"))
        self.cancelbtn.setText(_translate("changePasswordDilaod", "Cancel"))

    def doChangePassword(self):
        username = self.usernameld.text()
        old_password = self.oldPasswordled.text()
        new_pasword = self.newPasswordled.text()
        renew_password = self.renewpasswordled.text()
        if renew_password == new_pasword:
            if changePassword(username, old_password, new_pasword):
                self.statuslbl.setText('Password changed successfully')
                self.close()
            else:
                self.statuslbl.setText('Old Password is Wrong, \n Old Password / New Password must be not '
                                       'same')
        else:
            self.statuslbl.setText('New Password / Re-New Password not match')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    cp_dialog = Ui_changePasswordDilaod()
    cp_dialog.show()
    sys.exit(app.exec_())