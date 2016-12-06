# create a session
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from models.dbUtile import engine, ManBOMItem

Session = sessionmaker(bind=engine)
session = Session()

def add_manBOMItem(tools_id, raw_material_id, spare_parts_id, manBOM_id, cost_of_material, qty_of_material, gen_code):
	new_manBOMItem = ManBOMItem(tools_id, raw_material_id, spare_parts_id, manBOM_id,
												   cost_of_material, qty_of_material, gen_code)
	session.add(new_manBOMItem)
	session.commit()


# update bill of material item
def update_manBOMItem(id, tools_id,raw_material_id, spare_parts_id, manBOM_id,
								 cost_of_material,qty_of_material):
	res = session.query(ManBOMItem).filter(ManBOMItem.id == id).one()
	print(res)
	res.tools_id = tools_id,
	res.raw_material_id = raw_material_id
	res.spare_parts_id = spare_parts_id
	res.manBOM_id = manBOM_id
	res.cost_of_material = cost_of_material
	res.qty_of_material = qty_of_material
	session.commit()


# delete bill of material
def delete_manBOMItem(id):
	res = session.query(ManBOMItem).filter(ManBOMItem.id == id).one()
	print(res)
	session.delete(res)
	session.commit()


# select bill of material by key and value
def select_manBOMItem(key, value):
	return session.query(ManBOMItem).filter(getattr(ManBOMItem, key).contains(value)).all()


# select all bill of material item
def select_all_manBOMItem():
	return session.query(ManBOMItem).all()


def select_manBOMItem_by_code(code):
	return session.query(ManBOMItem).filter(ManBOMItem.gen_code ==
													code).one()


# select bill of material items for maintenance
def select_manBOMItem_for_BOM(manBOM_id):
	return session.query(ManBOMItem).filter(ManBOMItem.bill_of_material_id ==
											manBOM_id).all()


def select_max_manBOMItem_id():
	maxcode = session.query(func.max(ManBOMItem.id)).one()
	return (maxcode[0])


def select_max_manBOMItem_code():
	maxcode = session.query(func.max(ManBOMItem.gen_code)).one()
	return (maxcode[0])
