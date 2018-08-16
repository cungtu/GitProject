import stdio
n=stdio.readString()
max=0
for i in range (0,len(n)):
	if max<int(n[i]):
		max=int(n[i])
print(max)
	
