import sqlite3
import threading

# Function to create tables
def create_tables():
    # Users table
    users_conn = sqlite3.connect('users.db', check_same_thread=False)
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
    products_conn = sqlite3.connect('products.db', check_same_thread=False)
    products_cursor = products_conn.cursor()
    products_cursor.execute("DROP TABLE IF EXISTS Products")
    products_cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL UNIQUE,
                                price REAL NOT NULL
                            )''')
    products_conn.commit()
    products_conn.close()

    # Orders table
    orders_conn = sqlite3.connect('orders.db', check_same_thread=False)
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

# Function to insert users
def insert_users():
    users_data = [
        (1, 'Alice', 'alice@example.com'),
        (2, 'Bob', 'bob@example.com'),
        (3, 'Charlie', 'charlie@example.com'),
        (4, 'David', 'david@example.com'),
        (5, 'Eve', 'eve@example.com'),
        (6, 'Frank', 'frank@example.com'),
        (7, 'Grace', 'grace@example.com'),
        (8, 'Alice', 'alice@example.com'),  # Duplicate name
        (9, 'Henry', 'henry@example.com'),
        (10, '', 'jane@example.com'),  # Missing name
    ]
    users_conn = sqlite3.connect('users.db', check_same_thread=False)
    users_cursor = users_conn.cursor()
    for user in users_data:
        try:
            if not user[1] or not user[2]:
                raise ValueError("Name and email cannot be empty")
            existing_user = users_cursor.execute("SELECT id FROM Users WHERE name = ?", (user[1],)).fetchone()
            if existing_user:
                raise ValueError("Name must be unique")
            users_cursor.execute("INSERT INTO Users (id, name, email) VALUES (?, ?, ?)", user)
        except Exception as e:
            print(f"Failed to insert user {user}: {e}")
    users_conn.commit()
    users_conn.close()

# Function to insert products
def insert_products():
    products_data = [
        (1, 'Laptop', 1000.00),
        (2, 'Smartphone', 700.00),
        (3, 'Headphones', 150.00),
        (4, 'Monitor', 300.00),
        (5, 'Keyboard', 50.00),
        (6, 'Mouse', 30.00),
        (7, 'Laptop', 1000.00),  # Duplicate name
        (8, 'Smartwatch', 250.00),
        (9, 'Gaming Chair', 500.00),
        (10, 'Earbuds', -50.00),  # Negative price
    ]
    products_conn = sqlite3.connect('products.db', check_same_thread=False)
    products_cursor = products_conn.cursor()
    for product in products_data:
        try:
            if product[2] <= 0:
                raise ValueError("Price must be greater than zero")
            existing_product = products_cursor.execute("SELECT id FROM Products WHERE name = ?", (product[1],)).fetchone()
            if existing_product:
                # raise ValueError("Product name must be unique")
                print(f"Failed to insert product {product} :Product name must be unique")
                product = (product[0], '', product[2])  # Replace name with an empty string
            products_cursor.execute("INSERT INTO Products (id, name, price) VALUES (?, ?, ?)", product)
        except Exception as e:
            print(f"Failed to insert product {product}: {e}")
    products_conn.commit()
    products_conn.close()

# Function to insert orders
def insert_orders():
    orders_data = [
        (1, 1, 1, 2),
        (2, 2, 2, 1),
        (3, 3, 3, 5),
        (4, 4, 4, 1),
        (5, 5, 5, 3),
        (6, 6, 6, 4),
        (7, 7, 7, 2),
        (8, 8, 8, 0),  # Invalid quantity
        (9, 9, 1, -1),  # Negative quantity
        (10, 10, 11, 2),  # Non-existent product_id
    ]
    orders_conn = sqlite3.connect('orders.db', check_same_thread=False)
    orders_cursor = orders_conn.cursor()
    products_conn = sqlite3.connect('products.db', check_same_thread=False)
    products_cursor = products_conn.cursor()

    for order in orders_data:
        try:
            if order[3] <= 0:
                raise ValueError("Quantity must be greater than zero")
            product_exists = products_cursor.execute("SELECT id FROM Products WHERE id = ?", (order[2],)).fetchone()
            if not product_exists:
                raise ValueError("Product ID must exist in the Products table")
            orders_cursor.execute("INSERT INTO Orders (id, user_id, product_id, quantity) VALUES (?, ?, ?, ?)", order)
        except Exception as e:
            print(f"Failed to insert order {order}: {e}")

    orders_conn.commit()
    orders_conn.close()
    products_conn.close()

# Main function
def main():
    create_tables()

    threads = []
    threads.append(threading.Thread(target=insert_users))
    threads.append(threading.Thread(target=insert_products))

    # Run user and product insertions concurrently
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Insert orders sequentially to validate product existence
    insert_orders()

    print("Data insertion completed.")

if __name__ == "__main__":
    main()
