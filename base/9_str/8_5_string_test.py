# this program show several methods for str

def main():
    # get user str value
    user_string = input('Введите строковое значение: ')

    print('Вот, что обнаружено в отношении введенного значения: ')

    # analyze result
    if user_string.isalnum():
        print('Эта строка содержит буквы или цифры')
    if user_string.isdigit():
        print('Эта строка содержит только цифры')
    if user_string.isalpha():
        print('Это строка содержит только буквы алфавита')
    if user_string.isspace():
        print('Эта строка содержит только пробельные символы')
    if user_string.islower():
        print('Все буквы в строке находятся в нижнем регистре')
    if user_string.isupper():
        print('Все буквы в строке находятся в верхнем регистре')

        
if __name__ == '__main__':
    main()
    