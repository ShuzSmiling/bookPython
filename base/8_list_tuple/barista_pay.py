# Эта программа вычисляет ЗП
# для каждого сотрудника Меган

# NUM_EMPLOYEES - размер списка (кол-во сотрудников)
NUM_EMPLOYEES = 6


def main():
    # Создать список, которы будет содержать отработанные часы
    hours = [0] * NUM_EMPLOYEES
    
    # Получить часы, отработанные каждым сотрудником
    for index in range(NUM_EMPLOYEES):
        hours[index] = float(input(f'Введите число отработанных часов сотрудников {index + 1}: '))

    # получить почасовую ставку оплаты
    pay_rate = float(input('Введите почасовую ставку: '))
    
    # Показать зп каждого сотрудника
    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print(f'ЗП сотрудника {index + 1}: ${gross_pay:,.2f}')
    
    
if __name__ == '__main__':
    main()