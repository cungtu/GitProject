import stdio
n=stdio.readString()
m=stdio.readString()

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
if b==1:
	for k in range(0,a):
		for l in range (0,a+b):
			koQT=n[k:(l+lenght)-a]
			if koQT==str(m):
				tu+=1
else:
	for i in range (0, a):
		for j in range (0,a+b-1):
			QT=n[i:(j+lenght)-a]
			if QT ==str(m):
				tu+=1 
print(tu)

