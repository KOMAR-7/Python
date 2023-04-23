# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# Packing a tuple:
fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green) # apple
print(yellow) # banana
print(red) # cherry

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
# Assign the rest of the values as a list called "red":

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green) # apple
print(tropic) # ['mango', 'papaya', 'pineapple']
print(red) # cherry