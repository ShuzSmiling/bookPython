import sqlite3

def main():
    again = 'yes'
    
    conn = sqlite3.connect('./files/inventory.db')
    
    cur = conn.cursor()
    
    while again.lower() == 'yes':
        item_name = input('Название: ')
        price = float(input('Цена: '))

        cur.execute('''
                    INSERT INTO Inventory (ItemName, Price)
                    VALUES (?, ?)
                    ''', (item_name, price))
        
        again = input('Добавить еще одну позицию? (yes/no): ')
        
    conn.commit()
    
    conn.close()
    

if __name__ == '__main__':
    main()