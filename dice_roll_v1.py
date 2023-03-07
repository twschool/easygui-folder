import easygui
import random
player1 = -1
player2 = -1
for roll in range(1, 3):
    dice_roll_1 = random.randint(1, 6)
    dice_roll_2 = random.randint(1, 6)
    easygui.buttonbox(f"Player {roll} rolled a {dice_roll_1} and a {dice_roll_2}\nTotal dice roll"
                      f" {dice_roll_1 + dice_roll_2}", "Dice result", choices=["Ok"])
