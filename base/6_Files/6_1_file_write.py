# Эта программа пишет три строки данных 
# в файл

def main():
    # Открыть файл с именем 
    outfile = open('./files/text.txt', 'w')
    
    # Записать имена трех философов в файл
    outfile.write('Джон Локк\n')
    outfile.write('Дэведи Хьюм\n')
    outfile.write('Эдмунд Берк\n')
    
    # Закрыть файл
    outfile.close()
    

if __name__ == '__main__':
    main()