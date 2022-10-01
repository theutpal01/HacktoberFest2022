#include<bits/stdc++.h>
using namespace std;
//depth first search for printing the vertices of graph

void dfs(int source,vector<int>adj[],vector<bool>& visited)
{
  visited[source]=true; //Marking the current vertex as visited
  cout<<source<<" ";
  for(auto i:adj[source])  //Calling dfs for all the adjacent vertices of source vertex
  {
    if(!visited[i])
    dfs(i,adj,visited);
    }
} 
int main()
{
  int V,E;  //vertices and edges
  cin>>V>>E;
  vector<int> adj[V];vector<bool> visited(V,false);
  for(int i=0;i<E;i++)
  {
    int u,v;
    cin>>u>>v;
    adj[u].push_back(v);
    adj[v].push_back(u);
  }
  for(int i=0;i<V;i++){
    if(!visited[i])
      dfs(i,adj,visited);
  }
  return 0;
}

/*INPUT
3 3
0 1
1 2
0 2
OUTPUT 
0 1 2   
*/
