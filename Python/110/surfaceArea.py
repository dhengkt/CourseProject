# surfaceArea
# HsinYu Chi(Katie)

# This program will (use functions) to
# get the dimension of a rectangular box
# as input and find it's surface area.

def getDims():

    l,w,h = eval(input("Enter box's dimensions, seperated by commas: "))
    return(l,w,h)

def calc(length, width, height):

    area = 2 * (length * width + length * height + width * height)
    volume = length * width * height
    return(area,volume)

def outputResults(l,w,h,a,v):

    print("The box with dimensions "
          "%d x %d x %d has surface area %d "
          "and volume %d."%(l,w,h,a,v))

def main():

    print("This program will find the surface area "
          "and volume of a box, given its dimensions.\n")
    
    for i in range(2):
        
        L, W, H = getDims() 
        SA, V = calc(L,W,H)
        outputResults(L,W,H,SA,V)

main()
