class Robot:
    # Constructor
    def __init__(self, rX=0, rY=0, tX=0, tY=0):
        self._rx = rX
        self._ry = rY
        self._tx = tX
        self._ty = tY

        # Set helper attributes
        self.minSteps = -1  # -1 because it's not set yet
        self.paths = []  # Empty list that will contain the shortest paths

    def solve(self):
        # Call path method with the current positions as the starting positions,
        # number of steps so far = 0
        # Path so far is empty
        self.path(self._rx, self._ry, 0, [])

    def path(self, coordinateX, coordinateY, steps, path):
        if self.minSteps > 0 and self.minSteps < steps:
            return

        # Reached target
        if coordinateX == self._tx and coordinateY == self._ty:
            # If starting position and target position are the same return (Do nothing)
            if len(path) == 0:
                return
            pathString = ''.join(path)
            if self.minSteps < 0:
                self.minSteps = steps
                self.paths.append(pathString)
            elif self.minSteps == steps:
                if pathString not in self.paths:
                    self.paths.append(pathString)
            elif self.minSteps > steps:
                self.minSteps = steps
                self.paths = [pathString]
        else:
            if coordinateY < self._ty:
                self.path(coordinateX, coordinateY + 1, steps + 1, list(path) + ['N'])
            if coordinateX < self._tx:
                self.path(coordinateX + 1, coordinateY, steps + 1, list(path) + ['E'])
            if coordinateX > self._tx:
                self.path(coordinateX - 1, coordinateY, steps + 1, list(path) + ['W'])
            if coordinateY > self._ty:
                self.path(coordinateX, coordinateY - 1, steps + 1, list(path) + ['S'])

    # Prints solution
    def solution(self):
        for path in self.paths:
            print(path)
        print("Number of paths: ", len(self.paths))