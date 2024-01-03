from typing import List

def bubbleSort(arr: List[int], size: int):
    # Your code goes here.
    for i in range(size-1):
        for j in range(size-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp