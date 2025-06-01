import sqlite3

db = sqlite3.connect('website/dbs/users.db')

curs = db.cursor()

data = ['mohamed' , 'thisisforme']

curs.execute('CREATE TABLE users (username TEXT, password TEXT)')

db.commit()

db.close()