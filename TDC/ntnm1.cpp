#include <iostream>

using namespace std;
#include <stdlib.h>
#include <time.h>

int a[100][100];
int k,N;

void KhoiTao()
{
	cout<<"Nhap kich co ban co: ";
	cin>>N;
	for(int i = 0; i<N; i++)
		for(int j = 0; j<N; j++)
		{
			int k;
			bool ok;
			do
			{
				ok = false;
				srand(time(0));
				k = rand()%((N*N) + 1);

				for(int x = 0; x < i; x++)
					for(int y = 0; y< N; y++)
						if (a[x][y] == k)
						{
							ok = true;
							break;
						}
				for(int y = 0; y<j; y++)
					if (a[i][y] == k)
					{
						ok = true;
						break;
					}
			}while (ok);
			a[i][j] = k;		
		}
}
void VeBanCo()
{
	for(int i = 0; i<N; i++)
	{
		for(int j = 0; j<N; j++)
		{
			if (a[i][j] < 10)
				cout<<"   ";
			else if (a[i][j] < 100)
				cout<<"  ";
				
			cout<<a[i][j];
		}
		cout<<endl;
	}
}
int main()
{
	KhoiTao();	
	int min = 1;
	do
	{	
		system("clear");
		VeBanCo();
		int x, y;
		do
		{
			cout<<"So tiep theo o dong nao cot nao: ";
			cin>>x>>y;
		}while(!(x>=1 && x<=N && y>=1  &&y<=N && a[x-1][y-1] == min));
		a[x-1][y-1] = 0;
		min++;
		if (min > N*N)
		{
			cout<<"Chuc mung ban da chien thang\n";
			break;
		}		
	}while(1);
	system ("PAUSE");
	return 0;
}
