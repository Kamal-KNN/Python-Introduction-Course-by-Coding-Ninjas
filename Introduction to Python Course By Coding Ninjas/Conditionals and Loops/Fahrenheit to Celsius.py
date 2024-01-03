S=int(input())
E=int(input())
W=int(input())
i = S
while i<=E:
    cel=(5/9)*(i-32)
    print(str(i) + "\t" + str(int(cel)))
    i=i+W
