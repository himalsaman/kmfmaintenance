import re
from datetime import datetime

from models.ouboundModel import select_all_outbound, select_max_outb_code, select_outbound_by_customer

datetimestr = datetime.now().date()


def OutBCode():
	maxcode = select_max_outb_code()
	intcode = int(next(re.finditer(r'\d+$', maxcode)).group(0))
	nextgencode = intcode + 1
	gencode = 'kmfoutb {}'.format(nextgencode)
	return gencode


def getOutbounEmployeeRow():
	simplelist = []
	objlist = select_all_outbound()
	for item in objlist:
		if not item.employee == None and item.status == 1 and item.out_date.date() == datetimestr:
			simplelist.append(item)
	return simplelist


def getOutbounCustomerRow():
	simplelist = []
	objlist = select_all_outbound()
	for item in objlist:
		if not item.customers == None and item.out_date.date() == datetimestr:
			simplelist.append(item)
	return simplelist


def getOutbounOneCustomerRow(cust):
	simplelist = []
	objlist = select_outbound_by_customer(cust.id)
	for item in objlist:
		if item.out_date.date() == datetimestr and item.status == 1:
			simplelist.append(item)
	return simplelist


# print(item.out_date.date())

def geAlltOutboun():
	simplelist = []
	objlist = select_all_outbound()
	for item in objlist:
		simplelist.append(item)
	return simplelist
