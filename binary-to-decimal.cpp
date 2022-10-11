#include <iostream>
#include <math.h>
using namespace std;

int main(){
    int bin; 
    cout<< "enter your binary number: ";
    cin>>bin;

    int bina=bin, i=0, rem;
    int dec=0;
    while(bina){
        rem=bina%10;
        rem*=pow(2,i);

        dec+=rem;
        bina/=10;
        i++;
    }
    cout<<"your decimal conversion is: \n"<<dec;
}