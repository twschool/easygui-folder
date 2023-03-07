from easygui import *
while True:
    places = enterbox("Enter 5 places you want to go seperated by a comma")
    places_list = places.split(",")
    if len(places_list) > 5:
        msgbox("You need to list less than 5 places")
    else:
        break
