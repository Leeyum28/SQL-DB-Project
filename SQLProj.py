import sqlite3

connection = sqlite3.connect("lite.db")
cursor = connection.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

def insert_table(item, quantity, price):
    cursor.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))

def delete_data():
    cursor.execute("DELETE FROM store WHERE item='Hennesy'")

delete_data()
insert_table("PROPER TWELVE", 8, 29.99)

def view_table():
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    return rows

print(view_table())
connection.close()