# Averages
# Katie

# This program will ask the user to
# input number of scores, then the
# scores and find the average.

def getInput():

    n = eval(input("Enter the number of scores: "))
    tempList = []
    
    for i in range(n):
        score = eval(input("Enter score: "))
        tempList.append(score)
    return(tempList)

def findAvg(scores):

    m = len(scores)
    S = 0
    
    for i in range(m):
        S = S + scores[i]
        
    return(S/m)

def OutputResult(A,x):

    

def main():
    
    scoreList = getInput()
    avg = findAvg(scoreList)
    OutputResult(avg,len(scoreList))

main()
