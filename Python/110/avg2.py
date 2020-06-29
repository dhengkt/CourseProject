# avg2.py
# HsinYu Chi(Katie)

# This program to average two exam scores
# Illustrates use of multple input

def main():

    print("This program computes the average of two exam scores.")

    score1, score2 = eval(input("Enter two cores separated by a comma:"))
    average = (score1 + score2) / 2

    print("The average of the score is:", average)

main()
