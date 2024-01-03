from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
while i<=n:
    j=i
    p=2
    space=1
    while space<=n-i:
        print(" ",end="")
        space=space+1
    while j>=1:
        print(j,end="")
        j=j-1
    while p<=i:
        print(p,end="")
        p=p+1
    print()
    i=i+1