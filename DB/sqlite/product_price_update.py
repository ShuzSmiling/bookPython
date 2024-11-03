import sqlite3

def main():
    conn = sqlite3.connect('./files/chocolate.db')
    cur = conn.cursor()
    
    pid = int(input('Введите id товара: '))

    cur.execute('''
                    SELECT Description, RetailPrice
                    FROM Products
                    WHERE ProductID == ?
                ''', (pid,))
                
    results = cur.fetchone()

    if results != None:
        print(f'Текущая цена для {results[0]}: '
              f'${results[1]:.2f}')
        
        new_price = float(input('Введите новую цену: '))
        
        cur.execute('''
                    UPDATE Products
                    SET RetailPrice = ?
                    WHERE ProductID = ?
                    ''', (new_price, pid))
        
        conn.commit()
        print('Цена была изменена')
    
    else:
        print(f'ID изделия {pid} Не найдено')
        
    conn.close()
    

if __name__ == '__main__':
    main()