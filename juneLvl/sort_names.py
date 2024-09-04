name_first = input('Введите имя: ')
name_second = input('Введите второе имя: ')

print('Вот имена, ранжированные по алфавиту')

if name_first > name_second:
    print(name_first)
    print(name_second)
else:
    print(name_second)
    print(name_first)