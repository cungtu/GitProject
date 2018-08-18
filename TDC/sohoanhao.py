import stdio
n=stdio.readInt()
i=1
s=0
k=0
while s<n:
	if n%i==0:
		s=s+i
	i=i+1
if s==n:
	print(n)
else:
	while k!=n:

		k=0
		i=1
		n=n-1
		while i<n:
			if n%i==0:
				k=k+i
			i=i+1
	print(k)
