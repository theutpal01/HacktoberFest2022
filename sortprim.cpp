#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int n,v[1001],i,j,ok,k;
    cin>>n;
    for(i=1;i<=n;i++)
        cin>>v[i];
    for(i=1;i<=n;i++)
    {
        ok=0;
        for(j=2;j<=sqrt(v[i]);j++)
        {
            if(v[i]%j==0)
                ok=1;
            if(ok==1)
                j=sqrt(v[i]);
        }
            if(v[i]==2 || v[i]==3 || v[i]==5)
                ok=0;
            if(v[i]==0 || v[i]==1)
                ok=1;
            if(ok==1)
            {
            for(j=i;j<=n-1;j++)
                v[j]=v[j+1];
            n=n-1;
            i=i-1;
            }
        }
    ok=0;
    while(ok==0)
    {
        ok=1;
        for(i=1;i<=n-1;i++)
        {
            if(v[i]>v[i+1])
            {
                k=v[i];
                v[i]=v[i+1];
                v[i+1]=k;
                ok=0;
            }
        }
    }
    for(i=1;i<=n;i++)
        cout<<v[i]<<" ";
    return 0;
}
