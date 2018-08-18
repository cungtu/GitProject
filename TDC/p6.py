import stdio
a=stdio.readInt()
n=1
for i in range (2,a):
	if a%i==0:
		n=0
	if a%i!=0:
		n=2
		
if n==1:
	print(str(i))
if n==2:
	print(str(a))
else:
	print(str(a))
