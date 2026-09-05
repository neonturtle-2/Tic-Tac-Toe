import random

turn = random.randint(1, 2)
gameDone = False
winnerFound = False
boardString = ""
aiMemory = {}
moveScore = {}
gameHistory = []
winner = ""
XWins = 0
OWins = 0
Draws = 0
explorationChance = 20
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
    global XWins
    global OWins
    global Draws
    global explorationChance
    gameHistory = []
    while gameDone == False:
        if XWins + OWins + Draws % 1000 == 0 and explorationChance > 0:
            explorationChance -= 1
        if boardToString() not in aiMemory:
            moveScore = {}
            for location in possibleLocations:
                moveScore[location] = 0
            aiMemory[boardToString()] = moveScore
        gameHistory.append((boardToString(),))
        highestScore = float('-inf')
        bestMoves = []
        for move, score in aiMemory[boardToString()].items():
            if score > highestScore:
                bestMoves = [move]
                highestScore = score
            elif score == highestScore:
                bestMoves.append(move)
        if random.randint(0, 100) <= explorationChance:
            chosenLocation = random.choice(possibleLocations)
        else:
            chosenLocation = random.choice(bestMoves)
        gameHistory[-1] += (chosenLocation,)
        if turn == 1:
            board[chosenLocation - 1] = "X"
            turn = 2
        elif turn == 2:
            board[chosenLocation - 1] = "O"
            turn = 1
        possibleLocations.remove(chosenLocation)
        for condition in winConditions:
            if (
                board[condition[0]] != "-"
                and board[condition[0]] == board[condition[1]] == board[condition[2]]
            ):
                gameDone = True
                if board[condition[0]] == "X":
                    winnerFound = True
                    winner = "X"
                    XWins += 1
                    break
                elif board[condition[0]] == "O":
                    winnerFound = True
                    winner = "O"
                    OWins += 1
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
            break
        if not "-" in board:
            gameDone = True
            winnerFound = True
            Draws += 1

print("Training AI...")
print("Press Ctrl+C at any time to stop and generate a report.")
while True:
    try:
        resetBoard()
        gameplay()
    except KeyboardInterrupt:
        print("------------------------")
        print("Results:")
        print("X Wins: " + str(XWins))
        print("O Wins: " + str(OWins))
        print("Draws: " + str(Draws))
        print("Winrate: " + str(round((OWins) / (XWins + OWins + Draws) * 100, 2)) + " %")
        quit()