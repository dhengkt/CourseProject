import math
import geometry

def make_circle(x, y, radius):
    circle = geometry.Circle(x, y, radius)
    return circle;

circle1 = make_circle(0, 0, 1)
circle2 = make_circle(2, 3, 2)

# Test 1: getX(), getY(), getRadius(). -2 for each missing;  max of -4
if (circle1.getX() != 0 or circle2.getX() != 2):
    print "getX() is incorrect"
if (circle1.getY() != 0 or circle2.getY() != 3):
    print "getY() is incorrect"
if (circle1.getRadius() != 1 or circle2.getRadius() != 2):
    print "getRadius() is incorrect"

# Test 2: setX(), setY(), setRadius(). 1pt each, 3pts in total
circle1.setX(1)
circle1.setY(1)
circle1.setRadius(2)
circle2.setX(5)
circle2.setY(5)
circle2.setRadius(5)
if (circle1.getX() != 1 or circle2.getX() != 5):
    print "getX() is incorrect"
if (circle1.getY() != 1 or circle2.getY() != 5):
    print "getY() is incorrect"
if (circle1.getRadius() != 2 or circle2.getRadius() != 5):
    print "getRadius() is incorrect"

# Test 3: getPerimeter(). 3pts in total
if (circle1.getPerimeter() != 2 * math.pi * circle1.getRadius() or circle2.getPerimeter() != 2 * math.pi * circle2.getRadius()):
    print "getPerimeter() is incorrect"

# Test 4: getArea(). 3pts in total
if (circle1.getArea() != circle1.getRadius() * circle1.getRadius() * math.pi or circle2.getArea() != circle2.getRadius() * circle2.getRadius() * math.pi):
    print "getArea() is incorrect"

# Test 5: isPointWithinCircle(). 3pts in total
if (circle1.isPointWithinCircle(4, 4) != False or circle2.isPointWithinCircle(5, 5) != True):
    print "isPointWithinCircle() is incorrect"

print "Tests end"