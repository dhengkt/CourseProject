class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def __eq__(self, rhs):
        if self.__x == rhs.__x and self.__y == rhs.__y:
            return True
        else:
            return False

    def __ne__(self, rhs):
        if self == rhs:
            return False
        else:
            return True