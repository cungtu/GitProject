import sys
import stdio
import math
n=stdio.readInt()
d=1/(1*2)
s=d

for i in range(3,n+1):	
	s=1/(i*(i+1))
	
for a in range (3,n+1):
	d=1/(a*(a+1))	
	s=s+d
stdio.writeln((s))
		
