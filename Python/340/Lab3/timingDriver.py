# This set of test codes is for determining the running time of each function
# in bigo.py. by using timeit module in Python.
# The list size starts with n = 10 to n = 1000.
# For the find4 function, the passed-in list is already sorted.
import timeit

# List size = 10
set10 = '''import bigo
list = []
value = 6
for i in range(11):
    list.append(i)'''

# Code snippet whose execution time is to be measured
find110 = '''bigo.find1(list, value)'''
find210 = '''bigo.find2(list, value)'''
find310 = '''bigo.find3(list, value)'''
find410 = '''bigo.find4(list, value)'''

print("List size = 10")
print(timeit.timeit(setup=set10, stmt=find110))
print(timeit.timeit(setup=set10, stmt=find210))
print(timeit.timeit(setup=set10, stmt=find310))
print(timeit.timeit(setup=set10, stmt=find410))
print()

# List size = 50
set50 = '''import bigo
list = []
value = 6
for i in range(51):
    list.append(i)'''

find150 = '''bigo.find1(list, value)'''
find250 = '''bigo.find2(list, value)'''
find350 = '''bigo.find3(list, value)'''
find450 = '''bigo.find4(list, value)'''

print("List size = 50")
print(timeit.timeit(setup=set50, stmt=find150))
print(timeit.timeit(setup=set50, stmt=find250))
print(timeit.timeit(setup=set50, stmt=find350))
print(timeit.timeit(setup=set50, stmt=find450))
print()

# List size = 100
set100 = '''import bigo
list = []
value = 6
for i in range(101):
    list.append(i)'''

find1100 = '''bigo.find1(list, value)'''
find2100 = '''bigo.find2(list, value)'''
find3100 = '''bigo.find3(list, value)'''
find4100 = '''bigo.find4(list, value)'''

print("List size = 100")
print(timeit.timeit(setup=set100, stmt=find1100))
print(timeit.timeit(setup=set100, stmt=find2100))
print(timeit.timeit(setup=set100, stmt=find3100))
print(timeit.timeit(setup=set100, stmt=find4100))
print()

# List size = 150
set150 = '''import bigo
list = []
value = 6
for i in range(151):
    list.append(i)'''

find1150 = '''bigo.find1(list, value)'''
find2150 = '''bigo.find2(list, value)'''
find3150 = '''bigo.find3(list, value)'''
find4150 = '''bigo.find4(list, value)'''

print("List size = 150")
print(timeit.timeit(setup=set150, stmt=find1150))
print(timeit.timeit(setup=set150, stmt=find2150))
print(timeit.timeit(setup=set150, stmt=find3150))
print(timeit.timeit(setup=set150, stmt=find4150))
print()

# List size = 200
set200 = '''import bigo
list = []
value = 6
for i in range(201):
    list.append(i)'''

find1200 = '''bigo.find1(list, value)'''
find2200 = '''bigo.find2(list, value)'''
find3200 = '''bigo.find3(list, value)'''
find4200 = '''bigo.find4(list, value)'''

print("List size = 200")
print(timeit.timeit(setup=set200, stmt=find1200))
print(timeit.timeit(setup=set200, stmt=find2200))
print(timeit.timeit(setup=set200, stmt=find3200))
print(timeit.timeit(setup=set200, stmt=find4200))
print()

# List size = 250
set250 = '''import bigo
list = []
value = 6
for i in range(251):
    list.append(i)'''

find1250 = '''bigo.find1(list, value)'''
find2250 = '''bigo.find2(list, value)'''
find3250 = '''bigo.find3(list, value)'''
find4250 = '''bigo.find4(list, value)'''

print("List size = 250")
print(timeit.timeit(setup=set250, stmt=find1250))
print(timeit.timeit(setup=set250, stmt=find2250))
print(timeit.timeit(setup=set250, stmt=find3250))
print(timeit.timeit(setup=set250, stmt=find4250))
print()

# List size = 500
set500 = '''import bigo
list = []
value = 6
for i in range(501):
    list.append(i)'''

find1500 = '''bigo.find1(list, value)'''
find2500 = '''bigo.find2(list, value)'''
find3500 = '''bigo.find3(list, value)'''
find4500 = '''bigo.find4(list, value)'''

print("List size = 500")
print(timeit.timeit(setup=set150, stmt=find1500))
print(timeit.timeit(setup=set150, stmt=find2500))
print(timeit.timeit(setup=set150, stmt=find3500))
print(timeit.timeit(setup=set150, stmt=find4500))
print()

# List size = 550
set550 = '''import bigo
list = []
value = 6
for i in range(551):
    list.append(i)'''

find1550 = '''bigo.find1(list, value)'''
find2550 = '''bigo.find2(list, value)'''
find3550 = '''bigo.find3(list, value)'''
find4550 = '''bigo.find4(list, value)'''

print("List size = 550")
print(timeit.timeit(setup=set150, stmt=find1550))
print(timeit.timeit(setup=set150, stmt=find2550))
print(timeit.timeit(setup=set150, stmt=find3550))
print(timeit.timeit(setup=set150, stmt=find4550))
print()

# List size = 1000
set1000 = '''import bigo
list = []
value = 6
for i in range(1001):
    list.append(i)
'''

find11000 = '''bigo.find1(list, value)'''
find21000 = '''bigo.find2(list, value)'''
find31000 = '''bigo.find3(list, value)'''
find41000 = '''bigo.find4(list, value)'''

print("List size = 1000")
print(timeit.timeit(setup=set1000, stmt=find11000))
print(timeit.timeit(setup=set1000, stmt=find21000))
print(timeit.timeit(setup=set1000, stmt=find31000))
print(timeit.timeit(setup=set1000, stmt=find41000))
