# raw Material inventory Management
from models.rawMaterialModel import update_raw_material_inv_qty, update_raw_material_cost
from models.sparePartsModel import update_spare_parts_inv_qty, update_spare_parts_cost


def increaseRawMaterialInvQty(rawMaterial, newqty):
	newinvqty = rawMaterial.inv_qty + newqty
	update_raw_material_inv_qty(rawMaterial.id, newinvqty)


def decreaseRawMaterialInvQty(rawMaterial, newqty):
	newinvqty = rawMaterial.inv_qty - newqty
	update_raw_material_inv_qty(rawMaterial.id, newinvqty)

def upRawMaterialCost(rawMaterial, newCost):
	update_raw_material_cost(rawMaterial.id, newCost)



# spare Parts
def increaseSparePartsInvQty(spareParts, newqty):
	newinvqty = spareParts.inv_qty + newqty
	update_spare_parts_inv_qty(spareParts.id, newinvqty)


def decreaseSparePartsInvQty(spareParts, newqty):
	newinvqty = spareParts.inv_qty - newqty
	update_spare_parts_inv_qty(spareParts.id, newinvqty)

def upSparePartsCost(spareParts, newCost):
	update_spare_parts_cost(spareParts.id, newCost)