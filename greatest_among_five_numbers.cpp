#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a,b,c,d,e;
    cout<<"Enter the five numbers"<<endl;
    cin>>a>>b>>c>>d>>e;
    int maxi=max(a,max(b,max(c,max(d,e))));
    cout<<"The maximum number is"<<" "<<maxi<<endl;
    return 0;
}