from sqlalchemy.orm.session import sessionmaker

from models.dbUtile import engine, FinishProducts

Session = sessionmaker(bind=engine)
session = Session()


def add_finish_product(name, code, price, inv_qty, source, gen_code, mini_qty):
	new_finish_product = FinishProducts(name, code, price, inv_qty, source, gen_code, mini_qty)
	session.add(new_finish_product)
	session.commit()


def update_finish_product(id, name, code, price, inv_qty, source, gen_code):
	res = session.query(FinishProducts).filter(FinishProducts.id == id).one()
	res.name = name
	res.code = code
	res.price = price
	res.inv_qty = inv_qty
	res.source = source
	res.gen_code = gen_code
	if session.commit():
		return True
	else:
		return False


def update_finish_product_inv_qty(id, inv_qty):
	res = session.query(FinishProducts).filter(FinishProducts.id == id).one()
	res.inv_qty = inv_qty
	if session.commit():
		return True
	else:
		return False

def update_finish_product_mini_qty(id, mini_qty):
	res = session.query(FinishProducts).filter(FinishProducts.id == id).one()
	res.mini_qty = mini_qty
	if session.commit():
		return True
	else:
		return False

def update_finish_product_cost(id, cost):
	res = session.query(FinishProducts).filter(FinishProducts.id == id).one()
	res.price = cost
	if session.commit():
		return True
	else:
		return False


def delete_finish_product(id):
	res = session.query(FinishProducts).filter(FinishProducts.id == id).one()
	print(res)
	session.delete(res)
	session.commit()


def select_finish_product(key, value):
	return session.query(FinishProducts).filter(getattr(FinishProducts, key).contains(value)).all()


def select_finish_product_by_gen_code(value):
	return session.query(FinishProducts).filter(FinishProducts.gen_code == value).one()


def select_finish_product_by_id(value):
	return session.query(FinishProducts).filter(FinishProducts.id == value).one()


# select all raw material
def select_all_finish_product():
	return session.query(FinishProducts).all()
