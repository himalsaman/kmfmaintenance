from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from models.dbUtile import engine, BillOfMaterial

# create a session
Session = sessionmaker(bind=engine)
session = Session()


# add new bill of material item
def add_new_bill_of_material(maintenance_id, created_at, cost_of_spare_parts, cost_of_raw_material,
							 total_cost, gen_code):
	new_bill_of_material = BillOfMaterial(maintenance_id, created_at, cost_of_spare_parts,
										  cost_of_raw_material, total_cost, gen_code)
	session.add(new_bill_of_material)
	session.commit()
	print(new_bill_of_material)


# update bill of material
def update_bill_of_material(id, created_at, cost_of_spare_parts, cost_of_raw_material,
							total_cost):
	res = session.query(BillOfMaterial).filter(BillOfMaterial.id == id).one()
	res.created_at = created_at
	res.cost_of_raw_material = cost_of_raw_material
	res.cost_of_spare_parts = cost_of_spare_parts
	res.total_cost = total_cost
	session.commit()


# delete bill of material
def delete_bill_of_material(id):
	res = session.query(BillOfMaterial).filter(BillOfMaterial.id == id).one()
	print(res)
	session.delete(res)
	session.commit()


# select bill of material by key and value
def select_bill_of_material(key, value):
	res = session.query(BillOfMaterial).filter(getattr(BillOfMaterial, key).contains(value)).all()
	for b in res:
		print(b)


# select all bill of material item
def select_all_bill_of_material():
	res = session.query(BillOfMaterial).filter(BillOfMaterial).all()
	for b in res:
		print(b)

def select_bill_of_material_by_id(value):
	return session.query(BillOfMaterial).filter(BillOfMaterial.id == value).one()

# select bill of material for maintenance
def select_bill_of_material_for_maintenance(maintenance_id):
	res = session.query(BillOfMaterial).filter(BillOfMaterial.maintenance_id == maintenance_id).all()
	for bm in res:
		print(bm)

def select_max_BOM_id():
	maxcode = session.query(func.max(BillOfMaterial.id)).one()
	return (maxcode[0])

def select_max_BOM_code():
	maxcode = session.query(func.max(BillOfMaterial.gen_code)).one()
	return (maxcode[0])