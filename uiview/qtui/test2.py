import sqlite3


# class Mainn():
def connectdb():
	try:
		con = sqlite3.connect('maindatabas.db')
		cur = con.cursor()
		cur.executescript("""DROP TABLE IF EXISTS Information;
                            CREATE TABLE Information (Id INT,Name TEXT, age INT)""")
		con.commit()
		cur.execute('SELECT * FROM Information')
		data = cur.fetchall()
		for row in data:
			print(row)
	except sqlite3.Error:
		if con:
			print("Error! Rolling back")
			con.rollback()
	finally:
		if con:
			con.close()


def insertdata(idx, name, age):
	con = sqlite3.connect('maindatabas.db')
	cur = con.cursor()
	cur.execute("INSERT INTO Information VALUES("+idx+", '"+name+"', '"+age+"')")


# con.commit()


connectdb()
insertdata(str(10), "test", str(20))


