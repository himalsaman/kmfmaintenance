# raw Material inventory Management
from models.finishProductsModel import update_finish_product_inv_qty, update_finish_product_cost
from models.rawMaterialModel import update_raw_material_inv_qty, update_raw_material_cost
from models.sparePartsModel import update_spare_parts_inv_qty, update_spare_parts_cost
from models.toolsModel import update_tools_inv_qty, update_tools_cost


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

# finish products
def increaseFinishProductInvQty(finpro, newqty):
	newinvqty = finpro.inv_qty + newqty
	update_finish_product_inv_qty(finpro.id, newinvqty)

def decreaseFinishProductInvQty(finpro, newqty):
	newinvqty = finpro.inv_qty - newqty
	update_finish_product_inv_qty(finpro.id, newinvqty)

def upFinishProductCost(finpro, newCost):
	update_finish_product_cost(finpro.id, newCost)

# tools
def increaseToolsInvQty(finpro, newqty):
	if finpro.back == 0:
		newinvqty = finpro.inv_qty + newqty
	update_tools_inv_qty(finpro.id, newinvqty)

def decreaseToolsInvQty(finpro, newqty):
	if int(finpro.back) == 0:
		newinvqty = finpro.inv_qty - newqty
		update_tools_inv_qty(finpro.id, newinvqty)
	if int(finpro.back) == 1:
		newinvqty = finpro.inv_qty
		update_tools_inv_qty(finpro.id, newinvqty)

def updateToolsCost(finpro, newCost):
	update_tools_cost(finpro.id, newCost)