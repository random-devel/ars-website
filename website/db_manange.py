import sqlite3

db = sqlite3.connect('dbs/users.db')

curs = db.cursor()

data = ['mohamed' , 'thisisforme']

curs.execute('CREATE TABLE users (username TEXT, email TEXT)')

db.commit()

db.close()