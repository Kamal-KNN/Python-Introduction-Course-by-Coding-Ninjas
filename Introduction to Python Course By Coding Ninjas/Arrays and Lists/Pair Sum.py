
from sys import stdin


def pairSum(arr, n, x) :
    pair=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==x:
                pair.append((arr[i],arr[j]))
    return len(pair)