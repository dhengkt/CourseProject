import queue

class Vertex:
    def __init__(self, key):
        self.__id = key
        self.__connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.__connectedTo[nbr] = weight

    def __str__(self):
        return str(self.__id) + ' connectedTo ' + str([x.__id for x in self.__connectedTo])

    def getConnections(self):
        return self.__connectedTo.keys()

    def getId(self):
        return self.__id

    def getWeight(self, nbr):
        return self.__connectedTo[nbr]

class Graph:
    def __init__(self):
        self.__vertList = {}
        self.__numVertices = 0

    def addVertex(self, key):
        self.__numVertices += 1
        newVertex = Vertex(key)
        self.__vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.__vertList:
            return self.__vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.__vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.__vertList:
            nv = self.addVertex(f)
        if t not in self.__vertList:
            nv = self.addVertex(t)
        self.__vertList[f].addNeighbor(self.__vertList[t], cost)

    def getVertices(self):
        return self.__vertList.keys()

    def getVertList(self):
        return self.__vertList

    def __iter__(self):
        return iter(self.__vertList.values())