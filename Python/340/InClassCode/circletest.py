from geometry import Circle

print("Partial Testing for CSS340 Lab1")
c1 = Circle(3, 3, 7)
c2 = Circle()
print("First Circle Perimeter: " + str(c1.getPerimeter()))
print("First Circle Area: " + str(c1.getArea()))

c2.setX(3)
c2.setY(3)
c2.setRadius(2)

if c2.isPointWithinCircle(4, 3.7):
    print("(4, 3.7) is within circle two")
else:
    print("(4, 3.7) is not within circle two")

print("Moving second Circle")
c2.setX(3 + c2.getX())

if c2.isPointWithinCircle(4, 3.7):
    print("(7, 3.7) is within circle two")
else:
    print("(7, 3.7) is not within circle two")
