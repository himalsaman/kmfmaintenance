# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mmainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox

from Control.maintenanceLogic import getMaintenancePused, getMaintenanceHolded, \
	getMaintenanceUnderProccessing, \
	getMaintenanceWaitingDelevary, getMaintenanceFinishedAndDelivared, getMaintenanceCalcCost, \
	getMaintenanceUnderProccessingCost, getMaintenanceFinishedAndDelivaredCost, getMaintenanceWaitLaborCost
from Control.userControl import deleteLoginDataPKL, getLoginDataPKL
from models.customersModel import select_all_customers
from models.rawMaterialModel import select_all_raw_material
from models.sparePartsModel import select_all_spare_parts

# get now time
datetimestr = datetime.now()
timestampstr = datetimestr.strftime('%Y-%m-%d %H:%M:%S')


class Ui_MMainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(Ui_MMainWindow, self).__init__()

		self.setupUi(self)

	def setupUi(self, MMainWindow):
		self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

		MMainWindow.setObjectName("MMainWindow")
		MMainWindow.resize(816, 550)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(MMainWindow.sizePolicy().hasHeightForWidth())
		MMainWindow.setSizePolicy(sizePolicy)
		MMainWindow.setMinimumSize(QtCore.QSize(816, 550))
		MMainWindow.setMaximumSize(QtCore.QSize(816, 550))
		MMainWindow.setSizeIncrement(QtCore.QSize(816, 550))
		MMainWindow.setBaseSize(QtCore.QSize(816, 550))
		MMainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.centralwidget = QtWidgets.QWidget(MMainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.line_11 = QtWidgets.QFrame(self.centralwidget)
		self.line_11.setGeometry(QtCore.QRect(2, 179, 260, 3))
		self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_11.setObjectName("line_11")
		self.line_16 = QtWidgets.QFrame(self.centralwidget)
		self.line_16.setGeometry(QtCore.QRect(549, 89, 260, 3))
		self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_16.setObjectName("line_16")
		self.alocmbtn = QtWidgets.QPushButton(self.centralwidget)
		self.alocmbtn.setGeometry(QtCore.QRect(549, 199, 260, 50))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.alocmbtn.setFont(font)
		self.alocmbtn.setObjectName("alocmbtn")
		self.loggeduserlbl = QtWidgets.QLabel(self.centralwidget)
		self.loggeduserlbl.setGeometry(QtCore.QRect(59, 3, 200, 13))
		self.loggeduserlbl.setText("")
		self.loggeduserlbl.setObjectName("loggeduserlbl")
		self.label_33 = QtWidgets.QLabel(self.centralwidget)
		self.label_33.setGeometry(QtCore.QRect(549, 331, 160, 30))
		self.label_33.setObjectName("label_33")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(6, 3, 50, 13))
		self.label.setObjectName("label")
		self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox.setGeometry(QtCore.QRect(7, 69, 251, 101))
		self.groupBox.setTitle("")
		self.groupBox.setObjectName("groupBox")
		self.label_4 = QtWidgets.QLabel(self.groupBox)
		self.label_4.setGeometry(QtCore.QRect(5, 8, 241, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_4.setFont(font)
		self.label_4.setAlignment(QtCore.Qt.AlignCenter)
		self.label_4.setObjectName("label_4")
		self.tmplbl = QtWidgets.QLabel(self.groupBox)
		self.tmplbl.setGeometry(QtCore.QRect(16, 57, 70, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setUnderline(True)
		font.setWeight(75)
		self.tmplbl.setFont(font)
		self.tmplbl.setStyleSheet("color: rgb(255, 0, 0);\n"
								  "border-color: rgb(0, 0, 255);\n"
								  "background-color: rgb(255, 255, 255);")
		self.tmplbl.setText("")
		self.tmplbl.setAlignment(QtCore.Qt.AlignCenter)
		self.tmplbl.setObjectName("tmplbl")
		self.tmpbtn = QtWidgets.QPushButton(self.groupBox)
		self.tmpbtn.setGeometry(QtCore.QRect(160, 52, 75, 40))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.tmpbtn.setFont(font)
		self.tmpbtn.setObjectName("tmpbtn")
		self.line_14 = QtWidgets.QFrame(self.groupBox)
		self.line_14.setGeometry(QtCore.QRect(-2, 36, 240, 20))
		self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_14.setObjectName("line_14")
		self.line_17 = QtWidgets.QFrame(self.groupBox)
		self.line_17.setGeometry(QtCore.QRect(118, 52, 3, 40))
		self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_17.setObjectName("line_17")
		self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_2.setGeometry(QtCore.QRect(7, 303, 251, 150))
		self.groupBox_2.setTitle("")
		self.groupBox_2.setObjectName("groupBox_2")
		self.label_10 = QtWidgets.QLabel(self.groupBox_2)
		self.label_10.setGeometry(QtCore.QRect(5, 8, 241, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_10.setFont(font)
		self.label_10.setAlignment(QtCore.Qt.AlignCenter)
		self.label_10.setObjectName("label_10")
		self.tmhlbl = QtWidgets.QLabel(self.groupBox_2)
		self.tmhlbl.setGeometry(QtCore.QRect(11, 64, 70, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setUnderline(True)
		font.setWeight(75)
		self.tmhlbl.setFont(font)
		self.tmhlbl.setStyleSheet("color: rgb(255, 0, 0);\n"
								  "border-color: rgb(0, 0, 255);\n"
								  "background-color: rgb(255, 255, 255);")
		self.tmhlbl.setText("")
		self.tmhlbl.setAlignment(QtCore.Qt.AlignCenter)
		self.tmhlbl.setObjectName("tmhlbl")
		self.tmhbtn = QtWidgets.QPushButton(self.groupBox_2)
		self.tmhbtn.setGeometry(QtCore.QRect(157, 58, 75, 40))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.tmhbtn.setFont(font)
		self.tmhbtn.setObjectName("tmhbtn")
		self.label_18 = QtWidgets.QLabel(self.groupBox_2)
		self.label_18.setGeometry(QtCore.QRect(6, 112, 60, 30))
		self.label_18.setObjectName("label_18")
		self.tctmhlbl = QtWidgets.QLabel(self.groupBox_2)
		self.tctmhlbl.setGeometry(QtCore.QRect(68, 112, 150, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setUnderline(True)
		font.setWeight(75)
		self.tctmhlbl.setFont(font)
		self.tctmhlbl.setStyleSheet("color: rgb(255, 0, 0);\n"
									"border-color: rgb(0, 0, 255);\n"
									"background-color: rgb(255, 255, 255);")
		self.tctmhlbl.setText("")
		self.tctmhlbl.setAlignment(QtCore.Qt.AlignCenter)
		self.tctmhlbl.setObjectName("tctmhlbl")
		self.line_4 = QtWidgets.QFrame(self.groupBox_2)
		self.line_4.setGeometry(QtCore.QRect(-3, 97, 240, 20))
		self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_4.setObjectName("line_4")
		self.line_5 = QtWidgets.QFrame(self.groupBox_2)
		self.line_5.setGeometry(QtCore.QRect(-3, 40, 240, 20))
		self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_5.setObjectName("line_5")
		self.line_18 = QtWidgets.QFrame(self.groupBox_2)
		self.line_18.setGeometry(QtCore.QRect(118, 60, 3, 40))
		self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_18.setObjectName("line_18")
		self.label_37 = QtWidgets.QLabel(self.centralwidget)
		self.label_37.setGeometry(QtCore.QRect(549, 411, 100, 30))
		self.label_37.setObjectName("label_37")
		self.line_3 = QtWidgets.QFrame(self.centralwidget)
		self.line_3.setGeometry(QtCore.QRect(539, 69, 3, 440))
		self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.line_13 = QtWidgets.QFrame(self.centralwidget)
		self.line_13.setGeometry(QtCore.QRect(275, 224, 260, 3))
		self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_13.setObjectName("line_13")
		self.closebtn = QtWidgets.QPushButton(self.centralwidget)
		self.closebtn.setGeometry(QtCore.QRect(710, 459, 90, 50))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.closebtn.setFont(font)
		self.closebtn.setObjectName("closebtn")
		self.tprmlbl = QtWidgets.QLabel(self.centralwidget)
		self.tprmlbl.setGeometry(QtCore.QRect(700, 331, 100, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setUnderline(True)
		font.setWeight(75)
		self.tprmlbl.setFont(font)
		self.tprmlbl.setStyleSheet("color: rgb(255, 0, 0);\n"
								   "border-color: rgb(0, 0, 255);\n"
								   "background-color: rgb(255, 255, 255);")
		self.tprmlbl.setText("")
		self.tprmlbl.setAlignment(QtCore.Qt.AlignCenter)
		self.tprmlbl.setObjectName("tprmlbl")
		self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_7.setGeometry(QtCore.QRect(280, 345, 251, 150))
		self.groupBox_7.setTitle("")
		self.groupBox_7.setObjectName("groupBox_7")
		self.label_28 = QtWidgets.QLabel(self.groupBox_7)
		self.label_28.setGeometry(QtCore.QRect(5, 9, 240, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_28.setFont(font)
		self.label_28.setAlignment(QtCore.Qt.AlignCenter)
		self.label_28.setObjectName("label_28")
		self.tmfpdlbl = QtWidgets.QLabel(self.groupBox_7)
		self.tmfpdlbl.setGeometry(QtCore.QRect(9, 64, 70, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setUnderline(True)
		font.setWeight(75)
		self.tmfpdlbl.setFont(font)
		self.tmfpdlbl.setStyleSheet("color: rgb(255, 0, 0);\n"
									"border-color: rgb(0, 0, 255);\n"
									"background-color: rgb(255, 255, 255);")
		self.tmfpdlbl.setText("")
		self.tmfpdlbl.setAlignment(QtCore.Qt.AlignCenter)
		self.tmfpdlbl.setObjectName("tmfpdlbl")
		self.tmfpdbtn = QtWidgets.QPushButton(self.groupBox_7)
		self.tmfpdbtn.setGeometry(QtCore.QRect(157, 58, 75, 40))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.tmfpdbtn.setFont(font)
		self.tmfpdbtn.setObjectName("tmfpdbtn")
		self.label_30 = QtWidgets.QLabel(self.groupBox_7)
		self.label_30.setGeometry(QtCore.QRect(6, 112, 60, 30))
		self.label_30.setObjectName("label_30")
		self.tctmfpdlbl = QtWidgets.QLabel(self.groupBox_7)
		self.tctmfpdlbl.setGeometry(QtCore.QRect(68, 112, 150, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setUnderline(True)
		font.setWeight(75)
		self.tctmfpdlbl.setFont(font)
		self.tctmfpdlbl.setStyleSheet("color: rgb(255, 0, 0);\n"
									  "border-color: rgb(0, 0, 255);\n"
									  "background-color: rgb(255, 255, 255);")
		self.tctmfpdlbl.setText("")
		self.tctmfpdlbl.setAlignment(QtCore.Qt.AlignCenter)
		self.tctmfpdlbl.setObjectName("tctmfpdlbl")
		self.line_8 = QtWidgets.QFrame(self.groupBox_7)
		self.line_8.setGeometry(QtCore.QRect(-10, 97, 240, 20))
		self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_8.setObjectName("line_8")
		self.line_9 = QtWidgets.QFrame(self.groupBox_7)
		self.line_9.setGeometry(QtCore.QRect(-9, 40, 240, 20))
		self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_9.setObjectName("line_9")
		self.line_21 = QtWidgets.QFrame(self.groupBox_7)
		self.line_21.setGeometry(QtCore.QRect(118, 60, 3, 40))
		self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_21.setObjectName("line_21")
		self.groupBox_33 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_33.setGeometry(QtCore.QRect(10, 188, 251, 101))
		self.groupBox_33.setTitle("")
		self.groupBox_33.setObjectName("groupBox_33")
		self.loctextlbl = QtWidgets.QLabel(self.groupBox_33)
		self.loctextlbl.setGeometry(QtCore.QRect(5, 8, 241, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.loctextlbl.setFont(font)
		self.loctextlbl.setAlignment(QtCore.Qt.AlignCenter)
		self.loctextlbl.setObjectName("loctextlbl")
		self.loclbl = QtWidgets.QLabel(self.groupBox_33)
		self.loclbl.setGeometry(QtCore.QRect(16, 57, 70, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setUnderline(True)
		font.setWeight(75)
		self.loclbl.setFont(font)
		self.loclbl.setStyleSheet("color: rgb(255, 0, 0);\n"
								  "border-color: rgb(0, 0, 255);\n"
								  "background-color: rgb(255, 255, 255);")
		self.loclbl.setText("")
		self.loclbl.setAlignment(QtCore.Qt.AlignCenter)
		self.loclbl.setObjectName("loclbl")
		self.locbtn = QtWidgets.QPushButton(self.groupBox_33)
		self.locbtn.setGeometry(QtCore.QRect(160, 52, 75, 40))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.locbtn.setFont(font)
		self.locbtn.setObjectName("locbtn")
		self.line_233 = QtWidgets.QFrame(self.groupBox_33)
		self.line_233.setGeometry(QtCore.QRect(-2, 36, 240, 20))
		self.line_233.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_233.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_233.setObjectName("line_233")
		self.line_243 = QtWidgets.QFrame(self.groupBox_33)
		self.line_243.setGeometry(QtCore.QRect(118, 52, 3, 40))
		self.line_243.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_243.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_243.setObjectName("line_243")
		self.tclbl = QtWidgets.QLabel(self.centralwidget)
		self.tclbl.setGeometry(QtCore.QRect(700, 411, 100, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setUnderline(True)
		font.setWeight(75)
		self.tclbl.setFont(font)
		self.tclbl.setStyleSheet("color: rgb(255, 0, 0);\n"
								 "border-color: rgb(0, 0, 255);\n"
								 "background-color: rgb(255, 255, 255);")
		self.tclbl.setText("")
		self.tclbl.setAlignment(QtCore.Qt.AlignCenter)
		self.tclbl.setObjectName("tclbl")
		self.cnmncbtn = QtWidgets.QPushButton(self.centralwidget)
		self.cnmncbtn.setGeometry(QtCore.QRect(549, 99, 260, 50))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.cnmncbtn.setFont(font)
		self.cnmncbtn.setObjectName("cnmncbtn")
		self.cnmecbtn = QtWidgets.QPushButton(self.centralwidget)
		self.cnmecbtn.setGeometry(QtCore.QRect(549, 149, 260, 50))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.cnmecbtn.setFont(font)
		self.cnmecbtn.setObjectName("cnmecbtn")
		self.line = QtWidgets.QFrame(self.centralwidget)
		self.line.setGeometry(QtCore.QRect(-6, 19, 820, 3))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(-6, 19, 821, 31))
		font = QtGui.QFont()
		font.setPointSize(18)
		font.setBold(True)
		font.setItalic(False)
		font.setUnderline(True)
		font.setWeight(75)
		font.setStrikeOut(False)
		self.label_3.setFont(font)
		self.label_3.setStyleSheet("color: rgb(44, 0, 132);")
		self.label_3.setAlignment(QtCore.Qt.AlignCenter)
		self.label_3.setObjectName("label_3")
		self.line_12 = QtWidgets.QFrame(self.centralwidget)
		self.line_12.setGeometry(QtCore.QRect(2, 295, 260, 3))
		self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_12.setObjectName("line_12")
		self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_4.setGeometry(QtCore.QRect(280, 230, 251, 100))
		self.groupBox_4.setTitle("")
		self.groupBox_4.setObjectName("groupBox_4")
		self.label_14 = QtWidgets.QLabel(self.groupBox_4)
		self.label_14.setGeometry(QtCore.QRect(0, 4, 250, 40))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_14.setFont(font)
		self.label_14.setAlignment(QtCore.Qt.AlignCenter)
		self.label_14.setObjectName("label_14")
		self.tmfwpdlbl = QtWidgets.QLabel(self.groupBox_4)
		self.tmfwpdlbl.setGeometry(QtCore.QRect(10, 58, 70, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setUnderline(True)
		font.setWeight(75)
		self.tmfwpdlbl.setFont(font)
		self.tmfwpdlbl.setStyleSheet("color: rgb(255, 0, 0);\n"
									 "border-color: rgb(0, 0, 255);\n"
									 "background-color: rgb(255, 255, 255);")
		self.tmfwpdlbl.setText("")
		self.tmfwpdlbl.setAlignment(QtCore.Qt.AlignCenter)
		self.tmfwpdlbl.setObjectName("tmfwpdlbl")
		self.tmfwpdbtn = QtWidgets.QPushButton(self.groupBox_4)
		self.tmfwpdbtn.setGeometry(QtCore.QRect(159, 52, 75, 40))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.tmfwpdbtn.setFont(font)
		self.tmfwpdbtn.setObjectName("tmfwpdbtn")
		self.line_15 = QtWidgets.QFrame(self.groupBox_4)
		self.line_15.setGeometry(QtCore.QRect(-9, 37, 240, 20))
		self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_15.setObjectName("line_15")
		self.line_20 = QtWidgets.QFrame(self.groupBox_4)
		self.line_20.setGeometry(QtCore.QRect(118, 52, 3, 40))
		self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_20.setObjectName("line_20")
		self.line_2 = QtWidgets.QFrame(self.centralwidget)
		self.line_2.setGeometry(QtCore.QRect(-5, 59, 820, 3))
		self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.tpsplbl = QtWidgets.QLabel(self.centralwidget)
		self.tpsplbl.setGeometry(QtCore.QRect(700, 371, 100, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setUnderline(True)
		font.setWeight(75)
		self.tpsplbl.setFont(font)
		self.tpsplbl.setStyleSheet("color: rgb(255, 0, 0);\n"
								   "border-color: rgb(0, 0, 255);\n"
								   "background-color: rgb(255, 255, 255);")
		self.tpsplbl.setText("")
		self.tpsplbl.setAlignment(QtCore.Qt.AlignCenter)
		self.tpsplbl.setObjectName("tpsplbl")
		self.label_35 = QtWidgets.QLabel(self.centralwidget)
		self.label_35.setGeometry(QtCore.QRect(549, 371, 140, 30))
		self.label_35.setObjectName("label_35")
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(548, 69, 261, 16))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setUnderline(True)
		font.setWeight(75)
		self.label_5.setFont(font)
		self.label_5.setAlignment(QtCore.Qt.AlignCenter)
		self.label_5.setObjectName("label_5")
		self.line_10 = QtWidgets.QFrame(self.centralwidget)
		self.line_10.setGeometry(QtCore.QRect(269, 69, 3, 440))
		self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_10.setObjectName("line_10")
		self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_6.setGeometry(QtCore.QRect(280, 69, 251, 150))
		self.groupBox_6.setTitle("")
		self.groupBox_6.setObjectName("groupBox_6")
		self.label_24 = QtWidgets.QLabel(self.groupBox_6)
		self.label_24.setGeometry(QtCore.QRect(5, 8, 241, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_24.setFont(font)
		self.label_24.setAlignment(QtCore.Qt.AlignCenter)
		self.label_24.setObjectName("label_24")
		self.tmuplbl = QtWidgets.QLabel(self.groupBox_6)
		self.tmuplbl.setGeometry(QtCore.QRect(11, 64, 70, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setUnderline(True)
		font.setWeight(75)
		self.tmuplbl.setFont(font)
		self.tmuplbl.setStyleSheet("color: rgb(255, 0, 0);\n"
								   "border-color: rgb(0, 0, 255);\n"
								   "background-color: rgb(255, 255, 255);")
		self.tmuplbl.setText("")
		self.tmuplbl.setAlignment(QtCore.Qt.AlignCenter)
		self.tmuplbl.setObjectName("tmuplbl")
		self.tmupbtn = QtWidgets.QPushButton(self.groupBox_6)
		self.tmupbtn.setGeometry(QtCore.QRect(157, 58, 75, 40))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.tmupbtn.setFont(font)
		self.tmupbtn.setObjectName("tmupbtn")
		self.label_26 = QtWidgets.QLabel(self.groupBox_6)
		self.label_26.setGeometry(QtCore.QRect(6, 113, 60, 30))
		self.label_26.setObjectName("label_26")
		self.tctmuplbl = QtWidgets.QLabel(self.groupBox_6)
		self.tctmuplbl.setGeometry(QtCore.QRect(68, 113, 150, 30))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setUnderline(True)
		font.setWeight(75)
		self.tctmuplbl.setFont(font)
		self.tctmuplbl.setStyleSheet("color: rgb(255, 0, 0);\n"
									 "border-color: rgb(0, 0, 255);\n"
									 "background-color: rgb(255, 255, 255);")
		self.tctmuplbl.setText("")
		self.tctmuplbl.setAlignment(QtCore.Qt.AlignCenter)
		self.tctmuplbl.setObjectName("tctmuplbl")
		self.line_6 = QtWidgets.QFrame(self.groupBox_6)
		self.line_6.setGeometry(QtCore.QRect(-3, 97, 240, 20))
		self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_6.setObjectName("line_6")
		self.line_7 = QtWidgets.QFrame(self.groupBox_6)
		self.line_7.setGeometry(QtCore.QRect(-3, 40, 240, 20))
		self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_7.setObjectName("line_7")
		self.line_19 = QtWidgets.QFrame(self.groupBox_6)
		self.line_19.setGeometry(QtCore.QRect(119, 60, 3, 40))
		self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_19.setObjectName("line_19")
		self.label_6 = QtWidgets.QLabel(self.centralwidget)
		self.label_6.setGeometry(QtCore.QRect(613, 3, 70, 13))
		self.label_6.setObjectName("label_6")
		self.datetimelbl = QtWidgets.QLabel(self.centralwidget)
		self.datetimelbl.setGeometry(QtCore.QRect(682, 3, 130, 13))
		self.datetimelbl.setText("")
		self.datetimelbl.setObjectName("datetimelbl")
		self.line_22 = QtWidgets.QFrame(self.centralwidget)
		self.line_22.setGeometry(QtCore.QRect(275, 337, 260, 3))
		self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_22.setObjectName("line_22")
		self.reportbtn = QtWidgets.QPushButton(self.centralwidget)
		self.reportbtn.setGeometry(QtCore.QRect(549, 250, 260, 60))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.reportbtn.setFont(font)
		self.reportbtn.setObjectName("reportbtn")
		self.refreshbtn = QtWidgets.QPushButton(self.centralwidget)
		self.refreshbtn.setGeometry(QtCore.QRect(548, 459, 100, 50))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(95)
		self.refreshbtn.setFont(font)
		self.refreshbtn.setObjectName("reportbtn")
		self.refreshbtn.setStyleSheet("color: rgb(255, 255, 255);\n"
									  "background-color: rgb(0, 203, 0);")
		MMainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MMainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 21))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
		self.menubar.setSizePolicy(sizePolicy)
		self.menubar.setMaximumSize(QtCore.QSize(16777215, 16777215))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.menubar.setFont(font)
		self.menubar.setAcceptDrops(False)
		self.menubar.setStyleSheet("")
		self.menubar.setObjectName("menubar")

		self.menuFile = QtWidgets.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")

		self.menuCustomer = QtWidgets.QMenu(self.menubar)
		self.menuCustomer.setObjectName("menuCustomer")

		self.menuRaw_Material = QtWidgets.QMenu(self.menubar)
		self.menuRaw_Material.setObjectName("menuRaw_Material")

		self.menuSpare_Parts = QtWidgets.QMenu(self.menubar)
		self.menuSpare_Parts.setObjectName("menuSpare_Parts")

		self.menuTools = QtWidgets.QMenu(self.menubar)
		self.menuTools.setObjectName("menuTools")

		self.menuFP = QtWidgets.QMenu(self.menubar)
		self.menuFP.setObjectName("menuFB")

		self.menuoutbound = QtWidgets.QMenu(self.menubar)
		self.menuoutbound.setObjectName("menuoutbound")

		MMainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MMainWindow)
		self.statusbar.setObjectName("statusbar")
		MMainWindow.setStatusBar(self.statusbar)

		self.actionAddEmpl = QtWidgets.QAction(MMainWindow)
		self.actionAddEmpl.setObjectName("actionAddEmpl")

		self.actionAddUser = QtWidgets.QAction(MMainWindow)
		self.actionAddUser.setObjectName("actionAddUser")

		self.actionLogout = QtWidgets.QAction(MMainWindow)
		self.actionLogout.setObjectName("actionLogout")

		self.actionChange_Password = QtWidgets.QAction(MMainWindow)
		self.actionChange_Password.setObjectName("actionChange_Password")

		self.actionExit = QtWidgets.QAction(MMainWindow)
		self.actionExit.setObjectName("actionExit")

		self.actionAdd_New_customer = QtWidgets.QAction(MMainWindow)
		self.actionAdd_New_customer.setObjectName("actionAdd_New_customer")

		self.actionEdit_customer = QtWidgets.QAction(MMainWindow)
		self.actionEdit_customer.setObjectName("actionEdit_customer")

		self.actionSearch_customer = QtWidgets.QAction(MMainWindow)
		self.actionSearch_customer.setObjectName("actionSearch_customer")

		self.actionRports = QtWidgets.QAction(MMainWindow)
		self.actionRports.setObjectName("actionRports")

		self.actionAdd_New_2 = QtWidgets.QAction(MMainWindow)
		self.actionAdd_New_2.setObjectName("actionAdd_New_2")

		self.actionEdit_2 = QtWidgets.QAction(MMainWindow)
		self.actionEdit_2.setObjectName("actionEdit_2")

		self.actionSearch_2 = QtWidgets.QAction(MMainWindow)
		self.actionSearch_2.setObjectName("actionSearch_2")

		self.actionReports = QtWidgets.QAction(MMainWindow)
		self.actionReports.setObjectName("actionReports")

		self.actionAdd_New_RM = QtWidgets.QAction(MMainWindow)
		self.actionAdd_New_RM.setObjectName("actionAdd_New_RM")

		self.actionEdit_RM = QtWidgets.QAction(MMainWindow)
		self.actionEdit_RM.setObjectName("actionEdit_RM")

		self.actionSearch_RM = QtWidgets.QAction(MMainWindow)
		self.actionSearch_RM.setObjectName("actionSearch_RM")

		self.actionReports_2 = QtWidgets.QAction(MMainWindow)
		self.actionReports_2.setObjectName("actionReports_2")

		self.actionAdd_New_SP = QtWidgets.QAction(MMainWindow)
		self.actionAdd_New_SP.setObjectName("actionAdd_New_SP")

		self.actionEdit_SP = QtWidgets.QAction(MMainWindow)
		self.actionEdit_SP.setObjectName("actionEdit_SP")

		self.actionSearch_SP = QtWidgets.QAction(MMainWindow)
		self.actionSearch_SP.setObjectName("actionSearch_SP")

		self.actionReports_3 = QtWidgets.QAction(MMainWindow)
		self.actionReports_3.setObjectName("actionReports_3")

		self.actionAdd_TO = QtWidgets.QAction(MMainWindow)
		self.actionAdd_TO.setObjectName("actionAdd_TO")

		self.actionEdit_TO = QtWidgets.QAction(MMainWindow)
		self.actionEdit_TO.setObjectName("actionEdit_TO")

		self.actionSearch_TO = QtWidgets.QAction(MMainWindow)
		self.actionSearch_TO.setObjectName("actionSearch_TO")

		self.actionAdd_FP = QtWidgets.QAction(MMainWindow)
		self.actionAdd_FP.setObjectName("actionAdd_FP")

		self.actionEdit_FP = QtWidgets.QAction(MMainWindow)
		self.actionEdit_FP.setObjectName("actionEdit_FP")

		self.actionSearch_FP = QtWidgets.QAction(MMainWindow)
		self.actionSearch_FP.setObjectName("actionSearch_FP")

		self.actionAdd_New_OB = QtWidgets.QAction(MMainWindow)
		self.actionAdd_New_OB.setObjectName("actionAdd_New_OB")

		self.actionSearch_OB = QtWidgets.QAction(MMainWindow)
		self.actionSearch_OB.setObjectName("actionSearch_OB")

		self.menuFile.addAction(self.actionAddEmpl)
		self.menuFile.addAction(self.actionAddUser)
		self.menuFile.addAction(self.actionLogout)
		self.menuFile.addAction(self.actionChange_Password)
		self.menuFile.addAction(self.actionExit)

		self.menuCustomer.addAction(self.actionAdd_New_customer)
		self.menuCustomer.addAction(self.actionEdit_customer)
		self.menuCustomer.addAction(self.actionSearch_customer)

		self.menuRaw_Material.addAction(self.actionAdd_New_RM)
		self.menuRaw_Material.addAction(self.actionEdit_RM)
		self.menuRaw_Material.addAction(self.actionSearch_RM)

		self.menuSpare_Parts.addAction(self.actionAdd_New_SP)
		self.menuSpare_Parts.addAction(self.actionEdit_SP)
		self.menuSpare_Parts.addAction(self.actionSearch_SP)

		self.menuTools.addAction(self.actionAdd_TO)
		self.menuTools.addAction(self.actionEdit_TO)
		self.menuTools.addAction(self.actionSearch_TO)

		self.menuFP.addAction(self.actionAdd_FP)
		self.menuFP.addAction(self.actionEdit_FP)
		self.menuFP.addAction(self.actionSearch_FP)

		self.menuoutbound.addAction(self.actionAdd_New_OB)
		self.menuoutbound.addAction(self.actionSearch_OB)

		self.menubar.addAction(self.menuFile.menuAction())
		self.menubar.addAction(self.menuCustomer.menuAction())
		self.menubar.addAction(self.menuRaw_Material.menuAction())
		self.menubar.addAction(self.menuSpare_Parts.menuAction())
		self.menubar.addAction(self.menuTools.menuAction())
		self.menubar.addAction(self.menuFP.menuAction())
		self.menubar.addAction(self.menuoutbound.menuAction())

		# get logged user name
		self.loggeduserlbl.setText(getLoginDataPKL()['name'])
		# hid add labor cost button
		self.alocmbtn.setVisible(False)
		self.datetimelbl.setText(timestampstr)
		# actions of menu bar

		## file menu actions
		self.actionAddEmpl.triggered.connect(self.openAddEmplDialog)
		self.actionAddUser.triggered.connect(self.openAddUser)
		self.actionLogout.triggered.connect(self.doLogout)
		self.actionChange_Password.triggered.connect(self.openChangePasswordDialog)
		self.actionExit.triggered.connect(self.doExit)
		## customer menu actions
		self.actionAdd_New_customer.triggered.connect(self.openCreateNewCustomerDialog)
		self.actionEdit_customer.triggered.connect(self.openEditCustomerDialog)
		self.actionSearch_customer.triggered.connect(self.openSearchCustomerDialog)
		##raw material menu actions
		self.actionAdd_New_RM.triggered.connect(self.openCreateNewRawMaterial)
		self.actionEdit_RM.triggered.connect(self.openEditeNewRawMaterial)
		self.actionSearch_RM.triggered.connect(self.openSearchNewRawMaterial)
		## spare parts menu actions
		self.actionAdd_New_SP.triggered.connect(self.openCreateNewSparePart)
		self.actionEdit_SP.triggered.connect(self.openEditeNewSparePart)
		self.actionSearch_SP.triggered.connect(self.openSearchSparePart)

		self.actionAdd_FP.triggered.connect(self.openCreateNewFinishProduct)
		# labels counting

		self.tmplbl.setText(str(len(getMaintenancePused())))
		self.tmhlbl.setText(str(len(getMaintenanceHolded())))
		self.tmuplbl.setText(str(len(getMaintenanceUnderProccessing())))
		self.tmfwpdlbl.setText(str(len(getMaintenanceWaitingDelevary())))
		self.tmfpdlbl.setText(str(len(getMaintenanceFinishedAndDelivared())))
		self.loclbl.setText(str(len(getMaintenanceWaitLaborCost())))
		# label cost counting
		self.tctmhlbl.setText(str(getMaintenanceCalcCost()))
		self.tctmuplbl.setText(str(getMaintenanceUnderProccessingCost()))
		self.tctmfpdlbl.setText(str(getMaintenanceFinishedAndDelivaredCost()))
		self.tprmlbl.setText(str(len(select_all_raw_material())))
		self.tpsplbl.setText(str(len(select_all_spare_parts())))
		self.tclbl.setText(str(len(select_all_customers())))
		# buttons actions
		self.closebtn.clicked.connect(self.doExit)
		self.tmpbtn.clicked.connect(self.openPusedMaintenance)
		self.locbtn.clicked.connect(self.openLaborCostHoldedMaintenance)
		self.tmhbtn.clicked.connect(self.openConfirmHoldedMaintenance)
		self.tmupbtn.clicked.connect(self.openUnderProcessMaintenance)
		self.tmfwpdbtn.clicked.connect(self.openDelivaryWaitingMaintenance)
		self.tmfpdbtn.clicked.connect(self.openLastMaintenance)
		self.cnmncbtn.clicked.connect(self.openNewNaintenanceWithNewCustomer)
		self.cnmecbtn.clicked.connect(self.openNewNaintenanceExtCustomer)
		self.retranslateUi(MMainWindow)
		QtCore.QMetaObject.connectSlotsByName(MMainWindow)
		self.refreshbtn.clicked.connect(self.do_refresh)
		self.reportbtn.clicked.connect(self.openReports)

		self.actionAdd_FP.triggered.connect(self.openCreateNewFinishProduct)
		self.actionEdit_FP.triggered.connect(self.openEditNewFinishProduct)
		self.actionSearch_FP.triggered.connect(self.openSearchNewFinishProduct)

		self.actionAdd_TO.triggered.connect(self.openCreateNewTools)
		self.actionEdit_TO.triggered.connect(self.openEditeTools)
		self.actionSearch_TO.triggered.connect(self.openSearchTools)

		self.actionAdd_New_OB.triggered.connect(self.openNewOB)
		self.actionSearch_OB.triggered.connect(self.openSreachOB)

		# role handel
		role = getLoginDataPKL()['role']
		if int(role) == 2 or int(role) == 3:
			# labels
			self.label_18.setVisible(False)
			self.tctmhlbl.setVisible(False)
			self.label_26.setVisible(False)
			self.tctmuplbl.setVisible(False)
			self.label_30.setVisible(False)
			self.tctmfpdlbl.setVisible(False)

			# Botton
			self.tmhbtn.setEnabled(False)
			self.tmfpdbtn.setEnabled(False)
			self.alocmbtn.setEnabled(False)
			self.locbtn.setEnabled(False)

			# Actions
			self.actionAddUser.setEnabled(False)
			self.actionEdit_customer.setEnabled(False)
			self.actionAddEmpl.setEnabled(False)

		if int(role) == 3:
			# Botton
			self.tmupbtn.setEnabled(False)

		if int(role) == 2:
			# Botton
			self.tmpbtn.setEnabled(False)
			self.tmfwpdbtn.setEnabled(False)
			self.cnmncbtn.setEnabled(False)
			self.cnmecbtn.setEnabled(False)
			self.reportbtn.setEnabled(False)

			# Actions
			self.actionAdd_New_RM.setEnabled(False)
			self.actionEdit_RM.setEnabled(False)
			self.actionAdd_New_SP.setEnabled(False)
			self.actionEdit_SP.setEnabled(False)
			self.actionAdd_FP.setEnabled(False)
			self.actionEdit_FP.setEnabled(False)
			self.actionAdd_TO.setEnabled(False)
			self.actionEdit_TO.setEnabled(False)

		if int(role) == 1:
			# Button
			# self.alocmbtn.setEnabled(False)
			# self.locbtn.setEnabled(False)
			self.tmpbtn.setEnabled(False)
			self.actionAddUser.setEnabled(False)
			self.cnmncbtn.setEnabled(False)
			self.cnmecbtn.setEnabled(False)
			self.tmhbtn.setEnabled(False)
			self.tmupbtn.setEnabled(False)
			self.tmfwpdbtn.setEnabled(False)

			# Actions
			self.actionAdd_New_RM.setEnabled(False)
			self.actionAdd_New_SP.setEnabled(False)
			self.actionAdd_FP.setEnabled(False)
			self.actionAdd_TO.setEnabled(False)

	def retranslateUi(self, MMainWindow):
		_translate = QtCore.QCoreApplication.translate
		MMainWindow.setWindowTitle(_translate("MMainWindow", "Maintenance System"))
		self.alocmbtn.setText(_translate("MMainWindow", "Add Labor & Other Cost\'s For Maintenance"))
		self.label_33.setText(_translate("MMainWindow", "Total Piece\'s of  Raw Materials:"))
		self.label.setText(_translate("MMainWindow", "Welcome ,"))
		self.label_4.setText(_translate("MMainWindow", "Total of Maintenance\'s Pused \n"
													   " Not Have BOM"))
		self.tmpbtn.setText(_translate("MMainWindow", "Browse"))
		self.label_10.setText(_translate("MMainWindow", "Total of Maintenance\'s Hold \n"
														" waiting for customer confirm"))
		self.tmhbtn.setText(_translate("MMainWindow", "Browse"))
		self.label_18.setText(_translate("MMainWindow", "Total Cost :"))
		self.label_37.setText(_translate("MMainWindow", "Total Of Customers :"))
		self.closebtn.setText(_translate("MMainWindow", "Close"))
		self.label_28.setText(_translate("MMainWindow", "Total of Maintenance\'s \n"
														" was finisehed and product delivary"))
		self.tmfpdbtn.setText(_translate("MMainWindow", "Browse"))
		self.label_30.setText(_translate("MMainWindow", "Total Cost :"))
		self.cnmncbtn.setText(_translate("MMainWindow", "Create New Maintenance with New Customer"))
		self.cnmecbtn.setText(_translate("MMainWindow", "Create New Maintenance for Exists Customer"))
		self.label_3.setText(_translate("MMainWindow", "Maintenance Dashboard"))
		self.label_14.setText(_translate("MMainWindow", "Total of Maintenance\'s was finisehed \n"
														" waiting for product delivary"))
		self.tmfwpdbtn.setText(_translate("MMainWindow", "Browse"))
		self.label_35.setText(_translate("MMainWindow", "Total Piece\'s of Spare Parts :"))
		self.label_5.setText(_translate("MMainWindow", "Direct Action\'s"))
		self.label_24.setText(_translate("MMainWindow", "Total of Maitenance\'s \n"
														" Under Proccessing"))
		self.tmupbtn.setText(_translate("MMainWindow", "Browse"))
		self.label_26.setText(_translate("MMainWindow", "Total Cost :"))
		self.label_6.setText(_translate("MMainWindow", "Date & Time :"))
		self.reportbtn.setText(_translate("MMainWindow", "Reports"))
		self.menuFile.setTitle(_translate("MMainWindow", "File"))
		self.menuCustomer.setTitle(_translate("MMainWindow", "Customer"))
		self.menuRaw_Material.setTitle(_translate("MMainWindow", "Raw Material"))
		self.menuSpare_Parts.setTitle(_translate("MMainWindow", "Spare Parts"))
		self.actionAddEmpl.setText(_translate("MMainWindow", "Add Employee"))
		self.actionAddUser.setText(_translate("MMainWindow", "Add User"))
		self.actionLogout.setText(_translate("MMainWindow", "Logout"))
		self.actionChange_Password.setText(_translate("MMainWindow", "Change Password"))
		self.actionExit.setText(_translate("MMainWindow", "Exit"))
		self.actionAdd_New_customer.setText(_translate("MMainWindow", "Add New"))
		self.actionEdit_customer.setText(_translate("MMainWindow", "Edit"))
		self.actionSearch_customer.setText(_translate("MMainWindow", "Search"))
		self.actionRports.setText(_translate("MMainWindow", "Reports"))
		self.actionAdd_New_2.setText(_translate("MMainWindow", "Add New"))
		self.actionEdit_2.setText(_translate("MMainWindow", "Edit"))
		self.actionSearch_2.setText(_translate("MMainWindow", "Search"))
		self.actionReports.setText(_translate("MMainWindow", "Reports"))
		self.actionAdd_New_RM.setText(_translate("MMainWindow", "Add New"))
		self.actionEdit_RM.setText(_translate("MMainWindow", "Edit"))
		self.actionSearch_RM.setText(_translate("MMainWindow", "Search"))
		self.actionReports_2.setText(_translate("MMainWindow", "Reports"))

		self.menuTools.setTitle(_translate("MMainWindow", "Tools"))
		self.menuFP.setTitle(_translate("MMainWindow", "Finish Product"))
		self.menuoutbound.setTitle(_translate("MMainWindow", "Outbound"))

		self.actionAdd_New_SP.setText(_translate("MMainWindow", "Add New"))
		self.actionEdit_SP.setText(_translate("MMainWindow", "Edit"))
		self.actionSearch_SP.setText(_translate("MMainWindow", "Search"))

		self.actionAdd_TO.setText(_translate("MMainWindow", "Add New"))
		self.actionEdit_TO.setText(_translate("MMainWindow", "Edit"))
		self.actionSearch_TO.setText(_translate("MMainWindow", "Search"))

		self.actionAdd_FP.setText(_translate("MMainWindow", "Add New"))
		self.actionEdit_FP.setText(_translate("MMainWindow", "Edit"))
		self.actionSearch_FP.setText(_translate("MMainWindow", "Search"))

		self.actionAdd_New_OB.setText(_translate("MMainWindow", "Add New"))
		self.actionSearch_OB.setText(_translate("MMainWindow", "Search"))

		self.actionReports_3.setText(_translate("MMainWindow", "Reports"))
		self.loctextlbl.setText(_translate("MMainWindow", "Total of Maintenance\'s\n"
														  " Without Labor Cost"))
		self.locbtn.setText(_translate("MMainWindow", "Browse"))
		self.refreshbtn.setText(_translate("MMainWindow", "Refresh"))

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
		self.chPass_dialog.exec_()

	def openAddEmplDialog(self):
		from uiview.ui_addemployee import Ui_addemplDialog
		self.chPass_dialog = Ui_addemplDialog()
		self.chPass_dialog.exec_()

	def openCreateNewCustomerDialog(self):
		from uiview.ui_createNewCustomer import Ui_createNewCustomer
		self.cnc_dialog = Ui_createNewCustomer()
		self.cnc_dialog.exec_()

	def openEditCustomerDialog(self):
		from uiview.ui_updateCustomer import Ui_updateCustomer
		self.upc_dialog = Ui_updateCustomer()
		self.upc_dialog.exec_()

	def openSearchCustomerDialog(self):
		from uiview.ui_deleteCustomer import Ui_deleteCustomer
		self.cnc_dialog = Ui_deleteCustomer()
		self.cnc_dialog.exec_()

	def openCreateNewRawMaterial(self):
		from uiview.ui_addNewRMType import Ui_addNewRMTypeDialog
		self.di = Ui_addNewRMTypeDialog()
		self.di.exec_()

	def openEditeNewRawMaterial(self):
		from uiview.ui_updateNewRM import Ui_editRWDialog
		self.di = Ui_editRWDialog()
		self.di.exec_()

	def openSearchNewRawMaterial(self):
		from uiview.ui_searchRM import Ui_searchRMDialog
		self.di = Ui_searchRMDialog()
		self.di.exec_()

	def openCreateNewSparePart(self):
		from uiview.ui_addNewSPType import Ui_addNewSPTypeDialog
		self.di = Ui_addNewSPTypeDialog()
		self.di.exec_()

	def openEditeNewSparePart(self):
		from uiview.ui_updateNewSP import Ui_editSPDialog
		self.di = Ui_editSPDialog()
		self.di.exec_()

	def openSearchSparePart(self):
		from uiview.ui_searchSP import Ui_searchSPDialog
		self.di = Ui_searchSPDialog()
		self.di.exec_()

	def openCreateNewFinishProduct(self):
		from uiview.ui_addNewFPType import Ui_addNewFPTypeDialog
		self.di = Ui_addNewFPTypeDialog()
		self.di.exec_()

	def openEditNewFinishProduct(self):
		from uiview.ui_updateNewFP import Ui_editFPDialog
		self.di = Ui_editFPDialog()
		self.di.exec_()

	def openSearchNewFinishProduct(self):
		from uiview.ui_searchFP import Ui_searchFPDialog
		self.di = Ui_searchFPDialog()
		self.di.exec_()

	def openCreateNewTools(self):
		from uiview.ui_addNewTOType import Ui_addNewTOTypeDialog
		self.di = Ui_addNewTOTypeDialog()
		self.di.exec_()

	def openEditeTools(self):
		from uiview.ui_updateNewTO import Ui_editTODialog
		self.di = Ui_editTODialog()
		self.di.exec_()

	def openSearchTools(self):
		from uiview.ui_searchTO import Ui_searchTODialog
		self.di = Ui_searchTODialog()
		self.di.exec_()

	def openNewOB(self):
		from uiview.ui_oubound import Ui_createOBDialog
		self.di = Ui_createOBDialog()
		self.di.exec_()

	def openSreachOB(self):
		from uiview.ui_obsearch import Ui_OBsearch
		self.di = Ui_OBsearch()
		self.di.exec_()

	def openPusedMaintenance(self):
		from uiview.ui_pusedMaintenance import Ui_pusedMaintenanceDialog
		self.pmd = Ui_pusedMaintenanceDialog()
		self.pmd.exec_()

	def openLaborCostHoldedMaintenance(self):
		from uiview.ui_costHMaintenance import Ui_costHoldedMaintenanceDialog
		self.pmd = Ui_costHoldedMaintenanceDialog()
		self.pmd.exec_()

	def openConfirmHoldedMaintenance(self):
		from uiview.ui_confirmWMaintenance import Ui_confirmWMaintenanceDialog
		self.pmd = Ui_confirmWMaintenanceDialog()
		self.pmd.exec_()

	def openUnderProcessMaintenance(self):
		from uiview.ui_finishMaintenance import Ui_finishMaintenanceDialog
		self.pmd = Ui_finishMaintenanceDialog()
		self.pmd.exec_()

	def openDelivaryWaitingMaintenance(self):
		from uiview.ui_delivaryWMaintenance import Ui_delivaryMaintenanceDialog
		self.pmd = Ui_delivaryMaintenanceDialog()
		self.pmd.exec_()

	def openLastMaintenance(self):
		from uiview.ui_lastMaintenance import Ui_lastMaintenanceDialog
		self.pmd = Ui_lastMaintenanceDialog()
		self.pmd.exec_()

	def openNewNaintenanceWithNewCustomer(self):
		from uiview.ui_createNewCustomerWithMaintenance import Ui_createNewCustomerWithMaintenance
		self.pmd = Ui_createNewCustomerWithMaintenance()
		self.pmd.exec_()

	def openNewNaintenanceExtCustomer(self):
		from uiview.ui_createNewMaintExsistCust import Ui_createNewMaintenanceForExistsCustDialog
		self.pmd = Ui_createNewMaintenanceForExistsCustDialog()
		self.pmd.exec_()

	def openAddUser(self):
		from uiview.ui_addUser import Ui_adduserDialog
		self.ad = Ui_adduserDialog()
		self.ad.exec_()

	def do_refresh(self):
		self.datetimelbl.setText(timestampstr)

		# labels counting
		self.tmplbl.setText(str(len(getMaintenancePused())))
		self.tmhlbl.setText(str(len(getMaintenanceHolded())))
		self.tmuplbl.setText(str(len(getMaintenanceUnderProccessing())))
		self.tmfwpdlbl.setText(str(len(getMaintenanceWaitingDelevary())))
		self.tmfpdlbl.setText(str(len(getMaintenanceFinishedAndDelivared())))
		self.loclbl.setText(str(len(getMaintenanceWaitLaborCost())))

		# label cost counting
		self.tctmhlbl.setText(str(getMaintenanceCalcCost()))
		self.tctmuplbl.setText(str(getMaintenanceUnderProccessingCost()))
		self.tctmfpdlbl.setText(str(getMaintenanceFinishedAndDelivaredCost()))
		self.tprmlbl.setText(str(len(select_all_raw_material())))
		self.tpsplbl.setText(str(len(select_all_spare_parts())))
		self.tclbl.setText(str(len(select_all_customers())))

	def openReports(self):
		from uiview.ui_reporting import Ui_reportDialog
		self.pmd = Ui_reportDialog()
		self.pmd.exec_()


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	myapp = Ui_MMainWindow()
	myapp.show()
	app.exec_()
