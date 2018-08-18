#include <iostream>
using namespace std;
int main()
{
float  a,b,c,d,s;
	cin>>a;
	cin>>b;
	cin>>c;
	cin>>d;
s=(a*2+c*2+d+b)/6;
if (a<=10 & a>=0 & 10>=b & b>=0 & 10>=c & c>=0 & 10>=d & d>=0) 
{
	if (s>=9.0)
	{
		if (a>=6.5 and b>=6.5 and d>=6.5 and c>=6.5) 
			cout<<"XS\n";
		else if (a<=6.5 or b<=6.5 or d<=6.5 or c<=6.5) 
			cout<<"G\n"	;
	}
	else if (s>=8)
	{
		if (a>=5 & b>=5 & d>=5 & c>=5)
			cout<<"G\n";
		else if (a<=5 or b<=5 or d<=5 or c<=5)
			cout<<"K\n";
		
	} 
	else if (s>=6.5)
	{
		if (a>=3 & b>=3 & d>=3 & c>=3)
			cout<<"K\n";
		else if (a<=3 or b<=3 or d<=3 or c<=3)
			cout<<"TB\n";
	}
	else if (s>=5)
	{
		if (a>=2 & b>=2 & d>=2 & c>=2)
			cout<<"TB\n";
		else if (a<=2 or b<=2 or d<=2 or c<=2)
			cout<<"Y\n";
	} 
	else 
	{
		cout<<"Y\n";	
	} 
}
	return 0;
}

