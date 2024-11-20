import grading # do this

def main():
    # Get the test scores from the user
    score1 = int(input("Enter the first test score: "))
    score2 = int(input("Enter the second test score: "))
    score3 = int(input("Enter the third test score: "))
    score4 = int(input("Enter the fourth test score: "))
    score5 = int(input("Enter the fifth test score: "))

    # Calculate the average of the test scores
    average = grading.calcAverage(score1, score2, score3, score4, score5)

    # Determine the letter grade based on the average
    grade = grading.determineGrade(average)

    # Print the average and the letter grade
    print("The average of the test scores is:", average)
    print("The letter grade is:", grade)

main()