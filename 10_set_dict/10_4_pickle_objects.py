# This program show pickle module
import pickle


def main():
    again = 'yes'
    
    # open file for write
    output_file = open('../files/info.dat', 'wb')
    
    # get data users
    while again.lower() == 'yes':
        save_data(output_file)
        
        again = input('Желаете ввести еще данные? yes/no\n>>> ')
    
    output_file.close()
    

def save_data(files):
    person = {}
    
    person['name'] = input('Name: ')
    person['surname'] = input('Surname: ')
    person['weight'] = input('Weight: ')
    
    pickle.dump(person, files)
    

if __name__ == '__main__':
    main()
    
