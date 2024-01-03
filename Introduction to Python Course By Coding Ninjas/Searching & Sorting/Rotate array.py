from sys import stdin


def rotate(arr, n, d):
    #Your code goes here
    li=[]
    for i in range(d):
        li.append(arr[i])
    for i in range(d,n):
        arr[i-d]=arr[i]
    for i in range(d):
        arr[len(arr)-d+i]=li[i]
    return arr


    
    

























#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1