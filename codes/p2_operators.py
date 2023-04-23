'''Following are the different types of operators in Python -

1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators
'''

a = 3
b = 4

# Arithmetic Operators
print("The value of 3+4 is ", 3+4)
print("The value of 3-4 is ", 3-4)
print("The value of 3*4 is ", 3*4)
print("The value of 3/4 is ", 3/4)

# Assignment Operators
a = 34
a -= 12
a *= 12
a /= 12
print(a)

# Comparison Operators
# b = (14<=7)
# b = (14>=7)
# b = (14<7)
# b = (14>7)
# b = (14==7)
b = (14!=7)
print(b)

# Logical Operators
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is", (bool1 or bool2))
print("The value of not bool2 is", (not bool2))

# Identity Operators : is , is not
print("a is b: ",a is b)
print("a is not b: ",a is not b)

# Membership Operators: in , not in
x = ["apple", "banana"]
print("banana in x: ","banana" in x)
print("pineapple not in x: ","pineapple" not in x)

# Bitwise Operator 
a = 10
b = 4
# Print bitwise AND operation
print("a & b: ",a & b)

# Print bitwise OR operation
print("a | b: ",a | b)
 
# Print bitwise NOT operation
print("a ~ b: ",~a)
 
# print bitwise XOR operation
print("a ^ b: ",a ^ b)
 
# print bitwise right shift operation
print("a >> 2: ",a >> 2)
 
# print bitwise left shift operation
print("a << 2: ",a << 2)