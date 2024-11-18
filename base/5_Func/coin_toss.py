# Эта программа имитирует 10 бросков монеты
import random

# Константы
HEADS = 1 # Орел
TAILS = 2 # Решка
TOSSES = 10 # Кол-во бросков

def main():
    for _ in range(TOSSES):
        if random.randint(HEADS, TAILS) == HEADS:
            print('Орел')
        else:
            print('Решка')
            

if __name__ == '__main__':
    main()