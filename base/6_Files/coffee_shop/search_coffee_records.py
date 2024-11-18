# Эта программа позволяет пользователю производить поиск
# в файле coffee.txt записей, которые соответствуют
# Описанию

def main():
    # Создаем флаг
    found = False
    
    # Получаем искомое значение
    search = input('Введите искомое значение: ')
    
    # Открыть файл
    coffee_file = open('coffee.txt', 'r')
    
    # Прочитать поле с описанием
    descr = coffee_file.readline()
    
    # прочитать остаток файла
    while descr:
        # прочитать поле с кол-вом
        qty = float(coffee_file.readline())
        
        # Удалить \n из описания
        descr = descr.rstrip('\n')
        
        # Определить соответствует-ли эта запись 
        # поисковому значению
        if descr == search:
            print(f'Описание: {descr}')
            print(f'Кол-во: {qty}')
            
            found = True
            
        # Прочитать следующее описание
        descr = coffee_file.readline()
        
    # Закрыть файл
    coffee_file.close()
    
    # Если поисковое значение в файле не найдено
    # показать сообщение
    if not found:
        print('Это значение в файле не найдено')
        
        
if __name__ == '__main__':
    main()