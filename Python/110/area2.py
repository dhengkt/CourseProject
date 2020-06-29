# area.py
# Katie.C

# This program calculates the semiperimeter
# and use it to find the triangle's area.

from math import*

def main():
    
    # Get the three sides of a triangle from user.
    a,b,c=eval(input("Enter the three side of a triangle, separated by commas: "))

    if a+b>c and b+c>a and a+c>b:
        
        # Calculates the semi-perimeter and area.
        S = (1/2) * (a + b + c)
        A = round(sqrt(S*(S-a)*(S-b)*(S-c)),2)

        # Output the area of a triangle
        print("The area of this triangle is",A)

    else:
        #Tell the user there is an error
        print("This is not a triangle.")
    
main()
