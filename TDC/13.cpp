#include <iostream>
#include <math.h>

using namespace std;
int main()
{

int k=0, n,i=1;
cin>>n;
while (k<n)
	{
	   if (n%i==0)
			{		
   	   k=k+i;
			}
    i=i+1;
	}
if (k==n)
	{
    cout<<n<<endl;
	}
else
	{
    while (k!=n)
		{
        k=0;
        n=n-1;
        i=1;
        while (i<n)
				{
            if (n%i==0)
					{
                k=k+i;
					}
            i=i+1;
				}
		}	
   cout<<n<<endl;
    }
	return 0;
}
