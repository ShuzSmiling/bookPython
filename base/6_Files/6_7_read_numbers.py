# Эта программа демонстрирует, как прочитанные из файла
# числа конвертируются из строкового представления
# перед тем, как они используются в мат. операции

def main():
    # Открыть файл для чтения
    infile = open('./files/numbers.txt', 'r')
    
    # Прочитать три числа из файла
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())
    
    # Закрыть файл
    infile.close()
    
    # сложить три числа 
    total = num1 + num2 + num3
    
    # показать числа и их сумму
    print(f'Числа: {num1}, {num2}, {num3}')
    print(f'Их сумма: {total}')
    

if __name__ == '__main__':
    main()