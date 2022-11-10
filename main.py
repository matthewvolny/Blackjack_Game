import random

from art import logo

print(logo)

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

deck = ["2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS"]

def shuffle(deck):
    for i in range(len(deck)):
        random_num = random.randint(0, len(deck)-1)
        temp = deck[random_num]
        deck[random_num] = deck[i]
        deck[i] = temp

shuffle(deck)      
    
# while play_game == 'y':
#     print("game running")
