"""
Author: Nick
Date: September 25, 2024
Description: Program that calcuates distance of a line and prints it to the user.
"""

def distanceCalc(x1: float, y1: float, x2: float, y2: float):
    """
    Description:
        This function takes the coordinates obtained by the user and returns a distance.

    Args:
        x1: x of first coordinate pair
        y1: y of first coordinate pair
        y1: x of second coordinate pair
        x2: y of second coordinate pair
    
    Returns:
        newDistance: tuple containing new coordinate pair
    """

    # Perform the distance formula using square root
    newDistance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return newDistance

def infoPrint(x1: float, y1: float, x2: float, y2: float, distanceData): 
    """
    Description:
        This function takes all data and prints it out for the user.

    Args:
        x1: x of first coordinate pair
        y1: y of first coordinate pair
        y1: x of second coordinate pair
        x2: y of second coordinate pair
        distanceData: distance data obtained from the distanceCalc() function

    Returns:
        nothing
    """

    # Tell users what they provided
    print("The coordinates you provided are: ("+str(round(x1, 2))+", "+str(round(y1, 0))+"), ("+str(round(x2, 0))+", "+str(round(y2, 0))+").")
    
    # Add some decorative spacing then print the result
    print("- - -")
    print("The distance of the line is:", str(round(distanceData, 2)) + " units. Goodbye!")

def main():
    """
    Description:
        Mainline function for the calculator. 
        Responsable for executing the other calculator function and print function. 

    Returns:
        nothing
    """

    # Welcome the user!
    print("Welcome to the Distance Calculator!")
    
    # Use try/except to handle potential user input errors when someone inputs a non-numeric value. 
    try:
        # Getting the coordinates from the user
        x1 = float(input("Enter the x-coordinate of the first point: "))
        y1 = float(input("Enter the y-coordinate of the first point: "))
        x2 = float(input("Enter the x-coordinate of the second point: "))
        y2 = float(input("Enter the y-coordinate of the second point: "))
    except: 
        # If user submits invalid data such as text, catch it and tell the user and kill po
        print("An error has occured while gathering your numbers, ensure to use only float values!")
        return

    # Calculating the distance
    distanceValue = distanceCalc(x1, y1, x2, y2)

    # Print new distance
    infoPrint(x1, y1, x2, y2, distanceValue)
    
main()