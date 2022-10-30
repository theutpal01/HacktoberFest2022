#include <bits/stdc++.h>
using namespace std;

#define PI 3.1415926535897932384626
#define ll long long
#define lli long long int
#define fo(i,a,n) for(int i=a;i<n;i++)
#define pr(i,arr) for(auto i:arr)

typedef vector<int> vi;
typedef vector<ll> vl;
typedef map<ll,ll> ml;
typedef map<int,int> mi;

void file_i_p()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
}

ll fact(ll n) {
    ll res = 1;
    for(ll i=2;i<=n;i++) {
        res*=i;
    }
    return res;
}

ll _lcm(ll x,ll y) {
    return x*y/__gcd(x,y);
}

ll _gcd(ll a,ll b) {
    return a%b==0 ? b : _gcd(b,a%b);
}

int dp[1000][1000];

int ans(int arr[],int i,int j)
{
    if (i == j)
        return 0;

    if(dp[i][j]!=-1)
    {
        return dp[i][j];
    }

    int k;
    int min = INT_MAX;
    int count;
    for (k = i; k < j; k++)
    {
        count = ans(arr, i, k)
                + ans(arr, k + 1, j)
                + arr[i - 1] * arr[k] * arr[j];
 
        if (count < min)
            min = count;

    }
    return dp[i][j] =  min; 
}

void solve()
{

    int arr[] = { 1, 2, 3, 4, 3 };
    int n = sizeof(arr) / sizeof(arr[0]);
    fo(i,0,n+1)
    {
        fo(j,0,n+1)
        {
            dp[i][j] = -1;
        }
    }
    cout<<ans(arr,1,n-1);

}

int main() {
    
    file_i_p();

    solve();

    return 0;
}
