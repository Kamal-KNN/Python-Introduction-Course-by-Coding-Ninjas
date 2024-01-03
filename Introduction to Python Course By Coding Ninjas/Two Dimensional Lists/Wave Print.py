from sys import stdin

def wavePrint(mat, nRows, mCols):
    #Your code goes here
    n_rows=len(mat)
    m_col=mCols
    for j in range(m_col):
        if j%2==0:
            for i in range(n_rows):
                print(mat[i][j],end=" ")
        else:
            for k in range(nRows-1,0-1,-1):
                print(mat[k][j],end=" ")
    print()
    



























#Taking Iput Using Fast I/O
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
    wavePrint(mat, nRows, mCols)
    print()

    t -= 1