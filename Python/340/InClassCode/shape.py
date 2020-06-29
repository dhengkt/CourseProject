
class Square:
    def __init__(self,length):

        if length >= 0:
            self.__length = length
            self.length = length

        else:
            self.__length = 0


    def getLength(self):
        return self.__length


    def setLength(self,length):

        if length >= 0:
            self.__length = length

        else:
            self.__length = 0

    def getArea(self):
        return self.__length * self.__length


    def getPerimiter(self):
        return 4 * self.__length

