# This programm use dict from game card
import random

def main():
    # create deck of cards
    deck = create_deck()
    
    # get count card to be deal
    num_cards = int(input('Сколько карт раздать: '))

    # deal cards
    deal_cards(deck, num_cards)
    

# Function create_deck return dict
# representing a deck of cards
def create_deck():
    
    return {
        'Туз пик': 1, '2 пик': 2, '3 пик': 3, '4 пик': 4,
        '5 пик': 5, '6 пик': 6, '7 пик': 7, '8 пик': 8,
        '9 пик': 9, '10 пик': 10, 'Валет пик': 10, 'Дама пик': 10,
        'Король пик': 10,
        
        'Туз червей': 1, '2 червей': 2, '3 червей': 3, '4 червей': 4,
        '5 червей': 5, '6 червей': 6, '7 червей': 7, '8 червей': 8,
        '9 червей': 9, '10 червей': 10, 'Валет червей': 10, 'Дама червей': 10,
        'Король червей': 10,
        
        'Туз треф': 1, '2 треф': 2, '3 треф': 3, '4 треф': 4,
        '5 треф': 5, '6 треф': 6, '7 треф': 7, '8 треф': 8,
        '9 треф': 9, '10 треф': 10, 'Валет треф': 10, 'Дама треф': 10,
        'Король треф': 10,
        
        'Туз бубей': 1, '2 бубей': 2, '3 бубей': 3, '4 бубей': 4,
        '5 бубей': 5, '6 бубей': 6, '7 бубей': 7, '8 бубей': 8, 
        '9 бубей': 9, '10 бубей': 10, 'Валет бубей': 10, 'Дама бубей': 10,
        'Король бубей': 10
    }
    

# func distributes count of card on deck
def deal_cards(deck, number):
    hand_value = 0
    
    if number > len(deck):
        number = len(deck)
        
    for _ in range(number):
        card = random.choice(list(deck))
        
        print(card)
        hand_value += deck[card]
    
    print(f'Величина карт на руках: {hand_value}')
    

if __name__ == '__main__':
    main()