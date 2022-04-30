import sqlite3
import base64

def todo_console_app():

    conn = sqlite3.connect('test.db')
    create_sqlite_db(conn)

    user = None

    user = login_form(conn, user)

    while True:
        print("""
        1. Create a new todo
        2. Delete a todo by id
        3. Show all my todo
        4. Log out
        """)
        choice = input("Enter an option: ")
        if choice == "1":
            create_todo(conn, input("Title: "), user[0])
        elif choice == "2":
            print(get_todo_by_owner(conn, user[0]))
            delete_todo(conn, input("Id: "), user[0])
        elif choice == "3":
            print(get_todo_by_owner(conn, user[0]))
        elif choice == "4":
            user = None
            user = login_form(conn, user)
            if user is None:
                break
        else:
            print("Wrong option")

    conn.close()

def login_form(conn, user):
    while user is None:
        print("""
        1. Login
        2. Sign Up
        3. Exit""")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = login(conn, username, password)
            if user is not None:
                print("Login successful!")
            else:
                print("Login failed!")
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            signup(conn, username, password)
        elif choice == "3":
            break
    return user

def delete_todo(conn, id, owner):
    c = conn.cursor()
    todo = c.execute("SELECT owner FROM todo WHERE id=?", (id,)).fetchone()
    if todo[0] == owner:
        c.execute("DELETE FROM todo WHERE id=?", (id,))
        conn.commit()
    else:
        print("Error!!! Wrong id")

def create_todo(conn, title, owner):
    c = conn.cursor()
    c.execute("INSERT INTO todo VALUES (NULL, ?, ?)", (title, owner))
    conn.commit()

def login(conn, username, password):
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, encrypt_base64(password)))
    return c.fetchone()

def signup(conn, username, password):
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (NULL, ?, ?)", (username, encrypt_base64(password)))
    conn.commit()

def encrypt_base64(data):
    return base64.b64encode(data.encode("utf-8"))

def create_sqlite_db(conn):
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
    )
    """)
    c.execute("""
    CREATE TABLE IF NOT EXISTS todo (
    id INTEGER PRIMARY KEY,
    title TEXT,
    owner INTEGER,
    foreign key (owner) references users(id)
    )
    """)
    conn.commit()

def get_todo_by_owner(conn, owner):
    c = conn.cursor()
    c.execute("SELECT * FROM todo WHERE owner=?", (owner,))
    return c.fetchall()

if __name__ == '__main__':
    todo_console_app()