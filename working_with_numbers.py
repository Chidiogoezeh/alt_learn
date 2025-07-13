# Python can differentiate between floating numbers and integers\
# working with said as at when needed.
#Ypu can run arithematic operations in pyhton. This include +, -, *, /
print(4 + 5)
print(2 + 4.75)
print(-4.856)
# For complex mathematical operation, theorder of operation can be specified
print(4 * (7 + 3))
# the modulous operation can also be used
print(24 % 5) # Read as 24 mod 5. Here we are looking for the remainder
# Numbers can also be stored inside of variables
my_num = 7
print(my_num) # This numbercan be converted to a string
print(str(my_num)) # This is useful when you want to print numbers alongside strings
print(str(my_num) + " is my favorite number")
# Some of the most common functions related to numbers used in python
my_num = -5
print(abs(my_num)) # abs function gives the absolute value of any number
print(pow(4, 7)) # pow function allows the passage of 2 pieces of information, 1: number, 2: power to raise number to
print(max(1, 4)) # max function simply returns the larger of the 2 numbers passed into it
print(min(1, 4)) # max function simply returns the smaller of the 2 numbers passed into it
print(round(4.7)) # This allows the roundong of numbers from decimal places to round numbers also known as integers

# More python functions can be imported using
from math import * # This is a math modules that gives access to a lot of maths functions
print(floor(4.7)) # Floor simply drops the decimal point and verything after the decimal point
print(ceil(4.7)) # Ceil simply rounds the decimal 
print(sqrt(9)) # This gives the square root of a number
