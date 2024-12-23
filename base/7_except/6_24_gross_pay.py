# Эта программа вычисляет заработную плату до удержания

def main():
    try:
        # Получить кол-во отработанных часов
        hours = int(input('Сколько часов вы отработали: '))

        # Получить почасовую ставку оплаты труда
        pay_rate = float(input('Введите свою почасовую ставку: '))

        # Вычислить заработанную плату до удержания
        gross_pay = hours * pay_rate
        
        # показать заработанную плату
        print(f'Ваша ЗП за {hours} часов составляет ${gross_pay:,.2f}')
    
    except ValueError:
       print('Ошибка: Отработанные часы или почасовая ставка оплаты') 
       print('должны быть допустимыми числами')


if __name__ == '__main__':
    main()