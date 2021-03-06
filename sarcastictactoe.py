import os
import random
import time

red = '\033[31mO\033[0m'
blue = '\033[94mX\033[0m'
player_list = {}

def draw_board(board):
    print('      |     |      ')
    print('   ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] + '   ')
    print('      |     |      ')
    print('-------------------')
    print('      |     |      ')
    print('   ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] + '   ')
    print('      |     |      ')
    print('-------------------')
    print('      |     |      ')
    print('   ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] + '   ')
    print('      |     |      ')
    print()


def player_move(board, player, index):
    board[index] = player
    return board

def ai_input(board):
    while True:
        for i in range(1,len(board)):
            if board[i] != red and board[i] != blue:
                n = random.randint(1,9)    
                if board[n] == '\033[94mX\033[0m' or board[n] == '\033[31mO\033[0m':
                    continue
                else:
                    print(n)
                    return n   
    

def ai_move(board, ai, index):
    board[index] = ai
    return board

def get_input_from_user(board):
    while True:
        try:
            inputint = int(input("\033[1;36mEnter a number between 1 and 9: \033[0m"))
            if inputint > 9 or inputint < 1:
                print("\033[1;35mYou're special aren't you?\033[0m")
                continue

            if board[inputint] == '\033[94mX\033[0m' or board[inputint] == '\033[31mO\033[0m':
                print("\033[1;36mThat slot is taken. Please,choose another one!\033[0m")

            else:
                return inputint

        except ValueError:
            print("\033[1;35mWhich part of 'number' you didn't understand?...\033[0m")
            
def winning(board, char):
    return((board[1] == char and board[2] == char and board[3] == char) or
    (board[4] == char and board[5] == char and board[6] == char) or
    (board[7] == char and board[8] == char and board[9] == char) or
    (board[1] == char and board[4] == char and board[7] == char) or
    (board[2] == char and board[5] == char and board[8] == char) or
    (board[3] == char and board[6] == char and board[9] == char) or
    (board[1] == char and board[5] == char and board[9] == char) or
    (board[3] == char and board[5] == char and board[7] == char))

def board_full(board):
    for i in range(1,len(board)):
        if board[i] != red and board[i] != blue:
            return False
    return True

def add_player(player_list, name):
    if name in player_list:
        return
    else:
        player_list[name] = 0

def player_selection(red, blue):
    global player_list
    first_player = input("Enter player who will be " + blue + ": ")
    add_player(player_list, first_player)
    global first_player
    print(blue + " is " + first_player + "!")
    second_player = input("Enter player who will be " + red + ": ")
    add_player(player_list, second_player)
    global second_player
    print(red + " is " + second_player + "!")
    return blue

def start_game():
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    draw_board(board)
    print("\033[1;36mWelcome to\033[0m \033[1;31mSarcasTic\033[0m \033[1;32mTac\033[0m \033[1;33mToe!\033[0m")
    print()
    answer = input("Would you like to play against the computer? Yes or No: ")
    if answer == "No":
        return two_players()
    elif answer == "Yes":
        return one_player()

def one_player():
    act_player = blue
    ai = red
    print(act_player + " \033[1;36mstarts!\033[0m")
    print()
    time.sleep(1)    
    game_on = True
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while game_on:
        
        try:
            os.system("clear")
            draw_board(board)
            userinput = get_input_from_user(board)
            board = player_move(board, act_player, userinput) 
            draw_board(board)
            os.system('clear')
            time.sleep(0.5)
            draw_board(board)
            n = ai_input(board)
            board = ai_move(board, ai, n)
            draw_board(board)
            os.system("clear")
            if board_full(board) == True:
                print("\033[1;35mBored, huh?...\033[0m")
                game_on = False
            elif winning(board, ai):
                print("Beaten... lol..")
                game_on = False
            elif winning(board, act_player):
                print("\033[1;33mCongratulations " + act_player + "\033[1;33m, you won.\033[0m \033[1;30mNow go outside.\033[0m")
                print()
                game_on = False
            else:
                game_on = True

            if act_player == blue:
                ai = red

        except KeyboardInterrupt:
            print("\033[1;31mAlright, where's the fire? Exiting...\033[0m")    
            exit()


def two_players():
    act_player = player_selection(red, blue)
    os.system("clear")
    print(act_player + " \033[1;36mstarts!\033[0m")
    print()
    game_on = True
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while game_on:
        
        try:
            draw_board(board)
            userinput = get_input_from_user(board)
            board = player_move(board, act_player, userinput) 
            draw_board(board)
            os.system('clear')  
            if winning(board, act_player):
                if act_player == red:
                    player_list[second_player] += 1
                elif act_player == blue:
                    player_list[first_player] += 1
                print("\033[1;33mCongratulations " + act_player + "\033[1;33m, you won.\033[0m \033[1;30mNow go outside.\033[0m")
                print()
                print("The scores are: ")
                for name, score in player_list.items():
                    print(str(name) + ": " + str(score))
                game_on = False
            elif board_full(board) == True:
                print("\033[1;35mBored, huh?...\033[0m")
                game_on = False
            else:
                game_on = True

            if act_player == red:
                act_player = blue
            else:
                act_player = red

        except KeyboardInterrupt:
            print("\033[1;31mAlright, where's the fire? Exiting...\033[0m")    
            exit()

def main():
    try:
        os.system("clear")
        start_game()
        while True:
            start_game()
            while True:
                answer = input('Waste more time? (y/n): ')
                if answer in ('y', 'n'):
                    break
                print('Sigh....')
            if answer == 'y':
                continue
            else:
                print('Do something productive...')
                time.sleep(1)
                os.system("clear")
                break
    # elif False:
    #    two_player()
    except KeyboardInterrupt:
        print("I guess you have more important things to do huh...")
        time.sleep(1)
        os.system("clear")
        exit()

#This is the game right here:
main()
