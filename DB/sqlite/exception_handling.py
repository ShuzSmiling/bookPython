import sqlite3


def add_item(item_id, name, price):
    conn = None
    
    try:
        conn = sqlite3.connect('./files/inventory.db')
        
        cur = conn.cursor()
        
        cur.execute('''
                        INSERT INTO Inventory (
                            ItemID,
                            ItemName,
                            Price
                        )
                        VALUES (
                            ?, 
                            ?,
                            ?)
                    ''', (item_id, name, price))

        conn.commit()
    
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn != None:
            conn.close()


def main():
    again = 'yes'
    
    while again.lower() == 'yes':
        item_id = int(input('ID Товара: '))
        item_name = input('Название товара: ')
        price = float(input('Цена: '))

        add_item(item_id, item_name, price)
        
        again = input('Добавить еще одну позицию? (yes/no):')


if __name__ == '__main__':
    main()

