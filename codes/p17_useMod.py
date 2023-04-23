import p17_toImportMod as pMod
import platform
import math


pMod.greeting("Madi")

a = pMod.person1["age"]
print(a)

x = platform.system()
print(x)
# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

d = dir(math)
print(d)
print(math.sqrt(4))
print(dir(pMod))