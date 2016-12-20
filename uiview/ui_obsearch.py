# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_obsearch.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtGui

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog

from Control.materialsControl import increaseToolsInvQty
from Control.ouboundControl import geAlltOutboun
from models.dbUtile import Outbound
from models.ouboundModel import select_outbound_by_code, update_oubound_status
from uiview.uimodels.outboundAllTableModel import OutboundAllTableModel


class Ui_OBsearch(QDialog):
	def __init__(self):
		super(Ui_OBsearch, self).__init__()
		self.setupUi(self)

	def setupUi(self, OBsearch):
		self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
		OBsearch.setObjectName("OBsearch")
		OBsearch.resize(788, 575)
		self.label = QtWidgets.QLabel(OBsearch)
		self.label.setGeometry(QtCore.QRect(14, 3, 47, 20))
		self.label.setObjectName("label")
		self.userlbl = QtWidgets.QLabel(OBsearch)
		self.userlbl.setGeometry(QtCore.QRect(64, 3, 190, 20))
		self.userlbl.setText("")
		self.userlbl.setObjectName("userlbl")
		self.line = QtWidgets.QFrame(OBsearch)
		self.line.setGeometry(QtCore.QRect(4, 23, 780, 3))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.tableView = QtWidgets.QTableView(OBsearch)
		self.tableView.setGeometry(QtCore.QRect(9, 30, 770, 490))
		self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.tableView.setTabKeyNavigation(False)
		self.tableView.setProperty("showDropIndicator", False)
		self.tableView.setDragDropOverwriteMode(False)
		self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
		self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.tableView.setObjectName("tableView")
		self.line_2 = QtWidgets.QFrame(OBsearch)
		self.line_2.setGeometry(QtCore.QRect(4, 524, 780, 3))
		self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.closebtn = QtWidgets.QPushButton(OBsearch)
		self.closebtn.setGeometry(QtCore.QRect(700, 530, 80, 40))
		self.closebtn.setObjectName("closebtn")
		self.tableDataShow()
		self.closebtn.clicked.connect(self.close)
		self.retranslateUi(OBsearch)
		QtCore.QMetaObject.connectSlotsByName(OBsearch)

	def retranslateUi(self, OBsearch):
		_translate = QtCore.QCoreApplication.translate
		OBsearch.setWindowTitle(_translate("OBsearch", "Search Outbound"))
		self.label.setText(_translate("OBsearch", "Welcome,"))
		self.closebtn.setText(_translate("OBsearch", "Close"))

	def tableDataShow(self):
		mylist = geAlltOutboun()
		if mylist != []:
			self.tableData = OutboundAllTableModel()
			self.tableView.setModel(self.tableData)
			for idx, val in enumerate(mylist):
				self.tableData.addItems(Outbound(val.code,
												 val.out_date,
												 None,
												 val.customer_id,
												 val.employee_id,
												 val.raw_material_id,  # raw
												 val.spare_part_id,  # spare
												 val.tools_id,  # tools
												 val.product_id,  # product
												 val.req_qty,  # qty
												 val.status))

		self.tableView.setColumnWidth(0, 100)
		self.tableView.setColumnWidth(1, 155)
		self.tableView.setColumnWidth(2, 70)
		self.tableView.setColumnWidth(3, 155)
		self.tableView.setColumnWidth(4, 85)
		self.tableView.setColumnWidth(5, 48)
		self.tableView.setColumnWidth(6, 70)
		self.tableView.setColumnWidth(7, 45)

	def refresheddata(self):
		self.tableData = OutboundAllTableModel()
		self.tableView.setModel(self.tableData)
		self.tableDataShow()

	def contextMenuEvent(self, event):
		self.menu = QtWidgets.QMenu(self)
		closeAction = QtWidgets.QAction('Close', self)
		closeAction.triggered.connect(self.closeSlot)
		self.menu.addAction(closeAction)
		# add other required actions
		self.menu.popup(QtGui.QCursor.pos())

	def closeSlot(self):
		indexes = self.tableView.selectionModel().selectedRows(0)
		for ind in sorted(indexes):
			outitem = select_outbound_by_code(ind.data())
			if outitem.status == 1:
				if outitem.tools:
					if outitem.tools.back == 1:
						increaseToolsInvQty(outitem.tools, outitem.req_qty)
				update_oubound_status(outitem.id, 0)
			self.refresheddata()
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myapp = Ui_OBsearch()
	myapp.exec_()
