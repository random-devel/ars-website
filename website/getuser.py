import sqlite3
from email_validator import validate_email, EmailNotValidError

def validate_gmail(email):
    v = validate_email(email, check_deliverability=False)
    if v.email.endswith("@gmail.com"):
        get_usr_bymail(email)
    else:
        get_usr_byname(email)


def get_usr_bymail(email):
     with sqlite3.connect('dbs/users') as DB:
        curs = DB.cursor()
        curs.execute('SELECT * FROM users WHERE email = ? ',(email,))
        data = curs.fetchone()
        if not data:
            return
        else :return data

def get_usr_byname(username):
    with sqlite3.connect('dbs/users') as DB:
        curs = DB.cursor()
        curs.execute('SELECT * FROM users WHERE username = ? ',(username,))
        data = curs.fetchone()
        if not data:
            return
        else :return data


def get_usr_data():
    pass
