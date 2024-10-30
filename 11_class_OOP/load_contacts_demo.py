from modules.contact import Contact

import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = './files/contacts.dat'


def load_contacts():
    
    try:
        
        input_file = open(FILENAME, 'rb')
        contact_dict = pickle.load(input_file)
        input_file.close()

    except IOError:
        contact_dict = {}
    
    return contact_dict


def get_menu_choice():
    print()
    print('Меню')
    print('--------------------------')
    print('1. Найти контакт')
    print('2. Добавить новый контакт')
    print('3. Изменить контакт')
    print('4. Удалить контакт')
    print('5. Выйти из программы')
    print()
    
    while True:
        
        try:
            choice = int(input('Введите выбранный пункт: '))
            
            if LOOK_UP <= choice <= QUIT:
                return choice
            else:
                print(f'Ошибка: введите значение от {LOOK_UP} до {QUIT}')
            
        except ValueError:
            print('Ошибка: неверно выбранный пункт')
         
         
def look_up(mycontacts):
    name = input('Введите имя: ')
    print(mycontacts.get(name, 'Это имя не найдено'))
    

def add(mycontacts):
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    email = input('Введите email: ')

    entry = Contact(name, phone, email)
    
    if not name in mycontacts:
        mycontacts[name] = entry
        print('Запись добавлена')
    else:
        print('Эта запись уже существует')
        

def change(mycontacts):
    name = input('Введите имя: ')
    
    if name in mycontacts:
        phone = input('Введите новый телефон: ')
        email = input('Введите новый email: ')
        
        entry = Contact(name, phone, email)
        
        mycontacts[name] = entry
        print('Информация обновлена')
    else:
        print('Это имя не найдено')


def delete(mycontacts):
    name = input('Введите имя: ')
    
    if name in mycontacts:
        del mycontacts[name]
        print('Запись удалена')
    else:
        print('Это имя не найдено')


def save_contacts(mycontacs):
    output_file = open(FILENAME, 'wb')
    pickle.dump(mycontacs, output_file)
    output_file.close()


def main():
    mycontacts = load_contacts()
    
    choice = 0
    
    while choice != QUIT:
        choice = get_menu_choice()
        
        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)
    
    save_contacts(mycontacts)
    

if __name__ == '__main__':
    main()