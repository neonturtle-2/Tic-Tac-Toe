import random

turn = random.randint(1, 2)
gameDone = False
winnerFound = False
boardString = ""
aiMemory = {}
moveScore = {}
gameHistory = []
winner = ""
board = [
    "-",
    "-",
    "-",
    "-",
    "-",
    "-",
    "-",
    "-",
    "-",
]
possibleLocations = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
]
winConditions = (
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
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
    global winner
    global possibleLocations
    turn = random.randint(1, 2)
    gameDone = False
    winnerFound = False
    winner = ""
    board = [
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
        "-",
    ]
    possibleLocations = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
    ]


def printBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


def boardToString():
    boardString = "".join(board)
    return boardString


def gameplay():
    global turn
    global gameDone
    global winnerFound
    global board
    global possibleLocations
    global moveScore
    global winner
    global gameHistory
    gameHistory = []
    while gameDone == False:
        if boardToString() not in aiMemory:
            moveScore = {}
            for location in possibleLocations:
                moveScore[location] = 0
            aiMemory[boardToString()] = moveScore
        if turn == 1:
            try:
                position = int(input("Player 1 (X), choose a position: "))
            except ValueError:
                print("Please type in a number.")
                continue
            if position < 1 or position > 9:
                print(
                    "Position must be a number from 1 to 9, going from left to right and top to bottom."
                )
            elif board[position - 1] == "X" or board[position - 1] == "O":
                print("There is already a marker placed.")
            else:
                board[position - 1] = "X"
                possibleLocations.remove(position)
                turn = 2
        elif turn == 2:
            gameHistory.append((boardToString(),))
            highestScore = float('-inf')
            bestMoves = []
            print(aiMemory)
            for move, score in aiMemory[boardToString()].items():
                if score > highestScore:
                    bestMoves = [move]
                    highestScore = score
                elif score == highestScore:
                    bestMoves.append(move)
            if random.randint(0, 100) <= 20:
                chosenLocation = random.choice(possibleLocations)
            else:
                chosenLocation = random.choice(bestMoves)
            gameHistory[-1] += (chosenLocation,)
            board[chosenLocation - 1] = "O"
            possibleLocations.remove(chosenLocation)
            turn = 1
        for condition in winConditions:
            if (
                board[condition[0]] != "-"
                and board[condition[0]] == board[condition[1]] == board[condition[2]]
            ):
                gameDone = True
                if board[condition[0]] == "X":
                    print("X Won!")
                    winnerFound = True
                    winner = "X"
                    break
                elif board[condition[0]] == "O":
                    print("O Won!")
                    winnerFound = True
                    winner = "O"
                    break
        if winnerFound == True:
            incrementCount = 0.6
            for history in reversed(gameHistory):
                if winner == "O":
                    aiMemory[history[0]][history[1]] = round(
                        aiMemory[history[0]][history[1]] + incrementCount, 2
                    )
                elif winner == "X":
                    aiMemory[history[0]][history[1]] = round(
                        aiMemory[history[0]][history[1]] - incrementCount, 2
                    )
                incrementCount = round(incrementCount - 0.1, 1)
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


resetBoard()
printBoard()
gameplay()
