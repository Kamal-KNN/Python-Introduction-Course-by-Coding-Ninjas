
from sys import stdin


def isPermutation(string1, string2) :
	#Your code goes here
    string1="".join(sorted(string1))
    string2="".join(sorted(string2))
    if string1==string2:
        return True
    else:
        return False


























	


#main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')