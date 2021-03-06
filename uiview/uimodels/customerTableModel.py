from PyQt5.QtCore import *


class CustomerTableModel(QAbstractTableModel):
	"""Model class that drives the population of tabular display"""

	def __init__(self):
		super(CustomerTableModel, self).__init__()
		self.headers = ['Customer', 'Mobile Phone', 'Maint. Code']
		self.customers = []

	def rowCount(self, index=QModelIndex()):
		return len(self.customers)

	def addCustomer(self, customer):
		self.beginResetModel()
		self.customers.append(customer)
		self.endResetModel()

	def columnCount(self, index=QModelIndex()):
		return len(self.headers)

	def data(self, index, role=Qt.DisplayRole):
		col = index.column()
		customer = self.customers[index.row()]
		if role == Qt.DisplayRole:
			if col == 0:
				return QVariant(customer.name)
			elif col == 1:
				return QVariant(customer.mobile_number)
			elif col == 2:
				return QVariant(customer.gender)
			return QVariant()

	def headerData(self, section, orientation, role=Qt.DisplayRole):
		if role != Qt.DisplayRole:
			return QVariant()

		if orientation == Qt.Horizontal:
			return QVariant(self.headers[section])
		return QVariant(int(section + 1))
