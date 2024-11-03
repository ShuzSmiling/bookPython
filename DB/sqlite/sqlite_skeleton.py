import sqlite3

def main():
    conn = sqlite3.connect('./files/contacts.db')
    cur = conn.cursor()
    
    # Here insert the code for performing operations with the database.
    table_1 = '''CREATE TABLE IF NOT EXISTS Inventory (
                                                    ItemID INTEGER PRIMARY KEY NOT NULL,
                                                    ItemName TEXT,
                                                    Price REAL
        )
    '''
    
    table_2 = '''CREATE TABLE IF NOT EXISTS Customers(
                                                    CustomerID INTEGER PRIMARY KEY NOT NULL,
                                                    Name TEXT,
                                                    Email TEXT   
    )
    '''
    
    cur.execute(table_1)
    cur.execute(table_2)
    
    cur.execute('DROP TABLE Customers')
    
    cur.execute('''INSERT INTO Inventory (ItemName, Price)
                   VALUES ("Молоток", 12.99),
                          ("Кусачки", 13.99) 
                ''')
    cur.execute('''INSERT INTO Inventory (ItemName, Price)
                   VALUES ("Плоскогубцы", 14.99)
                ''')
    
    cur.execute('''INSERT INTO Inventory (ItemName, Price)
                   VALUES ("Электродрель", NULL)
                ''')
    
    
    conn.commit()
    conn.close()
    

if __name__ == '__main__':
    main()