from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from models.dbUtile import BillOfMaterialItem, engine

# create a session
Session = sessionmaker(bind=engine)
session = Session()


# add new bill of material item
def add_new_bill_of_material_item(tools_id, raw_material_id, spare_parts_id, bill_of_material_id, cost_of_material, qty_of_material, gen_code):
	new_bill_of_material_item = BillOfMaterialItem(tools_id, raw_material_id, spare_parts_id, bill_of_material_id,
												   cost_of_material, qty_of_material, gen_code)
	session.add(new_bill_of_material_item)
	session.commit()


# update bill of material item
def update_bill_of_material_item(id, tools_id,raw_material_id, spare_parts_id, bill_of_material_id,
								 cost_of_material,qty_of_material):
	res = session.query(BillOfMaterialItem).filter(BillOfMaterialItem.id == id).one()
	print(res)
	res.tools_id = tools_id,
	res.raw_material_id = raw_material_id
	res.spare_parts_id = spare_parts_id
	res.bill_of_material_id = bill_of_material_id
	res.cost_of_material = cost_of_material
	res.qty_of_material = qty_of_material
	session.commit()


# delete bill of material
def delete_bill_of_material_item(id):
	res = session.query(BillOfMaterialItem).filter(BillOfMaterialItem.id == id).one()
	print(res)
	session.delete(res)
	session.commit()


# select bill of material by key and value
def select_bill_of_material_item(key, value):
	return session.query(BillOfMaterialItem).filter(getattr(BillOfMaterialItem, key).contains(value)).all()


# select all bill of material item
def select_all_bill_of_material_item():
	return session.query(BillOfMaterialItem).filter(BillOfMaterialItem).all()


def select_bill_of_material_item_by_code(code):
	return session.query(BillOfMaterialItem).filter(BillOfMaterialItem.gen_code ==
													code).one()


# select bill of material items for maintenance
def select_bill_of_material_item_for_BOM(bill_of_material_id):
	return session.query(BillOfMaterialItem).filter(BillOfMaterialItem.bill_of_material_id ==
													bill_of_material_id).all()


def select_max_BOMITEM_id():
	maxcode = session.query(func.max(BillOfMaterialItem.id)).one()
	return (maxcode[0])


def select_max_BOMITEM_code():
	maxcode = session.query(func.max(BillOfMaterialItem.gen_code)).one()
	return (maxcode[0])
