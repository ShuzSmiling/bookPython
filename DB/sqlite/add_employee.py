import sqlite3

def main():
    conn = None
    
    try:
        conn = sqlite3.connect('employees.db')
        cur = conn.cursor()
        
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''
                        INSERT INTO Employees
                            (Name, Position, DepartamentID, LocationId)
                        VALUES
                            ('Анжела Тейлор', 'Аналитик', 4, 4)
                    ''')
        conn.commit()
        print('Сотрудник успешно добавлен')
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn != None:
            conn.close()
            

if __name__ == '__main__':
    main()