# Эта программа читаем содержимое файла
# friends.txt построчно

def main():
    # Открыть файл с именем friends.txt
    infile = open('./files/friends.txt')
    
    # прочитать три строки из файла
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    # Удалить \n из каждой строки
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')
    
    # Закрыть файл
    infile.close()
    
    print(line1)
    print(line2)
    print(line3)


if __name__ == '__main__':
    main()