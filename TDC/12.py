import stdio
n= stdio.readInt()
s=0
c=0
for i in range (1,n):
	if n%i==0:
		s=s+i
	
if n==s:
	print(str(s))
if n!=s:
	for a in range (1,n):
		for x in range (1,a):
			if x%a==0:
				c=c+1
	print(str(c))
