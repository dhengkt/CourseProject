class myClass:
    a = 1
    def __init__(self, value = 0):
        b = value
        self.c = value + 1
        self.__d = value + 2

x = myClass(5)
x.e = 8
#print(x.a, x.b, x.c, x.__d, x.e)
#print(x.a, x.c, x.__d, x.e)
print(x.a, x.c, x.e)

y = myClass(12)
y.a = 16
print(x.a, x.c, x.e)
#print(y.a, y.c, y.e)
print(y.a, y.c)

myClass.a = -13
print(x.a, x.c, x.e)
print(y.a, y.c)