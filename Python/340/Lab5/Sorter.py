import random
import sort
import sys
LIST_SIZE = 10

inList = []
userInput = input(sys.argv).split()
output = userInput.count("PRINT")

if output == 0:
    sortName = userInput[0]
    n = int(userInput[1])
    output = "NONE"
else:
    sortName = userInput[0]
    n = int(userInput[1])
    output = userInput[2]

for i in range(int(n)):
    randomNumber = random.randint(0, LIST_SIZE * 10)
    inList.append(randomNumber)

if output[0] == 'P':
    if sortName[0] == 'B':
        print(inList)
        sort.BubbleSort(inList)
        print(inList)
    elif sortName[0:3] == 'In':
        print(inList)
        sort.InsertionSort(inList)
        print(inList)
    elif sortName[0] == 'M':
        print(inList)
        sort.MergeSort(inList)
        print(inList)
    elif sortName[0] == 'I':
        print(inList)
        sort.IterativeMergeSort(inList)
        print(inList)
    elif sortName[0] == 'Q':
        print(inList)
        sort.QuickSort(inList)
        print(inList)
    elif sortName[0] == 'S':
        print(inList)
        sort.ShellSort(inList)
        print(inList)
elif output[0] == 'N':
    if sortName[0] == 'B':
        sort.BubbleSort(inList)
    elif sortName[0:3] == 'In':
        sort.InsertionSort(inList)
    elif sortName[0] == 'M':
        sort.MergeSort(inList)
    elif sortName[0] == 'I':
        sort.IterativeMergeSort(inList)
    elif sortName[0] == 'Q':
        sort.QuickSort(inList)
    elif sortName[0] == 'S':
        sort.ShellSort(inList)
