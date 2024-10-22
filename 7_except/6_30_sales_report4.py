# Эта программа показывает итоговую сумму

def main():
    # инициализировать накопитель
    total = 0.0
    filename = input('Введите название файла: ')
    
    try:
        infile = open(filename, 'r')
        
        for line in infile:
            total += float(line)
        
        infile.close()
    
    except Exception as err:
        print(err)
    
    else:
        print(f'{total:,.2f}')
    

if __name__ == '__main__':
    main()