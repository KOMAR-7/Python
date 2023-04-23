# Strings in python are surrounded by either single quotation marks, or double quotation marks.
a = "Madi"
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
a = 'Madi'
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, Madi!"
print(a[1]) #e
# String Length
print("Length of a string: ",len(a)) #12
# Check in String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "Madi is perfect"
print("Madi" in txt) #true
print("Madi" not in txt) #false