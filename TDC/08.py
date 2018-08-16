import stdio
N=stdio.readInt()
a=0
if N>=2:
	for i in range(1,N):
		if N%i==0:
			a=a+1
	stdio.writeln(str(a))

	
