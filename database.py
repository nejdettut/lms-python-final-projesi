import sqlite3
def connect():
    conn = sqlite3.connect("data/lms.db")
    conn.row_factory = sqlite3.Row
    return conn
def create_tables():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS courses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT
    )
    """)
    conn.commit()
    conn.close()

    def register_user(username, password):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()
def login_user(username, password):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )
    user = cur.fetchone()
    conn.close()
    return user is not None

def add_course(title, description):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO courses (title, description) VALUES (?, ?)",
        (title, description)
    )
    conn.commit()
    conn.close()
def get_courses():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM courses")
    courses = cur.fetchall()
    conn.close()
    return courses