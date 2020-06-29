# findSlope
# HsinYu Chi(Katie)

# This program finds slope of
# line between userentered points.

def getPoint():

    x, y = eval(input("Enter the point (seperate x and y by comma): "))
    return(x, y)

def findSlope(x1, y1, x2, y2):

    slope = (x2 - x1) / (y2 - y1)
    return(slope)

def OutputSlope(slope):

    print("The slope of this line is {0}.".format(slope))

def main():
    
    X1, Y1 = getPoint()
    X2, Y2 = getPoint()
    
    Slope = findSlope(X1, Y1, X2, Y2)

    OutputSlope(Slope)

main()
