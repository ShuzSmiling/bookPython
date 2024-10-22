# Эта программа применяет цикл for для чтения
# всех значений из файла sales.txt

def main():
    # Открыть файл sales.txt для чтения
    sales_file = open('./files/sales.txt', 'r')

    # Прочитать все строки из файла
    for line in sales_file:
        # конвертируем строку в число 
        amount = float(line)
        # Отформатировать и показать сумму
        print(f'{amount:.2f}')
        
    # Закрыть файл
    sales_file.close()
    

if __name__ == '__main__':
    main()