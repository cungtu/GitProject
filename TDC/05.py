import stdio
N=stdio.readInt()

if 1000<=N<=9999 :		
	k=N%10
	e=(N%100)-k
	f=(N%1000)-e*10-k
	g=N//1000
	if (str(k)+str(e)+str(f)+str(g))==N:	
		stdio.writeln('DX')
	else:
		stdio.writeln('KDX')
else:	
	stdio.writeln('-1')


