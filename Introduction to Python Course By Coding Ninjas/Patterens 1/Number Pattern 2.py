from collections import *
from os import *
from sys import *
from math import *


n = int(input())
print(1)
row = 1
while row <= n-1:
    col = 1
    while col <= row+1:
        if (col == 1 or col >= row+1):
            print(row, end="")
        else:
            print("0", end="")
        col = col + 1
    print()
    row = row + 1