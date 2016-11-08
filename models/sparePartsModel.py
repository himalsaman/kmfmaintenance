from sqlalchemy.orm import sessionmaker
from models.dbUtile import SpareParts, engine

# create a session
Session = sessionmaker(bind=engine)
session = Session()


# add new raw material
def add_spare_parts(name, code, price, inv_qty):
    new_spare_parts = SpareParts(name, code, price, inv_qty)
    session.add(new_spare_parts)
    session.commit()
    print  (new_spare_parts)


# update raw material
def update_spare_parts(id, name, code, price, inv_qty):
    res = session.query(SpareParts).filter(SpareParts.id == id).one()
    print (res)
    res.name = name
    res.code = code
    res.price = price
    res.inv_qty = inv_qty
    session.commit()


# delete raw material
def delete_spare_parts(id):
    res = session.query(SpareParts).filter(SpareParts.id == id).one()
    print (res)
    session.delete(res)
    session.commit()


# select row material by key and value
def select_spare_parts(key, value):
    res = session.query(SpareParts).filter(getattr(SpareParts, key).contains(value)).all()
    for r in res:
        print (r)


# select all raw material
def select_all_spare_parts():
    res = session.query(SpareParts).all()
    for r in res:
        print (r)
