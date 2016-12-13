from PyQt5.QtCore import *

from models.customersModel import select_customer_by_id
from models.employeeModel import select_employee_by_id
from models.finishProductsModel import select_finish_product_by_id
from models.rawMaterialModel import select_row_material_by_id
from models.sparePartsModel import select_spare_parts_by_id
from models.toolsModel import select_tools_by_id


class OutboundAllTableModel(QAbstractTableModel):
	"""Model class that drives the population of tabular display"""

	def __init__(self):
		super(OutboundAllTableModel, self).__init__()
		self.headers = ['Code', 'User Name', 'User Type', 'Item', 'Type', 'Qty', 'Out Date', 'Status']
		self.items = []

	def rowCount(self, index=QModelIndex()):
		return len(self.items)

	def addItems(self, item):
		self.beginResetModel()
		self.items.append(item)
		self.endResetModel()

	def columnCount(self, index=QModelIndex()):
		return len(self.headers)

	def data(self, index, role=Qt.DisplayRole):
		col = index.column()
		item = self.items[index.row()]

		if role == Qt.DisplayRole:
			if col == 0:
				return QVariant(item.code)
			if col == 1:
				if item.customer_id:
					cust = select_customer_by_id(item.customer_id)
					sname = cust.name
				if item.employee_id:
					empl = select_employee_by_id(item.employee_id)
					sname = empl.name
				return QVariant(sname)
			if col == 2:
				if item.customer_id:
					stype = "Customer"
				if item.employee_id:
					stype = "Employee"
				return QVariant(stype)
			elif col == 3:
				if item.raw_material_id:
					raw = select_row_material_by_id(item.raw_material_id)
					mname = raw.name
				if item.spare_part_id:
					spare = select_spare_parts_by_id(item.spare_part_id)
					mname = spare.name
				if item.tools_id:
					tool = select_tools_by_id(item.tools_id)
					mname = tool.name
				# return QVariant(mname)
				if item.product_id:
					tool = select_finish_product_by_id(item.product_id)
					mname = tool.name
				return QVariant(mname)
			elif col == 4:
				if item.raw_material_id:
					return QVariant('Raw Material')
				if item.spare_part_id:
					return QVariant('Spare Parts')
				if item.tools_id:
					return QVariant('Tools')
				if item.product_id:
					return QVariant('Finish Product')
			#
			elif col == 5:
				return QVariant(item.req_qty)
			elif col == 6:
				return QVariant(str(item.out_date.date()))
			elif col == 7:
				if item.status == 1:
					ssta = 'Open'
				if item.status == 0:
					ssta = 'Close'
				return QVariant(ssta)
			return QVariant()

	def headerData(self, section, orientation, role=Qt.DisplayRole):
		if role != Qt.DisplayRole:
			return QVariant()

		if orientation == Qt.Horizontal:
			return QVariant(self.headers[section])
		return QVariant(int(section + 1))
