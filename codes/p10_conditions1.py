a, b = 6, 5  
if a > b:  
    code = "a is greater than b"  
    print(code)  

# Else statement
if a < b:  
    code = "a is less than b"  
    print(code)  
else:  
    print("a is greater than b") 

# Elif statement
a, b = 9, 9  
  
# Initializing the if-else condition  
if a < b:  
    code = "a is less than b"  
elif a == b:  
    code = "a is equal to b"  
else:  
    code = "a is greater than b"  
  
print(code)  

# Nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# The Short hand if
# If you have only one statement to execute, you can put it on the same line as the if statement.
print("Short Hand If")
a = 7
if a<18: print("Number is smaller than 18")

# The Short hand if else
# if you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
print("Short Hand If ... Else")
print("You are not legally official") if age<18 else print("You are legally official")

# The use of And
# The and keyword is a logical operator, and is used to combine conditional statements:
print("Use of And")
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# The use of Or
# The or keyword is a logical operator, and is used to combine conditional statements:
print("Use of Or")
if a > b or a > c:
  print("At least one of the conditions is True")

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
print("Use of pass")
a = 33
b = 200
if b > a:
  pass

# in and is
print("use of in and is")
a=7
b=5
if a is 5:
    print("a is 5")
elif a is 7:
    print("a is 7")
else:
    print("a is not 5 or 7")

a = [1,2,3]
if 2 in a:
    print("2 is present in a")
else:
    print("2 is not present in a")
