# Эта программа показывает записи, которые
# находятся в файле employee.txt

def main():
    # Открыть файл
    emp_file = open('./files/employee.txt', 'r')
    
    # Прочитать первую строку с файлом
    name = emp_file.readline()
    
    while name:
        id_num = emp_file.readline()
        dept = emp_file.readline()
        
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')
        
        # показать запись
        print(f'Имя: {name}')
        print(f'ID: {id_num}')
        print(f'Отдел: {dept}')
        print()
        
        name = emp_file.readline()
        
    emp_file.close()
    
    
if __name__ == '__main__':
    main()