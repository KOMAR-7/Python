# # Read a file:
# f = open("myText.txt","r")
# print(f.read()) # I will read whole file
# print(f.read(5)) # I will read only 5 characters
# print(f.readline()) # I will read only the first line and if you use again I will go for the second line
# f.close() # I will close the file
# # Write a file:
# f = open("myText.txt","w")
# f.write("I will delete the previous word or in simple word I will overwrite")
# f = open("myText.txt","a")
# f.write("I will append your words to the current file")
# f = open("newText.txt","x")
# f.write("I will create a file if not present and I will raise an error if the file is already present")
# # Delete a file:
# import os
# os.remove("newText.txt")
# # Check and delete:
# import os
# if os.path.exists("newText.txt"):
#   os.remove("newText.txt")
# else:
#   print("The file does not exist")
# # Delete Folder:
# import os
# os.rmdir("forRemove")
# # Note: You can only remove empty folders.
# # with statement

# file handling
 
# # 1) without using with statement
# f = open('myFile.txt', 'w')
# f.write('Hello Madi!')
# f.close()
 
# # 2) without using with statement
# f = open('myFile.txt', 'w')
# try:
#     f.write('Hello Madi')
# finally:
#     f.close()

# #3) using with statement
# with open('myFile.txt', 'w') as f:
#     f.write('Hello Madi!')

# with open("myFile.txt","r") as f:
#     f.read()

# Replace content
with open("myFile.txt") as f:
    content=f.read()

content = content.replace("Hello","Omar")
with open("myFile.txt","w") as f:
        f.write(content)
