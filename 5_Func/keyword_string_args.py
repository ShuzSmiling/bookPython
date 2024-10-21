# Эта программа демонстрирует передачу в функцию двух файлов
# строковых значений в качестве именованных аргументов


def reverse_name(first, last):
    print(last, first)
    

def main():
    first_name = input('Введите свое имя: ')
    last_name = input('Введите свою фамилию: ')
    
    print('Ваше имя в обратном порядке')
    reverse_name(last=last_name, first=first_name)
    

if __name__ == '__main__':
    main()
    