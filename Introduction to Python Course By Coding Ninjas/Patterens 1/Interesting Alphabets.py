from math import *
from collections import *
from sys import *
from os import *

n=int(input())
i=n
while i>=1:  
    j=i    
    while j<=n:        
        print(chr((64)+j),end="")        
        j=j+1    
    print()    
    i=i-1