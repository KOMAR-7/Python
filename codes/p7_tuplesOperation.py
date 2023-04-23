# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# *********Add Items*********
print("*********Add Items*********")
x = ("apple", "banana", "cherry")
y = list(x) # type cast into list
y[1] = "kiwi" # perform list operation
x = tuple(y) # type case back to tuple
print(x) # ("apple", "kiwi", "cherry")

a = ("apple", "banana", "cherry")
b = ("orange",)
a += b
print(a)

# *********Remove Items*********
print("*********Remove Items*********")
# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items
tupleRem = ("apple", "banana", "cherry")
y = list(tupleRem)
y.remove("apple")
tupleRem = tuple(y) # ('banana', 'cherry')