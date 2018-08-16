#include <iostream>
#include <math.h>
using namespace std;
int main()
{
int n,s=0,k=2;
cin>>n;
while (  k>0)
{
	int SoNguyenTo = 1, i=2;
	while (i<= sqrt(k))
	{
		if (k%i==0)
			{
			SoNguyenTo = 0;
			break;
			}
		
		i = i+1;
			
	}
	if (SoNguyenTo==1)
		{
		s +=1;
		}
	if (s==n)
		{
		cout<<k<<endl;
		break;
		}
	k +=1;
}
	return 0;
}
