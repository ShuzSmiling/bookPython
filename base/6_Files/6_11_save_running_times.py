# Эта программа сохраняет последовательность, состоящую из
# длительностей видеоклипов, в файле video_times.txt

def main():
    # получить кол-во видеоклипов в проекте
    num_videos = int(input('Сколько видеоклипов в проекте? '))
    
    # Открыть файл для записи длительности видеоклипов
    video_file = open('./files/video_times.txt', 'w')
    
    # Получить длительность каждого видеоролика
    # и записать его в файл
    print('Введите длительность каждого видеоклипа')
    
    for count in range(1, num_videos + 1):
        run_time = float(input(f'Видеоклип № {count}: '))
        video_file.write(f'{run_time}\n')
        
    # Закрыть файл
    video_file.close()
    print('Времена сохранены в файл ./files/video_times.txt')


if __name__ == '__main__':
    main()