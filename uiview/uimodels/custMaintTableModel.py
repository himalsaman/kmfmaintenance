import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class CustomerMaintenanceTableModel(QAbstractTableModel):
	"""Model class that drives the population of tabular display"""

	def __init__(self):
		super(CustomerMaintenanceTableModel, self).__init__()
		self.headers = ['Maint. Code','Product']
		self.maintenances = []

	def rowCount(self, index=QModelIndex()):
		return len(self.maintenances)

	def addMaintenance(self, maintenanc):
		self.beginResetModel()
		self.maintenances.append(maintenanc)
		self.endResetModel()

	def columnCount(self, index=QModelIndex()):
		return len(self.headers)

	def data(self, index, role=Qt.DisplayRole):
		col = index.column()
		maintenance = self.maintenances[index.row()]
		if role == Qt.DisplayRole:
			if col == 0:
				return QVariant(maintenance.m_code)
			elif col == 1:
				return QVariant(maintenance.product_of_maintenance)
			return QVariant()

	def headerData(self, section, orientation, role=Qt.DisplayRole):
		if role != Qt.DisplayRole:
			return QVariant()

		if orientation == Qt.Horizontal:
			return QVariant(self.headers[section])
		return QVariant(int(section + 1))