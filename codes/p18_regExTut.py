import re
#Check if the string starts with "Madi" and ends with "perfect":
txt = "Madi is perfect"
x = re.search("^Madi.*perfect$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")

# Python is executable pseudocode. Perl is executable line noise.
# Python is an experiment in how much freedom programmers need. Too much freedom and nobody can read another's code; too little and expressiveness is endangered.

txt = '''Python is an experiment in how much freedom programmers need. Too much freedom and nobody can read another's code; too little and expressiveness is endangered.'''

# findall function:
x = re.findall("an", txt)
print(x) # ['an', 'an', 'an', 'an', 'an', 'an']

# search function:
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())
# The first white-space character is located in position: 6

# split function:
x = re.split("\s", txt);print(x)
# ['Python', 'is', 'an', 'experiment', 'in', 'how', 'much', 'freedom', 'programmers', 'need.', 'Too', 'much', 'freedom', 'and', 'nobody', 'can', 'read', "another's", 'code;', 'too', 'little', 'and', 'expressiveness', 'is', 'endangered.']
# You can control the number of occurrences by specifying the maxsplit parameter.
# x = re.split("\s", txt, 1)
# ['Python', 'is', 'an', 'experiment', 'in', 'how', 'much', 'freedom', 'programmers', 'need.', "Too much freedom and nobody can read another's code; too little and expressiveness is endangered."]

# sub function:
x = re.sub("\s",r"/", txt)
print(x)
# Python/is/an/experiment/in/how/much/freedom/programmers/need./Too/much/freedom/and/nobody/can/read/another's/code;/too/little/and/expressiveness/is/endangered.
# # You can control the number of replacements by specifying the count parameter:
# x = re.sub("\s",r"/", txt,7)
# print(x)
# # Python/is/an/experiment/in/how/much/freedom programmers need. Too much freedom and nobody can read another's code; too little and expressiveness is endangered.

# compile function
import re

# Target String one
str1 = "Madi's luck numbers are 555 75 777"

# pattern to find three consecutive digits
string_pattern = r"\d{3}"
# compile string pattern to re.Pattern object
regex_pattern = re.compile(string_pattern)

# print the type of compiled pattern
print(type(regex_pattern))
# Output <class 're.Pattern'>

# find all the matches in string one
result = regex_pattern.findall(str1)
print(result)
# Output ['555', '777']

# Target String two
str2 = "Neuro's luck numbers are 111 212 415"
# find all the matches in second string by reusing the same pattern
result = regex_pattern.findall(str2)
print(result)
# Output ['111', '212', '415']

