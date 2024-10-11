MIN_SALARY = 30000.0
MIN_YEARS = 2

salary = float(input('Введите свой годовой доход: '))
years_on_job = float(input('Введите кол-во лет рабочего стажа: '))

if salary > MIN_SALARY and years_on_job > MIN_YEARS:
    print('Ваша ссуда одобрена')
else:
    print('Ссуда не одобрена')
    
    
if salary > MIN_SALARY or years_on_job > MIN_YEARS:
    print('Ваша ссуда одобрена')
else:
    print('Ссуда не одобрена')