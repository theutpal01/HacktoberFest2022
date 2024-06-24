/*
Program to evaluate a^b in O( logb) time complexity
Time Complexity - O( logb)
Space Complexity - O( logb)
*/
#include<iostream>
#include<bits/stdc++.h>
using namespace std;

double expn( int a ,int b){
    if( b == 0)
        return 1;
    if(b == 1)
        return a;
    double r = expn(a ,b/2);
    if( b%2){
        return r*r * a;
    }
    else{
        return r*r;
    }
}
int main(){
    int a,b;
    cout<<"Calculate a powers b"<<"\n";
    cout<<"Enter a: ";
    cin>>a;
    cout<<"Enter b: ";
    cin>>b;

    double res = expn(a,b);
    cout<<"a^b = "<<res<<"\n";
    return 0;
}