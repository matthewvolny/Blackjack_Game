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

player_hand = []
dealer_hand = []

def deal_to_player(deck):
    player_hand.append(deck.pop())

def deal_to_dealer(deck):
    dealer_hand.append(deck.pop())

def deal_opening_hands():
    deal_to_player(deck)
    deal_to_dealer(deck)
    deal_to_player(deck)
    deal_to_dealer(deck)
    print(f"Your cards: {player_hand}")
    print(f"Dealer's cards {dealer_hand}")

deal_opening_hands()
# while play_game == 'y':
#     print("game running")
