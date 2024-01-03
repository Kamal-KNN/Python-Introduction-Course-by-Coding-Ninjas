def search(nums: [int], target: int):
    # write your code logic !!
    n=len(nums)-1
    s=0
    e=n-1
    while s<=e:
        mid=(s+e)>>1
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            e=mid-1
        else:
            s=mid+1
    return -1




    
n= int (input())
arr = list(map(int,input().strip().split()))[:n]
target =int (input())
print (search(arr, target))
