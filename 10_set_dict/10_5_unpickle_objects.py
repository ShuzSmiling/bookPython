# This programm show open pickle object
import pickle

def main():
    end_of_file = False
    
    input_file = open('../files/info.dat', 'rb')
    
    while not end_of_file:
        try:
            person = pickle.load(input_file)

            display_data(person)
        except EOFError:
            end_of_file = True
            
    input_file.close()
    

def display_data(person):
    print('Имя: ', person['name'])
    print('Фамилия: ', person['surname'])
    print('Масса: ', person['weight'])
    print()
    

if __name__ == '__main__':
    main()
    
