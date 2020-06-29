# avg.py
# HsinYu Chi(Katie)

# This program to average two exam scores
# Illustrates use of multple inputs

def main():

    print("This program computes the average of two exam scores.")

    score1 = eval(input("Enter the first score: "))
    score2 = eval(input("Enter the second score: "))
    average = (score1 + score2) / 2

    print("The average of the score is:", average)

main()
