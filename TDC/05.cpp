	#include <iostream>
	using namespace std;
	int main()
	{
	int N ,k,e,f,g;
		cin>>N;
		k=N%10;
		e=((N%100)-k)/10;
		f=((N%1000)-e*10-k)/100;
		g=N/1000;
		if (N<1000 or N>9999) 
			cout<<"-1\n";
		
		else if (e>k)	
			cout<<e<<endl;

		else if (f>k)
			cout<<f<<endl;
		else if (g>k)
			cout<<g<<endl;
		else	
			cout<<k<<endl;

		return 0;
	}
