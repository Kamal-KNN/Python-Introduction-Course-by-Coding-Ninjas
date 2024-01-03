from os import *
from sys import *
from collections import *
from math import *
num = int(input())    # Get the input number from the user

# Calculate the number of digits in the input number
num_digits = len(str(num))

# Calculate the sum of the cubes of each digit in the input number
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** num_digits
    temp //= 10

# Determine if the input number is an Armstrong number or not
if num == sum:
    print("true")
else:
    print("false")
