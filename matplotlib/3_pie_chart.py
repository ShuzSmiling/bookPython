# This programm show circular diagram
from matplotlib import pyplot as plt

def main():
    # create list values
    sales = [20, 60, 80, 40]
    
    # create list labels
    slice_labels = [
        'I квартал',
        'II квартал',
        'III квартал',
        'IV квартал'
    ]
    
    # create circular diagram
    plt.pie(sales, labels=slice_labels, colors=('r', 'g', 'b', 'm'))
    
    # add title
    plt.title('Продажи с разбивкой по кварталам')
    
    # show diagram
    plt.show()
    

if __name__ == '__main__':
    main()