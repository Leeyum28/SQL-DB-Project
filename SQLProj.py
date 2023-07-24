import sqlite3



def create_table():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

def insert_table(item, quantity, price):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    for item in cursor.fetchall():
        counter = 1
        itemname = item[0]
        list_of_items = []
        list_of_items += itemname
        complete_list = ''.join(list_of_items)
        if complete_list[0] != complete_list[1]:
            cursor.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
    connection.commit()
    connection.close()

def delete_data(item):
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM store WHERE item=?",(item,))
    connection.commit()
    connection.close()

#delete_data('HENNESSEY')
insert_table("PROPER TWELVE", 3, 38.99)

def view_table():
    connection = sqlite3.connect("lite.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    return rows

#print(view_table())
