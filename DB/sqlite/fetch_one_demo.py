import sqlite3

def main():
    conn = sqlite3.connect('./files/chocolate.db')
    cur = conn.cursor()
    
    cur.execute('SELECT Description, RetailPrice FROM Products')

    row = cur.fetchone()
    
    while row != None:
        print(f'{row[0]:35} {row[1]:5}')
        
        row = cur.fetchone()

    
    conn.close()
    
    
if __name__ == '__main__':
    main()