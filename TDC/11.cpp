#include <iostream>
using namespace std;
int main()
{
int n;
cin>>n;
while (n>=2)
{
	int Flag=1;
	for (int i=2;i<n;i++) 
		{
		if (n%i==0)
			{
			Flag=0;
			break;
			}
		}
	if (Flag==1)
		{
		cout<<n<<endl;
		break;
		}
	n=n-1;
}
	return 0;
}
