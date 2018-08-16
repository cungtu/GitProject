n=str(input())
intN=int(n)
kytu=len(n)
tam=1
kq=''
while kytu!=0:
	tong=int(n[kytu-1])+tam
	if tong ==2:
		du=0
		tam=1
		kq=str(du)+kq
	else:
		tam=0
		kq="1"+kq
	kytu=kytu-1
if tam==1:
	kq=str(tam)+kq
print(kq)
