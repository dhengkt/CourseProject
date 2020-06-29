# ConditionalTests
# HsinYu Chi(Katie)

# This module will examine
# conditional statements.

from math import*

def calcArea(a, b, c):

    s = (1/2) * (a + b + c)
    A = round(sqrt(s*(s-a)*(s-b)*(s-c)),2)
    return(A)

def main():

    x, y, z = eval(input("Enter sides: "))
    
    if (x + y) < z or (y + z) < x or (x + z) < y:
        print("These sides do not make triangle.")
        
    else:
        area = calcArea(x, y, z)
        print(area)

main()
