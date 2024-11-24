"""
    Author: Nick
    Date: November 5th, 2024
    Description: Choose your own adventure game that takes user input and guides them through a story.
"""

# Import the custom storyBookLib library
import storyBookLib 

# Import the os library to clear the screen
import os

def main():
    """
    Description:
        Mainline function for the game. 
        Responsable for running the story functions and gathering user input.

    Returns:
        nothing
    """
    # Clear the terminal screen
    os.system('clear')

    # Gather user details
    print("Welcome to the Mystical Island (or isle, however you want to say it). Let's personalize your journey.")
    name = input("Enter your name, traveler: ")

    # Get age and make sure it's a number
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please enter a valid number for your age.")

    # Clear the screen
    os.system('clear')
    # Customize the story for players over 60
    if age > 60:
        print("\nGreetings, " + name + ". Your years of wisdom might help you on this journey! You have been granted a walking staff.")
    else:
        print("\nWelcome, " + name + ". Your adventure begins now!")
        inventory = []

    print("\nYou must explore and find a way to escape. Where will you go? (there are 7 endings.)")
    print("TIP: You can type 'inventory' or 'i' to see what you're carrying during certain parts of the story.")

    # Start the story with the first prompt
    next_page = "ocean_shore"
    while next_page != "end":
        if next_page == "ocean_shore":
            next_page = storyBookLib.oceanShore(inventory)
        elif next_page == "forest_encounter":
            next_page = storyBookLib.forestEncounter(name, inventory)
        elif next_page == "river_crossing":
            next_page = storyBookLib.riverCrossing(inventory)
        elif next_page == "mysterious_clearing":
            next_page = storyBookLib.mysteriousClearing(inventory)
        elif next_page == "cave_shadows":
            next_page = storyBookLib.caveShadows(inventory)
        elif next_page == "mountain_peak":
            next_page = storyBookLib.mountainPeak(inventory)

# Run the mainline function
main()