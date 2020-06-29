import random
import sort
import time
LIST_SIZE = 10

# Bubble Sort
print("Data Output Format")
print("Test with list size 10")
print("Test with list size 100")
print("Test with list size 1000")
print("Test with list size 5000")
print("Test with list size 10000")
print()
print()
print("Bubble Sort")
testList = []
start: float = time.time_ns()
for i in range(LIST_SIZE):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.BubbleSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 10):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.BubbleSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 100):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.BubbleSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 500):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.BubbleSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 1000):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.BubbleSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))
print()
print()

# Insertion Sort
print("Insertion Sort")
testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.InsertionSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 10):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.InsertionSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 100):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.InsertionSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 500):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.InsertionSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 1000):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.InsertionSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))
print()
print()

# Merge Sort
print("Merge Sort")
testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.MergeSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 10):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.MergeSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 100):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.MergeSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 500):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.MergeSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 1000):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.MergeSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))
print()
print()

# Iterative Merge Sort
print("Iterative Merge Sort")
testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.IterativeMergeSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 10):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.IterativeMergeSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 100):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.IterativeMergeSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 500):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.IterativeMergeSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 1000):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.IterativeMergeSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))
print()
print()

# Quick Sort
print("Quick Sort")
testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.QuickSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 10):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.QuickSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 100):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.QuickSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 500):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.QuickSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 1000):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.QuickSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))
print()
print()

# Shell Sort
print("Shell Sort")
testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.ShellSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 10):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.ShellSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 100):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.ShellSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 500):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.ShellSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))

testList.clear()
start = time.time_ns()
for i in range(LIST_SIZE * 1000):
    randomNum = random.randint(0, LIST_SIZE * 10)
    testList.append(randomNum)
sort.ShellSort(testList)
end = time.time_ns()
runTime = (end - start) / 1000000
print("Run Time: {} ms.".format(runTime))
