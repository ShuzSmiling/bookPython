# Эта программа показывает итоговую сумму
# продаж из файла sales_data.txt

def main():
    # инициализировать накопитель
    total = 0.0
    filename = input('Введите название файла: ')
    
    try:
        # Открыть файл 
        infile = open(filename, 'r')
        
        # прочитать значение из файла
        # и просумировать
        for line in infile:
            total += float(line)
        
        # Закрыть файл
        infile.close()
        
        # Напечатать итог
        print(f'{total:,.2f}')
    
    except Exception as err:
        print(err)
        

if __name__ == '__main__':
    main()