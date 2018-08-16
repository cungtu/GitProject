#include <iostream>
using namespace std;
int main()
{
int s=0, n;
cin>>n;
for (int i=1 ; i<n;i++)
	{
	if (n%i==0)
		{
		s=s+i;
		}
	}
if (s==n)
	{
	cout<<"1\n";
	}
else 
	{
	cout<<"0\n";
	}
	return 0;
}
