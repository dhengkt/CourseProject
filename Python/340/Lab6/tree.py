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
        return self.getLeftChild() is None and self.getRightChild() is None

    def __str__(self):
        return str(self.__key) + " : " + str(self.__value)

class BinarySearchTree:
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
            self.__root = Node(key, value)
            self.__size = 1
            return
        currentNode = self.__root
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

    def __setitem__(self, key, value):
        self.put(key, value)

    def find(self, key):
        return self.findRec(self.__root, key)

    def findRec(self, rootNode, key):
        if rootNode is None:
            return False
        if int(rootNode.getKey()) == int(key):
            return rootNode.getValue()
        if rootNode.getKey() < int(key):
            return self.findRec(rootNode.getRightChild(), key)
        else:
            return self.findRec(rootNode.getRightChild(), key)

    def remove(self, key):
        if self.__root is None:
            return None
        if self.__root.getKey() == key:
            self.__size -= 1
            if self.__root.getLeftChild() is None:
                self.__root = self.__root.getRightChild()
            elif self.__root.getRightChild() is None:
                self.__root = self.__root.getLeftChild()
            else:
                replaceNode = self.__getAndRemoveRightSmall(self.__root)
                self.__root.setkey(replaceNode.getKey())
                self.__root.setValue(replaceNode.getValue())
        else:
            currentNode = self.__root
            while currentNode is not None:
                if currentNode.getLeftChild() and currentNode.getLeftChild().getKey() == key:
                    foundNode = currentNode.getLeftChild()
                    if foundNode.isLeaf():
                        currentNode.setLeftChild(None)
                    elif foundNode.getLeftChild() is None:
                        currentNode.setLeftChild(foundNode.getRightChild())
                    elif foundNode.getRightChild() is None:
                        currentNode.setLeftChild(foundNode.getLeftChild())
                    else:
                        replaceNode = self.__getAndRemoveRightSmall(foundNode)
                        foundNode.setKey(replaceNode.getKey())
                        foundNode.setValue(replaceNode.getValue())
                    break
                elif currentNode.getRightChild() and currentNode.getRightChild().getKey() == key:
                    foundNode = currentNode.getRightChild()
                    if foundNode.isLeaf():
                        currentNode.setRightChild(None)
                    elif foundNode.getLeftChild() is None:
                        currentNode.setRightChild(foundNode.getRightChild())
                    elif foundNode.getRightChild is None:
                        currentNode.setRightChild(foundNode.getLeftChild())
                    else:
                        replaceNode = self.__getAndRemoveRightSmall(foundNode)
                        foundNode.setKey(replaceNode.getKey())
                        foundNode.setValue(replaceNode.getValue())
                    break
                elif currentNode.getKey() > key:
                    currentNode = currentNode.getLeftChild()
                else:
                    currentNode = currentNode.getRightChild()
                if currentNode is not None:
                    self.__size -= 1

    def inOrderTraversal(self, func):
        self.inOrderTraversalRec(self.__root, func)

    def inOrderTraversalRec(self, theNode, func):
        if theNode is not None:
            self.inOrderTraversalRec(theNode.getLeftChild(), func)
            func(theNode.getKey(), theNode.getValue())
            self.inOrderTraversalRec(theNode.getRightChild(), func)

    def printInOrder(self):
        self.printInOrderRec(self.__root)

    def printInOrderRec(self, theNode):
        if theNode is not None:
            self.printInOrderRec(theNode.getLeftChild())
            print(theNode.getKey(), theNode.getValue())
            self.printInOrderRec(theNode.getRightChild())

    def printAccounts(self, key, value):
        print(key + value)

    def __getAndRemoveRightSmall(self, root):


# ===== end file ===== #
