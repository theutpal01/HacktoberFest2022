#include<bits/stdc++.h>
using namespace std;

int main(){
    string s;
    cout<<"Enter a string: ";
    cin>>s;
    string reversed_string="";
    for(int i=s.length()-1;i>=0;i--){
        reversed_string+=s[i];
    }
    cout<<"After reversing the string: "<<reversed_string;
    return 0;
}