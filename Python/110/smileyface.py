#smileyface.py
#HsinYu Chi(Katie)

# This program draws a smiley face.

from graphics import*

def main():

    #Create the window
    win = GraphWin("Smileyface",400,400)
    win.setCoords(0,0,400,400)
    win.setBackground("gray")

    #Draw the circle
    circle1 = Circle(Point(100,300),80)
    circle1.draw(win)
    circle1.setFill("Gold")
    circle1.setWidth(5)

    #Draw the face in the circle
    circle2 = Circle(Point(100,300),50)
    circle2.draw(win)
    #Block the top part of circle
    rectangle1 = Rectangle(Point(50,350),Point(150,300))
    rectangle1.draw(win)
    rectangle1.setFill("Gold")
    rectangle1.setOutline("Gold")

    #Draw the left eye and eyebrow
    circle3 = Circle(Point(70,330),20)
    circle3.draw(win)
    rectangle2 = Rectangle(Point(50,330),Point(90,310))
    rectangle2.draw(win)
    rectangle2.setFill("Gold")
    rectangle2.setOutline("Gold")
    circle4 = Circle(Point(70,330),10)
    circle4.draw(win)
    point1 = Point(70,330)
    point1.draw(win)

    #Draw the right eye and eyebrow
    circle5 = Circle(Point(130,330),20)
    circle5.draw(win)
    rectangle3 = Rectangle(Point(110,330),Point(150,310))
    rectangle3.draw(win)
    rectangle3.setFill("Gold")
    rectangle3.setOutline("Gold")
    circle6 = Circle(Point(130,330),10)
    circle6.draw(win)
    point2 = Point(130,330)
    point2.draw(win)

main()
