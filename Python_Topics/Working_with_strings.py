# Working with strings in Python, which is basically plain text
# \n is used to break strings into different lines during execution of code
# \" is used to put a quotation mark in your python string
# \ used to print out a back slash in python string

print("Altschool Africa")

# Values can be assigned to variables
phrase = "Altschool Africa"
print(phrase)

# Concatanate string is taking a string and apemdimg another string to it.
print(phrase + " is a cool institution to study")

# Strings are used in pyhton functions, functions are basically another block \
#  of code of code we can run, it will perform a specific operation for us.\
# Functions can be used to modify our strings and also get information about our strings

#Convert to a lower case
print(phrase.lower())
# Convert to upper case
print(phrase.upper())
# Check whether string is upper or lower case. Value is either true or false
print(phrase.isupper())
print(phrase.islower())
print(phrase.upper().isupper())

#Figure out the length of a string
print(len(phrase))

# Determine a specific character using the imdex of the character.\
# Pyhton index starts from 0
print(phrase[0])
print(phrase[4])

# Index function indicates where a specific character or string is located
print(phrase.index("A"))
print(phrase.index("Africa"))

# You can also replace strings with the replace function. First word is\ 
#  to be replaced, second word is what to replace the first word with
print(phrase.replace("Altschool", "Bestschool"))
