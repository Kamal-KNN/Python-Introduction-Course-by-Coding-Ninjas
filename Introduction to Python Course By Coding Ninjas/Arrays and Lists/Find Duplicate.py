
import sys

def duplicateNumber(arr, n) :
    uniquelist=[]
    duplicatelist=[]
    for i in arr:
        if i not in uniquelist:
            uniquelist.append(i)
        elif i not in duplicatelist :
            return i
    
    
   



