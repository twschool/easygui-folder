import winsound

import easygui as eg
password = "password"
while "password" in password.lower():
    password = eg.enterbox("Enter your password to your account: ", "Very secure password")
    choice = eg.buttonbox("Are you happy with your password", choices=["Yes", "No", "Is my data going to be leaked"])
    ez = choice[0]
    if ez == "I":
        winsound.PlaySound('SystemHand', winsound.SND_ALIAS)
        eg.buttonbox(choices=["Accept the Terms and conditions"], image="dee.gif")

    elif ez == "Y":
        eg.textbox("Good your password will be saved securely in a text document", "Password message lol")
    else:
        eg.msgbox("Ok fine", "You are annoying", "Bruh why did you enter a bad password thats on you")
        password = "password"
