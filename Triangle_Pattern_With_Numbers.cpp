//Print a right triangle of numbers
//By D3Falt
#include<iostream>
using namespace std;
int main(){
    int a;
    cout<<"Enter the number of levels :";
    cin>>a;
    for(int i=1;i<a+1;i++){
        for(int j=1;j<i+1;j++){
            cout<<j;
        }
        cout<<endl;
    }

//Replace line 11 by cout<<*; to make a pattern of stars