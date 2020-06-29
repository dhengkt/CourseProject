import random
LIST_SIZE = 100
def IterativeMergeSort(a):
    current_size = 1
    while current_size < len(a) - 1:
        left = 0
        while left < len(a) - 1:
            mid = left + current_size - 1
            right = ((2 * current_size + left - 1, len(a) - 1)[2 * current_size + left - 1 > len(a) - 1])
            merge(a, left, mid, right)
            left = left + current_size * 2
        current_size = 2 * current_size

    # Merge Function


def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = a[l + i]
    for i in range(0, n2):
        R[i] = a[m + i + 1]

    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] > R[j]:
            a[k] = R[j]
            j += 1
        else:
            a[k] = L[i]
            i += 1
        k += 1

    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1

def MergeSort(inList):
    if len(inList) > 1:
        mid = len(inList) // 2
        left = inList[:mid]
        right = inList[mid:]

        MergeSort(left)
        MergeSort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                inList[k] = left[i]
                i += 1
            else:
                inList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            inList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            inList[k] = right[j]
            j += 1
            k += 1


# Driver code
a = [12, 11, 13, 5, 6, 7]
b = [12, 11, 13, 5, 6, 7]
print("Given arrays are ")
print(a)
print(b)

IterativeMergeSort(a)
MergeSort(b)

print("Sorted arrays are ")
print(a)
print(b)

l3 = []
for i in range(LIST_SIZE):
    randNumber = random.randint(0, 10 * LIST_SIZE)
    l3.append(randNumber)

print("Iterative Merge Sort")
IterativeMergeSort(l3)
print(l3)