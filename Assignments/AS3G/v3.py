"""
    Author: Nick S
    Date: November 23th, 2024
    Description: Treasure Hunt Game V3
"""
# Used for randomly placing treasures
import random

# Extra, used to hide the already handled traceback errors.
import sys

def hide_treasure(board: list):
    """
        Description:
        This function hides 3 treasures in the board randomly.
        
        Args:
        board: 2D array containing the board

        Returns:
        nothing
    """
    # Get the number of rows and columns
    rows = len(board)
    cols = len(board[0])

    # Running count of treasures
    treasures = 0

    # Hide 3 treasures in the board randomly
    while treasures < 3:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if board[row][col] == " ":
            board[row][col] = "T"
            treasures += 1

def display_board(board: list, show_treasure: bool):
    """
        Description:
        This function displays the board to the user, showing the treasures if show_treasure is true.

        Args:
        board: 2D array containing the board
        show_treasure: boolean value to show the treasures

        Returns:
        nothing
    """

    # Get the number of rows and columns
    rows = len(board)
    cols = len(board[0])

    # Print column numbers at the top, first add some spacing
    print("   ", end="")
    for col in range(cols):
        # then print the column number, and add some spacing between them
        print(str(col) + "   ", end="")
    
    print()

    # Now create the rows
    for row in range(rows):
        # Print row number at the left
        print(str(row) + ":", end=" ")

        # Print the contents of the board
        for col in range(cols):
            if show_treasure:
                print(board[row][col], end=" ")
            else:
                if board[row][col] == "T":
                    print(" ", end=" ")
                else:
                    print(board[row][col], end=" ")
            
            # Print the vertical lines between the columns
            if col < cols - 1:
                print("|", end=" ")
        # Print the crosses between the rows
        print("\n  " + "+".join(["---"] * cols))

        
def make_user_move(board: list) -> bool:
    """
        Description:
        This function allows the user to make a move on the board, and checks if they have found a treasure.

        Args:
        board: 2D array containing the board

        Returns:
        boolean: True if the user has found a treasure, False otherwise
    """
    # Get a count of the rows and columns
    rows = len(board)
    cols = len(board[0])

    # Initialize variables for row and column
    row = -1
    col = -1

    # Input handling in a separate try-except block
    while True:
        try:
            # Get the row and column from the user
            row = int(input("What row would you like to search (0-" + str(rows - 1) + "): "))
            col = int(input("What col would you like to search (0-" + str(cols - 1) + "): "))

            # Validate the row and column input
            if row < 0 or row >= rows or col < 0 or col >= cols:
                print("Invalid row or column. Please enter a row and column between 0 and " + str(rows - 1) + ".")

                # Continue the loop if the input is invalid
                continue
            
            # Check if row -> col contains any non-empty spots.
            if board[row][col] in ("X", "$", "!"):
                print("You already looked there. Please enter a new row and column.")

                # Continue the loop if the input is invalid
                continue

            # Break the loop when valid input is provided
            break

        # Catch any non-numeric input
        except ValueError:
            print("Please enter a valid number for the row and column.")

    # Check if the user found a treasure
    if board[row][col] == "T":
        print("Nice! You found a treasure!")
        board[row][col] = "$"
        return True
    else:
        # Scan the surrounding area for treasures
        hide_treasure_nearby = False

        # Check adjacent cells
        if row > 0 and board[row - 1][col] == "T":
            hide_treasure_nearby = True
        if row < rows - 1 and board[row + 1][col] == "T":
            hide_treasure_nearby = True
        if col > 0 and board[row][col - 1] == "T":
            hide_treasure_nearby = True
        if col < cols - 1 and board[row][col + 1] == "T":
            hide_treasure_nearby = True

        # Check diagonal cells
        if row > 0 and col > 0 and board[row - 1][col - 1] == "T":
            hide_treasure_nearby = True
        if row > 0 and col < cols - 1 and board[row - 1][col + 1] == "T":
            hide_treasure_nearby = True
        if row < rows - 1 and col > 0 and board[row + 1][col - 1] == "T":
            hide_treasure_nearby = True
        if row < rows - 1 and col < cols - 1 and board[row + 1][col + 1] == "T":
            hide_treasure_nearby = True

        # Respond based on proximity to treasure
        if not hide_treasure_nearby:
            print("Nothing there.")
            board[row][col] = "X"
            return False
        else:
            print("You are close to a treasure!")
            board[row][col] = "!"
            return False
        
def main():
    """
        Description:
        Mainline function for the Treasure Hunt Game.
        Responsible for executing the other game functions and displaying the game to the user.

        Returns:
        nothing
    """

    # Initialize variables
    tries = 0
    treasures_found = 0
    rows_amount = 0
    cols_amount = 0

    # Welcome the user to the game
    print("Welcome to the Treasure Hunt Game!")
    print("Find the treasure ($) in the grid below. You have 10 tries to find 3 treasures.")

    # Part of verion 3, ask the user for the number of rows and columns
    try:
        # Get the number of rows and columns from the user
        rows_amount = int(input("Enter the number of rows between 3 and 10: "))
        cols_amount = int(input("Enter the number of columns 3 and 10: "))

        # Make sure the user enters a valid number of rows and columns
        while rows_amount < 3 or rows_amount > 10 or cols_amount < 3 or cols_amount > 10:
            print("Invalid number of rows or columns. Please enter a number between 3 and 10.")
            rows_amount = int(input("Enter the number of rows between 3 and 10: "))
            cols_amount = int(input("Enter the number of columns 3 and 10: "))

    # If the user enters a non-numeric value, catch it and tell the user to enter a valid number
    except ValueError:
        print("Please enter a valid number for the rows and columns.")
        main()

    print()

    # Create a board with the user's specified rows and columns
    board = []
    for _ in range(rows_amount):
        board.append([" "] * cols_amount)
    
    # Hide the treasures in the board
    hide_treasure(board)

    print("You have 10 tries left, and have found 0/3 treasures.\n")

    # Loop through the game until the user has found all the treasures or has run out of tries
    while tries < 10 and treasures_found < 3:
        display_board(board, False)
        if make_user_move(board):
            treasures_found += 1
        tries += 1
        print("You have", str(10 - tries), "tries left, and have found", str(treasures_found) + "/3 treasures.\n")
    
    # Display the final message to the user
    if treasures_found == 3:
        print("Congratulations! You found all the treasures!")
    else:
        print("Oh no! You only found", str(treasures_found) + "/3 treasures. Better luck next time!")
        display_board(board, True)

    print("*** GAME OVER ***")
    sys.exit(0) # Exit the program without any tracebacks because I have already handled the errors

# Call the mainline function
main()