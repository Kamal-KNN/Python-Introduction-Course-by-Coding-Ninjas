n=int(input())
i=1
while i<=n:
    j=1
    p=i
    space=1
    
    while j<=i:
        print(j,end="")
        j=j+1
    
    while space<=2*n-2*i:
        print(" ",end="")
        space=space+1
    while p>=1:
        print(p,end="")
        p=p-1
    print()
    i=i+1
