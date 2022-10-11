//Program to convert decimal to binary and vise versa
//By D3Falt
#include <bits/stdc++.h>
using namespace std;
int main(){
    cout<<"Enter a Decimal value:";
    int a;
    cin>>a;
    int bin=0;
    int a2=a;
    while(a2){
        int rem=a2%2;
        bin+=rem;
        bin*=10;
        a2/=2;
    }

    cout<<a<<" in binary is "<<bin ;
}