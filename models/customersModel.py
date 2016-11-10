from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from models.dbUtile import Customers, City, engine

# create a session
Session = sessionmaker(bind=engine)
session = Session()


# add new customer
def add_customer(name, mobile_number, gender, age, city_id):
    new_customer = Customers(name, mobile_number, gender, age, city_id)
    session.add(new_customer)
    session.commit()
    print (new_customer)


# update or edit exists customer
def update_customer(id, name, mobile_number, gender, age, city_id):
    res = session.query(Customers).filter(Customers.id == id).one()
    print  (res)
    res.name = name
    res.mobile_number = mobile_number
    res.gender = gender
    res.age = age
    res.city_id = city_id
    session.commit()


# delete customer
def delete_customer(id):
    res = session.query(Customers).filter(Customers.id == id).one()
    session.delete(res)
    session.commit()

# select customer by key and value
def select_customer(key, value):
    res = session.query(Customers).filter(getattr(Customers, key).contains(value)).all()
    for i in res :
        return i

# select customer by key and value
def select_customer_by_mob_num(mobile_number):
    try:
        res = session.query(Customers).filter(Customers.mobile_number == mobile_number).one()
        return res
    except NoResultFound:
        return False

def select_all_customers ():
    return session.query(Customers).all()