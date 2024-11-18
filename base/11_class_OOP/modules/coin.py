import random

# Класс coin имитирует монету, которую
# можно подбрасывать

class Coin:
    
    # Метод __init__ ициниализирует
    # атрибуты данных sideup значение 'Орел'
    
    def __init__(self):
        self.__sideup = 'Орел'
        
    # Метод toss генерирует случайное число
    # в диапазоне от 0 до 1. Если это число 
    # равно 0, то sideup получает значение 'Орел'
    # В противном случае = "Решка"

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Орел'
        else:
            self.__sideup = 'Решка'
    
    # Метод get_sideup возвращает значение
    # на которое ссылается sideup
    
    def get_sideup(self):
        return self.__sideup