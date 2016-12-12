from sqlalchemy import func
from sqlalchemy.orm.session import sessionmaker

from models.dbUtile import engine, Outbound

Session = sessionmaker(bind=engine)
session = Session()

def add_outbound(code, out_date, reason, customer_id, employee_id, raw_material_id,
				 spare_part_id, tools_id, product_id, req_qty, status):
	new_outbound = Outbound(code, out_date, reason, customer_id, employee_id, raw_material_id,
				 spare_part_id, tools_id, product_id, req_qty,status)
	session.add(new_outbound)
	session.commit()

def update_oubound(id, code, out_date, reason, customer_id, employee_id, raw_material_id,
				 spare_part_id, tools_id, product_id, req_qty):
	res = session.query(Outbound).filter(Outbound.id == id).one()
	res.code = code
	res.out_date = out_date
	res.reason = reason
	res.customer_id = customer_id
	res.employee_id = employee_id
	res.raw_material_id = raw_material_id
	res.spare_part_id = spare_part_id
	res.tools_id = tools_id
	res.product_id = product_id
	res.req_qty = req_qty
	if session.commit():
		return True
	else:
		return False

def select_outbound_by_id(id):
	return session.query(Outbound).filter(Outbound.id == id).one()

def delete_outbound(id):
	res = session.query(Outbound).filter(Outbound.id == id).one()
	print(res)
	session.delete(res)
	session.commit()

def update_oubound_status(id, status):
	res = session.query(Outbound).filter(Outbound.id == id).one()
	res.status = status
	if session.commit():
		return True
	else:
		return False

def select_outbound_by_code(code):
	return session.query(Outbound).filter(Outbound.code == code).one()

def select_outbound_by_customer(customer_id):
	return session.query(Outbound).filter(Outbound.customer_id == customer_id).all()

def select_outbound_by_product(product_id):
	return session.query(Outbound).filter(Outbound.id == product_id).one()

def select_outbound(key, value):
	return session.query(Outbound).filter(getattr(Outbound, key).contains(value)).all()

def select_all_outbound():
	return session.query(Outbound).all()

def select_max_outb_code():
	maxcode = session.query(func.max(Outbound.code)).one()
	return (maxcode[0])
