#include <iostream>
#include <math.h>

using namespace std;
int main()
{
int N,a;
cin>>N;
a=int(sqrt(N));
if (N%a==a)
	{
    cout<<N<<endl;
	}
if (N%a!=a)
{
	cout<<a*a<<endl;
}
return 0;
}
