from math import *
from collections import *
from sys import *
from os import *
## Read input as specified in
## Print output as specified in
n=int(input())
n1, n2=0,1
count=1
if n==1:
    print(n)
else:
    while count<n:
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
    print(nth)