# project2_A.py
# HsinYu Chi(Katie)

# This program will draw five shapes in
# 600 * 400 window.

from graphics import*

def main():

    #Create the window.
    win = GraphWin("progect2A",600,400)
    win.setCoords(0,0,600,400)
    win.setBackground("Pink")

    #The lines divide the space.
    #line1 = Line(Point(0,200),Point(600,200))
    #line1.draw(win)
    #line1.setWidth(3)

    #line2 = Line(Point(300,400),Point(300,200))
    #line2.draw(win)
    #line2.setWidth(3)

    #line3 = Line(Point(200,200),Point(200,0))
    #line3.draw(win)
    #line3.setWidth(3)

    #line4 = Line(Point(400,200),Point(400,0))
    #line4.draw(win)
    #line4.setWidth(3)

    #Draw shape one.
    I = Polygon(Point(50,250),Point(100,350),Point(250,350),
                Point(200,250))
    I.draw(win)
    I.setFill("Hot Pink")
    I.setWidth(5)

    #Draw shape two
    S = Polygon(Point(350,250),Point(400,350),Point(500,350),
                Point(550,250))
    S.draw(win)
    S.setFill("Orange")
    S.setWidth(5)

    #Draw shape three.
    W = Rectangle(Point(50,150),Point(150,50))
    W.draw(win)
    W.setFill("Sky Blue")
    W.setWidth(5)

    #Draw shape four.
    J = Polygon(Point(250,100),Point(300,150),Point(350,100),
                     Point(300,50))
    J.draw(win)
    J.setFill("Green")
    J.setWidth(5)

    #Draw shape five.
    Y = Polygon(Point(450,50),Point(500,150),Point(550,50),
                    Point(500,80))
    Y.draw(win)
    Y.setWidth(5)
    Y.setFill("Purple")
    
main()
    
