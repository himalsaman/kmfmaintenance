from models import customersModel, maintenanceModel
from models.customersModel import select_all_customers


def validCustomer(name, mobNum, mobile_number_1, mobile_number_2, mobile_number_3, mobile_number_4,gender, age, city_id):
	if not customersModel.select_customer_by_mob_num(mobNum):
		customersModel.add_customer(name, mobNum, mobile_number_1, mobile_number_2, mobile_number_3, mobile_number_4,gender, age, city_id)
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

def getAllcustomers():
	simplelist = []
	custList  = select_all_customers()
	for cust in custList:
			simplelist.append(cust)
	return simplelist
