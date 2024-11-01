def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    print('Первые 10 чисел')
    print('последовательности Фибоначчи')

    for number in range(1, 11):
        print(fib(number), number)
        

if __name__ == '__main__':
    main()