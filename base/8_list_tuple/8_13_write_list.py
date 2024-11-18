# Эта программа применяет метод writelines для сохранения
# списка строковых значений в файл

CITIES = ['Нью-Йорк', 'Бостон', 'Атланта', 'Даллас']


def main():
    # Открыть файл для записи
    outfile = open('../files/cities.txt', 'w')
    
    # Записать список в файл
    outfile.writelines(CITIES)
    
    # Закрыть файл
    outfile.close()


def main2():
    outfile = open('../files/cities2.txt', 'w')
    
    for item in CITIES:
        outfile.write(f'{item}\n') 
    
    outfile.close  


def main3():
    outfile = open('../files/cities3.txt', 'w')
    
    tmp_cities = [f'{item}\n' for item in CITIES]

    outfile.writelines(tmp_cities)
    outfile.close


if __name__ == '__main__':
    main()
    main2()
    main3()