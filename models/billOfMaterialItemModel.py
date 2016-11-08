from sqlalchemy.orm import sessionmaker
from models.dbUtile import BillOfMaterialItem, engine


# create a session
Session = sessionmaker(bind=engine)
session = sessionmaker()


# add new bill of material item
def add_new_bill_of_material_item(raw_material_id, spare_parts_id, maintenance_id, cost_of_material, qty_of_material):
    new_bill_of_material_item = BillOfMaterialItem(raw_material_id, spare_parts_id, maintenance_id, cost_of_material, qty_of_material)
    session.add(new_bill_of_material_item)
    session.commit()
    print (new_bill_of_material_item)


# update bill of material item
def update_bill_of_material_item(id, raw_material_id, spare_parts_id, maintenance_id, cost_of_material,
                                 qty_of_material):
    res = session.query(BillOfMaterialItem).filter(BillOfMaterialItem.id == id).one()
    print (res)
    res.raw_material_id = raw_material_id
    res.spare_parts_id = spare_parts_id
    res.maintenance_id = maintenance_id
    res.cost_of_material = cost_of_material
    res.qty_of_material = qty_of_material
    session.commit()


# delete bill of material
def delete_bill_of_material_item(id):
    res = session.query(BillOfMaterialItem).filter(BillOfMaterialItem.id == id).one()
    print (res)
    session.delete(res)
    session.commit()


# select bill of material by key and value
def select_bill_of_material_item(key, value):
    res = session.query(BillOfMaterialItem).filter(getattr(BillOfMaterialItem, key).contains(value)).all()
    for b in res:
        print (b)


# select all bill of material item
def select_all_bill_of_material_item():
    res = session.query(BillOfMaterialItem).filter(BillOfMaterialItem).all()
    for b in res:
        print (b)


# select bill of material items for maintenance
def select_bill_of_material_item_for_maintenance(maintenance_id):
    res = session.query(BillOfMaterialItem).filter(BillOfMaterialItem.maintenance_id == maintenance_id).all()
    for bm in res:
        print (bm)
