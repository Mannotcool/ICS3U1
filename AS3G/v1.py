# create a Treasure Hunt Game
import random

def main():
    # Create a 5x5 grid with empty strings, randomize the location of the treasure (T), ($) is found treasure, "X" is used space but not treasure
    # there is no player just gather input column and row to find the treasure
    # there are 10 tries, 3 treasures

    print("Welcome to the Treasure Hunt Game!")
    print("Find the treasure ($) in the grid below.")   
    print("You have 10 tries to find 3 treasures.")

    board = [[" " for _ in range(5)] for _ in range(5)]
    print(board)

main()


    