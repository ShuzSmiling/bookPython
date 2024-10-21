# Эта программа показывает случайное число
# из диапазона от 1 до 10
import random

def main():
    
    for i in range(5):
        print(f'Число равняется {random.randint(i, 1000):^10d}')
        


if __name__ == '__main__':
    main() 