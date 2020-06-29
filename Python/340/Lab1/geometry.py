# This class creates circle by using the values x, y, and radius from user.

from math import pi, pow, sqrt

class Circle:

    def __init__(self,x=0,y=0,radius=0):
        self.__x = x
        self.__y = y

        if radius > 0:
            self.__radius = radius
        else:
            print("Error: radius should be greater than zero.")

    def setX(self,x):
        self.__x = x

    def setY(self,y):
        self.__y = y

    def setRadius(self,radius):
        self.__radius = radius

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getRaidus(self):
        return self.__radius

    def getArea(self):
        return round(pow(self.getRaidus(),2) * pi,2)

    def getPerimeter(self):
        return round(pi * (self.__radius * 2),2)

    def isPointWithinCircle(self,targetX,targetY):
        disBetweenPoints = sqrt(pow(self.__x - targetX,2) + pow(self.__y - targetY,2))

        if disBetweenPoints <= self.__radius:
            return True
        else:
            return False
