import stdio
import math
n=stdio.readInt()
tam=0
if n>2:
	for i in range(2,n):
		if n%i==0:
			tam=1
			songuyento=1
			for j in range (2, i):
				if i%j==0:
					songuyento==0
			if songuyento==1 and tam==1:
				print(i)
