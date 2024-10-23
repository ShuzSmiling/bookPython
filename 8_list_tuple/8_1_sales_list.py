# константа NUM_DAYS содержит кол-во дней
# за которое мы соберем данные продаж
NUM_DAYS = 5

def main():
    # создать список, который будет держать продажи за день
    sales_list = [0] * NUM_DAYS
    
    print('Введите продажи за день')

    # получить продажи за каждый день
    for i in range(len(sales_list)):
        sales_list[i] = float(input(f'День № {i + 1}: '))

    # Показать введеные значения
    print('Вот значения, которые были введены')
    for value in sales_list:
        print(value)
        

if __name__ == '__main__':
    main()