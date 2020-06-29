# happybirthdaysingalong
# HsinYu Chi(Katie)

# This program will create a graphing window that
# ask user to input their name from an entry box, and
# a bouncing-ball sing-along to Happy birthday song.

from graphics import*

def main():

    # Create the window
    win = GraphWin("Happy Birthday sing-along",500,400)
    win.setCoords(0,0,50,40)
    win.setBackground("Light Blue")

    # Create the GUI to get input
    greet = Text(Point(25,36),"Happy birthday sing-along!")
    greet.draw(win)
    greet.setSize(24)

    instruction = Text(Point(25,24),"Please enter your name.")
    instruction.draw(win)
    instruction.setSize(18)

    name = Entry(Point(25,20),10)
    name.draw(win)
    name.setFill("White")

    instruction2 = Text(Point(25,10),"Click to start.")
    instruction2.draw(win)
    instruction2.setSize(15)
    around = Rectangle(Point(17,12),Point(33,8))
    around.draw(win)
    around.setOutline("Black")

    # Wait for mouse
    win.getMouse()
    greet.undraw()
    instruction.undraw()
    name.undraw()
    instruction2.undraw()
    around.undraw()

    # Decoration of window
    strea1 = Rectangle(Point(11,32),Point(15,28))
    strea1.draw(win)
    strea1.setWidth(2)
    strea1.setFill("White")

    strea2 = strea1.clone()
    strea2.move(6,0)
    strea2.draw(win)
    strea3 = strea2.clone()
    strea3.move(6,0)
    strea3.draw(win)
    strea4 = strea3.clone()
    strea4.move(6,0)
    strea4.draw(win)
    strea5 = strea4.clone()
    strea5.move(6,0)
    strea5.draw(win)

    strea6 = Rectangle(Point(2,26),Point(6,22))
    strea6.draw(win)
    strea6.setWidth(2)
    strea6.setFill("White")

    strea7 = strea6.clone()
    strea7.move(6,0)
    strea7.draw(win)
    strea8 = strea7.clone()
    strea8.move(6,0)
    strea8.draw(win)
    strea9 = strea8.clone()
    strea9.move(6,0)
    strea9.draw(win)
    strea10 = strea9.clone()
    strea10.move(6,0)
    strea10.draw(win)
    strea11 = strea10.clone()
    strea11.move(6,0)
    strea11.draw(win)
    strea12 = strea11.clone()
    strea12.move(6,0)
    strea12.draw(win)
    strea13 = strea12.clone()
    strea13.move(6,0)
    strea13.draw(win)

    d1 = Text(Point(13,30),"H")
    d1.draw(win)
    d1.setTextColor("Blue")
    d2 = Text(Point(19,30),"A")
    d2.draw(win)
    d2.setTextColor("Blue")
    d3= Text(Point(25,30),"P")
    d3.draw(win)
    d3.setTextColor("Blue")
    d4 = Text(Point(31,30),"P")
    d4.draw(win)
    d4.setTextColor("Blue")
    d5 = Text(Point(37,30),"Y")
    d5.draw(win)
    d5.setTextColor("Blue")
    d6 = Text(Point(4,24),"B")
    d6.draw(win)
    d6.setTextColor("Blue")
    d7 = Text(Point(10,24),"I")
    d7.draw(win)
    d7.setTextColor("Blue")
    d8 = Text(Point(16,24),"R")
    d8.draw(win)
    d8.setTextColor("Blue")
    d9 = Text(Point(22,24),"T")
    d9.draw(win)
    d9.setTextColor("Blue")
    d10 = Text(Point(28,24),"H")
    d10.draw(win)
    d10.setTextColor("Blue")
    d11 = Text(Point(34,24),"D")
    d11.draw(win)
    d11.setTextColor("Blue")
    d12 = Text(Point(40,24),"A")
    d12.draw(win)
    d12.setTextColor("Blue")
    d13 = Text(Point(46,24),"Y")
    d13.draw(win)
    d13.setTextColor("Blue")



    # Create the ball
    ball1 = Circle(Point(10,10),0.5)
    ball1.draw(win)
    ball1.setFill("Orange")
    ball1.setWidth(2)

    lyrics1 = Text(Point(25,6),"Happy birthday to you.")
    lyrics1.draw(win)
    lyrics1.setSize(20)

    # Using loop to let ball bounces
    for i in range(2):
        
        for i in range(6):
            time.sleep(0.2)
            ball1.move(2.5,-2)
            time.sleep(0.2)
            ball1.move(2.5,2)
        ball1.move(-30,0)
    lyrics1.undraw()
    ball1.undraw()
    
    # Second lyrics with name
    ball2 = Circle(Point(8,10),0.5)
    ball2.draw(win)
    ball2.setFill("Orange")
    ball2.setWidth(2)
    
    lyrics2 = Text(Point(20,6),"Happy birthday to")
    lyrics2.draw(win)
    lyrics2.setSize(20)

    Name = Text(Point(35,6),name.getText())
    Name.draw(win)
    Name.setSize(20)
    
    for i in range(6):
        time.sleep(0.2)
        ball2.move(2.5,-2)
        time.sleep(0.2)
        ball2.move(2,2)
        
    time.sleep(0.2)
    ball2.move(1,-2)
    time.sleep(0.2)
    ball2.move(0.5,2)
    ball2.move(-27,0)

    lyrics2.undraw()
    Name.undraw()

    # The last lyrics
    lyrics3 = Text(Point(25,6),"Happy birthday to you.")
    lyrics3.draw(win)
    lyrics3.setSize(20)

    # Using loop to let ball bounces
    for i in range(6):
        time.sleep(0.2)
        ball2.move(2.5,-2)
        time.sleep(0.2)
        ball2.move(2.5,2)
    ball1.move(-30,0)

    # Close the window after the song end
    time.sleep(0.4)
    win.close()

    
main()
