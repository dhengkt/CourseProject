import random


# Iterative mergesort function to
# sort arr[0...n-1]
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


l1 = []
for o in range(10):
    randomNumber = random.randint(0, 100)
    l1.append(randomNumber)

print(l1)
IterativeMergeSort(l1)
print(l1)
