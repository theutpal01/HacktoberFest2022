#include <bits/stdc++.h>
using namespace std;
class Solution {
  public:

    void bfs(int i, int j,int n,int m, vector<vector<int>> &vis,vector<vector<char>> grid )
    {
        vis[i][j]=1;
        queue<pair<int,int>>q;
        int ni=0,nj=0;
        q.push({i,j});
        while(!q.empty())
        {
            i=q.front().first;
            j=q.front().second;
            q.pop();

            for(int di=-1;di<=1;di++)
            {
                for(int dj=-1;dj<=1;dj++)
                {
                    ni=i+di;
                    nj=j+dj;
                    if(ni>=0 && nj>=0 && ni<n && nj<m && grid[ni][nj]=='1' && !vis[ni][nj])
                    {
                        vis[ni][nj]=1;
                        q.push({ni,nj});
                    }
                }
            }
        }
    }
    int numIslands(vector<vector<char>>& grid) {

        int n=grid.size();
        int m=grid[0].size();
        int c=0;
        vector<vector<int>> vis(n,vector<int>(m,0));

        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(!vis[i][j] && grid[i][j]=='1')
                {
                    c++;
                    bfs(i,j,n,m,vis,grid);
                }
            }
        }
        return c;
    }
};


int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n, m;
        cin >> n >> m;
        vector<vector<char>> grid(n, vector<char>(m, '#'));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> grid[i][j];
            }
        }
        Solution obj;
        int ans = obj.numIslands(grid);
        cout << ans << '\n';
    }
    return 0;
}
