# python program to check if x is a perfect square
import math


def is_fibonacci(n):
    sqrt1 = math.sqrt(5*n*n + 4)
    sqrt2 = math.sqrt(5*n*n - 4)
    if int(sqrt1)**2 == 5*n*n + 4 or int(sqrt2)**2 == 5*n*n - 4:
        print('true')
    else:
        print('false') 
n=int(input())
kamal=is_fibonacci(n)

