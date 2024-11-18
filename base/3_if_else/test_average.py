HIGH_SCORE = 95


test = 0
score_list = list()

for i in range(3):
    test = int(input(f'Введите оценку {i + 1}: '))
    score_list.append(test)
    
result = round(sum(score_list) / len(score_list), 2)
print(f'Ваш средний балл равен {result}')

if result > HIGH_SCORE:
    print('Поздравляем!\nОтличный результат!')