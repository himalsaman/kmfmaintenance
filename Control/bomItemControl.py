from models.billOfMaterialItemModel import add_new_bill_of_material_item, select_all_bill_of_material_item
from models.billOfMaterialModel import select_max_BOM_id
from models.rawMaterialModel import select_row_material_by_id
from models.sparePartsModel import select_spare_parts_by_id


def createNewBOMItem(raw_material_id, spare_parts_id, qty_of_material):
	bill_of_material_id = select_max_BOM_id()
	if raw_material_id :
		spare_parts_id = None
		BOMItemRW = select_row_material_by_id(raw_material_id)
		BOMItemCost = (BOMItemRW.cost_per_default_size / BOMItemRW.default_size) * qty_of_material
	elif spare_parts_id:
		raw_material_id = None
		BOMItemSP = select_spare_parts_by_id(spare_parts_id)
		BOMItemCost = BOMItemSP.price * qty_of_material

	add_new_bill_of_material_item(raw_material_id, spare_parts_id, bill_of_material_id,
									  BOMItemCost, qty_of_material)

# createNewBOMItem(2, None, 6)