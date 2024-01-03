
from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
	# Your code goes here
	kamal=""
	for i in string:
		if i==ch:
			pass
		else:
			kamal=kamal+i
	return kamal

























	

#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)