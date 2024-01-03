from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
while i<=n:
    j=1
    while j<=n-i+1:
        if i%2==0:
            print("0",end="")
        
        else:
                print("1",end="")
        #print(j,end="")
        j=j+1
    print()
    i=i+1