
# The while loop:
i = 1
while i < 6:
  print(i)
  i += 1
# 1 2 3 4 5 6
# Remember to increment i, or else the loop will continue forever.

# The break Statement

# Exit the loop when i is 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
# 1 2 3

# skip loop when i=3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
# 1 2 4 5 6

# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true

# Print a message once the condition is false:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

i=0
fruits= ["CustardApple","Watermelon","Banana"]
while i<len(fruits):
    print(fruits[i])
    i=i+1
# CustardApple Watermelon Banana
# *********For Loop*********

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# The for loop does not require an indexing variable to set beforehand.

for i in "Madi":
    print(i)   
# M a d i

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(6):
  print(x)
# range(6) is not the values of 0 to 6, but the values 0 to 5.

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)
# 2 5 8 11 14 17 20 23 26 29

