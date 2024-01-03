from os import *
from sys import *
from collections import *
from math import *


def ninjaPuzzle(n):

    for i in range(0,n):
        for j in range(0,n):
            if i>j:
                print(" ",end="")
            else:
                print("*",end="")
        print();


    