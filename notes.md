Spec:
    - [X] There are two players in the game (X and O)
    - [X] Players take turns until the game is over
    - [X] A player can claim a field if it is not already taken
    - [X] A turn ends when a player claims a field
    - [X] A player wins if they claim all the fields in a row, column or diagonal
    - [] A game is over if a player wins
    - [] A game is over when all fields are taken

Plan:
    - I need to work out what classes I need and what they will do:
        Player class?
        Game class?
        Turn class?
        Board class?

    - Game class would be responsible for ?
        *   Starting and ending the game, giving a winner
        *   Saying who's turn it is X or O
        *   Inputting a turn into the board
    
    - Turn class would be used for:
        *   the logic of changing turns, maybe using an array where [X,0] are switched
            then the first can be grabbed to get the player whos turn it is.
        *   maybe setting an variable like whos_turn = "X" or "O"

    - Player class
        *   Maybe not needed for this game, as a game starts with X and O everytime, so
        game could be responsible for initializing with player1 and player2
        *   Or player could have a name and a score attrribute, which is set as X and O and score as 0 at the start

    - Board class
        *   Easiest to do, just as a make board function which is done on initializing
        *   Can be made when a new game instance is made so new Game(new Board) etc.


Notes:
    - Currently I have a base of the app, whereby I have all the classes, but I now need to work on winning conditions
    - To be clean I think I will have them in another class that can be checked.
    - After each turn, it will call are winning conditions met.. etc
