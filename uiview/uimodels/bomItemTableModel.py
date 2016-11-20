import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from models.rawMaterialModel import select_all_raw_material, select_row_material_by_id
from models.sparePartsModel import select_spare_parts_by_id


class BomItemTableModel(QAbstractTableModel):
	"""Model class that drives the population of tabular display"""

	def __init__(self):
		super(BomItemTableModel, self).__init__()
		self.headers = ['Code', 'Item', 'Type','Qty', 'Cost']
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
				return QVariant(item.gen_code)
			elif col == 1:
				if item.raw_material_id:
					raw = select_row_material_by_id(item.raw_material_id)
					mname = raw.name
					return QVariant(mname)
				if item.spare_part_id:
					spare = select_spare_parts_by_id(item.spare_part_id)
					mname = spare.name
					return QVariant(mname)
			elif col == 2:
				if item.raw_material_id:
					return QVariant('Raw Material')
				if item.spare_part_id:
					return QVariant('Spare Parts')
			elif col == 3:
				return QVariant(item.qty_of_material)
			elif col == 4:
				return QVariant(item.cost_of_material)
			return QVariant()

	def headerData(self, section, orientation, role=Qt.DisplayRole):
		if role != Qt.DisplayRole:
			return QVariant()

		if orientation == Qt.Horizontal:
			return QVariant(self.headers[section])
		return QVariant(int(section + 1))