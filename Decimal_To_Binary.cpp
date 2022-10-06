//Program to convert decimal to binary and vise versa
//By D3Falt
#include <bits/stdc++.h>
using namespace std;
int main(){
    printf("Enter a Decimal value:");
    int a;
    scanf("%d",&a);
    cout<<"The value in Binary would be :"<<bitset<8>(a).to_string()<<endl;
}
