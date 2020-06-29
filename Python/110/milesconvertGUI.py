# milesconverterGUI
# HsinYu Chi(Katie)

# This program uses GUI to get Miles
# from user, and converts to Kilometers.

from graphics import*
from math import*

def main():

    # Draw the window
    win = GraphWin("Convert",500,400)
    win.setCoords(0,0,50,40)
    win.setBackground("Gray")

    # Greet to user
    greet = Text(Point(25,35),"This program will convert Miles to Kilometers.")
    greet.draw(win)
    greet.setSize(18)

    # Create GUI and get input
    text1 = Text(Point(22,25),"Miles: ")
    text1.draw(win)
    text1.setSize(16)
    
    text2 = Text(Point(20,20)," Kilometers: ")
    text2.draw(win)
    text2.setSize(16)

    entry = Entry(Point(30,25),5)
    entry.draw(win)
    entry.setFill("White")


    # Botton
    botton = Text(Point(25,8),"Click to contiune.")
    botton.draw(win)
    botton.setSize(15)
    around = Rectangle(Point(17,10),Point(33,6))
    around.draw(win)
    around.setWidth(2)

    # Calculates the result
    win.getMouse()
    mile = eval(entry.getText())
    km = round(1.60934 * mile,2)

    # Display the result
    botton.setText("Click to quit.")
    output = Text(Point(30,20),"")
    output.setText(km)
    output.draw(win)
    output.setSize(14)

    # Wait for click from user
    win.getMouse()
    win.close()

main()
