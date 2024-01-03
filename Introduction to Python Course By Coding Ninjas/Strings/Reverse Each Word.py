
from sys import stdin


def reverseEachWord(string) :
	# Your code goes here
	words=string.split()
	words=[words[::-1]for words in words]
	string=" ".join(words)
	return string
	






















	



#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)