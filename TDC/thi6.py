n=int(input())
m=int(input())
s=0
for i in range(2,m+1):
	tet=1
	for a in range (2,i):
		if i%a==0:
			tet=0
	if tet==1:
		s=i+s
print(s)
