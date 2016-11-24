import os
import pickle

from models import usersModel


def validLogin(username, password):
	if password == '':
		return False
	elif usersModel.select_user_by_username(username).password == password:
		logUser = usersModel.select_user_by_username(username)
		setLoginDataPKL(logUser.name, logUser.username, logUser.role)
		return logUser
	else:
		return False


def changePassword(username, old_password, password):
	loggedUser = usersModel.select_user_by_username(username)
	if old_password == loggedUser.password:
		if password == loggedUser.password:
			return False
		else:
			usersModel.update_user(loggedUser.username, password, loggedUser.role)
		return loggedUser
	else:
		return False


def setLoginDataPKL(name, username, role):
	myObj = {'name': name,
			 'username': username,
			 'role': role}
	f = open('loginUserData.pkl', 'wb')
	pickle.dump(myObj, f)
	f.close()


def getLoginDataPKL():
	# PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
	f = open("loginUserData.pkl", "rb")
	myNewObject = pickle.load(f)
	f.close()
	return myNewObject


def deleteLoginDataPKL():
	# PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
	os.remove("loginUserData.pkl")
