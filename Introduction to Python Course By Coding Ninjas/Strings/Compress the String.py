from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)


def getCompressedString(input) :
	# Write your code here.
	kamal=""
	count=1
	i=1
	for i in range(1,len(input)):
		if input[i]==input[i-1]:
			count=count+1
		elif count==1:
			kamal=kamal+input[i-1]
			count=1
		else:
			kamal=kamal+input[i-1]+str(count)
			count=1
	kamal=kamal+input[-1]+str(count)
	if kamal[-1]=="1":
		kamal=kamal[0:-1]
	return kamal
	
	



# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)