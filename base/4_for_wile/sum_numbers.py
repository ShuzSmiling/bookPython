# Эта программа вычисляет сумму серии
# чисел, вводимых пользователем

MAX = 5

# Инициализировать накапливающую переменную
total = 0

# Объясняем что делаем
print('Эта программа вычисляет сумму из')
print(f'{MAX} чисел, которые вы введете')

# Получить числа и накопить их
for counter in range(MAX):
    number = float(input('Введите число: '))
    total += number
    
# Показать сумму чисел
print(f'Сумма составляет {total}')