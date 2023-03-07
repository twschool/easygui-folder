import easygui as eg
import dice_roll_v1
number = random.randint(0, 100)
guess = -1
text = "Enter a number between 1 and 100"
while guess != number:
    guess = eg.integerbox(text, "Int stuff")
    if guess > number:
        text = "Lower"
    elif guess < number:
        text = "Higher"
