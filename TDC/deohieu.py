import stdio

n=stdio.readString()
x=len(n)
if 99>=n>=0:
	print('00')
if 999>n>99:
	print(n//100)
else:
	print(n[x-4]+n[x-3])



	

