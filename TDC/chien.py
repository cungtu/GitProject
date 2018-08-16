import stdio	
import sys
import math
n=int(sys.argv[1])

for i in range (1,n):
	if (n%i==0):	
		stdio.writeln(int(n))
		n=i
		
if n==i:
	stdio.writeln('no')
else:
	
	stdio.writeln(int(n)+int(i))
