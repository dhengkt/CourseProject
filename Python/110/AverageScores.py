# AverageScores
# HsinYu Chi(Katie)

# Use a function to find the average
# first of three exams scores, then
# of three projects.

def getInput1():

    return(85, 90, 100)

def getInput2():

    return(26, 52, 107)

def getAverage(x, y, z):

    avg = (x + y + z) / 3
    return(avg)

def OutputResults(a, b):

    print("The exam average is {0} and "
          "the project average is {1}."
          .format(round(a,2), round(b,2)))

def main():

    Ex1, Ex2, Ex3 = getInput1()
    P1, P2, P3 = getInput2()

    ExAvg = getAverage(Ex1, Ex2, Ex3)
    PAvg = getAverage(P1, P2, P3)

    OutputResults(ExAvg, PAvg)

main()
