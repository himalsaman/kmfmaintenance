# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_loginDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QLineEdit

from Control.userControl import validLogin


class Ui_loginDialog(QDialog):
	def __init__(self, parent=None):
		# QWidget.__init__(self, parent)
		super(Ui_loginDialog, self).__init__()
		self.setupUi(self)

	def setupUi(self, loginDialog):
		loginDialog.setObjectName("loginDialog")
		loginDialog.resize(400, 262)
		self.label = QtWidgets.QLabel(loginDialog)
		self.label.setGeometry(QtCore.QRect(10, 84, 381, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.usernameinput = QtWidgets.QLineEdit(loginDialog)
		self.usernameinput.setGeometry(QtCore.QRect(100, 104, 191, 20))
		self.usernameinput.setObjectName("usernameinput")
		self.label_2 = QtWidgets.QLabel(loginDialog)
		self.label_2.setGeometry(QtCore.QRect(10, 134, 381, 20))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.label_2.setFont(font)
		self.label_2.setAlignment(QtCore.Qt.AlignCenter)
		self.label_2.setObjectName("label_2")
		self.passwordinput = QtWidgets.QLineEdit(loginDialog)
		self.passwordinput.setGeometry(QtCore.QRect(100, 154, 191, 20))
		self.passwordinput.setObjectName("passwordinput")
		self.passwordinput.setEchoMode(QLineEdit.Password)
		self.loginbtn = QtWidgets.QPushButton(loginDialog)
		self.loginbtn.setGeometry(QtCore.QRect(99, 212, 75, 31))
		self.loginbtn.setObjectName("loginbtn")
		self.loginbtn.clicked.connect(self.doLogin)
		self.cancelbtn = QtWidgets.QPushButton(loginDialog)
		self.cancelbtn.setGeometry(QtCore.QRect(217, 212, 75, 31))
		self.cancelbtn.setObjectName("cancelbtn")
		self.cancelbtn.clicked.connect(self.close)
		self.statuplabel = QtWidgets.QLabel(loginDialog)
		self.statuplabel.setGeometry(QtCore.QRect(10, 184, 381, 20))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.statuplabel.setFont(font)
		self.statuplabel.setStyleSheet("color: rgb(255, 0, 0);")
		self.statuplabel.setText("")
		self.statuplabel.setScaledContents(False)
		self.statuplabel.setAlignment(QtCore.Qt.AlignCenter)
		self.statuplabel.setObjectName("statuplabel")
		self.label_4 = QtWidgets.QLabel(loginDialog)
		self.label_4.setGeometry(QtCore.QRect(10, 10, 381, 20))
		font = QtGui.QFont()
		font.setPointSize(16)
		self.label_4.setFont(font)
		self.label_4.setAlignment(QtCore.Qt.AlignCenter)
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(loginDialog)
		self.label_5.setGeometry(QtCore.QRect(10, 50, 381, 20))
		font = QtGui.QFont()
		font.setPointSize(16)
		self.label_5.setFont(font)
		self.label_5.setAlignment(QtCore.Qt.AlignCenter)
		self.label_5.setObjectName("label_5")
		self.line = QtWidgets.QFrame(loginDialog)
		self.line.setGeometry(QtCore.QRect(7, 74, 381, 20))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.retranslateUi(loginDialog)
		QtCore.QMetaObject.connectSlotsByName(loginDialog)

	def retranslateUi(self, loginDialog):
		_translate = QtCore.QCoreApplication.translate
		loginDialog.setWindowTitle(_translate("loginDialog", "Dialog"))
		self.label.setText(_translate("loginDialog", "User Name"))
		self.label_2.setText(_translate("loginDialog", "Password"))
		self.loginbtn.setText(_translate("loginDialog", "Login"))
		self.cancelbtn.setText(_translate("loginDialog", "Cancel"))
		self.label_4.setText(_translate("loginDialog", "Khatmah Medical Factory"))
		self.label_5.setText(_translate("loginDialog", "Maintenance System"))

	def doLogin(self):
		username = self.usernameinput.text()
		password = self.passwordinput.text()
		if validLogin(username, password):
			self.close()
			from uiview.ui_mmainWindow import Ui_MMainWindow
			self.main_window = Ui_MMainWindow()
			self.main_window.show()
		else:
			self.passwordinput.setText('')
			self.statuplabel.setText("Username / Password not valid")


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	myapp = Ui_loginDialog()
	myapp.show()
	app.exec_()
