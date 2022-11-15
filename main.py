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
    
    #move ace/s to last values in hand list
    for i in range(0, len(hand["hand"])):
        value = hand["hand"][i][0]
        if value == 'A':
            removed_ace = hand["hand"].pop(i)
            hand["hand"].append(removed_ace)    

    #score each card in hand
    for card in hand["hand"]:
        value = card[0]
        if value in base_cards:
            total += int(value)
        elif value in face_cards:
            total += 10
        else:
            if total + 11 > 21:
                total += 1
            else:
                total += 11          
    
    hand["total"] = total
    
def deal_opening_hands():
    deal_to_player(deck)
    deal_to_dealer(deck)
    deal_to_player(deck)
    deal_to_dealer(deck)
    calculateTotal(player_hand)
    calculateTotal(dealer_hand)
    print(f"Your cards: {player_hand['hand']}")
    print(player_hand["total"])
    print(f"Dealer's first card: {dealer_hand['hand'][0]}")
    print(dealer_hand["total"])

deal_opening_hands()


def assessHand(hand):
    if hand["total"] > 21:
        return False
    elif hand["total"] == 21:
        return True

while play_game == 'y':
    play_game = input(f"Type 'y' to get another card, type 'n' to pass: ")
    if play_game == 'y':
        deal_to_player(deck)
        calculateTotal(player_hand)
        if assessHand(player_hand):
            print("You win!")
            play_game = 'n'
        elif not assessHand(player_hand):
            print("You Bust!")
            play_game = 'n'
    else:
        if dealer_hand["total"] > player_hand["total"]:
            print("Dealer Wins!")
        if calculateTotal(dealer_hand) <= 16:
            deal_to_dealer(deck)
            calculateTotal(dealer_hand)
            if assessHand(dealer_hand):
                print("You win!")
                play_game = 'n'
            elif not assessHand(dealer_hand):
                print("You Bust!")
                play_game = 'n'
            
