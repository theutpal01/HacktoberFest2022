#include <bits/stdc++.h>
using namespace std;
class Graph
{
    int numVertex;
    bool *visited;
    list<int> *adj;

public:
    Graph(int b);
    void print();
    Graph transpose();
    void fillOrder(int s, stack<int> &st, bool visit[]);
    void DFS(int i, bool v[]);
    void insert(int src, int data);
};

Graph::Graph(int b)
{
    numVertex = b;
    adj = new list<int>[numVertex];
}

void Graph::DFS(int temp, bool visit[])
{
    visit[temp] = true;
    cout << temp << " ";

    list<int>::iterator i;
    for (i = adj[temp].begin(); i != adj[temp].end(); i++)
    {
        if (!visit[*i])
            DFS(*i, visit);
    }
}

void Graph::insert(int src, int data)
{
    adj[src].push_back(data);
}

Graph Graph::transpose()
{
    Graph gt(numVertex);
    for (int s = 0; s < numVertex; s++)
    {
        list<int>::iterator i;
        for (i = adj[s].begin(); i != adj[s].end(); i++)
        {
            gt.adj[*i].push_back(s);
        }
    }
    return gt;
}

void Graph::fillOrder(int s, stack<int> &st, bool visit[])
{
    visit[s] = true;

    list<int>::iterator i;
    for (i = adj[s].begin(); i != adj[s].end(); i++)
    {
        if (!visit[*i])
            fillOrder(*i, st, visit);
    }
    st.push(s);
}

void Graph::print()
{
    stack<int> st;
    for (int i = 0; i < numVertex; i++)
    {
        visited[i] = false;
    }

    for (int i = 0; i < numVertex; i++)
    {
        if (!visited[i])
        {
            fillOrder(i, st, visited);
        }
    }

    Graph gr = transpose();

    for (int i = 0; i < numVertex; i++)
    {
        visited[i] = false;
    }

    while (!st.empty())
    {
        int temp = st.top();
        st.pop();

        if (!visited[temp])
        {
            gr.DFS(temp, visited);
            cout<<endl;
        }
        
    }
}

int main()
{
    Graph g(8);

    g.insert(0, 1);
    g.insert(1, 2);
    g.insert(2, 3);
    g.insert(2, 4);
    g.insert(3, 0);
    g.insert(4, 5);
    g.insert(5, 6);
    g.insert(6, 4);
    g.insert(6, 7);

    cout<<"Strongly connected Nodes:\n";
    g.print();
}