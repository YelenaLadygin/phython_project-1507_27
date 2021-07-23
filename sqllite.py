import sqlite3
from Products import *

def create_Products_table(conn):
    conn.execute('''
        CREATE TABLE Products
        (ID INT PRIMARY KEY NOT NULL, 
        NAME TEXT NOT NULL, PRICE REAL NOT NULL,
         QUANTITY INT)
        ''')

def insert_into_Products_table(conn, e):
    conn.execute(f'''
        INSERT INTO Products 
        (ID,NAME,PRICE,QUANTITY)
         VALUES 
        ({e.id}, '{e.name}', {e.price}, {e.quantity})''')
    conn.commit()

    print("done")

def get_all_Products(conn):
    result = conn.execute('SELECT * FROM Products')
    emp_result = []
    for row in result:
        e = Products(row[0], row[1], row[2], row[3])
        emp_result.append(e)
    return emp_result

def get_Products_by_id(conn, id):
    result = conn.execute(f'SELECT * FROM Products WHERE id = {id}')
    for row in result:
        e = Products(row[0], row[1], row[2], row[3])
        return e
    return None

def update_Products(conn, e, id):
    conn.execute(f'''
                 UPDATE Products SET NAME = '{e.name}', PRICE = {e.price},  
                    QUANTITY = {e.quantity}   
                 WHERE ID = {id}''')
    conn.commit()

def delete_Products(conn, id):
    # more generic more complex
    conn.execute(f'DELETE FROM Products WHERE ID = {id}')
    conn.commit()

def drop_Products_table(conn):
    conn.execute("DROP TABLE Products;")
    conn.commit()
