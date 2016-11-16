
import re

from datetime import date, datetime

from pymysql import TIMESTAMP

from Control.maintenanceLogic import claculateBOMItemRMCost, claculateBOMItemSPCost
from models.billOfMaterialItemModel import select_bill_of_material_item_for_BOM
from models.billOfMaterialModel import  add_new_bill_of_material, select_max_BOM_id, select_max_BOM_code

datetimestr = datetime.now()
timestampstr = datetimestr.strftime('%Y/%m/%d %H:%M:%S')

# maintanance code calculation
def BOMCode():
	maxcode = select_max_BOM_code()
	intcode = int(next(re.finditer(r'\d+$', maxcode)).group(0))
	nextgencode = intcode + 1
	gencode = 'kmfBOM{}'.format(nextgencode)
	return gencode

#ctreate BOm for item
def createBOM(maintenance_id, BOMId):
	for item in select_bill_of_material_item_for_BOM(BOMId):
		if item.raw_material_id:
			RMC = item.cost_of_material
		if item.spare_parts_id:
			SPC = item.cost_of_material

	created_at = datetime.now().time()
	totalCost = RMC + SPC
	add_new_bill_of_material(maintenance_id, created_at, SPC, RMC, totalCost, BOMCode())

def getAllItemForBOM():
	simplelist = []
	bomid = select_max_BOM_id()
	itemList  = select_bill_of_material_item_for_BOM(bomid)
	# for item in itemList:
	# 	if not item.raw_material_id == None:
	# 		simplelist.append(item.rawMaterial)
	# 	if not item.raw_material_id == None:
	# 		simplelist.append(item.spareParts)
	return itemList

def getTotalMaterialCost():
	return  claculateBOMItemRMCost() + claculateBOMItemSPCost
