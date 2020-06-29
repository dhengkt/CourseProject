import bank
import tree

# test Binary Search Tree class
testTree = tree.BinarySearchTree()
testTree[16] = "test"
testTree[166] = "dog"
testTree[54] = "car"

print(testTree.isEmpty())
print(testTree.find(16))

# test the account class
testAccount = bank.Account("Katie", "Danvers", 1206)
testAccount2 = bank.Account("Steve", "Banner", 1234)

# test the transaction class

# test the fund class
