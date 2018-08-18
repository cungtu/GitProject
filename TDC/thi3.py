n=int(input())
m=int(input())
if m>n:
	t=m
	m=n
	n=t
for i in range(n+1,0,-1):
	if n%i==0 and m%i==0:
		print(i)
		break
		

