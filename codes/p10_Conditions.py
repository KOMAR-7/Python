# Equals: a == b # Relational Operator
# Not Equals: a != b # Relational Operator
# Less than: a < b # Comparison Operator
# Less than or equal to: a <= b # Relational Operator
# Greater than: a > b # Comparison Operator
# Greater than or equal to: a >= b # Relational Operator

age = int(input("Enter your Age: "))
if(age<18):
    print("Chota baccha hai")
elif(age<17):
    print("Ek saal aur rukja")
elif(age==18):
    print("Abhi to bada hua hai")
else:
    print("Waah bada ho chuka")

# Indentation
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.
# 4spaces or tab
# a = 33
# b = 200
# if b > a:
# print("b is greater than a") # you will get an error

# This technique is known as Ternary Operators, or Conditional Expressions.
# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.
print("Short Hand If")
a = 7
if a<18: print("Number is smaller than 18")

# Short Hand If ... Else
# if you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
print("Short Hand If ... Else")
print("You are not legally offcial") if age<18 else print("You are legally offcial")

# And
# The and keyword is a logical operator, and is used to combine conditional statements:
print("Use of And")
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# Or
# The or keyword is a logical operator, and is used to combine conditional statements:
print("Use of Or")
if a > b or a > c:
  print("At least one of the conditions is True")

# Not
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
print("Use of not")
if not a > b:
  print("a is NOT greater than b")

# Nested If
# You can have if statements inside if statements, this is called nested if statements.
print("Use of Nested If")
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

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