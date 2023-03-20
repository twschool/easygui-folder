import easygui as eg
import random as r
rounds_in_loop = 3
player_one_score = 0
player_two_score = 0


def rollin():
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
        return [False, "", 0]
    elif old == 3:
        return [True, "Three of a kind", 10]
    elif old == 4:
        return [True, "Four of a kind", 30]
    elif old == 5:
        return [True, "Yahtzee!", 50]

player_name_list = []
player_name_list.append(eg.enterbox(msg="Enter the name of player one")) 
player_name_list.append(eg.enterbox(msg="Enter the name of player two"))
false = True
while True:
    for pn in range(1, 3):
        round_result = []
        false = True
        user_score = 0
        for i in range(1, 4):
            if false is True:
                rt = rollin()
                bool_ = rt[0]
                output = rt[1]
                score = rt[2]
                ji = eg.buttonbox(choices=["Reroll", "I'm happy with this round"], msg=f"{output} Score: {score}")
                if ji != "Reroll":
                    user_score = score
                    false = False
    
                if bool_ is True:
                    round_result.append(f'Round {i}: "{output}"')
                else:
                    round_result.append(f'Round {i}: "No combination rolled"')
        eg.buttonbox(msg=f"You got {user_score}", choices=["Ok"])
        if pn == 1:
            player_one_score += user_score
        else:
            player_two_score += user_score
        result_string = ""
        for item in round_result:
            result_string = f"{result_string}{item}\n"

            # result_string.join(f"{item}\n")
        eg.buttonbox(msg=f"Hello {player_name_list[(pn - 1)]} this was your game result\n{result_string}", title="Game result", choices=["OK"])
        
    game = eg.buttonbox(msg="Exit or play again", title="Game menu", choices=["Exit", "Play again"])
    if game == "Exit":
        game_result = f"\nPlayer one ({player_name_list[0]}) Score: {player_one_score}\n" \
                      f"Player two ({player_name_list[1]}) Score: {player_two_score}" 
        if player_one_score > player_two_score:
            eg.msgbox(msg=f"{player_name_list[0]} had the biggest score{game_result}")
        elif player_one_score < player_two_score:
            eg.msgbox(msg=f"{player_name_list[1]} had the biggest score{game_result}")
        else:
            eg.msgbox(msg=f"{player_name_list[0]} the scores were equal{game_result}")

        exit("Game exited by user")