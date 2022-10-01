//Runtime: 28 ms
//Memory Usage: 16.5 MB

#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
vector<int> N;
for(int i=0;i<n;i++)
{
    N.push_back(i);
}
        int len = N.size() - 1, curr = -1, next = 0, ans = 0;
        for (int i = 0; next < len; i++) 
        {
            if (i > curr) ans++, curr = next;
            next = max(next, N[i] + i);
        }
        cout<<ans<<endl;
}