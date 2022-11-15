import random

from art import logo
from deck import deck

print(logo)

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def shuffle(deck):
    for i in range(len(deck)):
        random_num = random.randint(0, len(deck)-1)
        temp = deck[random_num]
        deck[random_num] = deck[i]
        deck[i] = temp

shuffle(deck)      

player_hand = {"hand": [], "total": None}
dealer_hand = {"hand": [], "total": None}

def deal_to_player(deck):
    player_hand["hand"].append(deck.pop())

def deal_to_dealer(deck):
    dealer_hand["hand"].append(deck.pop())

def calculateTotal(hand):

    base_cards = ['2','3','4','5','6','7','8','9','10']
    face_cards = ['J', 'Q', 'K']

    total = 0
    
    for card in hand["hand"]:
        if card[0] in base_cards:
            total += int(card[0])
        elif card[0] in face_cards:
            total += 10
        else:
            #ace condition
            if total + 11 > 21:
                total += 1
            else:
                total += 11          
    
    print(total)


def deal_opening_hands():
    deal_to_player(deck)
    deal_to_dealer(deck)
    deal_to_player(deck)
    deal_to_dealer(deck)
    calculateTotal(player_hand)
    calculateTotal(dealer_hand)
    print(f"Your cards: {player_hand['hand']}")
    print(f"Dealer's first card: {dealer_hand['hand'][0]}")

deal_opening_hands()

# while play_game == 'y':
#     play_game = input(f"Type 'y' to get another card, type 'n' to pass: ")
#     if play_game == 'y':
#         deal_to_player(deck)
