from sqlalchemy.orm import sessionmaker

from models.dbUtile import City, engine

# create a session
Session = sessionmaker(bind=engine)
session = Session()


# add new city
def add_city(name):
	new_city = City(name)
	session.add(new_city)
	session.commit()
	print(new_city)

def update_city(id, name):
	res = session.query(City).filter(City.id == id).one()
	print(res)
	res.name = name
	session.commit()

# delete city
def delete_city(id):
	res = session.query(City).filter(City.id == id).one()
	print(res)
	session.delete(res)
	session.commit()

def select_city_by_id(id):
	return session.query(City).filter(City.id == id).one()

def select_all_cities():
	res = session.query(City).all()
	# for c in res:
	#     return c
	return res