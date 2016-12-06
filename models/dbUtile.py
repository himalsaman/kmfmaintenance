from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, Float, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils.functions.database import create_database, database_exists

# create mysql engine
sdb = '10.0.0.3'
tdb = '127.0.0.1'
engine = create_engine('mysql+pymysql://root:root@'+tdb+'/maintenancedb?charset=utf8', echo=True)
metadata = MetaData()

# check if database is exists or not
# if not exists will be created it
if database_exists(engine.url) is False:
	print("The database is not exists.")
	print("It's will be created now")
	create_database(engine.url)
else:
	print("The database already exists.")

# create Base
Base = declarative_base()

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
		return "<User(name ="'{}'.format(self.name) + "\n" \
													  "username ="'{}'.format(self.username) + "\n" \
																							   "password ="'{}'.format(
			self.password) + "\n" \
							 "created_at ="'{}'.format(self.created_at) + "\n" \
																		  "role="'{}'.format(self.role) + ")>"

# create customer db table as class
class Customers(Base):
	__tablename__ = 'customers'  # name of table

	# create row's of table
	id = Column(Integer, primary_key=True, nullable=False)
	name = Column(String(200), nullable=False)
	mobile_number = Column(String(13), nullable=False, unique=True)
	mobile_number_1 = Column(String(13))
	mobile_number_2 = Column(String(13))
	mobile_number_3 = Column(String(13))
	mobile_number_4 = Column(String(13))
	gender = Column(String(10), nullable=True)
	age = Column(Integer, nullable=True)
	# one to one relationship with city table
	city_id = Column(Integer, ForeignKey('city.id'), nullable=True)
	city = relationship('City', backref=backref('customers_city', uselist=False))

	maintenance = relationship('Maintenance', backref=backref('maintenance_customers'))

	outbound = relationship('Outbound', backref=backref('outbound_customers'))

	def __init__(self, name, mobile_number, mobile_number_1, mobile_number_2, mobile_number_3, mobile_number_4, gender, age, city_id):
		self.name = name
		self.mobile_number = mobile_number
		self.mobile_number_1 = mobile_number_1
		self.mobile_number_2 = mobile_number_2
		self.mobile_number_3 = mobile_number_3
		self.mobile_number_4 = mobile_number_4
		self.gender = gender
		self.age = age
		self.city_id = city_id

	# return and print customer table creation arch
	def __repr__(self):
		return "<Customer(name ="'{}'.format(self.name) + "\n" \
				"mobile_number ="'{}'.format(self.mobile_number) + "\n" \
			   	"mobile_number_1 ="'{}'.format(self.mobile_number_1) + "\n" \
				"mobile_number_2 ="'{}'.format(self.mobile_number_2) + "\n" \
				"mobile_number_3 ="'{}'.format(self.mobile_number_3) + "\n" \
				"mobile_number_4 ="'{}'.format(self.mobile_number_4) + "\n" \
																					 "gender ="'{}'.format(
			self.gender) + "\n" \
						   "age ="'{}'.format(self.age) + "\n" \
														  "city_id ="'{}'.format(self.city_id) + ")>"

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
		return "<City (name ="'{}'.format(self.name) + ")>"

# create raw material db table as class
class RawMaterial(Base):
	__tablename__ = 'raw_material'  # name of table

	# create row's of table
	id = Column(Integer, primary_key=True, nullable=False)
	name = Column(String(100))
	code = Column(String(100), unique=True)
	default_size = Column(Float, nullable=False)
	string_size = Column(String(50))
	unit = Column(String(50), nullable=False)
	cost_per_default_size = Column(Float, nullable=False)
	inv_qty = Column(Float, nullable=False)
	# one to many relationship with bill_of_material
	billOfMaterialItem = relationship('BillOfMaterialItem', backref=backref('billOfMaterial_rawMaterial'))

	outbound = relationship('Outbound', backref=backref('outbound_raw_material'))

	def __init__(self, name, code, default_size, string_size, unit, cost_per_default_size, inv_qty):
		self.name = name
		self.code = code
		self.default_size = default_size
		self.string_size = string_size
		self.unit = unit
		self.cost_per_default_size = cost_per_default_size
		self.inv_qty = inv_qty

	# return and print raw material table creation arch
	def __repr__(self):
		return "<Row Material(name ="'{}'.format(self.name) + "\n" \
															  "code ="'{}'.format(self.code) + "\n" \
																							   "default_size ="'{}'.format(
			self.default_size) + "\n" \
								 "string_size ="'{}'.format(self.string_size) + "\n" \
																				"unit ="'{}'.format(self.unit) + "\n" \
																												 "cost_per_default_size ="'{}'.format(
			self.cost_per_default_size) + "\n" \
										  "inv_qty ="'{}'.format(self.inv_qty) + ")>"

# create spare parts db table as class
class SpareParts(Base):
	__tablename__ = 'spare_parts'

	# create row's of table
	id = Column(Integer, primary_key=True, nullable=False)
	name = Column(String(200))
	code = Column(String(20), nullable=False, unique=True)
	gen_code = Column(String(100), nullable=False)
	price = Column(Float, nullable=False)
	inv_qty = Column(Integer, nullable=False)
	unit = Column(String(20))
	billOfMaterialItem = relationship('BillOfMaterialItem', backref=backref('billOfMaterial_sparePart'))

	outbound = relationship('Outbound', backref=backref('outbound_spare_part'))

	def __init__(self, name, code, gen_code, price, inv_qyt, unit):
		self.name = name
		self.code = code
		self.price = price
		self.inv_qty = inv_qyt
		self.gen_code = gen_code
		self.unit = unit

	# return and print spare parts table creation arch
	def __repr__(self):
		return "<Spare Parts (name ="'{}'.format(self.name) + "\n" \
															  "code ="'{}'.format(self.code) + "\n" \
																							   "price ="'{}'.format(
			self.price) + "\n" \
						  "inv_qty ="'{}'.format(self.inv_qty) + "\n" \
																 "unit ="'{}'.format(self.unit) + "\n" \
																								  "gen_code ="'{}'.format(
			self.gen_code) + ")>"

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
	gen_code = Column(String(100))

	def __init__(self,raw_material_id, spare_parts_id, bill_of_material_id, cost_of_material,
				 qty_of_material, gen_code):
		self.raw_material_id = raw_material_id
		self.spare_part_id = spare_parts_id
		self.bill_of_material_id = bill_of_material_id
		self.cost_of_material = cost_of_material
		self.qty_of_material = qty_of_material
		self.gen_code = gen_code

	# return and print bill of material table creation arch
	def __repr__(self):
		return "<Bill of Material (raw_material_id ="'{}'.format(self.raw_material_id) + "\n" \
																						 "gen_code =" '{}'.format(
			self.gen_code) + "\n" \
							 "spare_part_id =" '{}'.format(self.spare_part_id) + "\n" \
																				 "bill_of_material_id =" '{}'.format(
			self.bill_of_material_id) + "\n" \
										"cost_of_material =" '{}'.format(
			self.cost_of_material) + "\n" \
									 "qty_of_material =" '{}'.format(self.qty_of_material) + ")>"

class BillOfMaterial(Base):
	__tablename__ = 'bill_of_material'

	id = Column(Integer, primary_key=True, nullable=False)
	billOfMaterialItem = relationship('BillOfMaterialItem', backref=backref('billOfMaterialItem_bom'))

	maintenance_id = Column(Integer, ForeignKey('maintenance.id'))
	maintenance = relationship('Maintenance', backref=backref('bom_maintenance'))

	created_at = Column(TIMESTAMP)
	cost_of_spare_parts = Column(Float)
	cost_of_raw_material = Column(Float)
	total_cost = Column(Float)
	gen_code = Column(String(100))

	def __init__(self, maintenance_id, created_at, cost_of_raw_material, cost_of_spare_parts, total_cost, gen_code):
		self.maintenance_id = maintenance_id
		self.created_at = created_at
		self.cost_of_spare_parts = cost_of_spare_parts
		self.cost_of_raw_material = cost_of_raw_material
		self.total_cost = total_cost
		self.gen_code = gen_code

	def __repr__(self):
		return "BOM (maintenance_id = " '{}'.format(self.maintenance_id) + "\n" \
																		   "cost_of_spare_parts = "'{}'.format(
			self.cost_of_spare_parts) + "\n" \
										"cost_of_raw_material = "'{}'.format(self.cost_of_raw_material) + "\n" \
																										  "total_cost= "'{}'.format(
			self.total_cost) + "\n" \
							   "gen_code = "'{}'.format(self.gen_code) + "\n" \
																		 "created_at = " '{}'.format(self.created_at)

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
	cost_of_labor = Column(Float)
	cost_of_another = Column(Float)
	cost_of_another_description = Column(String(1000))
	created_at = Column(TIMESTAMP)  # date of created to calculate BOM
	close_at = Column(TIMESTAMP)  # close date : the customer take product back
	product_of_maintenance = Column(String(200), nullable=True)
	maintenance_description = Column(String(20000))
	start_date = Column(TIMESTAMP)  # actually date for start
	done_date = Column(TIMESTAMP)  # actually date for finish maintenance
	m_code = Column(String(100))
	hidden = Column(Integer)

	def __init__(self, m_code, customer_id, cost_of_bill_of_material, cost_of_labor,
				 cost_of_another, cost_of_another_description, created_at, close_at,
				 product_of_maintenance, maintenance_description, start_date, done_date, hidden):
		self.m_code = m_code
		self.customers_id = customer_id
		self.cost_of_bill_of_material = cost_of_bill_of_material
		self.cost_of_labor = cost_of_labor
		self.cost_of_another = cost_of_another
		self.cost_of_another_description = cost_of_another_description
		self.created_at = created_at
		self.close_at = close_at
		self.product_of_maintenance = product_of_maintenance
		self.maintenance_description = maintenance_description
		self.start_date = start_date
		self.done_date = done_date
		self.hidden = hidden

	# self.customers = customers
	# self.bill_of_material_id = bill_of_material_id
	def getMainte(self):
		return self.code

	def setMainte(self, code):
		self.code = code

	def __repr__(self):
		return "Maintenance (m_code = " '{}'.format(self.m_code) + "\n" \
				"customers_id = " '{}'.format(self.customers.id) + "\n" \
				"cost_of_bill_of_material = "'{}'.format(self.cost_of_bill_of_material) + "\n" \
				"cost_of_labor ="'{}'.format(self.cost_of_labor) + "\n" \
				"cost_of_another ="'{}'.format(self.cost_of_another) + "\n" \
				"cost_of_another_description = "'{}'.format(self.cost_of_another_description) + \
			    "\n created_at = "'{}'.format(self.created_at) + "\n" \
				"close_at = "'{}'.format(self.close_at) + "\n" \
				"product_of_maintenance ="'{}'.format(self.product_of_maintenance) + "\n" \
				"maintenance_description = "'{}'.format(self.maintenance_description) + "\n" \
				"hidden = "'{}'.format(self.hidden) + "\n" + "start_date = "'{}'.format(
				self.start_date) + "\n done_date = "'{}'.format(self.done_date) + ")>"

class Tools(Base):
	__tablename__ = 'tools'

	id = Column(Integer, primary_key=True, nullable=False)
	name = Column(String(200))
	code =  Column(String(50))
	price = Column(Float)
	inv_qty = Column(Integer)
	unit = Column(String(50))
	gen_code = Column(String(100))

	outbound = relationship('Outbound', backref=backref('outbound_tools'))

	def __init__(self, name, code, price, inv_qty, unit, gen_code):
		self.name = name
		self.code = code
		self.price = price
		self.inv_qty = inv_qty
		self.unit = unit
		self.gen_code = gen_code

	def __repr__(self):
		return "Tools (name = " '{}'.format(self.name) + "\n" \
				"code = " '{}'.format(self.code) + "\n" \
				"price = " '{}'.format(self.price) + "\n" \
				"inv_qty = " '{}'.format(self.inv_qty) + "\n" \
				"unit = " '{}'.format(self.unit) + "\n" \
				"gen_code = " '{}'.format(self.gen_code) + "\n)>"

class FinishProducts(Base):
	__tablename__ = 'finish_products'

	id = Column(Integer, primary_key=True, nullable=False)
	name = Column(String(200))
	code =  Column(String(50))
	price = Column(Float)
	inv_qty = Column(Integer)
	source = Column(String(50))
	gen_code = Column(String(100))

	outbound = relationship('Outbound', backref=backref('outbound_finish_product'))

	def __init__(self, name, code, price, inv_qty, source, gen_code):
		self.name = name
		self.code = code
		self.price = price
		self.inv_qty = inv_qty
		self.source = source
		self.gen_code = gen_code

	def __repr__(self):
		return "Tools (name = " '{}'.format(self.name) + "\n" \
				"code = " '{}'.format(self.code) + "\n" \
				"price = " '{}'.format(self.price) + "\n" \
				"inv_qty = " '{}'.format(self.inv_qty) + "\n" \
				"source = " '{}'.format(self.source) + "\n" \
				"gen_code = " '{}'.format(self.gen_code) + "\n)>"

class Employees(Base):
	__tablename__ = 'employee'  # name of table

	# create row's of table
	id = Column(Integer, primary_key=True, nullable=False)
	name = Column(String(200), nullable=False)
	mobile_number = Column(String(13), nullable=False, unique=True)
	job_title = Column(String(100))
	nationality = Column(String(100))
	nat_id = Column(String(100))
	gender = Column(String(10), nullable=True)
	age = Column(Integer, nullable=True)
	# one to one relationship with city table

	outbound = relationship('Outbound', backref=backref('outbound_employee'))

	def __init__(self, name, mobile_number, job_title, nationality, nat_id, gender, age):
		self.name = name
		self.mobile_number = mobile_number
		self.job_title = job_title
		self.nationality = nationality
		self.nat_id = nat_id
		self.gender = gender
		self.age = age

	# return and print customer table creation arch
	def __repr__(self):
		return "<Customer(name ="'{}'.format(self.name) + "\n" \
				"mobile_number ="'{}'.format(self.mobile_number) + "\n" \
			   	"job_title ="'{}'.format(self.job_title) + "\n" \
				"nationality ="'{}'.format(self.nationality) + "\n" \
				"nat_id ="'{}'.format(self.nat_id) + "\n" \
				"gender ="'{}'.format(self.gender) + "\n" \
				"age ="'{}'.format(self.age) + ")>"

class Outbound(Base):
	__tablename__ = 'outbound'

	id = Column(Integer, primary_key=True, nullable=False)
	code = Column(String(50))
	out_date = Column(TIMESTAMP)
	reason = Column(String(100))

	customer_id = Column(Integer, ForeignKey('customers.id'))
	customers = relationship('Customers', backref=backref('outbound_customers'))

	employee_id = Column(Integer, ForeignKey('employee.id'))
	employee = relationship('Employees', backref=backref('outbound_employee'))

	raw_material_id = Column(Integer, ForeignKey('raw_material.id'))
	rawMaterial = relationship('RawMaterial', backref=backref('outbound_row_material'))

	# relationship with spare part table, if null must raw_material_id not null
	spare_part_id = Column(Integer, ForeignKey('spare_parts.id'))
	spareParts = relationship('SpareParts', backref=backref('outbound_spareParts'))

	tools_id = Column(Integer, ForeignKey('tools.id'))
	tools = relationship('Tools', backref=backref('outbound_tools'))

	product_id = Column(Integer, ForeignKey('finish_products.id'))
	finishProducts = relationship('FinishProducts', backref=backref('finish_products_outbound'))

	def __init__(self, code, out_date, reason, customer_id, employee_id, raw_material_id,
				 spare_part_id, tools_id, product_id):
		self.code = code
		self.out_date = out_date
		self.reason = reason
		self.customer_id = customer_id
		self.employee_id = employee_id
		self.raw_material_id = raw_material_id
		self.spare_part_id = spare_part_id
		self.tools_id = tools_id
		self.product_id = product_id

	def __repr__(self):
		return "<Outbound (code ="'{}'.format(self.code) + "\n" \
				"out_date =" '{}'.format(self.out_date) + "\n" \
				"reason =" '{}'.format(self.reason) + "\n" \
				"customer_id =" '{}'.format(self.customer_id) + "\n" \
				"employee_id =" '{}'.format(self.employee_id) + "\n" \
				"raw_material_id =" '{}'.format(self.raw_material_id) + "\n" \
				"spare_part_id =" '{}'.format(self.spare_part_id) + "\n" \
				"tools_id =" '{}'.format(self.tools_id) + "\n" \
				"product_id =" '{}'.format(self.product_id) + ")>"

Base.metadata.create_all(engine)
