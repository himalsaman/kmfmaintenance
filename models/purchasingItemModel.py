from datetime import datetime

from sqlalchemy.orm.session import sessionmaker

from models.dbUtile import engine, PurchasingItem

Session = sessionmaker(bind=engine)
session = Session()

datetimestr = datetime.now()
timestampstr = datetimestr.strftime('%Y-%m-%d %H:%M:%S')

def addPruchItem(code, raw_material_id, spare_part_id, tools_id, product_id, req_qty, approve_date,
				 deny_approve, deny_review, review_date, pur_qty, pur_price, purchasing_id):
	new_PruItem = PurchasingItem(code, raw_material_id, spare_part_id, tools_id, product_id, req_qty,
								 approve_date,deny_approve, deny_review, review_date, pur_qty, pur_price,
								 purchasing_id, hid)
	session.add(new_PruItem)
	session.commit()

def updatePurchItem(id, code, raw_material_id, spare_part_id, tools_id, product_id, req_qty, approve_date,
				 deny_approve, deny_review, review_date, pur_qty, pur_price, purchasing_id, hid):
	res = session.query(PurchasingItem).filter(PurchasingItem.id == id).one()
	res.code = code
	res.raw_material_id = raw_material_id
	res.spare_part_id = spare_part_id
	res.tools_id = tools_id
	res.product_id = product_id
	res.req_qty = req_qty
	res.approve_date = approve_date
	res.deny_approve = deny_approve
	res.deny_review = deny_review
	res.review_date = review_date
	res.pur_qty = pur_qty
	res.pur_price = pur_price
	res.purchasing_id = purchasing_id
	res.hid = hid
	if session.commet():
		return True
	else:
		return False

def updatePurchItem_raw_material_id(id, raw_material_id):
	res = session.query(PurchasingItem).filter(PurchasingItem.id == id).one()
	res.raw_material_id = raw_material_id
	if session.commet():
		return True
	else:
		return False

def updatePurchItem_spare_part_id(id, spare_part_id):
	res = session.query(PurchasingItem).filter(PurchasingItem.id == id).one()
	res.spare_part_id = spare_part_id
	if session.commet():
		return True
	else:
		return False

def updatePurchItem_tools_id(id, tools_id):
	res = session.query(PurchasingItem).filter(PurchasingItem.id == id).one()
	res.tools_id = tools_id
	if session.commet():
		return True
	else:
		return False

def updatePurchItem_product_id(id, product_id):
	res = session.query(PurchasingItem).filter(PurchasingItem.id == id).one()
	res.product_id = product_id
	if session.commet():
		return True
	else:
		return False

def updatePurchItem_req_qty(id, req_qty):
	res = session.query(PurchasingItem).filter(PurchasingItem.id == id).one()
	res.req_qty = req_qty
	if session.commet():
		return True
	else:
		return False

def updatePurchItem_approve_date(id, approve_date):
	res = session.query(PurchasingItem).filter(PurchasingItem.id == id).one()
	res.approve_date = approve_date
	if session.commet():
		return True
	else:
		return False

def updatePurchItem_deny_approve(id, deny_approve):
	res = session.query(PurchasingItem).filter(PurchasingItem.id == id).one()
	res.deny_approve = deny_approve
	if session.commet():
		return True
	else:
		return False

def updatePurchItem_deny_review(id, deny_review):
	res = session.query(PurchasingItem).filter(PurchasingItem.id == id).one()
	res.deny_review = deny_review
	if session.commet():
		return True
	else:
		return False

def updatePurchItem_review_date(id, review_date):
	res = session.query(PurchasingItem).filter(PurchasingItem.id == id).one()
	res.review_date = review_date
	if session.commet():
		return True
	else:
		return False

def updatePurchItem_pur_qty(id, pur_qty):
	res = session.query(PurchasingItem).filter(PurchasingItem.id == id).one()
	res.pur_qty = pur_qty
	if session.commet():
		return True
	else:
		return False

def updatePurchItem_pur_price(id, pur_price):
	res = session.query(PurchasingItem).filter(PurchasingItem.id == id).one()
	res.pur_price = pur_price
	if session.commet():
		return True
	else:
		return False

def updatePurchItem_purchasing_id(id, purchasing_id):
	res = session.query(PurchasingItem).filter(PurchasingItem.id == id).one()
	res.purchasing_id = purchasing_id
	if session.commet():
		return True
	else:
		return False

def deletePurchItem(id):
	res = session.query(PurchasingItem).filter(PurchasingItem.id == id).one()
	res.hid = 1
	if session.commit():
		return True
	else:
		return False

def deletePurchItemTotaly(id):
	res = session.query(PurchasingItem).filter(PurchasingItem.id == id).one()
	session.delete(res)
	session.commit()

def selectAllPurchItem():
	return session.query(PurchasingItem).all()

def selectPurchItemById(id):
	return session.query(PurchasingItem).filter(PurchasingItem.id == id).one()

def selectPurchItemByCode(code):
	return session.query(PurchasingItem).filter(PurchasingItem.code == code).one()

def selectPurchItemByKey(key, value):
	return session.query(PurchasingItem).filter(getattr(PurchasingItem, key).contains(value)).one()

def selectPurchItemByKeyList(key, value):
	return session.query(PurchasingItem).filter(getattr(PurchasingItem, key).contains(value)).all()

print(selectAllPurchItem())