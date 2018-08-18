#include <iostream>
using namespace std;
int main()
{
int N,a=0;
cin>>N;
if (N>=2)
{
	for (int i=2;i<N;i++) 
	{
		if (N%i==0)
			a=1;
	}
	if (a!=0) 
		cout<<"0\n";
	else
		cout<<"1\n";
}
	return 0;
}
