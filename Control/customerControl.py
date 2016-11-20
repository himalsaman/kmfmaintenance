from models import customersModel, maintenanceModel
from models.customersModel import select_all_customers


def validCustomer(name, mobNum, gender, age, city_id):
	if not customersModel.select_customer_by_mob_num(mobNum):
		customersModel.add_customer(name, mobNum, gender, age, city_id)
		return True
	else:
		return False
def valiedDeleteCustomer(mobNum):
	if customersModel.select_customer_by_mob_num(mobNum):
		selectedCust = customersModel.select_customer_by_mob_num(mobNum)
		if not maintenanceModel.select_maintenance_customer(selectedCust.customers_id):
			customersModel.delete_customer(selectedCust.id)
		else :
			return False

def getAllcustomersCount():
	print (len(select_all_customers()))

getAllcustomersCount()