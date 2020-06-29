# This driver code is for testing the basic functionality of bigo.py
import bigo
import random

def main():
    testList = []
    value1 = 6
    value2 = 16
    for i in range(11):
        testList.append(i)

    # Not sorted list
    nonSortedList = [2, 3, 1, 5, 4, 6, 8, 7, 10, 9]

    print("Basic Testing - value is in the list")
    print("{} is in the list: {}".format(value1, (bigo.find1(testList, value1))))
    print("{} is in the list: {}".format(value1, (bigo.find2(testList, value1))))
    print("{} is in the list: {}".format(value1, (bigo.find3(testList, value1))))
    print("{} is in the list: {}".format(value1, (bigo.find4(testList, value1))))
    print(bigo.find4(nonSortedList, value1))
    print()
    print("Basic Testing - value is not in the list")
    print("{} is in the list: {}".format(value2, (bigo.find1(testList, value2))))
    print("{} is in the list: {}".format(value2, (bigo.find2(testList, value2))))
    print("{} is in the list: {}".format(value2, (bigo.find3(testList, value2))))
    print("{} is in the list: {}".format(value2, (bigo.find4(testList, value2))))
    print(bigo.find4(nonSortedList, value2))
    print()

    # Putting random number in the list
    testList.clear()
    for k in range(11):
        testList.append(random.randint(0, 11))
    value1 = testList[5]
    value2 = random.randint(11, 50)

    print("Random Number Test - passed value is in the list")
    print("{} is in the list: {}".format(value1, (bigo.find1(testList, value1))))
    print("{} is in the list: {}".format(value1, (bigo.find2(testList, value1))))
    print("{} is in the list: {}".format(value1, (bigo.find3(testList, value1))))
    print("{} is in the list: {}".format(value1, (bigo.find4(testList, value1))))
    print()
    print("Random Number Test - passed value is not in the list")
    print("{} is in the list: {}".format(value2, (bigo.find1(testList, value2))))
    print("{} is in the list: {}".format(value2, (bigo.find2(testList, value2))))
    print("{} is in the list: {}".format(value2, (bigo.find3(testList, value2))))
    print("{} is in the list: {}".format(value2, (bigo.find4(testList, value2))))

main()
