# entry
# Katie

# This program will help us use an entry box.

from graphics import*

def main():

    win = GraphWin("Bounce",600,600)
    win.setCoords(0,0,100,100)

    prompt = Text(Point(50,80),"Enter the line's slope.")
    prompt.draw(win)
    prompt.setSize(20)

    slope = Entry(Point(50,50),5)
    slope.draw(win)
    slope.setText(0.0)
    slope.setFill("White")

    prompt2 = Text(Point(50,20),"Click to continue.")
    prompt2.draw(win)
    prompt2.setSize(20)

    win.getMouse()
    m = eval(slope.getText())
    time.sleep(1)
    win.close()

    print(m)

main()
    
