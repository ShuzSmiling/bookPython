# Эта программа получает от пользователя количество баллов
# и показывает соответствующий буквенный уровень знаний


A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

user_score = int(input('Введите баллы за контрольную: '))

if user_score >= A_SCORE:
    print('Ваш уровень знаний A')
else:
    if user_score >= B_SCORE:
        print('Ваш уровень знаний B')
    else:
        if user_score >= C_SCORE:
            print('Ваш уровень знаний C')
        else:
            if user_score >= D_SCORE:
                print('Ваш уровень знаний D')
            else:
                print('Ваш уровень знаний F')