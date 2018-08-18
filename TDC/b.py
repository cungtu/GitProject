nhapchuoi=(input())
a=list(nhapchuoi)

check=1
for i in range (len(a)-1,-1,-1):
    if (a[i] == "0"):
        a[i] = "1"
        check = 0
        break
    else:
        a[i] = '0'
        check=1
binary = ''.join(a)

if check == 1:
    binary = "1" + binary
   

print(binary)
