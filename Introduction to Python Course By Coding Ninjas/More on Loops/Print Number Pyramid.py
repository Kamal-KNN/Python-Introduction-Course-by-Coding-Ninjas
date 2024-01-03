n = int(input())

j = 1

while n >= j:
    for i in range(1, j):
        print(" ", end="")
    for i in range(j, n+1):
        print(i, end="")
    print("")
    j += 1

j = n - 1
while j >= 1:
    for i in range(1, j):
        print(" ", end="")
    for i in range(j, n):
        print(i, end="")
    print(n, end="")
    for i in range(j, n-1):
        print(" ", end="")
    print("")
    j -= 1