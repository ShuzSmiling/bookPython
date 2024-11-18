# Эта программа показывает содержимое
# файла

def main():
    # Получить имя файла
    filename = input('Введите имя файла: ')

    try:
        # Открыть файл
        infile = open(filename, 'r')
        
        # Прочитать содержимое файла
        content = infile.read()
        
        # Показать содержимое файла
        print(content)
        
        # Закрыть файл
        infile.close()
    
    except IOError:
        print('Произошла ошибка при попытке прочитать')
        print(f'файл {filename}')


if __name__ == '__main__':
    main()