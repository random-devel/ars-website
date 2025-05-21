import sqlite3

db = sqlite3.connect('dbs/product.db')

curs = db.cursor()

products = [[1,'scanner','90$'], [2,'hacktool','70$'], [3,'nmap','80$']]

curs.execute('select * from products where id = 2')

data = curs.fetchone()
print(data)
