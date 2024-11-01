def range_sum(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)


def main():
    numbes = [1, 2, 3, 4, 5, 7, 9]
    
    my_sum = range_sum(numbes, 2, 5)
    
    print(f'Сумма значений со 2 по 5 позицию равняется {my_sum}')
    

if __name__ == '__main__':
    main()