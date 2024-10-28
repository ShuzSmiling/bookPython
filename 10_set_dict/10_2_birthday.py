# This programm apply dict for
# name and birthday friends

# Global
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# main
def main():
    # create clear dict
    birthday = {}

    choice = 0
    
    while choice != QUIT:
        # get input num user
        choice = get_menu_choice()
        
        if choice == LOOK_UP:
            look_up(birthday)
        elif choice == ADD:
            add(birthday)
        elif choice == CHANGE:
            change(birthday)
        elif choice == DELETE:
            delete(birthday)


# func displays menu and
# get point to menu
def get_menu_choice():
    print()
    print('Друзья и их дни рождения')
    print('------------------------')
    print('1. Найти день рождения')
    print('2. Добавить новый день рождения')
    print('3. Изменить день рождения')
    print('4. Удалить день рождения')
    print('5. Выйти из программы')

    choice = int(input('Введите выбранный пункт: '))

    while QUIT < choice < LOOK_UP:
       choice = int(input('Введите выбранный пункт: '))

    return choice


# funct look_up search name in dict
def look_up(birthday):
    # get search name
    name = input('Введите имя: ')

    # search in dict
    print(birthday.get(name, 'не найдено'))


# func 'add' add new line in dict
def add(birthday):
    # get name and date birthday
    name = input('Введите имя: ')
    bday = input('Введите день рождения: ')
               
    if name not in birthday:
        birthday[name] = bday
    else:
        print('Эта запись уже существует')          
     
               
def change(birthday):
    name = input('Введите имя: ')    

    if name in birthday:
        bday = input('Введите новый день рождения: ')
        birthday[name] = bday
    else:
        print('Это имя не найдено')
                

def delete(birthday):
    name = input('Введите имя: ')

    if name in birthday:
        del birthday[name]
    else:
        print('Это имя не найдено')
 

if __name__ == '__main__':
    main()