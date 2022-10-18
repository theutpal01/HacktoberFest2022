//* Tower of Hanoi implementation in C++ using Recursion

#include <iostream>
using namespace std;

void TOH(int n,int A,int B,int C)
{
    if(n==0)
    {return;}
    TOH(n-1,A,C,B);
    cout<<A<<" --> "<<C<<endl;
    TOH(n-1,B,A,C);
        
}

int main()
{
    int n;
    cout<<"Enter the number of Discs ?"<<endl;
    cin>>n;
    cout<<"All discs are placed as 1-n from top to bottom in the first tower :"<<endl;
    cout<<"Steps to follow :"<<endl;
    TOH(n,1,2,3);
    return 0;
} 

