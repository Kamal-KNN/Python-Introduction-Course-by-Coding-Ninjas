
def printTable(start,end,step):
    S=start
    E=end
    W=step
    i = S
    while i<=E:
        cel=(5/9)*(i-32)
    
        print(str(i) + "\t" + str(int(cel)))
        i=i+W

	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)

