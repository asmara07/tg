import sqlite3

def init_db():
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()
    sql.execute(" CREATE TABLE IF NOT EXISTS users ( ' id INTEGER PRIMARY KEY AUTOINCREMENT',"
                " user_id INTEGER UNIQUE ,name TEXT, phone TEXT); " )

    connection.commit()
    connection.close()
def add_user(user_id, name, phone):
    connection = sqlite3.connect('users.db')
    sql = connection.cursor()
    sql.execute('INSERT OR IGNORE INTO users (user_id, name, phone) VALUES (?, ?, ?)', (user_id, name, phone))
    connection.commit()
    connection.close()
