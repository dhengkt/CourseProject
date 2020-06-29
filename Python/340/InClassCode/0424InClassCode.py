import random
count = 0
def func():
    global count
    count += 1

def complexity(n):
    for i in range(n):
        for j in range(i+1):
            func()

#n = eval(input("n = ")).strip()
#complexity(n)
#print("Number times count called: ", count)

def binarySearch(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] < item:
            low = mid + 1
        elif list[mid] > item:
            high = mid - 1
        else:
            return mid
    return None

mylist = []
for i in range(100):
    num = random.randint(0, 1000)
    mylist.append(num)
mylist.sort()
item = mylist[16]

#n = eval(input("my val: ").strip())
#print(binarySearch(mylist,item))
#print(mylist)

def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factorialIteral(n):
    val = 0
    for i in range(1, n + 1):
        val = val * 1
    return val

#n = eval(input("n = "))
#print("{}! is {}.".format(n, factorial(n)))

def numLeaves(height, maxBranches):
    if height < 0 or maxBranches < 0:
        return None
    elif height == 1:
        return 1
    else:
        return maxBranches * numLeaves(height - 1, maxBranches)

