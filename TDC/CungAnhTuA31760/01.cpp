#include <iostream>
using namespace std;
main()
{
int N ,k,e,f,g;
if (N>=1000 & N<=9999) 
	k=N%10;
	e=((N%100)-k)/10;
	f=((N%1000)-e*10-k)/100;
	g=N/1000;
	
	if (e>k)	
		cout<<e<<endl;

	if (f>k)
		cout<<f<<endl;
	if (g>k)
		cout<<g<<endl;
	else	
		cout<<k<<endl;
else
	cout<<"-1\n";
	return 0;
}
