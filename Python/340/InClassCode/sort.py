# Exercise of sorting
# Helper functions
def quickSortRec(inList, first, last):
    if last - first < 5:
        insertionSortPartial(inList, first, last)
        return
    # Choose the pivot using the sedgewick algorithm
    mid = (first + last) // 2
    if inList[first] > inList[last]:
        inList[first], inList[last] = inList[last], inList[first]
    if inList[first] > inList[mid]:
        inList[first], inList[mid] = inList[mid], inList[first]
    if inList[mid] > inList[last]:
        inList[mid], inList[last] = inList[last], inList[mid]

    pivot = inList[mid]
    inList[last - 1], inList[mid] = inList[mid], inList[last - 1]
    left = first + 1
    right = last - 2
    done = False
    while not done:
        while inList[left] < pivot:
            left += 1
        while inList[right] < pivot:
            right -= 1
        if right > left:
            inList[right], inList[left] = inList[left], inList[right]
            left += 1
            right -= 1
        else:
            done = True
        inList[left], inList[last - 1] = inList[last - 1], inList[left]
    quickSortRec(inList, first, left - 1)
    quickSortRec(inList, left + 1, last)


def mergeSortRec(inList, first, last):
    if first < last:
        mid = (first + last) // 2
        mergeSortRec(inList, first, mid)
        mergeSortRec(inList, mid + 1, last)
        merge(inList, first, mid, last)


def merge(inList, low, mid, high):
    temp = [0] * len(inList)
    for z in range(low, high + 1):
        temp[z] = inList[z]

    first = low
    sec = mid + 1

    for z in range(low, high + 1):
        if first > mid:
            inList[z] = temp[sec]
            sec += 1

        elif sec > high:
            inList[z] = temp[first]
            first += 1

        elif temp[sec] < temp[first]:
            inList[z] = temp[sec]
            sec += 1

        else:
            inList[z] = temp[first]
            first += 1

# Actual sorting methods
def bubbleSort(inList):
    for i in range(len(inList)):
        for j in range(len(inList) - i - 1):
            if inList[j] > inList[j+1]:
                inList[j], inList[j+1] = inList[j+1], inList[j]


def insertionSort(inList):
    for place in range(1, len(inList)):
        temp = inList[place]
        i = place
        while i > 0 and inList[i-1] > temp:
            inList[i] = inList[i-1]
            i -= 1
        inList[i] = temp


def selectionSort(inList):
    length = len(inList)
    for i in range(0, length):
        maxIndex = 0
        for j in range(1, length - i):
            if inList[j] > inList[maxIndex]:
                maxIndex = j
        inList[maxIndex], inList[length - i - 1] = inList[length - i - 1], inList[maxIndex]

def mergeSort(inList):
    last = len(inList) - 1
    mergeSortRec(inList, 0, last)


def quickSort(inList):
    size = len(inList)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            temp = inList[i]
            j = i
            while j >= gap and temp < inList[j - gap]:
                inList[j] = inList[j - gap]
                j -= gap
            inList[j] = temp
        if gap == 2:
            gap = 1
        else:
            gap = int(gap / 2.2)


