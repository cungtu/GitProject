import sys
import stdio
stdio.writeln('nhung bien se xe mang di dau gia:')
for a in range(1000, 99999):	
	prime = True
	for i in range(2, a):
		if a%i==0:
			prime = False
	if prime:
		temp=a
		sdn=0
		while a!=0:
			sdn = sdn*10 + a%10
			a = a//10
			if temp==sdn:
				stdio.write(str(temp) + '  ')
	



	
