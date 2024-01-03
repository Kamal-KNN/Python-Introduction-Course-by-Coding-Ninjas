n = int(input())
s = 2 * n - 1
for i in range(0, int(s / 2)):
    m = n
    for j in range(0, i):
        print(m, end="")
        m -= 1
    for k in range(0, s - 2 * i):
        print(n-i, end="")
    m = n - i + 1
    for l in range(0, i):
        print(m, end="")
        m += 1

    print("")

for i in range(int(s / 2), -1, -1):
    m = n
    for j in range(0, i):
        print(m, end="")
        m -= 1
    for k in range(0, s - 2 * i):
        print(n-i, end="")
    m = n - i + 1
    for l in range(0, i):
        print(m, end="")
        m += 1

    print("")