nhap=str(input())
intNhap=int(nhap)
kytu=len(nhap)
output=""
tam=1
while kytu!=0:
	tong=int(nhap[kytu-1])+tam
	if tong==2:
		tam =1
		ra=0
		output=str(ra)+output
	else:
		tam=0
		output="1"+output
	kytu-=1
if tam==1:
	output=str(tam)+output
print(output)
		
