fruit = ["apple", "banana", "cherry"]
fruit[1] = "blackcurrant"
print(fruit) # ['apple', 'blackcurrant', 'cherry']

fruit1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
fruit1[1:3] = ["blackcurrant", "watermelon"]
print(fruit1) # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

fruit2 = ["apple", "banana", "cherry"]
fruit2[1:2] = ["blackcurrant", "watermelon"]
print(fruit2) # ['apple', 'blackcurrant', 'watermelon', 'cherry']

fruit3 = ["apple", "banana", "cherry"]
fruit3[1:3] = ["watermelon"]
print(fruit3) # ['apple', 'watermelon']

# *********Add Items*********
print("*********Add Items*********")
# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index

fruitIns = ["apple", "banana", "cherry"]
fruitIns.insert(2, "watermelon")
print(fruitIns) # ['apple', 'banana', 'watermelon', 'cherry']

# Append
# To add an item to the end of the list, use the append() method
fruitApp = ["apple", "banana", "cherry"]
fruitApp.append("orange")
print(fruitApp) # ['apple', 'banana', 'cherry', 'orange']

# Extend
# To append elements from another list to the current list, use the extend() method.
# The elements will be added to the end of the list.
fruits = ["apple", "banana", "cherry"]
fruitsExtend = ("mango", "pineapple", "papaya")
fruits.extend(fruitsExtend)
print(fruits) # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# *********Remove Item*********
print("*********Remove Item*********")
# remove(item)
# The remove() method removes the specified item.
fruitRem = ["apple", "banana", "cherry"]
fruitRem.remove("banana")
print(fruitRem) # ["apple", "cherry"]

# pop(index)
# The pop() method removes the specified index
# If you do not specify the index, the pop() method removes the last item.
fruitPop = ["apple", "banana", "cherry"]
fruitPop.pop(1) # ["apple", "cherry"]
# fruitPop.pop() #  ["apple", "banana"]
print(fruitPop)

# del listName[index]
fruitDel = ["apple", "banana", "cherry"]
del fruitDel[0] # ['banana', 'cherry']
print(fruitDel)
# The del keyword can also delete the list completely.
del fruitDel
# print(fruitDel) error (fruitDel not defined)

# clear()
# The clear() method empties the list.
# The list still remains, but it has no content.
# Clear the list content:

fruitClr = ["apple", "banana", "cherry"]
fruitClr.clear()
print(fruitClr)

# *********Sort List*********
print("*********Sort List*********")
# Sort the list alphabetically:
fruitSrt = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruitSrt.sort()
print(fruitSrt) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# Sort the list numerically:
fruitPriceSrt = [100, 50, 65, 82, 23]
fruitPriceSrt.sort()
print(fruitPriceSrt) # [23, 50, 65, 82, 100]

# Sort the list descending:
revSort = [100, 50, 65, 82, 23]
revSort.sort(reverse = True)
print(revSort) # [100, 82, 65, 50, 23]
# or
# revSort.reverse()
# print(revSort)