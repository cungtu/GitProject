#include <iostream>
using namespace std;
int main()
{
int N,a=0;
cin>>N;

if (N>=2)

	for (int i=1;i<N;i++) 
	{
		if (N%i==0)
			a=a+1;
	}
	cout<<a<<endl;
	return 0;
}

