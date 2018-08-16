import stdio
n=stdio.readString()
m=stdio.readString()
b=len(m)
a=len(n)
if len(m)>len(n):
	
	t=m
	m=n
	n=t
	c=b
	b=a
	a=c
dem=0
nho=b
if len(m)==1:
	for k in range (0,a):
		for t in range (0,a+b):
			l=n[k:(t+nho)-a]
			if l==m:
				dem+=1
else:
	for i in range(0,a):
		for j in range(0,a+b-1):
			T=n[i:(j+nho)-a]
			if T==m:
				dem+=1
print(dem)	
	

