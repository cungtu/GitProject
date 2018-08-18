import stdio
n=stdio.readInt()

for j in range (2,n+1):
	NT=1
	for i in range (2,j):
		if j%i==0:
			NT=0
	if NT==1:
		print(j)
  


	
