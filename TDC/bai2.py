import stdio
n= stdio.readInt()
a=0
t=n
while (t>=1):
	a=a*10+t%10
	t=(t-t%10)/10	
if (a==n):
	stdio.writeln(str(n) + 'la so doi xung') 
else :
	stdio.writeln(str(n) + 'la so ko doi xung')

