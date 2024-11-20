import random

def winner(board):
    """This function checks for a winner in the Tic-Tac-Toe game.
    Returns 'X' if the user wins, 'O' if the computer wins, or "" if no winner."""
    
    # Check rows for winner
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != " ":
            return board[row][0]
    
    # Check columns for winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    
    # Check diagonal (top-left to bottom-right) for winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    
    # Check diagonal (bottom-left to top-right) for winner
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != " ":
        return board[2][0]
    
    return ""

def display_board(board):
    """Displays the Tic-Tac-Toe board with row and column labels."""
    print("   1   2   3")
    for i, row in enumerate(board, start=1):
        print(f"{i}: " + " | ".join(row))
        if i < 3:
            print("  ---+---+---")
    print()

def make_user_move(board):
    """Allows the user to make a move, with exception handling for invalid inputs."""
    valid_move = False
    while not valid_move:
        try:
            row = int(input("Enter the row (1-3): ")) - 1
            col = int(input("Enter the column (1-3): ")) - 1
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                board[row][col] = 'X'
                valid_move = True
            else:
                print("Invalid move. Please choose an empty square within the range!")
        except ValueError:
            print("Invalid input. Please enter numbers only for row and column.")

def make_computer_move(board):
    """Makes a random move for the computer or checks for winning/blocking moves."""
    

def main():
    """Main game loop for Tic-Tac-Toe."""
    free_cells = 9
    users_turn = True
    ttt_board = [[" " for _ in range(3)] for _ in range(3)]

    while winner(ttt_board) == "" and free_cells > 0:
        display_board(ttt_board)
        if users_turn:
            make_user_move(ttt_board)
            users_turn = not users_turn
        else:
            make_computer_move(ttt_board)
            users_turn = not users_turn
        free_cells -= 1

    display_board(ttt_board)
    if winner(ttt_board) == 'X':
        print("Y O U   W O N !")
    elif winner(ttt_board) == 'O':
        print("I   W O N !")
    else:
        print("S T A L E M A T E !")
    print("\n*** GAME OVER ***\n")

# Start the game!
main()