# Codes from midterm
# Question 2
a = 13
b = 14
value = 2
def myFunc(value, theList):
    global b
    theList[value] = 13
    a = 7
    value = a
    b = theList[0]
    return value

list1 = [1, "cat", [2, "cat"], {value:"dog"}]
value += 1
print(list1)
print(a, b, value)
d = myFunc(value, list1)
print(list1)
print(a, b, d, value)
list2 = []
list2.extend(list1)
list1[1:-1] = [1, 2, 3, 4]
print(list1)
print(list2)

# Question 3
# New Catalan Number
# C(n + 1) = sum((k+1) * C(n-k)) which C0 = 1
def theCat(n):
    result = 0
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    for i in range(n):
        result += (i + 1) * theCat(n - i - 1)
    return result

# Question 4
# Write a function which takes in the name of a file as an argument
# and counts the number of occurrences of each word in the file.
# It should print to the console the word and count of each of them.
# NOTE: I used Dictionary to store words and their count.
# The code I wrote can work, but I had wrong syntax.
def countWords(filename):
    words = []
    wordDic = {}
    file = open(filename, 'r')
    line = file.readline()
    while not line == "":
        words = line.split()
        for word in words:
            if word in wordDic:
                wordDic[word] += 1
            else:
                wordDic[word] = 1
    for item in wordDic:
        print("{} occurs {} times".format(item, wordDic[item]))


# Same question code by Professor
def uniqueOccurences(filename):
    words = {}
    theFile = open(filename)
    for line in theFile:
        for word in line.split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    for w in words:
        print(w, words[w])
