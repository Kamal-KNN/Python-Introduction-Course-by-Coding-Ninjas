n=int(input())
i=0
while i<n:    
    j=0    
    ch=chr(ord("A")+i)    
    while j<=i:        
        print(ch,end="")        
        ch=chr(ord(ch)+1)        
        j=j+1    
    print()    
    i=i+1