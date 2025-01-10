import sqlite3
from datetime import datetime
connection = sqlite3.connect("data.db")
sql = connection.cursor()

sql.execute("CREATE TABLE IF NOT EXISTS users "
            "(user_id INTEGER, name TEXT, "
            "phone_number TEXT, reg_date DATETIME);")
sql.execute("CREATE TABLE IF NOT EXISTS products "
            "(pr_id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "pr_name TEXT, pr_price REAL, pr_desc TEXT,"
            "pr_photo TEXT, pr_quantity INTEGER,"
            "reg_date DATETIME);")
sql.execute("CREATE TABLE IF NOT EXISTS cart "
            "(user_id INTEGER, pr_id INTEGER, "
            "pr_name TEXT, pr_count INTEGER, "
            "total_price REAL);")
connection.commit()
#TODO дз получение айди всех юзеров бота
def get_all_id():
    pass
def add_user(name, phone_number, user_id):
    connection = sqlite3.connect("data.db")
    sql = connection.cursor()
    sql.execute(f"INSERT INTO users (user_id, name, phone_number, reg_date) "
                f"VALUES (?, ?, ?, ?);", (user_id, name, phone_number, datetime.now()))
    connection.commit()

connection.commit()

def check_user(user_id):
    connection = sqlite3.connect("data.db")
    sql = connection.cursor()
    checker = sql.execute("SELECT * FROM users WHERE user_id=?;", (user_id ,)).fetchone()
    if checker:
        return True
    elif not checker:
        return False

def get_all_users():
    connection = sqlite3.connect("data.db")
    sql = connection.cursor()
    all_users = sql.execute("SELECT * FROM users;").fetchall()
    return all_users

def add_product(pr_name, pr_price, pr_desc, pr_quantity, pr_photo):
    connection = sqlite3.connect("data.db")
    sql = connection.cursor()
    sql.execute("INSERT INTO products (pr_name, pr_price, pr_desc, "
                "pr_quantity, pr_photo, reg_date) "
                "VALUES (?, ?, ?, ?, ?, ?);", (pr_name, pr_price, pr_desc,
                                              pr_quantity, pr_photo, datetime.now()))
    connection.commit()
def get_all_products():
    connection = sqlite3.connect("data.db")
    sql = connection.cursor()
    all_product = sql.execute("SELECT * FROM products;").fetchall()
    return all_product
def delete_exact_product(pr_id):
    connection = sqlite3.connect("data.db")
    sql = connection.cursor()
    sql.execute("DELETE FROM products WHERE pr_id = ?;", (pr_id, ))


kfc_menu = {' крыльев': 50,
    'бургер': 30,
    'картошка фри': 100}
def update_kfc_product_quantity(product_name, amount):
    if product_name in kfc_menu:
        kfc_menu[product_name] += amount
        if kfc_menu[product_name] < 0:
            kfc_menu[product_name] = 0
        print(f"Количество '{product_name}' обновлено: {kfc_menu[product_name]}")
    else:
        print(f"Продукт '{product_name}' не найден в меню.")

update_kfc_product_quantity('бургер', 12)
update_kfc_product_quantity('картошка фри', 20)
update_kfc_product_quantity('крылья', 10)

print(kfc_menu)

#TODO дз функция изменения количества определенного продукта
def change_quantity(something):
        pass

def delete_all_products():
    connection = sqlite3.connect("data.db")
    sql = connection.cursor()
    sql.execute("DELETE FROM products;")
    connection.commit()

def get_pr_id_name():
    connection = sqlite3.connect("data.db")
    sql = connection.cursor()
    # берем для кнопок продуктов нужную информацию
    all_product = sql.execute("SELECT pr_id, pr_name, pr_quantity "
                              "FROM products;").fetchall()
    # фильтрация продуктов, оставляем те, что в количестве больше 0
    #[(pr1_id, pr1_name, pr1_quantity), (pr2_id, pr2_name, pr2_quantity), ...]
    actual_products = [[product[0], product[1]] for product
                       in all_product if product[2] > 0]
    return actual_products
# работа с корзиной
def add_to_cart(user_id, pr_id, pr_name, pr_price, pr_quantity):
    connection = sqlite3.connect("data.db")
    sql = connection.cursor()
    total_price = pr_price * pr_quantity
    sql.execute("INSERT INTO cart (user_id, pr_id, pr_name, pr_count, "
                "total_price) VALUES (?, ? ,? ,?, ?);", (user_id, pr_id,
                                                         pr_name, pr_quantity,
                                                         total_price))
    connection.commit()
def delete_user_cart(user_id):
    connection = sqlite3.connect("data.db")
    sql = connection.cursor()
    sql.execute("DELETE FROM cart WHERE user_id=?;", (user_id, ))
    connection.commit()
#TODO дз получение информации о корзине юзера
# формат информации (название продуктов, количество, общая цена за это количество)

cart = {'бургер': (2), 'картошка фри': (1), 'напиток': (3)}

def get_cart_info(cart):
    return [(item, qty * price) for item, (qty, price) in cart.items()]

info = get_cart_info(cart)
print(info)

def get_user_cart(something):
    pass

 def delete_exact_product_from_cart(user_id,pr_id):
     connection = sqlite3.connect("data.db")









