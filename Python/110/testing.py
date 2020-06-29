# shape.py
# Katie

# This program create shapes.

from graphics import*

def main():

    win = GraphWin("Testing",500,500)
    win.setCoords(0,0,500,500)
    win.setBackground("gray")

    circle = Circle(Point(250,250),100)
    circle.draw(win)
    circle.setFill("Green")
    circle.setWidth(5)

main()
