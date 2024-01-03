from os import *
from sys import *
from collections import *
from math import *
n = int(input())
m = 2*n+1
for i in range(1,n+1):
    for j in range(1,m+1):
        
        if(j==((m+1)//2)):
            print("*",end="")
        elif(i==j or (m-i+1)==j):
            print("*",end="")
        else:
            print("0",end="")
    print("")
