# Эта программа получает от пользователя данные о сотрудниках
# и сохраняет их в виде записей в файле employee.txt

def main():
    # получить кол-во записей о сотрудниках для создания
    num_emps = int(input('Сколько записей о сотрудниках ' + 
                        'Вы хотите сделать? '))
    
    # Открыть файл для записи
    emp_file = open('./files/employee.txt', 'w')
    
    # получить данные каждого сотрудника
    # и записать их в файл
    for count in range(1, num_emps + 1):
        # получить данные о сотруднике
        print(f'Введите данные о сотруднике № {count}')
        name = input('Имя: ')
        id_num = input('ID: ')
        dept = input('Отдел: ')
        
        # Записать в файл данные как запись
        emp_file.write(f'{name}\n')
        emp_file.write(f'{id_num}\n')
        emp_file.write(f'{dept}\n')
        
        # показать пустую строку
        print()
        
    # Закрыть файл
    emp_file.close()
    print('Записи о сотрудниках сохранены в employees.txt')


if __name__ == '__main__':
    main()