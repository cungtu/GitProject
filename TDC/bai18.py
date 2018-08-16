import stdio
n=stdio.readString()
m=stdio.readString()
dem=0
if len (n)<len(m):
	c=n
	n=m
	m=c
	
#for i in range (ord("a"), ord("z")+1):
#	if n.count(chr(i))>=1 and m.count(chr(i))>=1:
#		dem=dem+1
#print(dem)
print (n.count(m))
