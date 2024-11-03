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
        sure = input(f'Вы уверены, что хотите удалить '
                    f'{results[0]}? (yes/no): ') 
       
        if sure.lower() == 'yes':
            cur.execute('''
                       DELETE FROM Products
                       WHERE ProductID = ?
                       ''', (pid, ))
           
            conn.commit()
            print('Изделие было удалено')
    
        else:
            print(f'ID изделия {pid} Не найдено')
        
    conn.close()
    

if __name__ == '__main__':
    main()