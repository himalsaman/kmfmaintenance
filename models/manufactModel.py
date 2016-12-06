from sqlalchemy.orm.session import sessionmaker

from models.dbUtile import engine, Manufacting

Session = sessionmaker(bind=engine)
session = Session()

def add_manufact( cost_of_bill_of_material, cost_of_labor, sales_price, created_at , product_of_manufact, start_date, done_date, m_code, hidden):
	new_manufact = Manufacting( cost_of_bill_of_material, cost_of_labor, sales_price, created_at , product_of_manufact, start_date, done_date, m_code, hidden)
	session.add(new_manufact)
	session.commit()

def update_manufact(id, cost_of_bill_of_material, cost_of_labor, sales_price, created_at , product_of_manufact, start_date, done_date, m_code, hidden):
	res = session.query(Manufacting).filter(Manufacting.id == id)
	res.cost_of_bill_of_material = cost_of_bill_of_material
	res.cost_of_labor = cost_of_labor
	res.sales_price = sales_price
	res.created_at = created_at
	res.product_of_manufact = product_of_manufact
	res.start_date = start_date
	res.done_date = done_date
	res.m_code = m_code
	res.hidden = hidden
	session.commit()

def update_manufact_cost_bill(id, cost_of_bill_of_material):
	res = session.query(Manufacting).filter(Manufacting.id == id)
	res.cost_of_bill_of_material = cost_of_bill_of_material
	session.commit()

def update_manufact_cost_labor(id,cost_of_labor):
	res = session.query(Manufacting).filter(Manufacting.id == id)
	res.cost_of_labor = cost_of_labor
	session.commit()

def update_manufact_sale_price(id, sales_price):
	res = session.query(Manufacting).filter(Manufacting.id == id)
	res.sales_price = sales_price
	session.commit()

def update_manufact_start_date(id, start_date):
	res = session.query(Manufacting).filter(Manufacting.id == id)
	res.start_date = start_date
	session.commit()

def update_manufact_done_date(id, done_date):
	res = session.query(Manufacting).filter(Manufacting.id == id)
	res.done_date = done_date
	session.commit()

def delete_manufact(id, hidden):
	res = session.query(Manufacting).filter(Manufacting.id == id)
	res.hidden = 1
	session.commit()

def select_all_manufact():
	return session.query(Manufacting).all()

def select_manuf_by_id(id):
	return  session.query(Manufacting).filter(Manufacting.id == id).one()

def select_manufact_by_key(key, value):
	return session.query(Manufacting).filter(getattr(Manufacting, key).contains(value)).all()

def select_manufact_by_key_one(key, value):
	return session.query(Manufacting).filter(getattr(Manufacting, key).contains(value)).one()

