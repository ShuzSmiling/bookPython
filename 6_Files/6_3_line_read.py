# Эта программа построчно читает
# содержимое файла text.txt

def main():
    # Открыть файл
    infile = open('./files/text.txt', 'r')
    
    # Прочитать 3 строки
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    # Закрыть файл
    infile.close()
    
    # Напечатать данные, прочитанные
    # в оперативную память
    print(line1)
    print(line2)
    print(line3)
    

if __name__ == '__main__':
    main()