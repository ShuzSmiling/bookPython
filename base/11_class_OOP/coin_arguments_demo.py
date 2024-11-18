# This programm transmit object Coin
# in function 
from modules.coin import Coin

def main():
    # create object
    my_coin = Coin()
    
    # This instruction show coin
    print(my_coin.get_sideup())

    # accepts object in function "Flip"
    flip(my_coin)
    
    # This instruction will show either
    # heads or tails
    print(my_coin.get_sideup())


# "Flip" toss
def flip(coin_obj):
    coin_obj.toss()
    

if __name__ == '__main__':
    main()