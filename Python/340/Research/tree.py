class node:
    def __init__(self, key, value=None):
        self.__key = key
        self.__value = value
        self.__leftChild = None
        self.__rightChild = None

    def getLeftChild(self):
        return self.__leftChild

    def getRightChild(self):
        return self.__rightChild

    def setLeftChild(self, theNode):
        self.__leftChild = theNode

    def setRightChild(self, theNode):
        self.__rightChild = theNode

    def getValue(self):
        return self.__value

    def setValue(self, value):
        self.__value = value

    def getKey(self):
        return self.__key

    def setKey(self, key):
        self.__key = key

    def isLeaf(self):
        return self.getLeftChild() is None and self.getRightChild() is None

    def find(self, value):
        if value == self.__value:
            return True
        elif value < self.__value:
            if self.getLeftChild() is not None:
                return self.getLeftChild().find(value)
            else:
                return False
        else:
            if self.getRightChild() is not None:
                return self.getRightChild().find(value)
            else:
                return False

class BinarySearchTree:
    def __init__(self):
        self.__root = None
        self.__size = 0

    def getCount(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def get(self, key):
        currentNode = self.__root
        while currentNode is not None:
            if currentNode.getKey() == key:
                return currentNode.getValue()
            elif currentNode.getKey() > key:
                currentNode = currentNode.getLeftChild()
            else:
                currentNode = currentNode.getRightChild()
        return None

    def __getitem__(self, key):
        return self.get(key)

    def put(self, key, value):
        if self.isEmpty():
            self.__root = node(key, value)
            self.__size += 1
            return
        currentNode = self.__root
        while currentNode is not None:
            if currentNode.getKey() == key:
                currentNode.setValue(value)
                return
            elif currentNode.getKey() > key:
                if currentNode.getLeftChild() is None:
                    newNode = node(key, value)
                    currentNode.setLeftChild(newNode)
                    break
                else:
                    currentNode = currentNode.getLeftChild()
            else:
                if currentNode.getRightChild() is None:
                    newNode = node(key, value)
                    currentNode.setRightChild(newNode)
                    break
                else:
                    currentNode = currentNode.getRightChild()
        self.__size += 1

    def find(self, value):
        currentNode = node(self.__root)
        return self.findNode(currentNode, value)

    def findNode(self, currentNode, value):
        if currentNode is None:
            return False
        elif currentNode == currentNode.getValue():
            return True
        elif value < currentNode.getValue():
            return self.findNode(currentNode.getLeftChild(), value)
        else:
            return self.findNode(currentNode.getRightChild(), value)

    def __setitem__(self, key, data):
        self.put(key, data)
