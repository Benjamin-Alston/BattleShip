# BattleShip
A python script that uses the tkinter library


# Features and Functionality
battleship() will in open up two windows.

The Command Room is where the user will place his or her ships and will reflect the AI's guesses.  To place one of the five ships on the board, begin by choosing a square on the grid.  The ship will be anchored in this square and the user will have to choose a direction for the rest of the ship to be placed (UP, DOWN, LEFT, RIGHT).  The viable directions will be printed to the shell. The user will type in a direction and the ship will be placed on the grid.  As the game progresses and the AI guesses, the squares will change to a blue X if there is no ship present and to a red X if one of the user's ships has been hit.  If a ship has been sunk, a message will appear in the shell.

The Radar window is where the user will guess where the enemy ships are. Click to choose a space on the grid. A miss will appear as a blue X, and a hit will appear as a red X.  If a ship is sunk, a message will appear in the shell.

# Limitations
This is the first iteration of the project, so there are a few limitations.
-There is currently no AI. The AI will simply guess a space to hit.
-The functionality for placing the user's ship does not take into consideration if another one of the user's ships is in the path it is considering. (addressed in 12192017battleship)
# What's Next for this Project
Besides addressing the limitations, my next goal is to eliminate use of the shell entirely.

# December 2, 2017
I began work on this project at the Local Hack Day 2017 event on the University of Iowa campus. That day, I worked on the project to its current state.  At the end of the day, I presented the program to the rest of the hackers. The entire conferenced voted on their favorite project, and I got Third Place.
# December 19, 2017
Spent 2 hours updating the placeYourShips() method
