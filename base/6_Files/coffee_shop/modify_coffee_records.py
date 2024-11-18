# Эта программа позволяет пользователю изменять кол-во
# в записи файла coffee.txt

import os

def main():
    # флаг
    found = False
    
    # получить искомое значение и кол-во
    search = input('Введите искомое описание: ')
    new_qty = int(input('Введите новое кол-во: '))

    # Открыть исходный файл
    coffee_file = open('coffee.txt', 'r')
    
    # Открыть временный файл
    temp_file = open('temp.txt', 'w')
    
    # Прочитать поле с описанием первой записи
    descr = coffee_file.readline()
    
    # прочитать остаток файла
    while descr:
        # Прочитать поле с кол-вом
        qty = float(coffee_file.readline())
        
        # Удалить \n из описания
        descr = descr.rstrip('\n')
        
        # Записать во временный файл либо эту запись,
        # либо новую запись, если эта запись
        # подлежит изменению
        if descr == search:
            # Записать во временный файл измененную запись
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{new_qty}\n')
            
            # Назначить флагу True
            found = True
            
        else:
            # Записать исходную запись во временный файл
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{qty}\n')
            
        descr = coffee_file.readline()
        
    coffee_file.close()
    temp_file.close()
    
    # Удалить ихсодный файл
    os.remove('coffee.txt')
    
    # Переименовать временный файл
    os.rename('temp.txt', 'coffee.txt')
    
    # Если искомое значение в файле не найдено
    if found:
        print('Файл обновлен')
    else:
        print('Это значение в файле не найдено')
        
        
if __name__ == '__main__':
    main()