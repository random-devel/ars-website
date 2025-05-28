import sqlite3

db = sqlite3.connect('dbs/users.db')

curs = db.cursor()

data = ['mohamed' , 'thisisforme']

curs.execute('INSERT INTO users (username,password) VALUES (?,?)',data)

db.commit()

db.close()