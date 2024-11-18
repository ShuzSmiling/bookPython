# This programm preseves objects CellPhone
import pickle

from modules.cellphone import CellPhone

FILENAME = './files/cellphones.dat'

def main():
    again = 'yes'
    
    # open file
    output_file = open(FILENAME, 'wb')

    # get data from the user
    while again.lower() == 'yes':
        # get phone details
        man = input('Введите производителя: ')
        mod = input('Введите номер модели: ')
        retail = float(input('Введите розничную цену: '))

        # create object CellPhone
        phone = CellPhone(man, mod, retail)
        
        # preserves obj and write in file
        pickle.dump(phone, output_file)
        
        again = input('Введете еще один элемент? yes/no: ')
        
    # close file
    output_file.close()
    print(f'Данны записаны в {FILENAME}')

    
if __name__ == '__main__':
    main()
