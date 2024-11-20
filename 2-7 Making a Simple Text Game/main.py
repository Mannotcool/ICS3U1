# Rock Paper Scissors
import random

def grabUserInput():
    x = "none"
    while x != "rock" and x != "paper" and x != "scissors":
        x = input("Enter your choice - Rock, Paper, or Scissors: ")
        x.lower()
        if x == "rock" or x == "paper" or x == "scissors":
            break
        else:
            print("Invalid input. Please enter rock, paper, or scissors.")
    return x

def calculateComputerChoice():
    computerChoice = random.randint(0, 2)
    if computerChoice == 0:
        computerChoice = "rock"
    elif computerChoice == 1:
        computerChoice = "paper"
    else:
        computerChoice = "scissors"
    return computerChoice

def calculateWinner(userChoice, computerChoice):
    if userChoice == computerChoice:
        return "It's a tie!"
    elif userChoice == "rock":
        if computerChoice == "paper":
            return "Computer wins!"
        else:
            return "You win!"
    elif userChoice == "paper":
        if computerChoice == "scissors":
            return "Computer wins!"
        else:
            return "You win!"
    elif userChoice == "scissors":
        if computerChoice == "rock":
            return "Computer wins!"
        else:
            return "You win!"



def main():
    print("Welcome to Rock, Paper, Scissors!")
    userChoice = grabUserInput()
    print("You chose: " + userChoice)

    # pick a random number between 0 and 2, where 0 is rock, 1 is paper, and 2 is scissors
    computerChoice = calculateComputerChoice()
    print("The computer chose: " + computerChoice)
    print(calculateWinner(userChoice, computerChoice))

    print("lets try again")



main()
