from matplotlib import pyplot as plt

def main():
    # Create list coordinate X & Y
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]
    
    # Build a line graph
    plt.plot(x_coords, y_coords, marker='^')
    
    # Add title
    plt.title('Продажи с разбивкой по годам')
    
    # Add x-label, y-label
    plt.xlabel('Год')
    plt.ylabel('Объем продаж')
    
    # Edit tick mark
    plt.xticks([0, 1, 2, 3, 4, 5],
               ['2016', '2017', '2018', '2019', '2020', '2021'])
    plt.yticks([0, 1, 2, 3, 4, 5, 6],
               ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m', '$6m'])
     
    # Edit axis boundary
    plt.xlim(xmin=-1, xmax=5)
    plt.ylim(ymin=-1, ymax=6)
    
    # Add grid
    plt.grid(True)
    
    # show line graph
    plt.show()
    

if __name__ == '__main__':
    main()