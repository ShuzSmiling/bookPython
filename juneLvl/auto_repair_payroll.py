BASE_HOURS = 40
OT_MULTIPLIER = 1.5

hours = float(input('Введите кол-во отработанных часов: '))
pay_rate = float(input('Введите почасовую ставку оплаты труда: '))

if hours > BASE_HOURS:
    overtime_hours = hours - BASE_HOURS
    
    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER
    
    pay = BASE_HOURS * pay_rate + overtime_pay
    print(f'Зарплата сотрудников, с учетом переработок: {overtime_hours} часов, составила: ${pay:,.2f}')
else:
    pay = hours * pay_rate 
    print(f'Зарплата сотрудников составила: ${pay:,.2f}')