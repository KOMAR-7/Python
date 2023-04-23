# Get the characters from position 2 to position 5 (not included):
b = "Hello, Madi!"
print(b[2:5]) #ell

# Get the characters from the start to position 5 (not included):
b = "Hello, Madi!"
print(b[:5]) #Hello

# Get the characters from position 2, and all the way to the end:
b = "Hello, Madi!"
print(b[2:]) #llo, Madi

# Get the characters:
# From: "a" in "World!" (position -5) 
# To, but not included: "i" in "World!" (position -2):
b = "Hello, Madi!"
#    0123456789..
#    .........-2-1
print(b[-4:-2]) #ad
#    start:not include
b = "Madistic"
print(b[0::2]) # Mdsi
#    start:end:skipAfter