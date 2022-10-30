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

int findLcs(string a,string b,int m,int n)
{
    if(m==0 || n==0)
    {
        return 0;
    }
    if(a[m-1] == b[n-1])
    {
        return 1+findLcs(a,b,m-1,n-1);
    }
    else
    {
        return max(findLcs(a,b,m,n-1),findLcs(a,b,m-1,n));
    }
    
}

void solve()
{
    string a = "AGGTAB";
    string b = "GXTXAYB";

    cout<<findLcs(a,b,a.length(),b.length());

}

int main() {
    
    file_i_p();

    solve();

    return 0;
}
