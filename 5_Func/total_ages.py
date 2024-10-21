# Эта программа использует возвращаемое значение функции


def summ(num1, num2):
    return num1 + num2


def main():
    # получить возраст пользователя
    first_age = int(input('Введите свой возраст: '))

    # получить возраст лучшего друга пользователя
    second_age = int(input('Введите возраст своего лучшего друга: '))
    
    # Получить сумму обоих возрастов
    total = summ(first_age, second_age)
    
    print(f'Вместе вам {total} лет.')
    

if __name__ == '__main__':
    main()
    