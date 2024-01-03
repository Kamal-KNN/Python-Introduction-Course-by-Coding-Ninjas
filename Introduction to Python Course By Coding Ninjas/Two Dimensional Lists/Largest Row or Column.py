'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

from sys import stdin

def findLargest(arr, nRows, mCols):
    max_row_sum =-2147483648
    max_row_ind = 0
    for i in range(nRows):
        sum_row=0
        for j in range(mCols):
            sum_row+=arr[i][j]
            
        if sum_row>max_row_sum:
            max_row_ind =i
            max_row_sum=sum_row
            
            
    max_col_sum =-2147483648
    max_col_ind = 0
    for j in range(mCols):
       sum_col=0
       for i in range(nRows):
           sum_col+=arr[i][j]
       if sum_col>max_col_sum:
           max_col_ind =j
           max_col_sum=sum_col
    if max_col_sum > max_row_sum:
        print("column",max_col_ind,max_col_sum)
    elif max_col_sum == max_row_sum:
        print("row",max_row_ind,max_row_sum)
    else:
        print("row",max_row_ind,max_row_sum)
        

   
























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
    findLargest(mat, nRows, mCols)

    t -= 1