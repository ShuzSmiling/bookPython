# Эта программа вычисляет отпускную цену
# розничного товара

# DICOUNT_PERCENTAGE используется в качестве
# глобальной константы для процента скидки
DISCOUNT_PERCENTAGE = 0.20

# Фнукция get_regular_price предлагает пользователю
# ввести обычную цену товара и возвращает 
# это значение

def get_regular_price():
    return float(input('Введите обычную цену товара: $'))


# Функция discount принимает цену товара 
# и возвращает сумму скидки, указанную в 
# DISCOUNT_PERCENTAGE
def discount(price):
    return price * DISCOUNT_PERCENTAGE


# Гланая функция
def main():
    # Получить обычную цену товара
    reg_price = get_regular_price()
    
    # Рассчитать отпускную цену
    sale_price = reg_price - discount(reg_price)
    
    # Показать отпускную цену
    print(f'Отпускная цена товара составляет ${sale_price:,.2f}.')


if __name__ == '__main__':
    main()
    