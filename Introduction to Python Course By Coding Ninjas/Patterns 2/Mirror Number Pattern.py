n = int(input())
currRow = 1
while currRow <= n:
    currCol = 1
    spaces = 1
    while spaces <= n - currRow :
        print(" ", end = "")
        spaces += 1
    while currCol <= currRow:

        print(currCol, end = "")
        currCol += 1
    print()
    currRow += 1