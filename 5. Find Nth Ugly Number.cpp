// { Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

#define ull unsigned long long


 // } Driver Code Ends
//User function template for C++
class Solution{
public: 
    // #define ull unsigned long long
    /* Function to get the nth ugly number*/
    ull getNthUglyNo(int n) {
        vector <ull> prime(1,1) ;
        ull i=0,j=0,k=0;
        while(prime.size()<n){
            prime.push_back(min(prime[i]*2,min(prime[j]*3,prime[k]*5)));
            if(prime.back()%2==0){
                i++;
            }
            if(prime.back()%3==0){
                j++;
            }
            if(prime.back()%5==0){
                k++;
            }
        }
        return prime[n-1];  
    }
};

// { Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        Solution ob;
        auto ans = ob.getNthUglyNo(n);
        cout << ans << "\n";
    }
    return 0;
}
  // } Driver Code Ends