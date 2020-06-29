import random



l1 = []
for o in range(10):
    randomNumber = random.randint(0, 100)
    l1.append(randomNumber)

print(l1)
IterativeMergeSort(l1)
print(l1)
