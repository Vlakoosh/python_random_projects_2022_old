# print board                   X
# take input for player         X
# make sure tile isn't taken    X
# switch turns                  X
# check for winner              X
# check for tie                 X
# reset board                   X
# count score                   X

#  1 2 3
#1|X|O|O|
#2|X|X|O|
#3|X|X|O|
#
#Player # enter your move: 

import os

current_player = "O"
game = True

board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

def reset_board():
    global board
    board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

def clear():
    os.system('CLS')

def print_board():
    print("  1 2 3")
    for row in range(3):
        print(f"{row+1}|", end="")
        for column in range(3):
            print(f"{board[row][column]}|",end="")
        print("\n")

def get_move():
    global current_player
    
    move = input(f"Player ({current_player}) enter your move in 'x,y' format or 'quit': ")
    
    while move != 'quit' and board[int(move[2])-1][int(move[0])-1] != "-":
        clear()
        print_board()
        print("Tile already taken by a player")
        move = input(f"Player ({current_player}) enter your move in 'x,y' format or 'quit': ")
    if move == 'quit':
        quit()
    board[int(move[2])-1][int(move[0])-1] = current_player
   

def check_for_winner():
    for row in range(3):
        if board[row-1][0] == board[row-1][1] == board[row-1][2]:
            if board[row-1][0] != "-":
                return board[row-1][0]
        elif board[0][row-1] == board[1][row-1] == board[2][row-1]:
            if board[0][row-1] != '-':
                return board[0][row-1]
    if board[0][0] == board[1][1] == board[2][2]:
        if board[1][1] != '-':
            return board[0][0]
    if board[2][0] == board[1][1] == board[0][2]:
        if board[1][1] != '-':
            return board[2][0]


def check_for_tie():
    count = 0
    for row in range(3):
        for column in range(3):
            if board[row-1][column-1] != '-':
                count += 1
            if count == 9:
                return True


def change_player():
    global current_player
    if current_player == "O":
        current_player = "X"
    else:
        current_player = "O"

print_board()

while game:
    status = None
    #clear screen
    #print board
    #check for winner
    #if no winner ask for move
    
    clear()
    print_board()
    
    #check for winner
    status = check_for_winner()
    
    #if there is no winner and all tiles are taken, reset the game
    if not status and check_for_tie():
        print("There is a tie")
        input("Press enter to continue: ")
        reset_board()
        change_player()
        continue
    
    if status:
        print(f"Player {status} has won!")
        input("Press enter to continue: ")
        current_player = status
        reset_board()
    else:
        get_move()

    change_player()