# Tic-Tac-Toe
A project on creating an AI that would learn how to play the game of tic-tac-toe from scratch. Started on August 29, 2026 and finished on September 5, 2026.
## What I built
An actual game of tic-tac-toe and an AI that would learn how to play the game using the programming language Python.
## How It Works
### Tic-Tac-Toe
The board is represented as a list, with empty strings for blank spots and either an X or O depending on what is placed. When displaying the board, it is formatted using dashes and pipes to visually see what the board looks like.
### The AI
The AI uses **reinforcement learning** to understand what moves it should make when playing the game. It does this by giving each move a starting score value of 0 and increasing or decreasing the value by a certain amount depending on whether it lost or won. The magnitude of the score change is determined whether the move was made later on in the game (which is larger due to the move possibly determining a win or loss) or in the beginning (which is smaller due to not affecting the game's outcome as much). The AI utilizes exploration and exploitation to maintain a balance of using what it knows vs. exploring unknown outcomes and eventually favors more towards its knowledge as training progresses.
## Libraries Used
  - ***random*** **module:** used for randomly picking whose turn it is at the beginning of a game and whether the AI should use exploration or exploitation.
## Results
I made **three** different python files:
  - [tictactoe.py](tictactoe.py): A working python version of tic-tac-toe with no AI functions, but allows two humans to play.
  - [tictactoe_randomai.py](tictactoe_randomai.py): Adds an AI that a human plays against. The AI plays as "O" and slowly learns how to play as more games are run.
  - [tictactoe_trainingai.py](tictactoe_trainingai.py): Makes two AIs play tic tac toe against each other, but the AI playing as "O" is the one actually learning.
## What I Learned
From this project, I grew my Python and coding skills and learned the basics of machine learning. I learned how to use lists and dictionaries as well as how to manipulate them to make the AI's "brain", global vs local variables, and the *random* module. I learned about reinforcement learning, why it works, and how to implement it in Python. I also strengthened my skills with the for loop and my debugging skills, which were greatly tested with the many errors and failed outcomes of my projects.
