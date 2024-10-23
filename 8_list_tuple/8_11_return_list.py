# Эта программа применяет функцию для создания списка
# Указанная функция возвращает ссылку на список

def main():
    # Получить список с хранящимися в нем значениями
    numbers = get_values()
    
    # показать значения в списке
    print('>> Числа в списке: ')
    print(numbers)
    

# Функция get_values получает от пользователя 
# ряд чисел и сохраняет их в списке
# Функция возвращает ссылку на список
def get_values():
    values = []
    again = 'yes'
    
    while again.lower() == 'yes':
        num = int(input('>> Введите числовое значение: '))
        values.append(num)
        
        print('>> Желаете добавить еще одно число?')
        print('>> yes|no')
        again = input('>> ')
        print()
        
    return values


if __name__ == '__main__':
    main()