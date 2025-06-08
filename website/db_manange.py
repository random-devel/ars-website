import sqlite3
import secrets
from datetime import datetime

conn = sqlite3.connect('dbs/users_data.db')
cursor = conn.cursor()

user_db = sqlite3.connect('dbs/users.db')
user_cursor = user_db.cursor()

user_cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
""")

user_cursor.execute("""CREATE TABLE IF NOT EXISTS users_roles (
    username TEXT PRIMARY KEY,
    role TEXT
)
""")

user_db.commit()
user_db.close()




#Create sessions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sessions (
    session_id TEXT PRIMARY KEY,
    username TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (username) REFERENCES users_data (username)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users_data (
    username TEXT PRIMARY KEY,
    email TEXT,
    phone TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    zip TEXT
)
""")
conn.commit()
conn.close()

def create_session(username: str) -> str:
    """Create a new session for a user"""
    session_id = secrets.token_urlsafe(32)
    with sqlite3.connect('dbs/users_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sessions (session_id, username) VALUES (?, ?)",
                      (session_id, username))
        conn.commit()
    return session_id

def get_session(session_id: str) -> dict:
    """Get user info from session"""
    with sqlite3.connect('dbs/users_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.username, s.created_at
            FROM sessions s
            WHERE s.session_id = ?
        """, (session_id,))
        result = cursor.fetchone()
        if result:
            return {
                "username": result[0],
                "created_at": result[1]
            }
    return None

def delete_session(session_id: str) -> bool:
    """Delete a session (for logout)"""
    with sqlite3.connect('dbs/users_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM sessions WHERE session_id = ?", (session_id,))
        conn.commit()
    return True

def db_auth(username : str, password : str):
    with sqlite3.connect('dbs/users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
    return user

def db_create_user(username : str, password : str):
    if db_check_user(username):
        return False
    else:
        with sqlite3.connect('dbs/users.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            make_user_data(username)
        return True

def db_check_user(username : str):
    with sqlite3.connect('dbs/users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
    return user

def make_user_data(username : str):
    with sqlite3.connect('dbs/users_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users_data (username, email, phone, address, city, state, zip) VALUES (?, ?, ?, ?, ?, ?, ?)", (username,'null','null','null','null','null','null'))
        conn.commit()
    return True

def fetch_user_data(username : str):
    with sqlite3.connect('dbs/users_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users_data WHERE username = ?", (username,))
        user = cursor.fetchone()
    return user

def update_user_data(username : str, data : dict):
    with sqlite3.connect('dbs/users_data.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users_data SET email = ?, phone = ?, address = ?, city = ?, state = ?, zip = ? WHERE username = ?", (data['email'], data['phone'], data['address'], data['city'], data['state'], data['zip'], username))
        conn.commit()
    return True