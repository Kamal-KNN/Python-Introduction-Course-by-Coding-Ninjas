n = int(input())
currRow = 1
while currRow <= n:
    currCol = 1
    ch = ord('A') + currRow - 1
    while currCol <= currRow:
        print(chr(ch), end = "")
        currCol += 1
    print()
    currRow += 1