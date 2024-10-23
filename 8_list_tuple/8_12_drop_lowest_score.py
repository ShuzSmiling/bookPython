# Эта программа получает серию оценок за лабораторные
# работы и вычисляет среднюю сумму
# отбрасывая самую низкую

def main():
    # Получить от пользователя оценки
    scores = get_scores()
    
    # Получить сумму оценок
    total = sum(scores)
   
    # Получить минимальную оценку
    lowest = min(scores)
    
    # Вычестиь самую низкую оценку
    total -= lowest 
    
    # Вычеслить среднюю оценку
    avg = total / (len(scores) - 1)
    
    # показать среднее значение
    print(f'Средняя оценка с учетом отброшенной: {avg}') 
    

def get_scores():
    test_scores = []
    again = 'yes'
    
    while again.lower() == 'yes':
        value = float(input('Введите оценку: '))
        test_scores.append(value)
        
        print('Желаете продолжить вносить оценку? yes/no')
        again = input('>> ')
        
    return test_scores

if __name__ == '__main__':
    main()