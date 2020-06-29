import point

class Robot:
    def __init__(self, rX=0, rY=0, tX=0, tY=0):
        self.__robot = point.Point(rX, rY)
        self.__treasure = point.Point(tX, tY)
        self.steps = 0
        self.paths = []
        # Find the paths automatically and print out result.
        self.findPaths(self.__robot.getX(), self.__robot.getY(), self.steps, self.paths)
        self.printPaths()

    def findPaths(self, currX, currY, steps, path):
        if steps > self.steps > 0:
            return
        if currX == self.__treasure.getX() and currY == self.__treasure.getY():
            if len(path) == 0:
                return
            # Generate a string to store one set of path.
            temPath = ''.join(path)
            if self.steps == steps or self.steps < 0:
                self.steps = steps
                # Check if it is duplicated.
                if temPath != self.paths:
                    self.paths.append(temPath)
            else:
                self.steps = steps
                self.paths = [temPath]
        else:
            if currY < self.__treasure.getY():
                self.findPaths(currX, currY + 1, steps + 1, list(path) + ['N'])
            if currX < self.__treasure.getX():
                self.findPaths(currX + 1, currY, steps + 1, list(path) + ['E'])
            if currX > self.__treasure.getX():
                self.findPaths(currX - 1, currY, steps + 1, list(path) + ['W'])
            if currY > self.__treasure.getY():
                self.findPaths(currX, currY - 1, steps + 1, list(path) + ['S'])

    def printPaths(self):
        for path in self.paths:
            print(path)
        print("Number of paths: ", len(self.paths))
