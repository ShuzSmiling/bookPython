# This programm get user password
# and check valid

from modules import login

def main():
    # get password
    password = input('Введите свой пароль: ')

    # check password
    while not login.valid_password(password):
        print('Этот пароль недопустим')
        password = input('Введите пароль: ')

    print('Это допустимый пароль')
    
    
if __name__ == '__main__':
    main()