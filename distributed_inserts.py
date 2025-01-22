import sqlite3
import threading

# def create_tables():
#     # Users table
#     users_conn = sqlite3.connect('users.db')
#     users_cursor = users_conn.cursor()
#     users_cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
#                             id INTEGER PRIMARY KEY,
#                             name TEXT NOT NULL,
#                             email TEXT NOT NULL
#                         )''')
#     users_conn.commit()
#     users_conn.close()

#     # Products table
#     products_conn = sqlite3.connect('products.db')
#     products_cursor = products_conn.cursor()
#     products_cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
#                                 id INTEGER PRIMARY KEY,
#                                 name TEXT NOT NULL,
#                                 price REAL NOT NULL
#                             )''')
#     products_conn.commit()
#     products_conn.close()

#     # Orders table
#     orders_conn = sqlite3.connect('orders.db')
#     orders_cursor = orders_conn.cursor()
#     orders_cursor.execute('''CREATE TABLE IF NOT EXISTS Orders (
#                               id INTEGER PRIMARY KEY,
#                               user_id INTEGER NOT NULL,
#                               product_id INTEGER NOT NULL,
#                               quantity INTEGER NOT NULL
#                           )''')
#     orders_conn.commit()
#     orders_conn.close()

def create_tables():
    # Users table
    users_conn = sqlite3.connect('users.db')
    users_cursor = users_conn.cursor()
    users_cursor.execute("DROP TABLE IF EXISTS Users")
    users_cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            email TEXT NOT NULL
                        )''')
    users_conn.commit()
    users_conn.close()

    # Products table
    products_conn = sqlite3.connect('products.db')
    products_cursor = products_conn.cursor()
    products_cursor.execute("DROP TABLE IF EXISTS Products")
    products_cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                price REAL NOT NULL
                            )''')
    products_conn.commit()
    products_conn.close()

    # Orders table
    orders_conn = sqlite3.connect('orders.db')
    orders_cursor = orders_conn.cursor()
    orders_cursor.execute("DROP TABLE IF EXISTS Orders")
    orders_cursor.execute('''CREATE TABLE IF NOT EXISTS Orders (
                              id INTEGER PRIMARY KEY,
                              user_id INTEGER NOT NULL,
                              product_id INTEGER NOT NULL,
                              quantity INTEGER NOT NULL
                          )''')
    orders_conn.commit()
    orders_conn.close()


def insert_users():
    users_data = [
        (1, 'Alice', 'alice@example.com'),
        (2, 'Bob', 'bob@example.com'),
        (3, 'Charlie', 'charlie@example.com'),
        (4, 'David', 'david@example.com'),
        (5, 'Eve', 'eve@example.com'),
        (6, 'Frank', 'frank@example.com'),
        (7, 'Grace', 'grace@example.com'),
        (8, 'Alice', 'alice@example.com'),
        (9, 'Henry', 'henry@example.com'),
        (10, '', 'jane@example.com'),
    ]
    users_conn = sqlite3.connect('users.db')
    users_cursor = users_conn.cursor()
    for user in users_data:
        try:
            if not user[1] or not user[2]:
                raise ValueError("Name and email cannot be empty")
            users_cursor.execute("INSERT INTO Users (id, name, email) VALUES (?, ?, ?)", user)
        except Exception as e:
            print(f"Failed to insert user {user}: {e}")
    users_conn.commit()
    users_conn.close()

def insert_products():
    products_data = [
        (1, 'Laptop', 1000.00),
        (2, 'Smartphone', 700.00),
        (3, 'Headphones', 150.00),
        (4, 'Monitor', 300.00),
        (5, 'Keyboard', 50.00),
        (6, 'Mouse', 30.00),
        (7, 'Laptop', 1000.00),
        (8, 'Smartwatch', 250.00),
        (9, 'Gaming Chair', 500.00),
        (10, 'Earbuds', -50.00),
    ]
    products_conn = sqlite3.connect('products.db')
    products_cursor = products_conn.cursor()
    for product in products_data:
        try:
            if product[2] <= 0:
                raise ValueError("Price must be greater than zero")
            products_cursor.execute("INSERT INTO Products (id, name, price) VALUES (?, ?, ?)", product)
        except Exception as e:
            print(f"Failed to insert product {product}: {e}")
    products_conn.commit()
    products_conn.close()

def insert_orders():
    orders_data = [
        (1, 1, 1, 2),
        (2, 2, 2, 1),
        (3, 3, 3, 5),
        (4, 4, 4, 1),
        (5, 5, 5, 3),
        (6, 6, 6, 4),
        (7, 7, 7, 2),
        (8, 8, 8, 0),
        (9, 9, 1, -1),
        (10, 10, 11, 2),
    ]
    orders_conn = sqlite3.connect('orders.db')
    orders_cursor = orders_conn.cursor()
    for order in orders_data:
        try:
            if order[3] <= 0:
                raise ValueError("Quantity must be greater than zero")
            orders_cursor.execute("INSERT INTO Orders (id, user_id, product_id, quantity) VALUES (?, ?, ?, ?)", order)
        except Exception as e:
            print(f"Failed to insert order {order}: {e}")
    orders_conn.commit()
    orders_conn.close()

def main():
    create_tables()

    threads = []
    threads.append(threading.Thread(target=insert_users))
    threads.append(threading.Thread(target=insert_products))
    threads.append(threading.Thread(target=insert_orders))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Data insertion completed.")

if __name__ == "__main__":
    main()
