# testobjects
# HsinYu Chi(Katie)

# This program will introduce
# new objects and methods.

from graphics import*

def main():

    #Create the window.
    win = GraphWin("Testing",400,400)

    #Tell the users to input their name.
    #greet = Text(Point(200,100),"Enter your name")
    #greet.draw(win)
    #greet.setSize(36)

    #win.getMouse()
    win.setBackground("Orange")

    #Entry box for user to input.
    getName = Entry(Point(200,200),20)
    getName.draw(win)
    getName.setFill("White")
    getName.setText("Enter your name.")

    #Tell users to click.
    cont = Text(Point(200,300),"Click to continue")
    cont.draw(win)
    cont.setSize(36)

    #Close evevrything after user put their name.
    win.getMouse()
    name = getName.getText()
    #greet.undraw()
    getName.undraw()
    cont.undraw()

    #Print the text.
    line1 = Text(Point(200,100),"Your name is " + name + ".")
    line1.draw(win)
    line1.setSize(18)
    line1.setTextColor("Navy")
    
    line2 = Text(Point(200,200),"Programming is interactive!")
    line2.draw(win)
    line2.setSize(18)
    line2.setTextColor("Navy")

main()
