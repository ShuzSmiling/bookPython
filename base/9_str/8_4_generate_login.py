# this prograv get name, surname, idnumber student

from modules import login

def main():
    # get name, surname, idnumber
    first = input('Введите свое имя: ') 
    last = input('Введите свою фамилию: ')
    idnumber = input('Введите свой номер студенат: ')

    
    # get login for system
    print('Ваше имя для входа в систему: ')
    print(login.get_login_name(first=first, 
                               last=last, 
                               idnumber=idnumber))
    

if __name__ == '__main__':
    main()