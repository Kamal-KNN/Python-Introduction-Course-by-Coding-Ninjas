
import sys

def intersections(arr1, n, arr2, m) :
    #Your code goes here
    li=[]
    for i in arr1:
        if arr2.count(i)>0:
            print(i, end=" ")
            arr2.remove(i)
    # 
