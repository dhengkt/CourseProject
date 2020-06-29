# Let's bounce
# Katie

# This program will help us "bounce" an object (ball).

from graphics import*

def main():

    win = GraphWin("Bounce",600,600)
    win.setCoords(0,0,100,100)

    ball = Circle(Point(20,80),5)
    ball.draw(win)
    ball.setFill("Black")

    #for i in range(10):
        
    for i in range(30):
        time.sleep(0.05)
        ball.move(1,-2)

    for i in range(30):
        time.sleep(0.05)
        ball.move(1,2)


main()
    
