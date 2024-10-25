# This programm causes split
# use sym '/'

def main():
    # create str value date
    date_string = '26/11/2020'
    
    # split date
    date_list = date_string.split('/')
    
    # show all date
    print(f'День: {date_list[0]}')
    print(f'Месяц: {date_list[1]}')
    print(f'Год: {date_list[2]}')
    

if __name__ == '__main__':
    main()
    