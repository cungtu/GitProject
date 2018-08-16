n=int(input())
m=input()
x=m.split()
tong=0
dem=0
for i in x:
	tong=float(i)+tong
kq=tong/n
for i in x:
	if float(i)>kq:
		dem+=1
print(dem)



