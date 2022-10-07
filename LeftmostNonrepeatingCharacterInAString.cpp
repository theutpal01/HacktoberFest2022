//This program will take string as a input and print the index of leftmost non-repeating character in a string and if every character is repeating it will print -1
#include<bits/stdc++.h>
using namespace std;

const int CHAR=256;
int NonRep(string &str)
{
    int count[CHAR]={0};

    for(int i=0;i<str.length();i++)
    {
        count[str[i]]++;
    }
    for(int i=0;i<str.length();i++)
    {
        if(count[str[i]]==1)
        return i;
    }
    return -1;
}

int main()
{
    string s;
    cin>>s;

    cout<<NonRep(s)<<"\n";
}