class Robot:
    def __init__(self, robotX=0, robotY=0, treasureX=0, treasureY=0):
        self.__robotX = robotX
        self.__robotY = robotY
        self.__treasureX = treasureX
        self.__treasureY = treasureY

        self.paths = []
        self.findPaths(self.__robotX, self.__robotY, [])
        self.printPaths()

    def findPaths(self, currX, currY, path):
        if currX == self.__treasureX and currY == self.__treasureY:
            # If starting position and treasure position are the same return (Do nothing)
            if len(path) == 0:
                return
        else:
            if currY < self.__treasureY:
                self.findPaths(currX, currY + 1, list(path) + ['N'])
            if currX < self.__treasureX:
                self.findPaths(currX + 1, currY, list(path) + ['E'])
            if currX > self.__treasureX:
                self.findPaths(currX - 1, currY, list(path) + ['W'])
            if currY > self.__treasureY:
                self.findPaths(currX, currY - 1, list(path) + ['S'])

    def printPaths(self):
        for path in self.paths:
            print(path)
        print("Number of paths: ", len(self.paths))
