# sum_n.py
# HsinYu Chi(Katie)

# This program will use a loop
# to find the sum of the first n number.

def main():

    #Get the number n from user.
    n = eval(input("Enter a natural number of n: "))

    #Calculates the sum of n.
    total = 0
    for i in range(n):
        total = total + (i+1)

    #Out put the result.    
    print("The total of n is ",total,".",sep="")

main()
