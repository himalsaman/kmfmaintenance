from sqlalchemy_utils.functions.database import create_database, database_exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, Float, ForeignKey, MetaData, UnicodeText
from sqlalchemy.orm import relationship, backref

# create mysql engine
engine = create_engine('mysql+pymysql://root:root@localhost/maintenancedb?charset=utf8', echo=True)
metadata = MetaData()

# check if database is exists or not
# if not exists will be created it
if database_exists(engine.url) is False:
    print ("The database is not exists.")
    print ("It's will be created now")
    create_database(engine.url)
else:
    print ("The database already exists.")

# create Base
Base = declarative_base()


# create DB schema

# -#############################################################
### DB schema have 6 table
# 1- users
# 2- customers ( 1:1 city, 1:* maintenance)
# 3- city
# 4- raw_material
# 5- bill_of_material (1:& raw_material, 1:& spare_parts)
# 6- spare_parts
# 7- maintenance(1:1 customer, 1:& bill_of_material)
# -############################################################

# create user db table as class
class User(Base):
    __tablename__ = 'users'  # name of table

    # create row's of table
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    role = Column(String(20), nullable=False)

    def __init__(self, name, username, password, created_at, role):
        self.name = name
        self.username = username
        self.password = password
        self.created_at = created_at
        self.role = role

    # return and print user table creatation arch
    def __repr__(self):
        return "<User(name ="'{}'.format(self.name)+"\n"\
                "username ="'{}'.format(self.username)+"\n"\
                "password ="'{}'.format(self.password)+"\n"\
                "created_at ="'{}'.format(self.created_at)+"\n"\
                "role="'{}'.format(self.role)+")>"


# create customer db table as class
class Customers(Base):
    __tablename__ = 'customers'  # name of table

    # create row's of table
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200), nullable=False)
    mobile_number = Column(String(13), nullable=False, unique=True)
    gender = Column(String(10), nullable=True)
    age = Column(Integer, nullable=True)
    # one to one relationship with city table
    city_id = Column(Integer, ForeignKey('city.id'), nullable=True)
    city = relationship('City', backref=backref('customers_city', uselist=False))

    maintenance = relationship('Maintenance', backref=backref('maintenance_customers'))

    def __init__(self, name, mobile_number, gender, age, city_id):
        self.name = name
        self.mobile_number = mobile_number
        self.gender = gender
        self.age = age
        self.city_id = city_id

    # return and print customer table creation arch
    def __repr__(self):
        return "<Customer(name ="'{}'.format(self.name)+"\n"\
                "mobile_number ="'{}'.format(self.mobile_number)+"\n"\
                "gender ="'{}'.format(self.gender)+"\n"\
                "age ="'{}'.format(self.age)+"\n"\
                "city_id ="'{}'.format(self.city_id)+")>"

# create city db table as class
class City(Base):
    __tablename__ = 'city'  # name of table

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50))
    # one to one relationship with customer table
    customers = relationship('Customers', backref=backref('customers_city'))  # any error remove backref property

    def __init__(self, name):
        self.name = name

    # return and print city table creation arch
    def __repr__(self):
        return "<City (name ="'{}'.format(self.name)+")>"


# create raw material db table as class
class RawMaterial(Base):
    __tablename__ = 'raw_material'  # name of table

    # create row's of table
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100))
    default_size = Column(Integer, nullable=False)
    string_size = Column(String(50))
    unit = Column(String(50), nullable=False)
    cost_per_default_size = Column(Float, nullable=False)
    inv_qty = Column(Float, nullable=False)
    # one to many relationship with bill_of_material
    billOfMaterialItem = relationship('BillOfMaterialItem', backref=backref('billOfMaterial_rawMaterial'))

    def __init__(self, name, default_size, string_size, unit, cost_per_default_size, inv_qty):
        self.name = name
        self.default_size = default_size
        self.string_size = string_size
        self.unit = unit
        self.cost_per_default_size = cost_per_default_size
        self.inv_qty = inv_qty

    # return and print raw material table creation arch
    def __repr__(self):
        return "<Row Material(name ="'{}'.format(self.name)+"\n"\
                "default_size ="'{}'.format(self.default_size)+"\n"\
                "string_size ="'{}'.format(self.string_size)+"\n"\
                "unit ="'{}'.format(self.unit)+"\n"\
                "cost_per_default_size ="'{}'.format(self.cost_per_default_size)+"\n"\
                "inv_qty ="'{}'.format(self.inv_qty)+")>"


# create spare parts db table as class
class SpareParts(Base):
    __tablename__ = 'spare_parts'

    # create row's of table
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200))
    code = Column(String(20), nullable=False, unique=True)
    price = Column(Float, nullable=False)
    inv_qty = Column(Integer, nullable=False)
    billOfMaterialItem = relationship('BillOfMaterialItem', backref=backref('billOfMaterial_sparePart'))

    def __init__(self, name, code, price, inv_qyt):
        self.name = name
        self.code = code
        self.price = price
        self.inv_qty = inv_qyt

    # return and print spare parts table creation arch
    def __repr__(self):
        return "<Spare Parts (name ="'{}'.format(self.name)+"\n"\
                "code ="'{}'.format(self.code)+"\n"\
                "price ="'{}'.format(self.price)+"\n"\
                "inv_qty ="'{}'.format(self.inv_qty)+")>"


# many bill_of_material_item  to one maintenance
# one row can be raw material or spare part with him calculation
class BillOfMaterialItem(Base):
    __tablename__ = 'bill_of_material_item'  # name of table

    # create row's of table
    id = Column(Integer, primary_key=True, nullable=False)

    # relationship with raw material table, if null must spare_part_id not null
    raw_material_id = Column(Integer, ForeignKey('raw_material.id'))
    rawMaterial = relationship('RawMaterial', backref=backref('billOfMaterialItem_row_material'))

    # relationship with spare part table, if null must raw_material_id not null
    spare_part_id = Column(Integer, ForeignKey('spare_parts.id'))
    spareParts = relationship('SpareParts', backref=backref('billOfMaterialItem_spareParts'))

    # relationship with maintenance table
    # because each row mu assign for the target maintenance
    bill_of_material_id = Column(Integer, ForeignKey('bill_of_material.id'))
    billOfMaterial = relationship('BillOfMaterial', backref=backref('billOfMaterialItem_bom'))

    # cost and qty can be for raw material or spare part not both together
    cost_of_material = Column(Float)
    qty_of_material = Column(Float)

    def __init__(self, raw_material_id, spare_parts_id, maintenance_id, cost_of_material, qty_of_material):
        self.raw_material_id = raw_material_id
        self.spare_part_id = spare_parts_id
        self.maintenance_id = maintenance_id
        self.cost_of_material = cost_of_material
        self.qty_of_material = qty_of_material

    # return and print bill of material table creation arch
    def __repr__(self):
        return "<Bill of Material (raw_material_id ="'{}'.format(self.rawMaterial.name)+"\n"\
                "spare_part_id =" '{}'.format(self.spareParts.code)+"\n"\
                "maintenance_id =" '{}'.format(self.maintenance_id)+"\n"\
                "cost_of_material =" '{}'.format(self.cost_of_material)+"\n"\
                "qty_of_material =" '{}'.format(self.qty_of_material)+")>"

class BillOfMaterial(Base):
    __tablename__ = 'bill_of_material'

    id = Column(Integer, primary_key=True, nullable=False)
    billOfMaterialItem = relationship('BillOfMaterialItem', backref=backref('billOfMaterialItem_bom'))

    maintenance_id = Column(Integer, ForeignKey('maintenance.id'))
    maintenance = relationship('Maintenance', backref=backref('bom_maintenance'))

    def __init__(self, maintenance_id):
        self.maintenance_id = maintenance_id

    def __repr__(self, maintenance_id):
        return "BOM (maintenance_id = " '{}'.format(self.maintenance.id)

# create maintenance db table as class
class Maintenance(Base):
    __tablename__ = 'maintenance'

    # create row's of table
    id = Column(Integer, primary_key=True, nullable=False)

    customers_id = Column(Integer, ForeignKey('customers.id'))
    customers = relationship('Customers', backref=backref('maintenance_customers'))

    # bill_of_material_id = Column(Integer, ForeignKey('bill_of_material.id'))
    # billOfMaterials = relationship('BillOfMaterial', backref=backref('bom_maintenance'))


    billOfMaterial = relationship('BillOfMaterial', backref=backref('billOfMaterial_maintenance'))

    cost_of_bill_of_material = Column(Float)
    cost_of_spare_parts = Column(Float)
    cost_of_raw_material = Column(Float)
    cost_of_labor = Column(Float)
    cost_of_another = Column(Float)
    cost_of_another_description = Column(String(1000))
    created_at = Column(TIMESTAMP, nullable=False)
    close_at = Column(TIMESTAMP)
    product_of_maintenance = Column(String(200), nullable=False)
    maintenance_description = Column(UnicodeText)

    def __init__(self, customers_id, cost_of_bill_of_material, cost_of_raw_material, cost_of_spare_parts, cost_of_labor,
                 cost_of_another, cost_of_another_description, created_at, close_at, product_of_maintenance,
                 maintenance_description, bill_of_material_id):
        self.customers_id = customers_id
        self.cost_of_bill_of_material = cost_of_bill_of_material
        self.cost_of_spare_parts = cost_of_spare_parts
        self.cost_of_raw_material = cost_of_raw_material
        self.cost_of_labor = cost_of_labor
        self.cost_of_another = cost_of_another
        self.cost_of_another_description = cost_of_another_description
        self.created_at = created_at
        self.close_at = close_at
        self.product_of_maintenance = product_of_maintenance
        self.maintenance_description = maintenance_description
        # self.bill_of_material_id = bill_of_material_id

    def __repr__(self):
        return "Maintenance (customers_id = " '{}'.format(self.customers.name)+"\n"\
               "cost_of_bill_of_material = "'{}'.format(self.cost_of_bill_of_material)+"\n"\
               "cost_of_spare_parts = "'{}'.format(self.cost_of_spare_parts)+"\n"\
               "cost_of_raw_material = "'{}'.format(self.cost_of_raw_material)+"\n"\
               "cost_of_labor ="'{}'.format(self.cost_of_labor)+"\n"\
               "cost_of_another ="'{}'.format(self.cost_of_another)+"\n"\
               "cost_of_another_description = "'{}'.format(self.cost_of_another_description)+"\n"\
               "created_at = "'{}'.format(self.created_at)+"\n"\
               "close_at = "'{}'.format(self.close_at)+"\n"\
               "product_of_maintenance ="'{}'.format(self.product_of_maintenance)+"\n"\
               "maintenance_description = "'{}'.format(self.maintenance_description)+"\n" \
               # "bill_of_material_id = "'{}'.format(self.bill_of_material_id) + "\n" \
        ")>"


Base.metadata.create_all(engine)
