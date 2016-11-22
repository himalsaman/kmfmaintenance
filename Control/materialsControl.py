# raw Material inventory Management
from models.rawMaterialModel import update_raw_material, update_raw_material_inv_qty


def increaseRawMaterialInvQty(rawMaterial, newqty):
	newinvqty = rawMaterial.inv_qty + newqty
	update_raw_material_inv_qty(rawMaterial.id, newinvqty)


def decreaseRawMaterialInvQty(rawMaterial, newqty):
	newinvqty = rawMaterial.inv_qty - newqty
	update_raw_material_inv_qty(rawMaterial.id, newinvqty)

# spare Parts
def increaseSparePartsInvQty(sparePart, newqty):
	newinvqty = sparePart.inv_qty + newqty
	update_raw_material_inv_qty(sparePart.id, newinvqty)


def decreaseSparePartsInvQty(sparePart, newqty):
	newinvqty = sparePart.inv_qty - newqty
	update_raw_material_inv_qty(sparePart.id, newinvqty)
