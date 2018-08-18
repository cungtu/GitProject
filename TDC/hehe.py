n=int(input())
m=int(input())
z=int(input())
if n>0 and m>0 and z>0:
	for i in range(min(n,m,z),0,-1):
		if n%i==0 and m%i==0 and z%i==0:
			print(i)
			break
		 
