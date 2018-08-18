import sys
n=int(sys.argv[1])
S=0
for i in range (1,n+1):
  S=S+(1/(i*(i+1)))
print(str(S))
