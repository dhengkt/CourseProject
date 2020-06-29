class Node:
    def __init__(self, key, value=None):
        self.__key = key
        self.__value = value
        self.__leftChild = None
        self.__rightChild = None

    def getLeftChild(self):
        return self.__leftChild

    def getRightChild(self):
        return self.__rightChild

    def getKey(self):
        return self.__key

    def getValue(self):
        return self.__value

    def setLeftChild(self, node):
        self.__leftChild = node

    def setRightChild(self, node):
        self.__rightChild = node

    def setKey(self, key):
        self.__key = key

    def setValue(self, value):
        self.__value = value

    def isLeaf(self):
        return self.getLeftChild() is None and self.getRightChild() is None

    def __str__(self):
        return str(self.__key) + " " + str(self.__value)

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.__size = 0

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.size() == 0

    def get(self, key):
        currentNode = Node(self.root)
        while currentNode is not None:
            if currentNode.getKey() == key:
                return currentNode.getValue()
            elif currentNode.getKey() > key:
                currentNode = currentNode.getLeftChild()
            else:
                currentNode = currentNode.getRightChild()
        return None

    def __getitem__(self, item):
        return self.get(item)

    def put(self, key, value):
        if self.isEmpty():
            self.root = Node(key, value)
            self.__size = 1
            return
        currentNode = self.root
        while currentNode is not None:
            if currentNode.getKey() == key:
                currentNode.setValue(value)
                return
            elif currentNode.getKey() > key:
                if currentNode.getLeftChild() is None:
                    newNode = Node(key, value)
                    currentNode.setLeftChild(newNode)
                    break
                else:
                    currentNode = currentNode.getLeftChild()
            else:
                if currentNode.getRightChild() is None:
                    newNode = Node(key, value)
                    currentNode.setRightChild(newNode)
                    break
                else:
                    currentNode = currentNode.getRightChild()
        self.__size += 1

    def __setitem__(self, key, value):
        self.put(key, value)

    def inOrderTraversal(self, func):
        theNode = self.root
        self.__inOrderTraversalRec(self.root, func)

    def __inOrderTraversalRec(self, theNode, func):
        if theNode is not None:
            self.__inOrderTraversalRec(theNode.getLeftChild(), func)
            func(theNode.getKey(), theNode.getValue())
            self.__inOrderTraversalRec(theNode.getRightChild())
