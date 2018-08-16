import stdio
n=stdio.readString()
m=stdio.readString()
s=0
a=len(n)
b=len(m)
if len(m)>len(n):
	t=a	
	a=b
	b=t
	c=n
	n=m
	m=c
tu=0 
lenght=b 
for i in range (0,a):
	for j in range (0, a+b-1):
		kq=n[i:(lenght+j)-a]
		if kq==str(m):
			tu+=1
print(tu)
