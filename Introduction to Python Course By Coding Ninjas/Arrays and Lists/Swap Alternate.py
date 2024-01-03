from sys import stdin

def swapAlternate(arr, n) :
    #Your code goes here
    for i in range(1,len(arr),2):
        arr[i-1],arr[i]=arr[i],arr[i-1]