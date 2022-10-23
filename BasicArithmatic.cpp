#include<iostream>
using namespace std;

void operations(int a,int b)                                
{
    int add=a+b;
    cout<<"Sum of the number is :"<<add<<endl;
    int sub=a-b;
    cout<<"Difference of the number is :"<<sub<<endl;
    int multi=a*b;
    cout<<"Product of the number is :"<<multi<<endl;
    int div=a%b;
    cout<<"division of the number is :"<<div<<endl;
}

int main()
{
    int a,b;
    cout<<"Enter two numbers :";
    cin>>a>>b;
    operations(a,b);
    return 0;
}
