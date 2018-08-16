import stdio
N=stdio.readInt()
if 1000<=N<=9999 :
	k=N%10
	e=(N%100)-k
	f=(N%1000)-e*10-k
	g=N//1000
	max=k
	if e>k:	
		e=max
	if f>k:
		f=max
	if g>k:
		g=max
	stdio.writeln(str(max))
else:
	stdio.writeln('-1')
