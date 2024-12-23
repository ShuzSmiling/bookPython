# Класс bankaccount имитирует банковский счет

class BankAccount:
    
    # Метод __init__ принимает аргумент
    # с остатком на счете
    # Он присваивается атрибуту __balance
    def __init__(self, bal):
        self.__balance = bal
        
    # Метод deposit вносит
    # на счет вклад
    def deposit(self, amount):
        self.__balance += amount
        
    
    # Метод withdraw снимает сумму
    # со счета
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Ошибка: недостаточно средств')
    
    
    # Метод get_balance возвращает
    # остаток средств на счете
    def get_balance(self):
        return self.__balance
    
    
    # Метод __str__ возвращает строковое
    # значение, сообщающее о состоянии объекта
    def __str__(self):
        return f'Остаток составляет ${self.__balance:,.2f}'