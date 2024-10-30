from modules.coin import Coin
    
def main():
    # создать объект на основе класса coin
    my_coin = Coin()
    
    # показать обращенную вверх сторону монеты
    print(f'Эта сторона обращена вверх: {my_coin.get_sideup()}')
    
    # подбросить монету 10 раз
    for _ in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())
    

if __name__ == '__main__':
    main()