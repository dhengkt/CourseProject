# lines
# HsinYu Chi(Katie)

# This program uses GUI to get slope and y-int,
# creates a graphing grid, and graphs the resluting
# line.

from graphics import*

def main():

    # Create GUI and get input
    slope,y_int = eval(input("Enter slope and y-int: "))

    # Draw graph paper
    win = GraphWin("Lines",800,800)
    win.setCoords(-10,-10,10,10)
    win.setBackground("White")

    # Create GUI and get input
    #greet = Text(Point(0,6),"Enter the slope and y-intercept.")
    #greet.draw(win)
    #greet.setSize(16)

    # Create entry boxes
    #slope = Entry(Point(0,2),5)
    #slope.draw(win)
    #y_intercept = Entry(Point(0,-2),5)
    #y_intercept.draw(win)

    #win.getMouse()
    #greet.undraw()
    #slope.undraw()
    #y_intercept.undraw()
    

    # Creates axes
    y_axis = Line(Point(0,-10),Point(0,10))
    y_axis.draw(win)
    
    x_axis = Line(Point(-10,0),Point(10,0))
    x_axis.draw(win)

    # Create graphing grid using loop
    for i in range(-10,11,1):
        
        # Create vertical line
        tempLine = y_axis.clone()
        tempLine.draw(win)
        tempLine.move(i,0)
        
        # Create hoizontal line
        tempLine = x_axis.clone()
        tempLine.draw(win)
        tempLine.move(0,i)

    # Add arrow on axes    
    y_axis.setArrow("both")
    x_axis.setArrow("both")

    y_axis.setWidth(3)
    x_axis.setWidth(3)

    # Graph the line

    line = Line(Point(-10,slope*(-10)+y_int), Point(10,y_int+slope*10))
    line.draw(win)
    line.setOutline("Gold")
    line.setWidth(3)
    line.setArrow("both")

main()
