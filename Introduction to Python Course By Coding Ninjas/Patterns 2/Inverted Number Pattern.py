n = int(input())
currRow = 1
while currRow <= n:
    currCol = 1
    while currCol <= (n - currRow + 1) :
        print(n - currRow + 1, end = "")
        currCol += 1
    print()
    currRow += 1