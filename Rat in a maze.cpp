// Rat in a Maze Problem - I
// Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
// Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.
#include<bits/stdc++.h>
using namespace std;
class Solution{
    public:
    void ratInMaze(vector<vector<int>> &m, int n, int row, int col, vector<string> &ans, string s, vector<vector<int>> &vis)
    {
        if(row== n-1 && col== n-1)
        {
            ans.push_back(s);
            return;
        }
    
        //downward
        if(row+1< n && vis[row+1][col]== 0 && m[row+1][col]== 1)
        {
            vis[row][col]= 1;
            ratInMaze(m, n, row+1, col, ans, s+'D', vis);
            vis[row][col]= 0;
        }
    
        //leftward
        if(col-1>= 0 && vis[row][col-1]== 0 && m[row][col-1]== 1)
        {
            vis[row][col]= 1;
            ratInMaze(m, n, row, col-1, ans, s+'L', vis);
            vis[row][col]= 0;
        }
    
        //rightward
        if(col+1< n && vis[row][col+1]== 0 && m[row][col+1]== 1)
        {
            vis[row][col]= 1;
            ratInMaze(m, n, row, col+1, ans, s+'R', vis);
            vis[row][col]= 0;
        }
    
        //upward
        if(row-1>= 0 && vis[row-1][col]== 0 && m[row-1][col]== 1)
        {
            vis[row][col]= 1;
            ratInMaze(m, n, row-1, col, ans, s+'U', vis);
            vis[row][col]= 0;
        }
        return;
    }

    vector<string> findPath(vector<vector<int>> &m, int n) 
    {
        vector<string> ans;
        vector<vector<int>> vis(n, vector<int>(n,0));
        string s= "";
        int row= 0;
        int col= 0;
        if(m[row][col]== 1)
        {
            ratInMaze(m, n, row, col, ans, s, vis);
        }
        return ans;
    }
};

int main(){
    //Enter matrix dimension



    int t=1;
    cin>>t;

    while(t--){
        Solution ob;
        int n=0;
    cin>>n;



    vector<vector<int>>m(n,vector<int>(n,0));

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>m[i][j];
        }
    }

    vector<string>ans;
    ans=ob.findPath(m,n);

    for(auto str:ans)cout<<str<<endl;
    }
    
}