# Программа демонстрирует использование глобальной константы
# для представления ставки взноса компании
CONTRIBUTION_RATE = 0.05


# Функция show_pay_contrib принимает заработную плату
# в качестве аргумента и показывает взнос в 
# пенсионные накопления исходя из этого размера оплаты
def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print(f'Взнос исходя из заработной платы: ${contrib:,.2f}')
    

# Функция show_bonus_contrib принимает сумму премий
# в качестве аргумента и показывает взнос
# в пенсионное накоплнеие исходя из этой суммы оплаты
def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print(f'Взнос исходя из суммы премий: ${contrib:,.2f}')


def main():
    gross_pay = float(input('Введите ЗП: '))
    bonus = float(input('Введите сумму премий: '))
    show_pay_contrib(gross=gross_pay)
    show_bonus_contrib(bonus=bonus)
    

if __name__ == '__main__':
    main()