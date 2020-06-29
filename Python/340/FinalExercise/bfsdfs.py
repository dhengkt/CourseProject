import graphs
import queue

def BFS(graph, start):
    start.graphs.setDistance(0)
    start.graphs.setPred(None)
    vertQueue = queue.Queue()
    vertQueue.put(start)
    while not vertQueue.empty():
        currentVert = vertQueue.get()
        for nbr in currentVert