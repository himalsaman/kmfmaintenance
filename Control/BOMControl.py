import random
import re
from datetime import datetime

from models.billOfMaterialItemModel import select_bill_of_material_item_for_BOM
from models.billOfMaterialModel import add_new_bill_of_material, select_max_BOM_id, select_max_BOM_code, \
	check_BOM_first_time, update_bill_of_material

datetimestr = datetime.now()
timestampstr = datetimestr.strftime('%Y-%m-%d %H:%M:%S')


# maintanance code calculation
def BOMCode():
	maxcode = select_max_BOM_code()
	intcode = int(next(re.finditer(r'\d+$', maxcode)).group(0))
	nextgencode = intcode + 1
	gencode = 'kmfBOM{}'.format(nextgencode)
	return gencode


# first maintenance for created new customer
def creatBOMWithNewMAint(maint_id):
	if not check_BOM_first_time():
		gencode = 'kmfBOM{}'.format(random.randrange(1, 10, 2))
	else:
		gencode = BOMCode()
	bom = add_new_bill_of_material(maint_id, timestampstr, None, None, None, gencode)
	return bom


# calculate raw material cost
def claculateBOMItemRMCost(bomid):
	bomitem = select_bill_of_material_item_for_BOM(bomid)
	costList = []
	for item in bomitem:
		if item.raw_material_id:
			costList.append(item.cost_of_material)

	return sum(costList)


# calculate raw material cost
def claculateBOMItemSPCost(bomid):
	bomitem = select_bill_of_material_item_for_BOM(bomid)
	costList = []
	for item in bomitem:
		if item.spare_part_id:
			costList.append(item.cost_of_material)

	return sum(costList)


def finishBOM():
	bomid = select_max_BOM_id()
	totall = claculateBOMItemSPCost() + claculateBOMItemRMCost()
	update_bill_of_material(bomid, claculateBOMItemSPCost(), claculateBOMItemRMCost(), totall)


# ctreate BOm for item
def createBOM(maintenance_id, BOMId):
	for item in select_bill_of_material_item_for_BOM(BOMId):
		if item.raw_material_id:
			RMC = item.cost_of_material
		if item.spare_parts_id:
			SPC = item.cost_of_material

	created_at = datetime.now().time()
	totalCost = RMC + SPC
	add_new_bill_of_material(maintenance_id, created_at, SPC, RMC, totalCost, BOMCode())


def getAllItemForBOM(bomid):
	simplelist = []
	itemList = select_bill_of_material_item_for_BOM(bomid)
	return itemList


def getTotalMaterialCost():
	return claculateBOMItemRMCost() + claculateBOMItemSPCost

