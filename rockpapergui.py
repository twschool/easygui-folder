import random
import easygui as eg
text = "Welcome to rock paper scissors\n" \
       "Rock beats Scissors, Paper beats Rock, and Paper beats Rock"
item_list = ["Rock", "Paper", "Scissors"]
is_playing = eg.buttonbox(f"{text}\nWould you like to play rock paper scissors",
                          "Are you playing?", choices=["Yes", "No"])
if is_playing == "No":
    exit("Why?")
while True:
    computer_choice = random.choice(item_list)
    player_item = eg.buttonbox("Rock, Paper, Or Scissors", "Item choice",
                               choices=["Rock", "Paper", "Scissors"])
    cc = computer_choice
    pi = player_item
    win = False
    if computer_choice == player_item:
        play_again = eg.buttonbox("Draw\nPlay again", choices=["Yes", "No"])
    elif pi == "Rock" and cc == "Paper" or pi == "Scissors" and \
         cc == "Rock" or pi == "Paper" and cc == "Scissors":
        play_again = eg.buttonbox("You lost\nPlay again", choices=["Yes", "No"])
    else:
        play_again = eg.buttonbox("You won\nPlay again", choices=["Yes", "No"])
    if play_again == "No":
        eg.buttonbox("I have kidnapped your family", choices=["I am okay with this"], image="dee.gif")
        exit("You will never see them again")



