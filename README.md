# Tictactoe rose tech test

## Specification
Build the business logic for a game of tic tac toe. It should be easy to implement a working game of tic tac toe by combining your code with any user interface, whether web or command line.

## Project in use
![image]()

#### Requirements
* There are two players in the game (X and O)
* Players take turns until the game is over
* A player can claim a field if it is not already taken
* A turn ends when a player claims a field
* A player wins if they claim all the fields in a row, column or diagonal
* A game is over if a player wins
* A game is over when all fields are taken

## How to use
* Clone this repo
* Ensure you have `python3` installed
* Run `pip install pytest` or `pip3 install pytest`
* Run tests with `pytest`

## Technologies used
* Python
* Pytest

## What I did
* My notes page [here](notes.md) outlines my stages of planning and what I did.
* Summarising, this involved working out what classes I would need and what their responsibilties are.
  * eg. the Turn Controller class, simply switches the players in an array and selects the first as the current turn player. Then the Player class, just contains initialization of a player with a name and score.


