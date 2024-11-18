# Эта программа демонстрирует аргумент,
# передаваемый в функцию

# Функция show_double принимает аргумент,
# и показывает его удвоеное значение
def show_double(number):
    print(number ** 2)

def main(value):
    show_double(number=value)
    

if __name__ == '__main__':
    main(5)
    