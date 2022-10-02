/*
Program to print the Prime Factors of a user input number
Time Complexity - O( sqrt(n) )
Space Complexity - O(1)
*/

#include<iostream>
#include<bits/stdc++.h>
using namespace std;

/*
below function return a list of prime factors of given number, with their multiplicity
*/
vector<pair<int,int>> prime_factorise(int n){
    vector<pair<int,int>> ret;
    int c = 0;
    while(n%2 == 0){
        n/=2;
        c++;
    }
    ret.push_back(make_pair(2,c));
    
    for(int i = 3; i <= sqrt(n) ;i+=2){
        
        if( n%i == 0){
            c = 0;
            while(n%i == 0){
                n/=i;
                c++;
            }
            ret.push_back(make_pair(i,c));
        }
    }
    if( n != 1){
        ret.push_back( make_pair(n,1));
    }
    return ret;
}

int main(){
    int n;
    cout<<"Enter a Number: ";
    cin>>n;
    cout<<"Prime Factors of "<<n<<" are: (";
    vector<pair<int,int>> ret = prime_factorise(n);
    for( auto i: ret){
        cout<<i.first<<", ";
    }
    cout<<" )";
    return 0;
}