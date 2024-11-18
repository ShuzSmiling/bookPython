MIN_SALARY = 30000
MIN_YEARS = 2

salary = int(input('Сколько вы зарабатываете: '))
years_on_job = round(float(input('Стаж на текущем месте работы: ')), 1)

if salary >= MIN_SALARY:
    if years_on_job >= 2:
        print('Ваша ссуда одобрена')
    else:
        print(f'Вы должны отработать не менее {MIN_YEARS} лет что бы получить одобрение')
else:
    print(f'Вы должны зарабатывать не менее ${MIN_SALARY:,.2f} в год,\nчтобы получить одобрение')