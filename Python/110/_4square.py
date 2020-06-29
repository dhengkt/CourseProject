#_4square.py
# HsinYu Chi(Katie)

# This program creates a graphing window
# with four squares, for practice.

from graphics import*

def main():

    #Create the window
    win = GraphWin("4square",400,400)
    win.setCoords(0,0,400,400)
    win.setBackground("gray")

    #Draw lines
    line1 = Line(Point(200,0),Point(200,400))
    line1.draw(win)
    line2 = Line(Point(0,200),Point(400,200))
    line2.draw(win)

    #Draw the square
    square = Rectangle(Point(220,180),Point(380,20))
    square.draw(win)
    square.setFill("Gold")
    square.setWidth(5)

    greet = Text(Point(100,100),"HI!")
    greet.draw(win)
    greet.setSize(36)
    greet.setTextColor("Navy")

    #Draw the trangle
    trangle = Polygon(Point(220,380,),Point(220,220,),Point(380,220))
    trangle.draw(win)
    trangle.setFill("Orange")
    trangle.setWidth(5)

    #Draw the circle
    circle1 = Circle(Point(100,300),80)
    circle1.draw(win)
    circle1.setFill("Red")
    circle1.setWidth(5)
    
main()
