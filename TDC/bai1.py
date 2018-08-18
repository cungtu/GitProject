import stdio
import sys
import math
a=stdio.readInt()
b=0
for i in range (2,a):
	if (a%i==0):
		b = 1 
if b== 1:
	stdio.writeln('day ko phai la so nguyen to')
		
else :
	stdio.writeln(str(a)+ ' la so nguyen to')
		
