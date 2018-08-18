import stdio
import math
N=stdio.readInt()
a=int(math.sqrt(N))
if N%a==a:
    print(str(N))
if N%a!=a:
	print(str(a**2))
