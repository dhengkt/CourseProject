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
        return self.getLeftChild() == None and self.getRightChild() == None


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
        while currentNode != None:
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
        while currentNode != None:
            if currentNode.getKey() == key:
                currentNode.setValue(value)
                return
            elif currentNode.getKey() > key:
                if currentNode.getLeftChild() == None:
                    newNode = node(key, value)
                    currentNode.setLeftChild(newNode)
                    break
                else:
                    currentNode = currentNode.getLeftChild()
            else:
                if currentNode.getRightChild() == None:
                    newNode = node(key, value)
                    currentNode.setRightChild(newNode)
                    break
                else:
                    currentNode = currentNode.getRightChild()
        self.__size += 1

    def __setitem__(self, key, data):
        self.put(key, data)

    def remove(self, key):
        if self.__root == None:
            return None
        if self.__root.getKey() == key:
            self.__size -= 1
            if self.__root.getLeftChild() == None:
                self.__root = self.__root.getRightChild()
            elif self.__root.getRightChild() == None:
                self.root = self.__root.getLeftChild()
            else:
                replaceNode = self.__getAndRemoveRightSmall(self.__root)
                self.__root.setkey(replaceNode.getKey())
                self.__root.setValue(replaceNode.getValue())
