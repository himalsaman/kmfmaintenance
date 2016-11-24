from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from models.dbUtile import User, engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()


# add new user function to users table
def add_user(name, username, password, created_at, role):
	new_user = User(name, username, password, created_at, role)
	session.add(new_user)
	session.commit()
	print(new_user)


# update or edit exists user in users table
def update_user(username, password, role):
	res = session.query(User).filter(User.username == username).one()
	print(res)
	res.password = password
	res.role = role
	session.commit()


# delete user from users table
def delete_user(username):
	res = session.query(User).filter(User.username == username).one()
	print(res)
	session.delete(res)
	session.commit()


# select user by username
def select_user_by_username(username):
	try:
		res = session.query(User).filter(User.username == username).one()
		return res
	except NoResultFound:
		return False


# select name and username of all users from users table in db
def select_all_users():
	res = session.query(User).all()
	for user in res:
		print(user.id, user.name, user.username, user.role)
