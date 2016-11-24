import random

import select

import re
from datetime import datetime

from pymysql import TIMESTAMP
from pymysql.times import Timestamp
from sqlalchemy.sql.functions import func, current_timestamp
from sqlalchemy.sql.sqltypes import TIMESTAMP

from Control.BOMControl import creatBOMWithNewMAint
from Control.bomItemControl import createNewBOMItem
from models.billOfMaterialItemModel import add_new_bill_of_material_item, select_bill_of_material_item_for_BOM
from models.billOfMaterialModel import add_new_bill_of_material, select_max_BOM_id, update_bill_of_material, \
	select_bill_of_material_by_id
from models.customersModel import select_all_customers, add_customer, select_customer_by_id, select_max_customer_id
from models.dbUtile import Customers, Maintenance
from models.maintenanceModel import select_all_maintenance, add_new_maintenance, check_maintenance_first_time,\
	select_max_maintenance_code, select_maintenance, select_maintenance_by_id, select_All_maintenance_customer

datetimestr = datetime.now()
timestampstr = datetimestr.strftime('%Y-%m-%d %H:%M:%S')

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
	maint = add_new_maintenance( gencode, new_customers.id,None, None, None, None, None, None,
										None,None, None,None )
	# print(new_mainte.id)
	return maint

def creatMaintenanceExtCustomer(customer):
	if not check_maintenance_first_time():
		gencode = 'kmfma{}'.format(random.randrange(1, 10, 2))
	else:
		gencode = maintenanceCode()
	maint = add_new_maintenance( gencode, customer.id,None, None, None, None, None, None,
										None,None, None,None )
	# print(new_mainte.id)
	return maint

def getAllMaintenanceNotCreated():
	simplelist = []
	maintenancesList  = select_all_maintenance()
	for mainte in maintenancesList:
		if mainte.created_at == None :
			simplelist.append(mainte.customers)
	return simplelist

def getMaintenancePused():
	simplelist = []
	mainlist = select_all_maintenance()
	for mainte in mainlist:
		if mainte.created_at == None or mainte.cost_of_bill_of_material == None:
			simplelist.append(mainte)
	return simplelist

def getMaintenanceWaitLaborCost():
	simplelist = []
	mainlist = select_all_maintenance()
	for mainte in mainlist:
		if mainte.created_at != None \
				and mainte.cost_of_labor == None \
				and mainte.cost_of_bill_of_material!= None:
			simplelist.append(mainte)
	return simplelist

def getMaintenanceHolded():
	simplelist = []
	mainlist = select_all_maintenance()
	for mainte in mainlist:
		if mainte.created_at != None \
				and mainte.start_date == None \
				and mainte.cost_of_labor != None:
			simplelist.append(mainte)
	return simplelist

def getMaintenanceCalcCost():
	simplelistbm = []
	simplelistla = []
	simplelistan = []
	mainlist = select_all_maintenance()
	for mainte in mainlist:
		if mainte.created_at != None \
				and mainte.start_date == None :
			if not mainte.cost_of_bill_of_material == None:
				# mainte.cost_of_bill_of_material = None
				simplelistbm.append(mainte.cost_of_bill_of_material)
			if not mainte.cost_of_labor == None:
				# mainte.cost_of_labor = None
				simplelistla.append(mainte.cost_of_labor )
			if not mainte.cost_of_another == None:
				# mainte.cost_of_another = None
				simplelistan.append(mainte.cost_of_another)
		summ = sum(simplelistbm) + sum(simplelistla) + sum(simplelistan)
	return summ

def getMaintenanceUnderProccessing():
	simplelist = []
	mainlist = select_all_maintenance()
	for mainte in mainlist:
		if mainte.start_date != None and mainte.done_date== None:
			simplelist.append(mainte)
	return simplelist

def getMaintenanceUnderProccessingCost():
	simplelistbm = []
	simplelistla = []
	simplelistan = []
	mainlist = select_all_maintenance()
	for mainte in mainlist:
		if mainte.start_date != None and mainte.done_date == None:
			if not mainte.cost_of_bill_of_material == None:
			# 	mainte.cost_of_bill_of_material = 0
				simplelistbm.append(mainte.cost_of_bill_of_material)
			if not mainte.cost_of_labor == None:
			# 	mainte.cost_of_labor = 0
				simplelistla.append(mainte.cost_of_labor )
			if not mainte.cost_of_another == None:
			# 	mainte.cost_of_another = 0
				simplelistan.append(mainte.cost_of_another)
		summ = sum(simplelistbm) + sum(simplelistla) + sum(simplelistan)
	return summ

def getMaintenanceWaitingDelevary():
	simplelist = []
	mainlist = select_all_maintenance()
	for mainte in mainlist:
		if mainte.done_date != None and mainte.close_at == None:
			simplelist.append(mainte)
	return simplelist

def getMaintenanceFinishedAndDelivared():
	simplelist = []
	mainlist = select_all_maintenance()
	for mainte in mainlist:
		if mainte.close_at != None :
			simplelist.append(mainte)
	return simplelist

def getMaintenanceFinishedAndDelivaredCost():
	simplelistbm = []
	simplelistla = []
	simplelistan = []
	mainlist = select_all_maintenance()
	for mainte in mainlist:
		if mainte.close_at != None:
			if not mainte.cost_of_bill_of_material == None:
			# 	mainte.cost_of_bill_of_material = 0
				simplelistbm.append(mainte.cost_of_bill_of_material)
			if not mainte.cost_of_labor == None:
			# 	mainte.cost_of_labor = 0
				simplelistla.append(mainte.cost_of_labor )
			if not mainte.cost_of_another == None:
			# 	mainte.cost_of_another = 0
				simplelistan.append(mainte.cost_of_another)
		summ = sum(simplelistbm) + sum(simplelistla) + sum(simplelistan)
	return summ


def getMaintenanceForCustomer(customer):
	simplelist = []
	mainlist = select_All_maintenance_customer(customer.id)
	for mainte in mainlist:
			simplelist.append(mainte)
	return simplelist

def getMaintenanceStatus(mainte):
	if mainte.created_at != None :
		if mainte.cost_of_labor == None:
			satus = 'Wait Labor Cost'
		if mainte.start_date == None:
			satus = 'Wait Customer Confirmation'
		if mainte.done_date == None:
			satus = 'Under Processing '
		if mainte.close_at == None:
			satus = 'Wait Delivery to Customer '
		if mainte.close_at != None:
			satus = 'Finished'
		if mainte.hidden == 1:
			satus = 'Canceled'
		if mainte.hidden == 1 and mainte.start_date == None:
			satus = 'Canceled By Customer'
	return satus

