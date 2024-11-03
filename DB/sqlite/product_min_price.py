import sqlite3

def main():
    conn = sqlite3.connect('./files/chocolate.db')

    cur = conn.cursor()
    
    min_price = float(input('Введите минимальную цену: '))

    cur.execute('''
                    SELECT Description, RetailPrice
                    FROM Products
                    WHERE RetailPrice >= ?
                ''', (min_price, ))
    
    results = cur.fetchall()
    
    if len(results) > 0:
        print('Вот результаты:')
        print()
        print('Описание                             Цена')
        print('-----------------------------------------')

        for row in results:
            print(f'{row[0]:35} {row[1]:5}')
    else:
        print('Ни одно изделие не найдено')

    conn.close()
    
    
if __name__ == '__main__':
    main()