from _testcapi import return_null_without_error

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import func

from models.dbUtile import Maintenance, engine

# create a session
Session = sessionmaker(bind=engine)
session = Session()


# add new maintenance
def add_new_maintenance(m_code, customer_id, cost_of_bill_of_material, cost_of_labor,
						cost_of_another, cost_of_another_description, created_at, close_at,
						product_of_maintenance,maintenance_description, start_date, done_date):
	new_maintenance = Maintenance(m_code, customer_id, cost_of_bill_of_material, cost_of_labor,
						cost_of_another, cost_of_another_description, created_at, close_at,
						product_of_maintenance,maintenance_description, start_date, done_date)
	session.add(new_maintenance)
	session.commit()
	return new_maintenance


# update maintenance
def update_maintenance(id, cost_of_bill_of_material,
					   cost_of_labor,
					   cost_of_another, cost_of_another_description, created_at, close_at,
					   product_of_maintenance, maintenance_description, start_date, done_date):
	res = session.query(Maintenance).filter(Maintenance.id == id and Maintenance.hidden == 0).one()
	res.cost_of_bill_of_material = cost_of_bill_of_material
	res.cost_of_labor = cost_of_labor
	res.cost_of_another = cost_of_another
	res.cost_of_another_description = cost_of_another_description
	res.created_at = created_at
	res.close_at = close_at
	res.product_of_maintenance = product_of_maintenance
	res.maintenance_description = maintenance_description
	res.start_date = start_date
	res.done_date = done_date
	session.commit()

def update_maintenance_from_BOM(id, cost_of_bill_of_material, created_at):
	res = session.query(Maintenance).filter(Maintenance.id == id and Maintenance.hidden == 0).one()
	res.cost_of_bill_of_material = cost_of_bill_of_material
	res.created_at = created_at
	session.commit()

def update_maintenance_product(id,product_of_maintenance, maintenance_description):
	res = session.query(Maintenance).filter(Maintenance.id == id and Maintenance.hidden == 0).one()
	res.product_of_maintenance = product_of_maintenance
	res.maintenance_description = maintenance_description
	session.commit()

def update_maintenance_confirm(id,start_date):
	res = session.query(Maintenance).filter(Maintenance.id == id and Maintenance.hidden == 0).one()
	res.start_date = start_date
	session.commit()

def update_maintenance_finish(id,done_date):
	res = session.query(Maintenance).filter(Maintenance.id == id and Maintenance.hidden == 0).one()
	res.done_date = done_date
	session.commit()

def update_maintenance_close(id,close_at):
	res = session.query(Maintenance).filter(Maintenance.id == id and Maintenance.hidden == 0).one()
	res.close_at = close_at
	session.commit()


# delete maintenance
def delete_maintenance(id):
	res = session.query(Maintenance).filter(Maintenance.id == id).one()
	# print  res
	# session.delete(res)
	res.hidden = 1
	session.commit()


# select maintenance by key and value
def select_maintenance(key, value):
	return  session.query(Maintenance).filter(getattr(Maintenance, key).contains(value) and Maintenance.hidden == 0).all()



def select_maintenance_customer(value):
	return session.query(Maintenance).filter(Maintenance.customers_id == value and Maintenance.hidden == 0).all()

def select_maintenance_by_id(value):
	return session.query(Maintenance).filter(Maintenance.id == value and Maintenance.hidden == 0).one()
# select maintenance by key and value
def select_all_maintenance():
	return session.query(Maintenance).filter(Maintenance.hidden == 0).all()

def select_max_maintenance_code():
	maxcode = session.query(func.max(Maintenance.m_code)).one()
	return (maxcode[0])

def select_max_maintenance_id():
	maxcode = session.query(func.max(Maintenance.id)).one()
	return (maxcode[0])

def check_maintenance_first_time():
	return session.query(Maintenance).first()

def select_maintenance_by_code(value):
	return session.query(Maintenance).filter(Maintenance.m_code == value and Maintenance.hidden == 0).one()