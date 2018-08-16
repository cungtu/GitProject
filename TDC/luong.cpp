#include <iostream>
// bai tim so doi xung trong khoang 10000>n>=1000
using namespace std;
int main()
{
int n, variable=0;
cin>>n;
int t=n;
while(t>0)
{
variable=variable*10+t%10;
t=t/10;
}
if (n>9999 or n<1000)
cout<<"-1"<<endl;
else if (variable==n)
cout<<"DX"<<endl;
else
cout << "KDX"<<endl;
return 0;
}
