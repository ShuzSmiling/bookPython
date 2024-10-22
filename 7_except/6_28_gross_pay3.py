# Эта программа вычисляет заработную плату до удержания

def main():
    try:
        # Получить кол-во отработанных часов
        hours = int(input('Сколько часов вы отработали: '))

        # получить почасовую ставку оплаты труда
        pay_rate = float(input('Введите почасовую ставку: '))

        # вычислить заработаную плату
        gross_pay = hours * pay_rate
        
        # Показать заработную плату
        print(f'ЗП: ${gross_pay:,.2f}')
        
    except ValueError as err:
        print(err)
        

if __name__ == '__main__':
    main()