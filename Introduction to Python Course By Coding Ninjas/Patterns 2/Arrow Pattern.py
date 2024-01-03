n = int(input())
i = 0

# For upper arrow portion
while i <= n//2: 
    j = 0
    space = 0
    while space < i:
        print(" ", end="")
        space += 1
    while j <= i:
        print("* ", end="")
        j += 1
    print()
    i += 1

# For lower arrow portion
i = n//2 - 1
while i >= 0: 
    j = 0
    space = 0
    while space < i:
        print(" ", end="")
        space += 1
    while j <= i:
        print("* ", end="")
        j += 1
    print()
    i -= 1