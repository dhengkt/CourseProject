import math

class Point:
    #Constructor takes two integer (x, y) values 
    def __init__(self, x, y):
        self.__x = int(x)
        self.__y = int(y)

    def getY(self):
        return self.__y

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setCoord(self, x, y):
        self.__x = x
        self.__y = y

    def getCoord(self):
        return  (str(self))

    def distanceTo(self, other):
        pointX = self.__x - other.__x
        pointY = self.__y - other.__y

        #Calculating the euclidean distance between points
        return math.sqrt(pointX * pointX + pointY * pointY)

    def __str__(self):
        return ("(" + str(self.__x) + ", " + str(self.__y) + ")")


