# Эта программа демонстрирует функцию sqrt
import math

def main():
    # Получить число
    number = float(input('Введите число: '))

    # Получить квадратный корень числа
    square_root = math.sqrt(number)
    
    # Показать квадратный корень
    print(f'Квадратный корень из {number} составляет {square_root}')

    
if __name__ == '__main__':
    main()