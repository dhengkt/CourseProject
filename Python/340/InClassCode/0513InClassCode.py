# In-class Code questions
def intersection(list1, list2):
    ansList = []
    for elem in list1:
        if elem in list2 and not elem in ansList:
            ansList.append(elem)
    return ansList


def union(list1, list2):
    ansList = []
    ansList.extend(list1)
    for elem in list2:
        if not elem in ansList:
            ansList.append(elem)
    return ansList


l1 = [1, 3, 7, 9, "cat", 8, "dog"]
l2 = [3, 6, 9, "cat", 12]
print(intersection(l1, l2))
print(union(l1, l2))
