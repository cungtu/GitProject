import stdio
N=stdio.readInt()
a=0
if N>=2:
	for i in range (2,N):
		if(N%i==0):
			a=1
	if a!=0: 
		stdio.writeln('0')
	else:
		stdio.writeln('1')
