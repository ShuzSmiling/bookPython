# Эта программа применяет рекурсию для нахождения
# наибольшего общего делителя (НОД или GCD) двух чисел
def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


def main():
    num1 = 49
    num2 = 28 
     
    print(f'Наибольший общий делитель'
          f'эти двух чисел равен {gcd(num1, num2)}')

          
if __name__ == '__main__':
    main()