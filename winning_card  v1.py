from random import choice
from random import choice
from easygui import buttonbox

card_list = ["two", "three", "four", "five", "six", "seven", "eight",
             "nine", "ten", "Jack", "Queen", "King", "Ace"]
suits_list = ["Clubs", "Diamonds", "Hearts", "Spades"]
msg = "nothing"
while True:
    computer_card = choice(card_list)
    computer_choice = choice(suits_list)
    user_card = choice(card_list)
    user_choice = choice(suits_list)
    comp_index = card_list.index(computer_card)
    user_index = card_list.index(user_card)
    if comp_index < user_index:
        user_won = False
        msg = "The user has lost"
    elif comp_index > user_index:
        user_won = True
        msg = "The user has won"
    elif comp_index == user_index:
        user_won = None
        msg = "The user has tied"
    else:
        msg = "I am so confused"
    game = buttonbox(msg=f"{msg}\nThe user had the {user_card} of {user_choice}\n"
                         f"The computer had the {computer_card} of {computer_choice}",
                     choices=["Play again", "Exit"], title="Round result")
    if game == "Exit":
        exit()





