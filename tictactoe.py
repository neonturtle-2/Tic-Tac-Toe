import random
turn = random.randint(1,2)
gameDone = False
winnerFound = False
board = [
    "-" , "-", "-",
    "-" , "-", "-",
    "-" , "-", "-",
]
winConditions = (
    [0, 1, 2],
    [3, 4, 5],
    [6 ,7 ,8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
)
def resetBoard():
    global turn
    global gameDone
    global winnerFound
    global board
    turn = random.randint(1,2)
    gameDone = False
    winnerFound = False
    board = [
    "-" , "-", "-",
    "-" , "-", "-",
    "-" , "-", "-",
    ]
resetBoard()

def printBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def gameplay():
    global turn
    global gameDone
    global winnerFound
    global board
    while gameDone == False:
        try:
            if turn == 1:
                position = int(input("Player " + str(turn) + " (X), choose a position: "))
            elif turn == 2:
                position = int(input("Player " + str(turn) + " (O), choose a position: "))
        except ValueError:
            print("Please type in a number.")
            continue
        if position < 1 or position > 9:
            print("Position must be a number from 1 to 9, going from left to right and top to bottom.")
        elif board[position-1] == "X" or board[position-1] == "O":
            print("There is already a marker placed.")
        else:
            if turn == 1:
                board[position-1] = "X"
                turn = 2
            elif turn == 2:
                board[position-1] = "O"  
                turn = 1        
            for condition in winConditions:
                if board[condition[0]] != "-" and board[condition[0]] == board[condition[1]] == board[condition[2]]:
                    gameDone = True
                    if board[condition[0]] == "X":
                        print("X Won!")
                        winnerFound = True
                        break
                    elif board[condition[0]] == "O":
                        print("O Won!")
                        winnerFound = True
                        break
            if winnerFound == True:
                printBoard()
                break
            if not "-" in board:
                gameDone = True
                winnerFound = True
                print("The game was a draw.")
            printBoard()
    playagain = str(input("Would you like to play again? Y/N "))
    if playagain.upper() == "Y":
        resetBoard()
        printBoard()
        gameplay()
    elif playagain.upper() == "N":
        print("Thanks for playing!")

printBoard()
gameplay()