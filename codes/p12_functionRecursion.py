# Function
def perfect():
    print("Madi is perfect")


perfect()  # function calling

# Function with Paramenter


def message(myName):
    print("Brooooo ", myName, ", Madi is a feeling!!!")


message("Omar")


def myArgsFunc(*pracHb):
    print("I am from myArgsFunc")
    print("The hobby to be played now: " + pracHb[1])

myArgsFunc("Chess", "Football", "Cricket")


def myKeyArgs(hobby1, hobby2, hobby3):
    print("I am from myKeyArgs")
    print("The hobby to be played now: " + hobby2)

myKeyArgs(hobby1="Chess", hobby2="Football", hobby3="Cricket")


def arbKeyArg(**ch):
    print("Arbitary Keyword Arguments")
    print("Madi is " + ch["heart"])


arbKeyArg(heart="Feeling", face="Emotion")


def defaArg(country="India"):
    print("I am from default argument")
    print("I am from " + country)


defaArg()


def listAsArg(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

listAsArg(fruits)


def retFunc(x):
    return 5 * x

print(retFunc(3))
print(retFunc(5))
print(retFunc(9))


def willUse():
    pass

# Recurssion:
# n = 5
# product = 1
# for i in range(n):
#     product= product*(i+1)
# print(product)


def factIter(n):
    product = 1
    for i in range(n):
        product = product*(i+1)
    return product


f = factIter(5)
print(f)

# n! = 1*2*3*4*5*.....*n
# n! = [1*2*3*4*5*n-1]*n
# n! = n*(n-1)!
print("Recursive Function")


def factRecurssive(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factRecurssive(n-1)


fr = factRecurssive(3)
print("Recursive Factorial is ",fr)

# Lambda Function / Anonymous Function / one liner Function:
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# def myAdd(x,y):
# 	return x+y

# print(myAdd(5,7))

x = lambda a, b: a + b
print(x(7, 5))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# Ex2.
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))