import re

from models.billOfMaterialItemModel import add_new_bill_of_material_item, select_max_BOMITEM_code
from models.rawMaterialModel import select_row_material_by_id
from models.sparePartsModel import select_spare_parts_by_id


def BOMItemCode():
	maxcode = select_max_BOMITEM_code()
	intcode = int(next(re.finditer(r'\d+$', maxcode)).group(0))
	nextgencode = intcode + 1
	gencode = 'kmfBOMI{}'.format(nextgencode)
	return gencode


def createNewBOMItem(bomId, raw_material_id, spare_parts_id, qty_of_material):
	bill_of_material_id = bomId
	if raw_material_id:
		spare_parts_id = None
		BOMItemRW = select_row_material_by_id(raw_material_id)
		BOMItemCost = (BOMItemRW.cost_per_default_size / BOMItemRW.default_size) * qty_of_material
	elif spare_parts_id:
		raw_material_id = None
		BOMItemSP = select_spare_parts_by_id(spare_parts_id)
		BOMItemCost = BOMItemSP.price * qty_of_material

	add_new_bill_of_material_item(raw_material_id, spare_parts_id, bill_of_material_id,
								  BOMItemCost, qty_of_material, BOMItemCode())
