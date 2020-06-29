# smileyface_almostSpider-man.py
# HsinYu Chi(Katie)

# This program draws a smiley face(Spider-man ver.).

from graphics import*

def main():

    #Create the window
    win = GraphWin("Smileyface",400,400)
    win.setCoords(0,0,400,400)
    win.setBackground("gray")

    #Draw a hair.
    hair = Circle(Point(260,320),20)
    hair.draw(win)
    hair.setWidth(3)

    #Blcok the circle.
    blockhair = Polygon(Point(240,300),Point(280,300),Point(280,340))
    blockhair.draw(win)
    blockhair.setFill("Gray")
    blockhair.setOutline("Gray")
    blockhair.setWidth(3)

    #Draw the face.
    circle1 = Circle(Point(200,200),130)
    circle1.draw(win)
    circle1.setFill("Red")
    circle1.setWidth(5)

    #Draw the mouth.
    mouth = Oval(Point(140,180),Point(260,100))
    mouth.draw(win)
    mouth.setWidth(3)

    #Block the half of mouth.
    blockmouth = Rectangle(Point(140,180),Point(260,140))
    blockmouth.draw(win)
    blockmouth.setWidth(3)
    blockmouth.setOutline("Red")
    blockmouth.setFill("Red")

    #Draw the eyes.
    eye1 = Circle(Point(140,220),50)
    eye1.draw(win)
    eye1.setFill("White")
    eye1.setWidth(5)
    
    #Block the half of eye.
    blockeye1 = Polygon(Point(90,270),Point(190,170),Point(190,270))
    blockeye1.draw(win)
    blockeye1.setFill("Red")
    blockeye1.setOutline("Red")
    blockeye1.setWidth(5)
    line1 = Line(Point(103,257),Point(173,180))
    line1.draw(win)
    line1.setWidth(5)

    #Draw the eyes.
    eye2 = Circle(Point(260,220),50)
    eye2.draw(win)
    eye2.setFill("White")
    eye2.setWidth(5)
    
    #Block the half of eye.
    blockeye2 = Polygon(Point(310,270),Point(210,170),Point(210,270))
    blockeye2.draw(win)
    blockeye2.setFill("Red")
    blockeye2.setOutline("Red")
    blockeye2.setWidth(5)
    line2 = Line(Point(297,257),Point(227,180))
    line2.draw(win)
    line2.setWidth(5)

    #Block the original circle.
    circle1 = Circle(Point(200,200),130)
    circle1.draw(win)
    circle1.setWidth(5)

    #Draw the eyebrows.
    eyebrow1 = Line(Point(120,280),Point(180,240))
    eyebrow1.draw(win)
    eyebrow1.setWidth(3)
    eyebrow2 = Line(Point(280,280),Point(220,240))
    eyebrow2.draw(win)
    eyebrow2.setWidth(3)
    
    
main()
