from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
# Python program to
# print Diamond shape

# Function to print
# Diamond shape
n=int(input())

i=1
a=(n//2)+1
for i in range(1,a+1):
    j=1
    for j in range(1,n+1):
        if j>=(a+1)-i and j<a+i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    # For lower portion
b=n//2
i=1
for i in range(1,b+1):
    j=1
    for j in range(1,n):
        if j>=i+1 and j<=n-i :
            print("*",end="")
        else :
            print(" ",end="")
    print()


# Driver Code
# number of rows input

