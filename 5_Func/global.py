# создать глобальную переменную
number = 0


def show_number():
    print(f'Вы ввели число {number}')


def main(): 
    global number
    
    number = int(input('Введите число: '))
    show_number()
    

if __name__ == '__main__':
    main()