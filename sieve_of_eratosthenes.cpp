/*
program to print all prime number form 1 to N usin seive of eratosthenes algorithms
Time Complexity - O( loglogN )
Space Complexity - O( N)
*/
#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cout<<"Enter N: ";
    cin>>n;
    vector<int> table(n+1 , 1);
    table[0] = table[1] = 0;
    for(int i = 2;i*i<=n;i++){
        if(table[i]){
            for(int j = i*i; j<=n; j+=i){
                table[j] = 0;
            }
        }
    }
    cout<<"Prime in range [ 1 : "<<n<<" ] : ";
    for(int i = 2;i<=n;i++){
        if(table[i]){
            cout<<i<<" ";
        }
    }
    return 0;
}

