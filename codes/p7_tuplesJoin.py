# To join two or more tuples you can use the + operator:
# Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3) # ('a', 'b', 'c', 1, 2, 3)

# Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:
# Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple) # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')