n=int(input())
m=n+1
while True:
	tet=1
	for i in range(2,m):
		if m%i==0:
			tet=0
	if tet==1:
		print(m)
		break
	m+=1		
