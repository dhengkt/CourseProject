# Mastermind
# HsinYu Chi(Katie)

# This program

def getSecretCode():

    secretcode = ['b', 'o', 'p', 'o']
    
    return(secretcode)

def getGuess():

    guess = input("Enter a guess: ")
    

    return(guess)

def testGuess(ocode,sc):

    tempguess = []
    tempscode = []
    for i in range(4):
        tempguess.append(ocode[i])
        tempscode.append(sc[i])

    # Find black.
    for i in range(4):
        if tempguess[i] == tempscode[i]:
            tempguess[i] = "BK"

            tempscode[i] = "BK"
    # Find white.        
    for i in range(4):
        if tempguess[i] != "BK":
            for j in range(4):
                if tempguess[i] == tempscode[j]:
                    tempguess[i] = "WT"

    # Count black and white.
    black = tempguess.count("BK")
    white = tempguess.count("WT")
            
    return(black,white)

def oneTurn(sc):

    

def main():

    Secretcode = getSecretCode()
    Guess = getGuess()
    Black, White = testGuess(Guess,Secretcode)


main()
