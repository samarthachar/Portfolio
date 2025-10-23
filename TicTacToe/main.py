#Note: This is a cli game

import random
import time

choices = list(range(1, 10))

box_dict = {
    1 : " ",
    2: " ",
    3: " ",
    4: " ",
    5: " ",
    6: " ",
    7: " ",
    8: " ",
    9: " "
}
def print_board():
    print(f"""
                        Game Board                 Input Numbers

                        {box_dict[1]} | {box_dict[2]} | {box_dict[3]}        |           1 | 2 | 3
                      -------------                ------------
                        {box_dict[4]} | {box_dict[5]} | {box_dict[6]}        |           4 | 5 | 6
                      -------------                ------------
                        {box_dict[7]} | {box_dict[8]} | {box_dict[9]}        |           7 | 8 | 9
             """)

def create_checks():
    # Rows
    row_1 = [box_dict[1], box_dict[2], box_dict[3]]
    row_2 = [box_dict[4], box_dict[5], box_dict[6]]
    row_3 = [box_dict[7], box_dict[8], box_dict[9]]

    # Columns
    col1 = [box_dict[1], box_dict[4], box_dict[7]]
    col2 = [box_dict[2], box_dict[5], box_dict[8]]
    col3 = [box_dict[3], box_dict[6], box_dict[9]]

    # Diagonals
    dia1 = [box_dict[1], box_dict[5], box_dict[9]]
    dia2 = [box_dict[3], box_dict[5], box_dict[7]]

    # Ways to win
    return  [row_1, row_2, row_3, col1, col2, col3, dia1, dia2]

def check_win():
    for way in ways_to_win:
        if (way[0] == way[1] == way[2]) and way[0] != " ":
            return way[0], "win"
    if not choices:
        return "", "draw"
    return "",False

def play_normal():
    global game_round, game_on, ways_to_win, choices
    while game_on:
        print_board()

        if game_round % 2 == 0:
            inp = input("Player1(O), please input number (1-9) : ")
            player = "O"
        else:
            inp = input("Player2(X), please input number (1-9) : ")
            player = "X"

        try:
            inp = int(inp)
            choices.remove(inp)
        except ValueError:
            print("Please input a number between 1 and 9.")
            continue

        if inp not in range(1, 10):
            print("Please input a number between 1 and 9.")
            continue
        if box_dict[inp] != " ":
            print("Sorry, that spot is already taken!")
            continue
        box_dict[inp] = player
        ways_to_win = create_checks()
        win = check_win()
        if win[1] == "win":
            print_board()
            print(f"Congrats!: {win[0]} won!")
            game_on = False
        elif win[1] == "draw":
            print_board()
            print("Draw!")
            game_on = False
        game_round += 1


def play_bot():
    global game_round, game_on, ways_to_win, choices
    while game_on:
        print_board()

        if game_round % 2 == 0:
            inp = input("Player1(O), please input number (1-9) : ")
            player = "O"
        else:
            time.sleep(3)
            inp = random.choice(choices)
            print(f"Bot(X), please input number (1-9) : {inp}")
            player = "X"

        try:
            inp = int(inp)
            choices.remove(inp)
        except ValueError:
            print("Please input a number between 1 and 9.")
            continue

        if inp not in range(1, 10):
            print("Please input a number between 1 and 9.")
            continue
        if box_dict[inp] != " ":
            print("Sorry, that spot is already taken!")
            continue
        box_dict[inp] = player
        ways_to_win = create_checks()
        win = check_win()
        if win[1] == "win":
            print_board()
            if win[0] == "O":
                print("Congrats! : You Won!")
            else:

                print("Bot Won: Game Over")
            game_on = False
        elif win[1] == "draw":
            print("Draw!")
            print_board()
            game_on = False
        game_round += 1

ways_to_win = create_checks()
game_on = True
game_round = 0
game_type = input("Enter 'bot' to play against a bot, or just ignore to play against a person: ").lower()

if game_type == "bot":
    play_bot()
else:
    play_normal()






