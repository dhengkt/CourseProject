# Random function
# HsinYu Chi(Katie)

# This program will generate a random list
# find the average, maximum and minimum values
# of the list, and output the results.

from random import*

def getInput():

    n = eval(input("Enter a number between 10 to 50: "))
    numList = []
    for i in range(n):
        t = randrange(50,101)
        numList.append(t)
    return(numList)

def averageList(List):

    l = len(List)
    S = 0

    for i in range(l):
        S = S + List[i]    
    return(round(S/l,2))

def findmax(numList):

    j = len(numList)
    Max = numList[0]
    for i in range(j):
        if Max < numList[i]:
            Max = numList[i]
    return(Max)

def findmin(nList):

    k = len(nList)
    Min = nList[0]
    for i in range(k):
        if Min > nList[i]:
            Min = nList[i]
    return(Min)

def OutputResults(L,Avg,a,b):

    print("The random list is {0}, the average is {1}, "
          "the maximum is {2}, and the minimum is {3}.".format(L,Avg,a,b))
    
def main():

    rList = getInput()
    avg = averageList(rList)
    M = findmax(rList)
    m = findmin(rList)
    OutputResults(rList, avg, M, m)

main()
