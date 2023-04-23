# let us create a test string

testString1 = "Hello World!"
print("Original String: "+ testString1)
# Print(this string in lower case)

# Converting a string to lower case
print("Converting to LowerCase")
print(testString1.lower())

# Converting a string to upper case
print("Converting to Upper Case")
print(testString1.upper())

# Capitalizing a string
# Only the first letter in the string will be capitalized
print("Capitalizing the String")
print(testString1.capitalize())

# Trying to slice out a substring between given indexes
print("Substring from index 1 to 7")
print(testString1[1:8])

#Substring from the start till character at index = 7 (start of string is index 0)
print("Substring from the start till character at index = 7 (start of string is index 0): ")
print(testString1[:8])

#Substring from the character at index = 7, till the end of the string (remember: start of string is index 0)
print("Substring from the character at index = 7, till the end of the string (remember: start of string is index 0): ")
print(testString1[7:])


#Find the position of a  substring within the string
#This gives us the first index during a left to right scan. If the string is not found, it returns -1
print("Find the index from which the substring 'llo' begins within the test string")
print(testString1.find('llo'))

print("Now, let's look for a substring which is not a part of the given string")
print(testString1.find('xxy'))

# Now, trying to find the index of a substring between specified indexes only
print("Now, trying to find a substring between specified indexes only: looking for 'l' between 4 and 9")
print(testString1.find('l',4,9))

# rfind is used, to find the index from the reverse
# So, testString1.rfind('l') will look for the last index of l in the string
print("find('l') on the given string returns the following index (scanning the string from left to right):")
print(testString1.find('l'))

print("rfind('l') on the given string returns the following index (this scans the string from right to left):")
print(testString1.rfind('l'))

# Now let us try to replace/substitute a substring of this string with another string
print("Replacing World with Planet")
print(testString1.replace("World","Planet"))


# Now let us try to split the string, into separate words
# let us split it wherever there is a space
print("Splitting the string into words, wherever there is a space")
print(testString1.split(" "))
print(testString1.rsplit(" "))

# Remove leading and trailing whitespace characters
testString2 = "Hello World!  "
print("Current Test String=" + testString2)
# print("Length (there are whitespaces at the end):" + len(testString2))
# print("Length after stripping "+ len(testString2.strip()))

print("Example 2")
# Basic Functions
len('turtle') # 6

# Basic Methods
print('  I am alone '.strip())               # 'I am alone' --> Strips all whitespace characters from both ends.
print('On an island'.strip('d'))             # 'On an islan' --> # Strips all passed characters from both ends.
print('but life is good!'.split())           # ['but', 'life', 'is', 'good!']
print('Help me'.replace('me', 'you'))        # 'Help you' --> Replaces first with second param
print('Need to make fire'.startswith('Need'))# True
print('and cook rice'.endswith('rice'))      # True
print('bye bye'.index('e'))                  # 2
print('still there?'.upper())                # STILL THERE?
print('HELLO?!'.lower())                     # hello?!
print('ok, I am done.'.capitalize())         # 'Ok, I am done.'
print('oh hi there'.find('i'))               # 4 --> returns the starting index position of the first occurrence
print('oh hi there'.count('e'))              # 2

# Original String: Hello World!
# Converting to LowerCase
# hello world!
# Converting to Upper Case
# HELLO WORLD!
# Capitalizing the String
# Hello world!
# Substring from index 1 to 7
# ello Wo
# Substring from the start till character at index = 7 (start of string is index 0):
# Hello Wo
# Substring from the character at index = 7, till the end of the string (remember: start of string is index 0):
# orld!
# Find the index from which the substring 'llo' begins within the test string
# 2
# Now, let's look for a substring which is not a part of the given string
# -1
# Now, trying to find a substring between specified indexes only: looking for 'l' between 4 and 9
# -1
# find('l') on the given string returns the following index (scanning the string from left to right):
# 2
# rfind('l') on the given string returns the following index (this scans the string from right to left):
# 9
# Replacing World with Planet
# Hello Planet!
# Splitting the string into words, wherever there is a space
# ['Hello', 'World!']
# ['Hello', 'World!']
# Current Test String=Hello World!