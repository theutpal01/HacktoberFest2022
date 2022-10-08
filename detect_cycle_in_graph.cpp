#include<iostream>
#include<vector>
using namespace std;
int find_adj(vector<vector<int>>&G,int V,bool &flag,int s,int c)
{
	for(int i=1;i<=V&&flag!=true;i++)
	{
		if(G[c][i]==1)
		{
			if(i==s)
				flag=1;
			else
				find_adj(G,V,flag,s,i);
		}
	}
}
int main()
{
	int V,E;
	cin>>V>>E;
	vector<vector<int>>G(V+1,vector<int>(V+1,0));
	int u,v;
	for(int i=0;i<E;i++)
	{
		cin>>u>>v;
		G[u][v]=1;
	}
	cout<<"adjacency matrix is "<<endl;
	for(int i=1;i<=V;i++)
	{
		for(int j=1;j<=V;j++)
			cout<<G[i][j]<<" ";
		cout<<endl;
	}
	bool flag=false;
	for(int s=1;s<=V;s++)
	{
		find_adj(G,V,flag,s,s);
		if(flag==true)
		{
			cout<<"yes there is a cycle";
			break;
		}
	}
}
/*
5 7
1 2
1 4
2 3
2 5
3 4
3 1
4 5
*/
