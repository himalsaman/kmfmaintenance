from sqlalchemy.orm.session import sessionmaker

from models.dbUtile import engine, Tools

Session = sessionmaker(bind=engine)
session = Session()

def add_tools(name, code, price, inv_qty, unit, gen_code):
	new_tools = Tools(name, code, price, inv_qty, unit, gen_code)
	session.add(new_tools)
	session.commit()

def update_tools(id, name, code, price, inv_qty, unit, gen_code):
	res = session.query(Tools).filter(Tools.id == id).one()
	res.name = name
	res.code = code
	res.price = price
	res.inv_qty = inv_qty
	res.unit = unit
	res.gen_code = gen_code
	if session.commit():
		return True
	else:
		return False

def update_tools_inv_qty(id, inv_qty):
	res = session.query(Tools).filter(Tools.id == id).one()
	res.inv_qty = inv_qty
	if session.commit():
		return True
	else:
		return False

def update_tools_cost(id, cost):
	res = session.query(Tools).filter(Tools.id == id).one()
	res.price = cost
	if session.commit():
		return True
	else:
		return False

def delete_tools(id):
	res = session.query(Tools).filter(Tools.id == id).one()
	print(res)
	session.delete(res)
	session.commit()

def select_tools(key, value):
	return session.query(Tools).filter(getattr(Tools, key).contains(value)).all()

def select_tools_by_gen_code(value):
	return session.query(Tools).filter(Tools.gen_code == value).one()

def select_tools_by_id(value):
	return session.query(Tools).filter(Tools.id == value).one()

# select all raw material
def select_all_tools():
	return session.query(Tools).all()

