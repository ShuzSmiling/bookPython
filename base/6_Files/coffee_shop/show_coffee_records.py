# Эта программа показывает записи
# из файла coffee.txt

def main():
    # Открыть файл coffee.txt
    coffee_file = open('coffee.txt', 'r')
    
    # прочить поле с описание первой записи
    descr = coffee_file.readline()
    
    # Просчитать остаток файла
    while descr:
        # прочить поле с кол-вом
        qty = float(coffee_file.readline())
        
        # Удалить \n из описания
        descr = descr.rstrip('\n')
        
        # показать запись
        print(f'Описание: {descr}')
        print(f'Кол-во: {qty}')
        
        # прочитать следующее описание
        descr = coffee_file.readline()
        
    # Закрыть файл
    coffee_file.close()
    
    
if __name__ == '__main__':
    main()