from math import *
def main():
    
    R = eval(input("Enter the radius of a circle: "))
    C = round(2 * pi * R,2)
    A = round(pi * (R ** 2),2)
    print("The circumference is", C, "and the area is", A, end=".")

main()
