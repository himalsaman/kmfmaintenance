# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setupUi(self)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")

        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 280, 80))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()

        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        for i in range(20):
            Dialog.resize(300, i*21)
            self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 118, 78))
            name = 'radioButton{}'.format(i)
            self.name = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
            self.name.setGeometry(QtCore.QRect(20, i*20, 90, 17))
            self.name.setObjectName("radioButton")
            self.name.setText(name)
            # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        # self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # def retranslateUi(self, Dialog):
    #     _translate = QtCore.QCoreApplication.translate
    #     Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
    #     self.radioButton.setText(_translate("Dialog", "RadioButton"))
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = Ui_Dialog()
    myapp.exec_()
