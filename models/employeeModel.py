from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import sessionmaker

from models.dbUtile import engine, Employees

Session = sessionmaker(bind=engine)
session = Session()

def add_employee(name, mobile_number, job_title, nationality, nat_id, gender, age):
	new_employee = Employees(name, mobile_number, job_title, nationality, nat_id, gender, age)
	session.add(new_employee)
	session.commit()
	return  new_employee

def update_employee(id, name, mobile_number, job_title, nationality, nat_id, gender, age):
	res = session.query(Employees).filter(Employees.id == id).one()
	res.name = name
	res.mobile_number = mobile_number
	res.job_title = job_title
	res.nationality = nationality
	res.nat_id = nat_id
	res.gender = gender
	res.age = age
	session.commit()

def delete_employee(id):
	res = session.query(Employees).filter(Employees.id == id).one()
	session.delete(res)
	session.commit()


def select_employee(key, value):
	try:
		return session.query(Employees).filter(getattr(Employees, key).contains(value)).all()
	except NoResultFound:
		return  False

def select_employee_by_mob_num(mobile_number):
	try:
		return session.query(Employees).filter(Employees.mobile_number == mobile_number).one()
	except NoResultFound:
		return False

def select_employee_by_id(id):
	try:
		res = session.query(Employees).filter(Employees.id == id).one()
		return res
	except NoResultFound:
		return False

def select_all_employees():
	return session.query(Employees).all()

def select_max_employee_id():
	maxcode = session.query(func.max(Employees.id)).one()
	return (maxcode[0])

def select_employee_exact(key, value):
	try:
		res = session.query(Employees).filter(getattr(Employees, key) == value).one()
		return  res
	except NoResultFound:
		return False

def select_employee_obj(obj):
	try:
		res = session.query(Employees).filter(Employees == obj).one()
		return  res
	except NoResultFound:
		return False

