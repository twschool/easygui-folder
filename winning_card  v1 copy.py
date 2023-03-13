import random as r
from easygui import buttonbox


card_list = ["two", "three", "four", "five", "six", "seven", "eight",
             "nine", "ten", "Jack", "Queen", "King", "Ace"]
suits_list = ["Clubs", "Diamonds", "Hearts", "Spades"]
deck = []
for suit in suits_list:
    for card in card_list:
        deck.append([card, suit])
while True:
    r.shuffle(deck)
    cards = ""
    pos = -1
    limit = 7
    for item in deck:
        pos += 1
        if pos == limit:
            break
        else:
            cards = f"{cards}\n*  Card: {item[0].title()} of {item[1]}"
    ending = buttonbox(cards,title="Cards Drawn", choices=["Play again", "Exit"])
    if ending == "Exit":
        exit()