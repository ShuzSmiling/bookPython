# this programm import module Coin
# and create 3 copy class

from modules.coin import Coin

def main():
    # create 3 objects class Coin
    coin1 = Coin()
    coin2 = Coin()
    coin3 = Coin()

    # Show coin
    print('вот три монеты, у которых эти стороны обращены вверх')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()
    
    # toss
    print('подбрасываю три монеты')
    print()
    coin1.toss()
    coin2.toss()
    coin3.toss()

    # show coin
    print('Теперь обращены вверх эти стороны')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    

if __name__ == '__main__':
    main()