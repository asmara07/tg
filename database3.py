import sqlite3
def init_db():
    connection = sqlite3.connect('bot.db')
    sql= connection.cursor()
    sql.execute("CREATE TABLE IF NOT EXISTS users" 
               "(id INTEGER PRIMARY KEY,username TEXT",
              "first_name TEXT phone TEXT,language TEXT) ")
    sql.execute("CREATE TABLE IF NOT EXISTS cart" 
            "(user_id INTEGER, product TEXT,quantity INTEGER",
                "PRIMARY KEY (user_id, product))")

    sql.execute("CREATE TABLE IF NOT EXISTS reviews" 
            "(user_id INTEGER,review TEXT)")

    connection.commit()
    connection.close()


def register_user(user_id, username, first_name, phone, language):
    connection = sqlite3.connect('bot.db')
    sql = connection.cursor()
    sql.execute(f"INSERT OR REPLACE INTO users (id, username, first_name, phone, language)"
       f"VALUES (?, ?, ?, ?, ?);",(user_id, username, first_name, phone, language))
    connection.commit()
    connection.close()

def add_review(user_id, review):
    connection = sqlite3.connect('bot.db')
    sql = connection.cursor()
    sql.execute('INSERT INTO reviews (user_id, review) VALUES (?, ?)', (user_id, review))
    connection.commit()
    connection.close()


def add_to_cart(user_id, product, quantity):
    connection = sqlite3.connect('bot.db')
    sql = connection.cursor()
    sql.execute('INSERT INTO cart (user_id, product, quantity), VALUES (?, ?, ?)',
       " ON CONFLICT(user_id, product) DO UPDATE SET quantity = quantity + ?, (user_id, product, quantity, quantity))")
    connection.commit()
    connection.close()

def get_cart(user_id):
    connection = sqlite3.connect('bot.db')
    sql= connection.cursor()
    sql.execute('SELECT product, quantity FROM cart WHERE user_id = ?', (user_id,))
    items = sql.fetchall()
    connection.close()
    return items