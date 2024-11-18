# this programm tests class CellPhone

from modules.cellphone import CellPhone

def main():
    # get data for phone
    man = input('Введите производителя: ')
    mod = input('Введите номер модели: ')
    retail = float(input('Введите розничную цену: '))

    
    # create instance of a CellPhone class
    phone = CellPhone(man, mod, retail)
    
    # Show input data
    print('Вот введеные Вами данные:')
    print(f'Производитель: {phone.get_manufact()}')
    print(f'Номер модели: {phone.get_model()}')
    print(f'Розничная цена: ${phone.get_retail_price():,.2f}')
    

if __name__ == '__main__':
    main()