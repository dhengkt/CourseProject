import random
import sort
LIST_SIZE = 100

l = []
for i in range(LIST_SIZE):
    randNumber = random.randint(0, 10*LIST_SIZE)
    l.append(randNumber)


print(l)
sort.mergeSort(l)
print(l)