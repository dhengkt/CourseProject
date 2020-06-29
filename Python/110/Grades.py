# Grades
# HsinYu Chi(Katie)

# This program will assign leter grades,
# after getting an exam score as input.

def getInput():

    #x = round(eval(input("Enter your grade: ")),2)
    x = 82
    return(x)

def calcGrade(s):
    
    if s >= 90:
        grade = "A"
    elif s >= 80:
        grade = "B"
    elif s >= 70:
        grade = "C"
    elif s >=60:
        grade = "D"
    else:
        grade = "F"

    return(grade)

    

def main():

    score = getInput()
    letterGrade = calcGrade(score)
    print(letterGrade)
    #OutputResult(score,letterGrade)

main()
