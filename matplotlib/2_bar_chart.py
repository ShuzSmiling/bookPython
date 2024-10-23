# This programm show histogramm
from matplotlib import pyplot as plt

def main():
    # create list coordinate X
    left_edges = [0, 10, 20, 30, 40]
    
    # create list height
    heights = [100, 200, 300, 400, 500]
    
    # create variable for width column
    bar_width = 10
    
    # build histogramm
    plt.bar(left_edges, heights, bar_width, color=('r', 'g', 'b', 'm', 'k'))
    
    # add title
    plt.title('Продажи с разбивкой по годам')
    
    # add title on x,y axes
    plt.xlabel('Год')
    plt.ylabel('Объем продаж')
    
    # edit ticks
    plt.xticks([5, 15, 25, 35, 45],
               ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 100, 200 , 300, 400, 500],
               ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
    
    # show histogramm
    plt.show()
    
    
if __name__ == '__main__':
    main()