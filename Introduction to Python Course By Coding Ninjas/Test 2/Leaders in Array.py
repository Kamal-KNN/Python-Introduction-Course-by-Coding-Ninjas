## Read input as specified in the question.
## Print output as specified in the question.
n= int(input())
a = input().strip().split(' ')
A = list(map(int, a))
for i in range(0, n):
    for j in range(i+1, n):
        if A[i]<A[j]:
            break
        if j == n-1:
            print (A[i],end=' ')
print(A[n-1])