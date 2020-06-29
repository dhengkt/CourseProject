import point

class Robot:
    #Constructor takes a point for start and treasure
    def __init__(self, startPoint = None, treasurePoint = None):
        self.__robot = startPoint
        self.__treasure = treasurePoint

        #Helper variables 
        self.paths = []
        self.minMoves = -1

    #Getters
    def getX(self):
        return self.__robot.getX()

    def getY(self):
        return self.__robot.getY()

    def getTreasureX(self):
        return self.__treasure.getX()

    def getTreasureY(self):
        return self.__treasure.getY()

    def findTreasure(self):
        #Calls findTreasure function with default values
        self.searchMap(self.getX(), self.getY(), 0, [])

    #Takes direction commands in the format: North, South, East, West - will move robot accordingly
    def move(self, direction):
        if direction == "N":
            self.setX(self.getX() + 1)
        elif direction == "S":
            self.setX(self.getX() - 1)
        elif direction == "E":
            self.setY(self.getY() + 1)
        elif direction == "W":
            self.setY(self.getY() - 1)
        else:
            return None

    def searchMap(self, coordX, coordY, moves, path):
        #Handles the minimum solution
        if self.minMoves > 0 and self.minMoves < moves:
            return
        #If treasure found
        if coordX == self.getTreasureX() and coordY == self.getTreasureY():
            if len(path) == 0:
                return
            #Concatenates string
            pathsTemp = "".join(path)

            #Path test cases
            if self.minMoves < 0:
                self.minMoves = moves
                self.paths.append(pathsTemp)

            elif self.minMoves == moves:
                if pathsTemp not in self.paths:
                    self.paths.append(pathsTemp)

            elif self.minMoves > moves:
                self.minMoves = moves
                self.paths = [pathsTemp]
        #If treasure has not been found
        else:
            if coordY < self.getTreasureY():
                self.searchMap(coordX, coordY + 1, moves + 1, list(path) + ["N"] )

            if coordY > self.getTreasureY():
                self.searchMap(coordX, coordY - 1, moves + 1, list(path) + ["S"] )

            if coordX < self.getTreasureX():
                self.searchMap(coordX + 1, coordY , moves + 1, list(path) + ["E"] )

            if coordX < self.getTreasureX():
                self.searchMap(coordX - 1, coordY , moves + 1, list(path) + ["W"] )

    def pathsToTreasure(self):
        for path in self.paths:
            print(path)
        print("Total shortest paths to the treasure: ", len(self.paths))
       
    def __str__(self):
        return ("(" + str(self.getX()) + ", " + str(self.getY()) + ")")
