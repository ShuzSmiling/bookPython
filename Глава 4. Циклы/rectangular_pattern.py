# Эта программа выводит прямоугольную комбинацию
# звездочек
rows = int(input('Сколько строк: '))
cols = int(input('Сколько столбцов: '))
sym = input('Символ: ')

for r in range(rows):
    for c in range(cols):
        print(f'{sym}', end='')
    print()