import easygui as eg
days_string = eg.enterbox("Enter the days you used technology. Seperate with a space")
days_list = days_string.split(" ")
days_of_week = 7
print(days_list)
for day in days_list:
    days_of_week -= 1
eg.buttonbox(f"You had {days_of_week} tech free days", choices=["Okay"])
