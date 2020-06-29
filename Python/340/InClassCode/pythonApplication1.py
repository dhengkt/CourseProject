import mod1
import importlib

#for i in mod1.__dic__.keys():
#    print(i)

print(mod1.var1)
mod1.var1 = 77
print(mod1.var1)
import mod1
print(mod1.var1)

importlib.reload(mod1)
print(mod1.var1)

import mod1
from mod1 import list1
from mod1 import var1

print(list1, var1)
var1 = 7
list1[0] = "giraffe"
print(list1, var1)
print(mod1.list1, mod1.var1)
