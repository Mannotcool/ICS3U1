# THERE ARE NO COMMENTS ON THIS FILE, PLEASE REFER TO v3.py FOR COMMENTS

"""
    Author: Nick S
    Date: November 23th, 2024
    Description: Treasure Hunt Game V1
"""

import random

def hide_treasure(board):
    treasures = 0
    while treasures < 3:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        if board[row][col] == " ":
            board[row][col] = "T"
            treasures += 1

def display_board(board, show_treasure):
    print("   0   1   2   3   4")
    for row in range(5):
        print(str(row) + ":", end=" ")
        for col in range(5):
            if show_treasure:
                print(board[row][col], end=" ")
                
            else:
                if board[row][col] == "T":
                    print(" ", end=" ")
                else:
                    print(board[row][col], end=" ")
            if col < 4:
                print("|", end=" ")
        print("\n  ---+---+---+---+---")
        
def make_user_move(board):
    """
        Allows the user to make a move on the board and checks if they have found a treasure.

        Args:
        board: 2D array containing the board

        Returns:
        boolean: True if the user has found a treasure, False otherwise
    """
    # Initialize variables
    row = -1
    col = -1
    valid_input = False

    # Input validation loop
    while not valid_input:
        try:
            # Get user input
            row = int(input("What row would you like to search (0-4): "))
            col = int(input("What col would you like to search (0-4): "))

            # Validate the row and column
            if row < 0 or row > 4 or col < 0 or col > 4:
                print("Invalid row or column. Please enter a row and column between 0 and 4.")
            elif board[row][col] in ("X", "$"):
                print("You already looked there. Please enter a new row and column.")
            else:
                valid_input = True
        except ValueError:
            print("Please enter a valid number for the row and column.")

    # Process the move after valid input
    if board[row][col] == "T":
        print("Nice! You found a treasure!")
        board[row][col] = "$"
        return True
    else:
        print("Nothing there.")
        board[row][col] = "X"
        return False

def main():
    print("Welcome to the Treasure Hunt Game!")
    print("Find the treasure ($) in the grid below. You have 10 tries to find 3 treasures.")

    tries = 0
    treasures_found = 0

    board = [[" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]]
    hide_treasure(board)
    print("You have 10 tries left, and have found 0/3 treasures.\n")

    while tries < 10 and treasures_found < 3:
        display_board(board, True)
        if make_user_move(board):
            treasures_found += 1
        tries += 1
        print("You have", str(10 - tries), "tries left, and have found", str(treasures_found) + "/3 treasures.\n")
    
    if treasures_found == 3:
        print("Congratulations! You found all the treasures!")
    else:
        print("Oh no! You only found", str(treasures_found) + "/3 treasures. Better luck next time!")
        display_board(board, True)

    print("*** GAME OVER ***")

main()