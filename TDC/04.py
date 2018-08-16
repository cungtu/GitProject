import stdio
N=stdio.readInt()
if  0<=N<=99:
	stdio.writeln('00')
if 100<=N<=999:
	stdio.writeln('0'+str(N//100))
if N>=1000:
	stdio.writeln(str(N//1000)+str((N%1000)//100))	
