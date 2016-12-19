from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import sessionmaker

from models.dbUtile import engine, Purchasing

Session = sessionmaker(bind=engine)
session = Session()

datetimestr = datetime.now()
timestampstr = datetimestr.strftime('%Y-%m-%d %H:%M:%S')

def addNewPurchasing(code, req_date, pur_empl_id, pur_date, review_date, deny_review,
				 deny_approve, total, approve_date, invoice_num,hid):
	new_purch = Purchasing(code, req_date, pur_empl_id, pur_date, review_date, deny_review,
				 deny_approve, total, approve_date, invoice_num, hid)
	session.add(new_purch)
	session.commit()

def updatePurch(id, code, req_date, pur_empl_id, pur_date, review_date, deny_review,
				 deny_approve, total, approve_date, invoice_num, hid):
	res = session.query(Purchasing).filter(Purchasing.id == id).one()
	res.code = code
	res.req_date = req_date
	res.pur_empl_id = pur_empl_id
	res.pur_date = pur_date
	res.review_date = review_date
	res.deny_review  = deny_review
	res.deny_approve = deny_approve
	res.total = total
	res.approve_date = approve_date
	res.invoice_num = invoice_num
	res.hid = hid
	if session.commit():
		return  True
	else:
		return False

def updatePurch_pur_empl_id(id, pur_empl_id):
	res = session.query(Purchasing).filter(Purchasing.id == id ).one()
	res.pur_empl_id = pur_empl_id
	if session.commit():
		return True
	else:
		return False

def updatePurch_pur_date(id, pur_date):
	res = session.query(Purchasing).filter(Purchasing.id == id ).one()
	res.pur_date = pur_date
	if session.commit():
		return True
	else:
		return False

def updatePurch_review_date(id, review_date):
	res = session.query(Purchasing).filter(Purchasing.id == id ).one()
	res.review_date = review_date
	if session.commit():
		return True
	else:
		return False

def updatePurch_deny_review(id, deny_review):
	res = session.query(Purchasing).filter(Purchasing.id == id ).one()
	res.deny_review = deny_review
	if session.commit():
		return True
	else:
		return False

def updatePurch_deny_approve(id, deny_approve):
	res = session.query(Purchasing).filter(Purchasing.id == id ).one()
	res.deny_approve = deny_approve
	if session.commit():
		return True
	else:
		return False

def updatePurch_total(id, total):
	res = session.query(Purchasing).filter(Purchasing.id == id ).one()
	res.total = total
	if session.commit():
		return True
	else:
		return False

def updatePurch_approve_date(id, approve_date):
	res = session.query(Purchasing).filter(Purchasing.id == id ).one()
	res.approve_date = approve_date
	if session.commit():
		return True
	else:
		return False

def updatePurch_invoice_num(id, invoice_num):
	res = session.query(Purchasing).filter(Purchasing.id == id ).one()
	res.invoice_num = invoice_num
	if session.commit():
		return True
	else:
		return False

def deletePurch(id):
	res = session.query(Purchasing).filter(Purchasing.id == id).one()
	res.hid = 1
	if session.commit():
		return True
	else:
		return False

def deletePurchTotaly(id):
	res = session.query(Purchasing).filter(Purchasing.id == id).one()
	session.delete(res)
	session.commit()

def selectAllPurch():
	return session.query(Purchasing).all()

def selectPurchById(id):
	return session.query(Purchasing).filter(Purchasing.id == id).one()

def selectPurchByCode(code):
	return session.query(Purchasing).filter(Purchasing.code == code).one()

def selectPurchByKey(key, value):
	return session.query(Purchasing).filter(getattr(Purchasing, key).contains(value)).one()

def selectPurchByKeyList(key, value):
	return session.query(Purchasing).filter(getattr(Purchasing, key).contains(value)).all()

def select_max_Purchasing_code():
	try:
		maxcode = session.query(func.max(Purchasing.code)).one()
		return (maxcode[0])
	except NoResultFound:
		return False



