import stdio
import math

n = stdio.readInt()
s = 0
k = 2
while k>0:
	SoNguyenTo = 1
	i = 2
	while i<= math.sqrt(k):
		if k%i==0:
			SoNguyenTo = 0
			break
		i = i+1
	if SoNguyenTo==1:
		s +=1
	if s==n:
		stdio.writeln(k)
		break
	k +=1
