from sqlalchemy.orm import sessionmaker
from models.dbUtile import RawMaterial, engine

# create a session
Session = sessionmaker(bind=engine)
session = Session()


# add new raw material
def add_raw_material(name, code,default_size, string_size, unit, cost_per_default_size, inv_qty):
    new_raw_material = RawMaterial(name, code, default_size, string_size, unit, cost_per_default_size, inv_qty)
    session.add(new_raw_material)
    session.commit()
    print  (new_raw_material)


# update raw material
def update_raw_material(id, code, name, default_size, string_size, unit, cost_per_default_size, inv_qty):
    res = session.query(RawMaterial).filter(RawMaterial.id == id).one()
    print (res)
    res.code = code
    res.name = name
    res.default_size = default_size
    res.string_size = string_size
    res.unit = unit
    res.cost_per_default_size = cost_per_default_size
    res.inv_qty = inv_qty
    if session.commit():
        return True
    else:
        return False


# delete raw material
def delete_raw_material(id):
    res = session.query(RawMaterial).filter(RawMaterial.id == id).one()
    print (res)
    session.delete(res)
    session.commit()


# select row material by key and value
def select_row_material(key, value):
    return session.query(RawMaterial).filter(getattr(RawMaterial, key).contains(value)).all()

def select_row_material_bycode(value):
    return session.query(RawMaterial).filter(RawMaterial.code == value).one()



# select all raw material
def select_all_raw_material():
    return session.query(RawMaterial).all()
