# imports
import time
import timeit

# Practice Codes done in class
# Swap two lists
def swapLists(list1, list2):
    start = time.time()
    temp = []

    for item in range(len(list1)):
        temp.append(list1[item])

    end = time.time()
    print("Time: " + str(end - start))

    return list2, temp

def swapListsByPro(a, b):
    start = time.time()
    temp = a[:]
    a[:] = []

    for item in b:
        a.append(item)
    b[:] = []

    for i in temp:
        b.append(i)

    end = time.time()
    print("Time: " + str(end - start))

    return a, b

# List Example2
def myFunc(value, theList):
    theList[value] = 13
    value = 12
    return

# Performance of list operations: measurements
# Concatenate in O(n)
def test1():
    myList = []
    for i in range(1000):
        myList = myList + [i]
    return None

# Append is O(1)
def test2():
    myList = []
    for i in range(1000):
        myList.append(i)
    return None

def test3():
    myList = [x for x in range(1000)]
    return None

def test4():
    myList = [range(1000)]
    return None

# Console Part
l = [1, 9, 9, 7, 1, 6]
k = [1, 2, 1, 1]
m, n = swapLists(l, k)
print(m, n)

a, b = swapListsByPro(m, n)
print(a, b)
print()

list1 = [x for x in range(6)]
value = 3

print("Before myFunc is called.")
print(list1)
print(value)

myFunc(value, list1)

print("After myFunc is called.")
print(list1)
print(value)

list2 = list1
list1[1] = 8
print("List2: ")
print(list2)

# Performance of list operations: measurements
t = timeit.Timer("test1()", "from __main__ import test1")
duration = t.timeit(1000)
print("Concatenation Time: ", duration, " ms")
t = timeit.Timer("test2()", "from __main__ import test2")
duration = t.timeit(1000)
print("Append Time:        ", duration, " ms")
t = timeit.Timer("test3()", "from __main__ import test3")
duration = t.timeit(1000)
print("Comprehension Time: ", duration, " ms")
t = timeit.Timer("test4()", "from __main__ import test4")
duration = t.timeit(1000)
print("Range Time:         ", duration, " ms")
