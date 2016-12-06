from sqlalchemy.orm.session import sessionmaker

from models.dbUtile import engine, ManBOM

Session = sessionmaker(bind=engine)
session = Session()

def add_manBOM( manufact_id, created_at, cost_of_raw_material, cost_of_spare_parts, total_cost, gen_code):
	new_manBOM = ManBOM( manufact_id, created_at, cost_of_raw_material, cost_of_spare_parts, total_cost, gen_code)
	session.add(new_manBOM)
	session.commit()

def update_manBOM(id, manufact_id, created_at, cost_of_raw_material, cost_of_spare_parts, total_cost, gen_code):
	res = session.query(ManBOM).filter(ManBOM.id == id).one()
	res.manufact_id = manufact_id
	res.created_at = created_at
	res.cost_of_raw_material = cost_of_raw_material
	res.cost_of_spare_parts = cost_of_spare_parts
	res.total_cost = total_cost
	res.gen_code = gen_code
	if session.commit():
		return True
	else:
		return  False

def delete_manBOM(id):
	res = session.query(ManBOM).filter(ManBOM.id == id).one()
	session.delete(res)
	session.commit()

def select_manBOM_by_id(id):
	return session.query(ManBOM).filter(ManBOM.id == id).one()

def select_manBOM_by_code(code):
	return session.query(ManBOM).filter(ManBOM.gen_code == code).one()

def select_manBOM_by_manuf(manu_id):
	return session.query(ManBOM).filter(ManBOM.manufact_id == manu_id).one()

def select_all_manBOM():
	return session.query(ManBOM).all()

select_all_manBOM()