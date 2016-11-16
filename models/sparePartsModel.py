from sqlalchemy.orm import sessionmaker
from models.dbUtile import SpareParts, engine

# create a session
Session = sessionmaker(bind=engine)
session = Session()


# add new raw material
def add_spare_parts(name, code, gen_code,  price, inv_qty, unit):
    new_spare_parts = SpareParts(name, code, gen_code, price, inv_qty, unit)
    session.add(new_spare_parts)
    session.commit()
    print  (new_spare_parts)


# update raw material
def update_spare_parts(id, name, code, gen_code, price, inv_qty, unit):
    res = session.query(SpareParts).filter(SpareParts.id == id).one()
    print (res)
    res.name = name
    res.code = code
    res.price = price
    res.inv_qty = inv_qty
    res.gen_code = gen_code
    res.unit = unit
    session.commit()


# delete raw material
def delete_spare_parts(id):
    res = session.query(SpareParts).filter(SpareParts.id == id).one()
    print (res)
    session.delete(res)
    session.commit()


# select row material by key and value
def select_spare_parts(key, value):
    return session.query(SpareParts).filter(getattr(SpareParts, key).contains(value)).all()


def select_spare_parts_bygen_code(gen_code):
    return session.query(SpareParts).filter(SpareParts.gen_code == gen_code).one()

def select_spare_parts_bycode(code):
    return session.query(SpareParts).filter(SpareParts.gen_code == code).one()

def select_spare_parts_by_id(code):
    return session.query(SpareParts).filter(SpareParts.id == code).one()

# select all raw material
def select_all_spare_parts():
    return session.query(SpareParts).all()
