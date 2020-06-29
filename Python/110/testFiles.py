# testFiles
# Katie

# This program is designed
# to test opening and readind
# from a file.

def main():

    inFile=open("MathClasses.txt","r")
    
    newData = inFile.readline()
    print(newData)

main()
