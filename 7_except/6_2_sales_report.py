# Эта программа показывает итоговый объем
# продаж из файла sales_data.txt

def main():
    # Инициализировать накопитель
    total = 0.0
    filename = input('Введите название файла: ')
    
    try:
        # Открыть файл
        infile = open(filename, 'r')
        
        # Прочитать значения из файла 
        # и накопить в переменной
        for line in infile:
            total += float(line)

        # Закрыть файл
        infile.close()
        
        # Напечатать итог
        print(f'{total:,.2f}')
        
    except IOError:
        print('Произошла ошибка при попытке прочитать файл')
    
    except ValueError:
        print('В файле найдены нечисловые значения')
        
    except:
        print('Произошла ошибка')
        

if __name__ == '__main__':
    main()