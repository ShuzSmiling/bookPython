import sqlite3

def main():
    conn = sqlite3.connect('./files/chocolate.db')
    cur = conn.cursor()
    
    cur.execute('SELECT Description, RetailPrice FROM Products WHERE RetailPrice > 10.00')

    results = cur.fetchall()
    
    for row in results:
        print(f'{row[0]:35} {row[1]:5}')
        
    conn.close()
    

if __name__ == '__main__':
    main()