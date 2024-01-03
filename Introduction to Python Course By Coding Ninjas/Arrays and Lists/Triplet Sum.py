from sys import stdin

def findTriplet(arr, n, x) :
    #Your code goes here
    #return your answer
    result=[]
    for i in range(n-1):
        for j in range(i+1,n):
            pair=arr[i]+arr[j]
            for k in range(j+1,n):
                if pair+arr[k]==x:
                    result.append((arr[i],arr[j],arr[k]))
    return len(result)


