# Эта программа добавляет записи о запасах кофе
# в файл coffee.txt

def main():
    # Создать переменную для управления циклом
    another = 'да'
    
    # Открыть файл coffee.txt в режиме дозаписи
    coffee_file = open('coffee.txt', 'a')
    
    # Добавить запись в файл
    while another.lower() == 'да':
        # получить данные с записью о кофе
        print('Введите следующие данные о кофе')
        descr = input('Описание: ')
        qty = int(input('Кол-во (в фунтах): '))
        
        # Добавить данные в файл
        coffee_file.write(f'{descr}\n')
        coffee_file.write(f'{qty}\n')
        
        # Определеить, желает ли пользователь добавить
        # в файл еще одну запись
        print('Желаете добавить еще одну запись?')
        another = input('Да/Нет: ')
        
    coffee_file.close()
    print('Данные добавлены в coffee.txt')
    
    
if __name__ == '__main__':
    main()