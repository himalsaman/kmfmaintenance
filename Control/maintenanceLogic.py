import random

import select

import re
from datetime import datetime

from pymysql import TIMESTAMP
from pymysql.times import Timestamp
from sqlalchemy.sql.sqltypes import TIMESTAMP

from Control.bomItemControl import createNewBOMItem
from models.billOfMaterialItemModel import add_new_bill_of_material_item, select_bill_of_material_item_for_BOM
from models.billOfMaterialModel import add_new_bill_of_material, select_max_BOM_id, update_bill_of_material, \
	select_bill_of_material_by_id
from models.customersModel import select_all_customers, add_customer, select_customer_by_id, select_max_customer_id
from models.dbUtile import Customers, Maintenance
from models.maintenanceModel import select_all_maintenance, add_new_maintenance, check_maintenance_first_time,\
	select_max_maintenance_code, select_maintenance, select_maintenance_by_id

datetimestr = datetime.now()
timestampstr = datetimestr.strftime('%Y/%m/%d %H:%M:%S')

# maintanance code calculation
def maintenanceCode():
	maxcode = select_max_maintenance_code()
	intcode = int(next(re.finditer(r'\d+$', maxcode)).group(0))
	nextgencode = intcode + 1
	gencode = 'kmfma{}'.format(nextgencode)
	return gencode

#first maintenance for created new customer
def creatMaintenanceWithNewCustomer(name, mobile_number, gender, age, city_id):

	if not check_maintenance_first_time():
		gencode = 'kmfma{}'.format(random.randrange(1, 10, 2))
	else:
		gencode = maintenanceCode()
		new_customers = add_customer(name, mobile_number, gender, age, city_id)
		add_new_maintenance( gencode, new_customers.id,None, None, None, None, None, None, None,
							 None, None,None )
		return True
# calculate raw material cost
def claculateBOMItemRMCost():
	bomid = select_max_BOM_id()
	bomitem = select_bill_of_material_item_for_BOM(bomid)
	costList = []
	for item in bomitem:
		if item.raw_material_id :
			costList.append(item.cost_of_material)

	return  sum(costList)

# calculate raw material cost
def claculateBOMItemSPCost():
	bomid = select_max_BOM_id()
	bomitem = select_bill_of_material_item_for_BOM(bomid)
	costList = []
	for item in bomitem:
		if item.spare_part_id :
			costList.append(item.cost_of_material)

	return  sum(costList)
def finishBOM():
	bomid = select_max_BOM_id()
	totall = claculateBOMItemSPCost() + claculateBOMItemRMCost()
	update_bill_of_material(bomid, timestampstr, claculateBOMItemSPCost(),
							claculateBOMItemRMCost(),totall)


		#creat new maintenance for exsist customer
def createMaintenanceForExsistCustomer(customer_id):
	add_new_maintenance(maintenanceCode(), customer_id,  None, None,
						None, None, None, None,
						None,None, None, None)


def getAllMaintenanceNotCreated():
	simplelist = []
	maintenancesList  = select_all_maintenance()
	for mainte in maintenancesList:
		if mainte.created_at == None :
			simplelist.append(mainte.customers)
	return simplelist


