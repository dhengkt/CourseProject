# Just for review since the professor will collect the quiz back

# Problem 1
a = 'a'
b = 'b'
c = 'c'

def f1(c, d):
    global b
    a = 'x'
    myName = a + b + c +d
    b = 'r'
    a = 'y'
    return myName, a

myName, d = f1('j', 'd')
print(myName)
myName = a + b + c + d
print(myName)

# Problem 2
class myClass:
    attr1 = 1
    def __init__(self, val = -1):
        attr2 = val
        self.attr3 = val + 1
        self.__attr4 = attr2 + 2


x = myClass(22)
y = myClass(14)
x.attr5 = 8
y.attr1 = 7
print(x.attr1)
print(x.attr3)
print(x.attr5)

# Problem 4
def removeDups(list):
    size = len(list)
    i = 0
    while i < size:
        j = i + 1
        while j < size:
            if list[i] == list[j]:
                list.remove(list[j])
                size = size - 1
            else:
                j += 1
        i += 1
    return list

list1 = [1, 2, 3, 2, 5, 6]
list2 = removeDups(list1)
print(list2)

