import sqlite3

MIN_CHOICE = 1
MAX_CHOICE = 5
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
EXIT = 5


def display_menu():
    print('\n----- Меню ведения учета инструментов -----')
    print('1. создать новую позицию')
    print('2. Прочитать позицию')
    print('3. Обновить позицию')
    print('4. удалить позицию')
    print('5. Выйти из программы')

    
def get_menu_choice():
    choice = int(input('Введите ваш вариант: '))

    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f'Допустимые варианты в диапазоне от {MIN_CHOICE} до {MAX_CHOICE}')
        choice = int(input('Введите ваш вариант: '))

    return choice


def create():
    print('создать новую позицию')
    name = input('Название позиции: ')
    price = input('Цена: ')
    insert_row(name, price)
    

def read():
    name = input('введите название искомой позиции: ')
    num_found = display_item(name)
    print(f'{num_found} строк(а) найдено')


def update():
    read()
    
    selected_id = int(input('Выберите ID Обновляемой позиции: '))
    name = input('Введите новое название позиции: ')
    price = input('Введите новую цену: ')

    num_updated = update_row(selected_id, name, price)
    print(f'{num_updated} строк(а) обновлено')
    

def delete():
    read()
    
    selected_id = int(input('Выберите ID удаляемой позиции: '))

    sure = input('Вы уверены, что хотите удалить эту позицию? (yes/no): ')
    
    if sure.lower() == 'yes':
        num_deleted = delete_row(selected_id)
        print(f'{num_deleted} строк(а) удалено')
        

def insert_row(name, price):
    conn = None
    
    try:
        conn = sqlite3.connect('./files/inventory.db')
        cur = conn.cursor()
        cur.execute('''
                        INSERT INTO Inventory (ItemName, Price)
                        VALUES (?, ?)
                    ''', (name, price))
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()
            
            
def display_item(name):
    conn = None
    result = []
    
    try: 
        conn = sqlite3.connect('./files/inventory.db')
        cur = conn.cursor()
        cur.execute('''
                    SELECT * 
                    FROM Inventory
                    WHERE ItemName == ?
                    ''', (name, ))
        result = cur.fetchall()
        
        for row in result:
            print(f'{row[0]:<3} Название: {row[1]:<15}'
                  f'Цена: {row[2]:<6}')
    except sqlite3.Error as err:
        print('Ошибка БД', err)
    finally:
        if conn != None:
            conn.close()
            return len(result)


def update_row(id, name, price):
    conn = None
    
    try:
        conn = sqlite3.connect('./files/inventory.db')
        cur = conn.cursor()
        cur.execute('''
                    UPDATE Inventory
                    SET ItemName = ?, 
                        Price = ?
                    WHERE ItemID == ?
                    ''', (name, price, id))
        conn.commit()
        num_updated = cur.rowcount
    except sqlite3.Error as err:
        print('Ошибка БД', err)
    finally:
        if conn != None:
            conn.close()
            
        return num_updated
    

def delete_row(id):
    conn = None
    
    try:
        conn = sqlite3.connect('./files/inventory.db')
        cur = conn.cursor()
        cur.execute('''
                        DELETE Inventory
                        WHERE ItemID == ?
                    ''', (id, ))
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.Error as err:
        print('Ошибка БД', err)
    finally:
        if conn != None:
            conn.close()
        return num_deleted


def main():
    choice = 0
    while choice != EXIT:
        display_menu()

        choice = get_menu_choice()

        if choice == CREATE:
            create()
        elif choice == READ:
            read()
        elif choice == UPDATE:
            update()
        elif choice == DELETE:
            delete()
            
            
if __name__ == '__main__':
    main()