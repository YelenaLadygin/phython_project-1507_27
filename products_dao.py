import sqlite3
from Products import *

conn = sqlite3.connect('Products.db')

def create_Products_table():
    conn.execute('''
        CREATE TABLE PRODUCTS
        (ID INT PRIMARY KEY NOT NULL, 
        NAME TEXT NOT NULL, PRICE REAL NOT NULL,
         QUANTITY INT)
        ''')

def insert_into_Products_table(e):
    conn.execute(f'''
        INSERT INTO PRODUCT 
        (ID,NAME,PRICE,QUANTITY)
         VALUES 
        ({e.id}, '{e.name}', {e.price},  {e.quantity})''')
    conn.commit()

    print("done")

def get_all_Products():
    result = conn.execute('SELECT * FROM PRODUCTS')
    emp_result = []
    for row in result:
        e = Products(row[0], row[1], row[2], row[3])
        emp_result.append(e)
    return emp_result

def get_Products_by_id(id):
    result = conn.execute(f'SELECT * FROM PRODUCTS WHERE id = {id}')
    for row in result:
        e = Products(row[0], row[1], row[2], row[3])
        return e
    return None

def update_Products(e, id):
    conn.execute(f'''
                 UPDATE PRODUCTS SET NAME = '{e.name}', PRICE = {e.price},  
                    QUANTITY = {e.quantity}   
                 WHERE ID = {id}''')
    conn.commit()

def delete_Products(id):
    # more generic more complex
    conn.execute(f'DELETE FROM PRODUCTS WHERE ID = {id}')
    conn.commit()

def drop_Products_table():
    conn.execute("DROP TABLE PRODUCTS;")
    conn.commit()


print('========== ID is 2 ===============')
e2 = get_Products_by_id(2)
print(e2)
print('========== ALL ===============')
emp_list = get_all_Products()
for emp in emp_list:
    print(emp)
