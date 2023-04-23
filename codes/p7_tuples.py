# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# A tuple can contain different data types:
fruit = ("apple", "banana", "cherry")
print(fruit) # ('apple', 'banana', 'cherry')

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
# One item tuple, remember the comma:
oneTpl = ("apple",)
print(type(oneTpl)) # <class 'tuple'>

#NOT a tuple
ntTpl = ("apple")
print(type(ntTpl)) # <class 'str'>