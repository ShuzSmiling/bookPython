# Эта программа читает значения из файла
# video_times.txt и вычисляет их сумму

def main():
    # Открыть файл video_times.txt для чтения
    video_files = open('./files/video_times.txt', 'r')
    
    # Инициилизировать накопитель
    total = 0.0
    
    # Счетчик для подсчета видеоклипов
    count = 0 
    
    print('Длительность всех видеоклипов')

    # получить значения из файла и просумировать их
    for line in video_files:
        run_time = float(line)
        count += 1
        print(f'Видеоклип № {count}: {run_time}', sep='')
        total += run_time
        
    video_files.close()

    print(f'Общая длина составляет {total} секунд')
    

if __name__ == '__main__':
    main()