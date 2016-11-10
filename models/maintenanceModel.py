from _testcapi import return_null_without_error

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from models.dbUtile import Maintenance, engine

# create a session
Session = sessionmaker(bind=engine)
session = Session()


# add new maintenance
def add_new_maintenance(customer_id, cost_of_bill_of_material, cost_of_spare_parts, cost_of_raw_material, cost_of_labor,
						cost_of_another, cost_of_another_description, created_at, close_at, product_of_maintenance,
						maintenance_description):
	new_maintenance = Maintenance(customer_id, cost_of_bill_of_material, cost_of_spare_parts, cost_of_raw_material,
								  cost_of_labor,
								  cost_of_another, cost_of_another_description, created_at, close_at,
								  product_of_maintenance,
								  maintenance_description)
	session.add(new_maintenance)
	session.commit()
	print(new_maintenance)


# update maintenance
def update_maintenance(id, customer_id, cost_of_bill_of_material, cost_of_spare_parts, cost_of_raw_material,
					   cost_of_labor,
					   cost_of_another, cost_of_another_description, created_at, close_at, product_of_maintenance,
					   maintenance_description):
	res = session.query(Maintenance).filter(Maintenance.id == id).one()
	print(res)
	res.customer_id = customer_id
	res.cost_of_bill_of_material = cost_of_bill_of_material
	res.cost_of_spare_parts = cost_of_spare_parts
	res.cost_of_material = cost_of_raw_material
	res.cost_of_labor = cost_of_labor
	res.cost_of_another = cost_of_another
	res.cost_of_another_description = cost_of_another_description
	res.create_at = created_at
	res.close_at = close_at
	res.product_of_maintenance = product_of_maintenance
	res.maintenance_description = maintenance_description
	session.commit()


# delete maintenance
def delete_maintenance(id):
	res = session.query(Maintenance).filter(Maintenance.id == id).one()
	# print  res
	session.delete(res)
	session.commit()


# select maintenance by key and value
def select_maintenance(key, value):
	res = session.query(Maintenance).filter(getattr(Maintenance, key).contains(value)).all()
	for m in res:
		return m


def select_maintenance_customer(value):
	try :
		res = session.query(Maintenance).filter(Maintenance.customers_id == value).one()
		return res
	except NoResultFound:
		return False

# select maintenance by key and value
def select_all_maintenance():
	res = session.query(Maintenance).all()
	for m in res:
		return m
