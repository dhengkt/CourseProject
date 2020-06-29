
class BSTree:

    def __init__(self):
        self.__root = None
        self.__size = 0

    def getSize(self):
        return self.__size

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.size() == 0

    def put(self, key, value):
        if self.isEmpty():
            self.__root = BSTreeNode(key, value)
            self.__size = 1
            return
        currentNode = self.__root
        while currentNode != None:
            if currentNode.getKey() == key:
                currentNode.setValue(value)
                return
            elif currentNode.getKey() > key:
                if currentNode.getLeftChild() == None:
                    newNode = BSTreeNode(key, value)
                    currentNode.setLeftChild(newNode)
                    break
                else:
                    currentNode = currentNode.getLeftChild()
            else:
                if currentNode.getRightChild() == None:
                    newNode = BSTreeNode(key, value)
                    currentNode.setRightChild(newNode)
                    break
                else:
                    currentNode = currentNode.getRightChild()
        self.__size += 1

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

    def __setitem__(self, key, value):
        self.put(key, value)

    def searchTree(self, key):
        return self.searchTreeRec(self.__root, key)

    def searchTreeRec(self, rootNode, key):
        if rootNode is None:
            return False
        if int(rootNode.getKey()) == int(key):
            return rootNode.getValue()
        if rootNode.getKey() < int(key):
            return self.searchTreeRec(rootNode.getRightChild(), key)
        else:
            return self.searchTreeRec(rootNode.getRightChild(), key)

    # def preOrderTraversal(self, func):
    #     self.inOrderTraversalRec(self.__root, func)
    #
    # def preOrderTraversalRec(self, theNode, func):
    #     if theNode != None:
    #         func(theNode.getKey(), theNode.getValue())
    #         self.inOrderTraversalRec(theNode.getLeftChild(), func)
    #         self.__inOrderTraversalRec(theNode.getRightChild(), func)

    def inOrderTraversal(self, func):
        self.inOrderTraversalRec(self.__root, func)

    def inOrderTraversalRec(self, theNode, func):
        if theNode != None:
            self.inOrderTraversalRec(theNode.getLeftChild(), func)
            func(theNode.getKey(), theNode.getValue())
            self.inOrderTraversalRec(theNode.getRightChild(), func)

    def printInOrder(self):
        self.printInOrderRec(self.__root)

    def printInOrderRec(self, theNode):
        if theNode != None:
            self.printInOrderRec(theNode.getLeftChild())
            print(theNode.getKey(), theNode.getValue())
            self.printInOrderRec(theNode.getRightChild())

    def printAccounts(self, key, value):
        print(key + value)

    # def postOrderTraversal(self, func):
    #     self.__inOrderTraversalRec(self.__root, func)
    #
    # def postOrderTraversalRec(self, theNode, func):
    #     if theNode != None:
    #         self.__inOrderTraversalRec(theNode.getLeftChild(), func)
    #         self.__inOrderTraversalRec(theNode.getRightChild(), func)
    #         func(theNode.getKey(), theNode.getValue())


class BSTreeNode:
    def __init__(self, key, value = None):
        self.__key = key
        self.__value = value
        self.__leftChild = None
        self.__rightChild = None

    def getLeftChild(self):
        return self.__leftChild

    def getRightChild(self):
        return self.__rightChild

    def setLeftChild(self, node):
        self.__leftChild = node

    def setRightChild(self, node):
        self.__rightChild = node

    def getKey(self):
        return self.__key

    def getValue(self):
        return self.__value

    def setKey(self, key):
        self.__key = key

    def setValue(self, value):
        self.__value = value

    def isLeaf(self):
        return self.getLeftChild() == None and self.getRightChild() == None

    def __str__(self):
        return str(self.__key) + " : " + str(self.__value)