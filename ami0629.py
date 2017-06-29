import os
import random

EMPTY_BOARD = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

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

red = '\033[31mO\033[0m'
blue = '\033[94mX\033[0m'

def player_move(board, player, index):
    board[index] = player
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

def start_game():
    players = [red, blue]
    act_player = players[random.randint(0,1)]
    os.system("clear")
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    draw_board(board)
    print("\033[1;36mWelcome to\033[0m \033[1;31mSarcasTic\033[0m \033[1;32mTac\033[0m \033[1;33mToe!\033[0m")
    print()
    print(act_player + " \033[1;36mstarts!\033[0m")
    print()
    game_on = True
    while game_on:
        
        try:
            userinput = get_input_from_user(board)
            board = player_move(board, act_player, userinput)
            os.system('clear')        
            draw_board(board)

            if winning(board, act_player):
                print("\033[1;33mCongratulations " + act_player + "\033[1;33m, you won.\033[0m \033[1;30mNow go outside.\033[0m")
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
    while True:
        start_game()
        while True:
            answer = input('Run again? (y/n): ')
            if answer in ('y', 'n'):
                break
            print('Invalid input.')
        if answer == 'y':
            continue
        else:
            print('Goodbye')
            break

#This is the game right here:
main()
