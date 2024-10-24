# Эта программа показывает пошаговые инструкции
# для разборки бельевой сушилки фирмы Acme.

# Функция startup_message показывает
# первоначальное сообщение программы на экране
def startup_message():
    print('Эта программа дает рекомендации')
    print('по разборке бельевой сушилки фирмы ACME.')
    print('Данный процесс состоит из 4-х шагов')
    print()
    

# Функция step_1 показывает инструкции 
# для шага 1
def step_1():
    print('Шаг 1: Отключить сушилку')
    print('Отодвинуть ее от стены')
    print()


# Функция step_2 показывает инструкции
# для шага 2
def step_2():
    print('Шаг 2: удалить шесть винтов')
    print('с задней стороны сушилки')
    print()
    

# Функция step_3 показывает инструкции
# для шага 3 
def step_3():
    print('Шаг 3: удалить заднюю панель')
    print('сушилки')
    print()
    

# Функция step_4 показывает инструкции
# для шага 4
def step_4():
     print('Шаг 4: вынуть верхний блок')
     print('сушилки')
     print()


# Главная функция выполняет основную логику программы
def main():
    # Показать стартовое сообщение
    startup_message()
    input('Нажмите Enter, что бы продолжить')
    
    # Показать шаг 1
    step_1()
    input('Нажмите Enter что бы продолжить')
    
    # Показать шаг 2
    step_2()
    input('Нажмите Enter что бы продолжить')
    
    # Показать шаг 3
    step_3()
    input('Нажмите Enter что бы продолжить')
    
    # Показать шаг 4
    step_4()
    input('Нажмите Enter что бы продолжить')
    
    
if __name__ == '__main__':
    main()