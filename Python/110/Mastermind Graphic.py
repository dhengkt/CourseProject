# Mastermind graphic
# HsinYu Chi(Katie)

# This program draws the GUI for mastermind game.

from graphics import*

def main():

    win = GraphWin("Mastermind", 400, 800)
    win.setCoords(0,0,400,800)
    win.setBackground("Antiquewhite")

    area = Rectangle(Point(10,790),Point(390,20))
    area.draw(win)
    area.setOutline("Black")
    area.setFill("Lightsalmon")

    block1 = Rectangle(Point(10,790),Point(390,130))
    block1.draw(win)
    block1.setOutline("Black")
    block1.setFill("Lightsalmon")

    line1 = Line(Point(250,790),Point(250,130))
    line1.draw(win)
    line1.setOutline("Black")
    line2 = line1.clone()
    line2.draw(win)
    line2.move(60,0)
    line3 = Line(Point(10,730),Point(390,730))
    line3.draw(win)
    line3.setOutline("Black")

    # Create the entry box for guess.
    guess = Entry(Point(320,75),10)
    guess.draw(win)
    guess.setFill("White")
    

    # Draw the guess balls.
    for y in range(160,760,60):
        for x in range(40,240,60):
            gb = Circle(Point(x,y),20)
            gb.draw(win)
            gb.setWidth(3)
            gb.setFill("Sandybrown")
    # Draw the secret balls.
    for x in range(40,240,60):
        sb = Circle(Point(x,760),20)
        sb.draw(win)
        sb.setWidth(3)
        sb.setFill("Sandybrown")

    # Draw the check balls.
    for j in range(150,750,60):
        for i in range(270,300,20):
            cb1 = Circle(Point(i,j),5)
            cb1.draw(win)
            cb1.setFill("Peachpuff")
            cb1.setOutline("Black")
    for s in range(170,770,60):
        for k in range(270,300,20):
            cb2 = Circle(Point(k,s),5)
            cb2.draw(win)
            cb2.setOutline("Black")
            cb2.setFill("Peachpuff")
    
    # Check botton.
    area1 = Rectangle(Point(320,170),Point(380,150))
    area1.draw(win)
    area1.setOutline("Black")
    area1.setFill("White")

    text1 = Text(Point(350,160),"Check")
    text1.draw(win)
    text1.setSize(13)

    # Draw the color balls.
    cb1 = Circle(Point(40,100),20)
    cb1.draw(win)
    cb1.setFill("Red")
    tcb1 = Text(Point(40,100),"r")
    tcb1.draw(win)
    tcb1.setSize(16)
    cb2 = cb1.clone()
    cb2.draw(win)
    cb2.move(60,0)
    cb2.setFill("Mediumpurple")
    tcb2 = Text(Point(100,100),"m")
    tcb2.draw(win)
    tcb2.setSize(16)
    cb3 = cb2.clone()
    cb3.draw(win)
    cb3.move(60,0)
    cb3.setFill("Dodgerblue")
    tcb3 = Text(Point(160,100),"b")
    tcb3.draw(win)
    tcb3.setSize(16)
    cb4 = cb3.clone()
    cb4.draw(win)
    cb4.move(60,0)
    cb4.setFill("Limegreen")
    tcb4 = Text(Point(220,100),"g")
    tcb4.draw(win)
    tcb4.setSize(16)
    cb5 = cb1.clone()
    cb5.draw(win)
    cb5.move(0,-50)
    cb5.setFill("Saddlebrown")
    tcb5 = Text(Point(40,50),"s")
    tcb5.draw(win)
    tcb5.setSize(16)
    cb6 = cb5.clone()
    cb6.draw(win)
    cb6.move(60,0)
    cb6.setFill("Darkorange")
    tcb6 = Text(Point(100,50),"o")
    tcb6.draw(win)
    tcb6.setSize(16)
    cb7 = cb6.clone()
    cb7.draw(win)
    cb7.move(60,0)
    cb7.setFill("Gold")
    tcb7 = Text(Point(160,50),"y")
    tcb7.draw(win)
    tcb7.setSize(16)
    cb8 = cb7.clone()
    cb8.draw(win)
    cb8.move(60,0)
    cb8.setFill("Pink")
    tcb8 = Text(Point(220,50),"p")
    tcb8.draw(win)
    tcb8.setSize(16)
    

main()
