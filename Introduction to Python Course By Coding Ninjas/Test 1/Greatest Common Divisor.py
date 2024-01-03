from os import *
from sys import *
from collections import *
from math import *
def findGcd(X, Y):

    while Y != 0:
        X, Y = Y, X % Y
    return X


    t = int(input())

    for _ in range(t):
        X, Y = map(int, input().split())
        print(gcd(X, Y))