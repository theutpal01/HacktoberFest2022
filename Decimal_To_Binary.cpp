//Program to convert decimal to binary and vise versa
//By D3Falt
#include <bits/stdc++.h>
using namespace std;
int main(){
    cout<<"Enter a Decimal value:";
    int a;
    cin>>a;
    int bin=0;
    int a2=a, i=0, rem;
    
    while(a2){
        rem=a2%2;
        rem*=pow(10,i);
        bin+=rem;
        a2/=2;
        i++;
    }

    cout<<a<<" in binary is "<<bin ;
}