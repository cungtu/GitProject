import stdio
import sys

n=stdio.readInt()
while n>=0:
	flang=True
	for i in range (2,n):
		if n%i==0:
			flang=False
			break
	if flang ==True:
		print(str(n))
		break
	n-=1
