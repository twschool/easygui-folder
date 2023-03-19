import easygui as eg
import random as r
rounds_in_loop = 3

def rollin():
    print("Rollin function called")
    rolls_list = []
    # For each round
    for I in range(0, 5):
        # For each roll in a round
        rolls_list.append(r.randint(1, 6))
    old = 0
    most_number = 0
    for num in range(1, 7):
        new = rolls_list.count(num)
        if new > old:
            print(f"New: {new}, Old: {old}")
            print(f"Rolls list: ({rolls_list})")
            old = new
            most_number = num
    print(f"{old}")
    if old < 3:
        return [False, ""]
    elif old == 3:
        return [True, "Three of a kind"]
    elif old == 4:
        return [True, "Four of a kind"]
    elif old == 5:
        return [True, "Yahtzee!"]

while True:
    round_result = []
    for i in range(1, 4):
        rt = rollin()
        bool_ = rt[0]
        output = rt[1]
        if bool_ is True:
            round_result.append(f'Round {i}: "{output}"')
        else:
            round_result.append(f'Round {i}: "No combination rolled"')
    result_string = ""
    print(round_result)
    for item in round_result:
        print(item)
        result_string = f"{result_string}{item}\n"

        # result_string.join(f"{item}\n")
    game = eg.buttonbox(msg=f"Hello Player this was your game result\n{result_string}", title="Game result", choices=["Play again", "Exit"])
    if game == "Exit":
        exit("Game exited by user")