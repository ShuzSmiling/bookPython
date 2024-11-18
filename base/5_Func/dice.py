# Эта программа имитирует бросание кубинов
import random

# Константы для минимального и максимально случайных чисел
MIN = 1
MAX = 6

def main():
    # Переменная, которая управляет циклом
    
    again = 'yes'
    
    while again.lower() == 'yes':
        print('Бросаем кубики...')
        print('Значение граней: ')
        print(random.randint(MIN, MAX), random.randint(MIN, MAX))
        print()
        
        # Сделать еще один бросок кубика
        again = input('Бросить кубик еще раз? (yes/no): ')
        

if __name__ == '__main__':
    main()