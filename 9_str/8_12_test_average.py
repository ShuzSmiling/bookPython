# this programm calculate result scores

def main():
    # open file
    csv_file = open('files/scores.csv', 'r')
    
    # read line file in list
    lines = csv_file.readlines()
    
    # close file
    csv_file.close()
    
    # prcess line
    for line in lines:
        # get result scores in tokens
        tokens = line.replace('\ufeff', '').replace('\n', '').split(';')
        
        # calculate all scores
        total = 0.0
        for token in tokens:
            total += float(token)
            
        # calculate avg scores
        average = total / len(tokens)
        print(f'средний балл: {average}')


if __name__ == '__main__':
    main()