from sqlalchemy.orm import sessionmaker

from models.dbUtile import RawMaterial, engine

# create a session
Session = sessionmaker(bind=engine)
session = Session()


# add new raw material
def add_raw_material(name, code, default_size, string_size, unit, cost_per_default_size, inv_qty, mini_qty):
	new_raw_material = RawMaterial(name, code, default_size, string_size, unit, cost_per_default_size, inv_qty, mini_qty)
	session.add(new_raw_material)
	session.commit()
	# print(new_raw_material)

def update_raw_material(id, code, name, default_size, string_size, unit, cost_per_default_size, inv_qty, mini_qty):
	res = session.query(RawMaterial).filter(RawMaterial.id == id).one()
	print(res)
	res.code = code
	res.name = name
	res.default_size = default_size
	res.string_size = string_size
	res.unit = unit
	res.cost_per_default_size = cost_per_default_size
	res.inv_qty = inv_qty
	res.mini_qty = mini_qty
	if session.commit():
		return True
	else:
		return False

def update_raw_material_inv_qty(id, inv_qty):
	res = session.query(RawMaterial).filter(RawMaterial.id == id).one()
	res.inv_qty = inv_qty
	if session.commit():
		return True
	else:
		return False

def update_raw_material_mini_qty(id, mini_qty):
	res = session.query(RawMaterial).filter(RawMaterial.id == id).one()
	res.mini_qty = mini_qty
	if session.commit():
		return True
	else:
		return False

def update_raw_material_cost(id, cost):
	res = session.query(RawMaterial).filter(RawMaterial.id == id).one()
	res.cost_per_default_size = cost
	if session.commit():
		return True
	else:
		return False

def delete_raw_material(id):
	res = session.query(RawMaterial).filter(RawMaterial.id == id).one()
	print(res)
	session.delete(res)
	session.commit()

def select_row_material(key, value):
	return session.query(RawMaterial).filter(getattr(RawMaterial, key).contains(value)).all()

def select_row_material_bycode(value):
	return session.query(RawMaterial).filter(RawMaterial.code == value).one()

def select_row_material_by_id(value):
	return session.query(RawMaterial).filter(RawMaterial.id == value).one()

def select_all_raw_material():
	return session.query(RawMaterial).all()
