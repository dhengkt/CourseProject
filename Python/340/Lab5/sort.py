# Created by HsinYu Chi
# Helper function
def merge(inList, start, mid, end):
    temp = [0] * len(inList)
    for i in range(start, end + 1):
        temp[i] = inList[i]

    first = start
    sec = mid + 1

    for j in range(start, end + 1):
        if first > mid:
            inList[j] = temp[sec]
            sec += 1

        elif sec > end:
            inList[j] = temp[first]
            first += 1

        elif temp[sec] < temp[first]:
            inList[j] = temp[sec]
            sec += 1

        else:
            inList[j] = temp[first]
            first += 1


def mergeSortRec(inList, first, last):
    if first < last:
        mid = (first + last) // 2
        mergeSortRec(inList, first, mid)
        mergeSortRec(inList, mid + 1, last)
        merge(inList, first, mid, last)


def quickSortRec(inList, first, last):
    if first < last:
        split = partition(inList, first, last)
        quickSortRec(inList, first, split - 1)
        quickSortRec(inList, split + 1, last)

def partition(inList, first, last):
    pivot = inList[first]
    left = first + 1
    right = last
    done = False

    while not done:
        while left <= right and inList[left] <= pivot:
            left += 1

        while inList[right] >= pivot and right >= left:
            right -= 1

        if right < left:
            done = True
        else:
            temp = inList[left]
            inList[left], inList[right] = inList[right], temp

    temp = inList[first]
    inList[first], inList[right] = inList[right], temp
    return right


# Sorting Methods
def BubbleSort(inList):
    for i in range(len(inList)):
        for j in range(len(inList) - i - 1):
            if inList[j] > inList[j+1]:
                inList[j], inList[j+1] = inList[j+1], inList[j]


def InsertionSort(inList):
    for place in range(1, len(inList)):
        temp = inList[place]
        i = place
        while i > 0 and inList[i-1] > temp:
            inList[i] = inList[i-1]
            i -= 1
        inList[i] = temp


def MergeSort(inList):
    last = len(inList) - 1
    mergeSortRec(inList, 0, last)


def IterativeMergeSort(list):
    length = len(list)
    temp = [0] * length
    size = 1
    while size < length:
        pos = 0
        while pos < length:
            if pos + 2 * size - 1 >= length:
                merge(list, pos, pos + size - 1, length - 1)
            else:
                merge(list, pos, pos + size - 1, pos + 2 * size - 1)
            pos += 2 * size
        size += size


def QuickSort(inList):
    quickSortRec(inList, 0, len(inList) - 1)


def ShellSort(inList):
    length = len(inList)
    gap = length // 2

    while gap > 0:
        for i in range(gap, length):
            temp = inList[i]
            j = i
            while j >= gap and inList[j - gap] > temp:
                inList[j] = inList[j - gap]
                j -= gap
            inList[j] = temp
        gap //= 2
