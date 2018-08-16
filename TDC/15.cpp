#include <iostream>
#include <math.h>

using namespace std;
int main()
{
int n,m=0;
cin>>n;
for (int i=2; i<n+1;i++)
	{
	int t = 0;
	for (int k=2;k<=sqrt(i);k++)
		{	 
		if (i % k == 0)
			{
			t = 1;
			break;
			}
		}
	if (i > m & n % i == 0 & t == 0)
		{
		m =i;
		}
	}

cout<<m<<endl;
	return 0;
}
	
