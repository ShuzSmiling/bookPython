# Эта программа считывает содержимое файла в список

def main():
    # Открыть файл для чтения
    infile = open('../files/cities3.txt', 'r')
    
    # Прочитать содержимое файла
    cities = infile.readlines()

    # Закрыть файл
    infile.close()
    
    # Удалить из каждого элемента \n
    index = 0
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1
        
    # Напечатать содержимое списка
    print(cities)
    

# Вызвать главную функцию
if __name__ == '__main__':
    main()