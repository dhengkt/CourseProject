# Averages2
# Katie

# This program will ask the user to
# input scores until done, 
# and find the average.

def getInput():

    tempList = []
    score = 0
    
    while score > 0:
        score = eval(input("Enter score (use negative number to stop): "))
        if score > 0:
            tempList.append(score)
            
    return(tempList)

def findAvg(scores):

    m = len(scores)
    S = 0
    
    for i in range(m):
        S = S + scores[i]
        
    return(S/m)

#def OutputResult(A,x):

    

def main():
    
    scoreList = getInput()
    print(scoreList)
    #avg = findAvg(scoreList)
    #OutputResult(avg,len(scoreList))

main()
