#include <iostream>
#include<bits/stdc++.h>
using namespace std;

const int N=1e5+10;
//const int N=INT_MAX

int graph[N][N];   //matrix

vector<pair<int,int>> list[N]; //list

int main()
{
    // Adjacency matrix     //Time complexity= O(n^2)
    int n,m;
    cin>>n>>m;
    for(int i=0;i<m;i++){
        int v1,v2,wt;
        cin>>v1>>v2>>wt;
        graph[v1][v2]=wt;
        graph[v2][v1]=wt;
    }
    
    // Adjacency list       //Time complexity= O(n+m)
    int n,m;
    cin>>n>>m;
    for(int i=0;i<m;i++){
        int v1,v2,wt;
        cin>>v1>>v2>>wt;
        list[v1].push_back({v2, wt});
        list[v2].push_back({v1, wt});
    }
    
    //Finding if there is a connection between two edges or not
    
    if(graph[i][j]==1){     //Adjacency matrix --> O(1)
        //connected
    }
    // graph[i][j] ->weight
    
    for(int child: list[i]){    //Adjacency list --> O(n)
        if(child==j){
            //connected
        }
    }
    for(pair<int,int> child: list[i]){
        if(child.first==j){
            //connected
            //child.second ->weight
        }
    }
    
    
}
