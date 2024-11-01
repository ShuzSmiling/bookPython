def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def main():
    number = int(input('Введите неотрицательное целое число: '))

    fact = factorial(number)
    
    print(f'Факториал числа {number} = {fact}')
    
    
if __name__ == '__main__':
    main()