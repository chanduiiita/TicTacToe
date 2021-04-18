board = []
for i in range (1,10):
    board.append(str(i))

def display_board():
    for i in range (0,3):
        for j in range (0,3):
            print("===",end=" ")
        print()
        for j in range (0,3):
            print("|" + board[3*i+j] + "|", end=" ")
        print()
    for i in range (0,3):
        print("===",end=" ")
    print()
    print("Turn of player " + str(turn+1) + " Please enter a number")

GAME_OVER = 0
turn = 0
sign = ["X","O"]

def valid(x):
    if x not in range (1,10):
        return 0
    elif board[x-1] not in ["1","2","3","4","5","6","7","8","9"]:
        return 0
    else:
        return 1

def change():
    global turn
    turn = (turn + 1)%2

def check():
    global GAME_OVER
    for i in range (0,3):
        flag = 1
        for j in range (0,3):
            if board[i*3+j] != board[i*3]:
                flag=0
        if flag == 1:
            print("Player " + str(turn+1) + " wins")
            GAME_OVER = 1
            return

    for j in range (0,3):
        flag = 1
        for i in range (0,3):
            if board[i*3+j] != board[j]:
                flag=0
        if flag == 1:
            print("Player " + str(turn + 1) + " wins")
            GAME_OVER = 1
            return
    flag=1
    for j in range (0,3):
        if board[j*4] != board[0]:
            flag=0
    if flag == 1:
        print("Player " + str(turn+1) + " wins")
        GAME_OVER = 1
    flag=1
    for j in range (0,3):
        if board[(j+1)*2] != board[2]:
            flag = 0
    if flag == 1:
        print("Player " + str(turn+1) + " wins")
        GAME_OVER = 1
    flag = 1
    for i in range(0, 9):
        if board[i] not in ["X", "O"]:
            flag = 0
    if flag == 1:
        GAME_OVER = 1
        print("Its a draw")
        return


def TicTacToe():
    while GAME_OVER == 0:
        display_board()
        x = int(input())
        while valid(x) != 1:
            x = int(input("Invalid input, Please try again"))
        board[x-1] = sign[turn]
        check()
        change()

TicTacToe()


