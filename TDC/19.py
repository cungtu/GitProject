import stdio
str1=stdio.readString()
str2=stdio.readString()
if len (str1)>len(str2):
	a=str1
	b=str2
else:
	a=str2
	b=str1
dem=0
leght=len(b)
for i in range (0,len(a)):
	temp=a[i:(i+leght)-len(a)]
	if temp == b :
		dem=dem+1
print(dem)


