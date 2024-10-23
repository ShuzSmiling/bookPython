# Эта программа демонстрирует двумерный список

def main():
    # Create nested list
    value = [[1, 2, 3],
             [10, 20, 30],
             [100, 200, 300]]
            
    # display elem list
    for row in value:
        for element in row:
            print(f'{row}: {element}')


if __name__ == '__main__':
    main()