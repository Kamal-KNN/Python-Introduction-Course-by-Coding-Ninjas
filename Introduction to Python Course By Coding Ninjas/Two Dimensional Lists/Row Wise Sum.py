from sys import stdin

def rowWiseSum(mat, nRows, mCols):
    #Your code goes here
    for ele in mat:
        k=0
        #print(ele)
        for j in range(len(ele)):
            k=ele[j]+k
        print(k,end=" ")


    




















#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    rowWiseSum(mat, nRows, mCols)
    print()

    t -= 1