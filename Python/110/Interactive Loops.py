# Interactive Loops
# Katie

# Program to look at types of loop structures.

def main():

    #initialize the variable
    x = 0
    total = 0

    while x >= 0:
        
        total = total + x    
        x = eval(input("Enter score (use neg. to quit): "))

    print("The total is", total, end=".")
    

main()
