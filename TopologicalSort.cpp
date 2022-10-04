#include<bits/stdc++.h>
using namespace std;

class Graph{
    int V;
    vector<list<int>>adj;
    public:
    Graph(int n){
        this->V= n;
        adj.resize(n);
    }

    void addEdge(int u, int v){
        adj[u].push_back(v);
    }
    void DFS();
    void DFSUntil(int start, vector<bool>&visited);

    void TopologicalSort();
    void TopologicalSortUntil(int u, stack<int>&s, vector<bool>&visited);
};

void Graph::TopologicalSort(){

    stack<int>s;
    vector<bool>visited;

    visited.resize(this->V, false);

    for(int i =0; i< this->V; i++){
        if(!visited[i])
        TopologicalSortUntil(i, s, visited);
    }

while(!s.empty()){
    cout<<s.top()<<" ";
    s.pop();
}
  
}

void Graph::TopologicalSortUntil(int u, stack<int>&s, vector<bool>&visited){

for(auto x: adj[u]){
    if(!visited[x])
    TopologicalSortUntil(x,s,visited);
}

s.push(u);
visited[u] = true;
}

int main(){

    Graph g(6);

    g.addEdge(0,1);
    g.addEdge(0,2);
    g.addEdge(1,3);
    g.addEdge(1,4);
    g.addEdge(2,3);
    g.addEdge(2,5);
    g.addEdge(3,4);
    g.addEdge(3,5);
    cout<<"Toplogical Sort : ";
    g.TopologicalSort();
    return 0;
}