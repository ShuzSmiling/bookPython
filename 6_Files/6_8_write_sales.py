# Эта программа предлагает пользователю ввести суммы
# продаж и записывает эти суммы в файл sales.txt

def main():
    # получить кол-во дней
    num_days = int(input('За какое кол-во дней' + 
                         'Вы располагаете продажами? '))

    # Открыть новый файл с имененм sales.txt
    sales_file = open('./files/sales.txt', 'w')
    
    # получить суммы продаж за каждый день
    # и записать их в файл
    for count in range(1, num_days + 1):
        # получить продажи за день
        sales = float(input(
            f'Введите продажи за день № {count}: $'
        ))
        
        # Записать суммы продаж за день
        sales_file.write(f'{sales}\n')
        
    # Закрыть файл
    sales_file.close()
    print('Данные записаны в ./files/sales.txt')
    

if __name__ == '__main__':
    main()