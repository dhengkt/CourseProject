import tree

def func1(key, value):
    print("THE KEY: " + str(key) + " THE VALUE: " + str(value))


jollyTree = tree.BinarySearchTree()
jollyTree.put(1234, "hello")
jollyTree.put(65, "goodbye")
jollyTree[675] = "cat"
jollyTree[4000] = "dog"

print(jollyTree[675])
print(jollyTree.find(675))
