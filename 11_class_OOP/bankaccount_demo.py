# Эта программа демонстрирует класс BankAccount

from modules.bankaccount import BankAccount

def main():
    # Получить начальный остаток
    start_bal = float(input('Введите свой начальный остаток: '))

    # создать объект BankAccount
    savings = BankAccount(start_bal)
    
    # внести на счет зп пользователя
    pay = float(input('Сколько вы получили на этой неделе: '))
    print('Вношу эту сумму на Ваш счет')
    savings.deposit(pay)
    
    # показать остаток
    print(savings)
    
    # получить сумму для снятия с банковского счета
    cash = float(input('Сколько хотите снять: '))
    print('Снимаю эту сумму с Вашего банковского счета.')
    savings.withdraw(cash)
    
    # показать остаток
    print(savings)
    
    
if __name__ == '__main__':
    main()