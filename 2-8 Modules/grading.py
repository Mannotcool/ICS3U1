def calcAverage(score1, score2, score3, score4, score5):
    """
    Description:
        Takes 5 tests scores and returns the average of them.

    Args:
        score1: first test score
        score2: second test score
        score3: third test score
        score4: fourth test score
        score5: fifth test score
    
    Returns:
        average: average of the test scores
    """

    average = (score1 + score2 + score3 + score4 + score5) / 5
    return average

def determineGrade(score):
    """
    Description:
        Takes the test score from the user and returns a letter grade.

    Args:
        score: test score
    
    Returns:
        grade: letter grade
    """
    # Determine the grade based on the score
    if score >= 90:
        grade = "A"
        if score % 10 >= 5:
            grade += "+"
        elif score % 10 <= 4:
            grade += "-"
    elif score >= 80:
        grade = "B"
        if score % 10 >= 5:
            grade += "+"
        elif score % 10 <= 4:
            grade += "-"
    elif score >= 70:
        grade = "C"
        if score % 10 >= 5:
            grade += "+"
        elif score % 10 <= 4:
            grade += "-"
    elif score >= 60:
        grade = "D"
        if score % 10 >= 5:
            grade += "+"
        elif score % 10 <= 4:
            grade += "-"
    else:
        grade = "F"
    return grade