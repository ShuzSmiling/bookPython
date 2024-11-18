# this program creat five object CellPhone
# and save in list

from modules.cellphone import CellPhone


def main():
    # get list objects CellPhone
    phones = make_list()
    
    # Show data in list
    print('Вот введенные данные:')
    display_list(phones)
    

# func make_list accepts input data on 
# five phone and return list object CellPhone
def make_list():
    # create clear list
    phone_list = []
    
    # add five objects in list
    print('Введите данные о 5-ти телефонах:')
    for count in range(1, 6):
        # get data number
        print(f'Номер телефона {count}:')
        man = input('Введите производителя: ')
        mod = input('Введите номер модели: ')
        retail = float(input('Введите розничную цену: '))
        print()
        
        # create new object CellPhone 
        phone = CellPhone(man, mod, retail)
        
        # add object in list
        phone_list.append(phone)
        
    return phone_list


def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()
        
    
if __name__ == '__main__':
    main()