#include <iostream>
#include <string>

using namespace std;
int main()
{
int n,m;
cin>>n;
string t;
t = "";
while(n>0)
	{
	m=n%2;
     t = str(m) + t;
    n = n / 2;
	} 
cout<<"so nhi phan la : "<<t<<endl;
	return 0;
}
