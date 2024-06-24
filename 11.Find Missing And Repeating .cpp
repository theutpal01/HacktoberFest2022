// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;
 // } Driver Code Ends
class Solution{
public:
    int *findTwoElement(int *arr, int n){
            long long rep,miss,total=0,counter=0;
            int *ans1=new int(2);
            //Find rep number
            sort(arr,arr+n);
            for(int i=0;i<n;i++){
                if(arr[i]==arr[i+1]){
                    rep=arr[i];
                    break;
                }
            }
            ans1[0]=rep;
            // Function to get the missing number
            for(int i=0;i<n;i++){
                total+=arr[i];
            }
            total =( n*n+ n)/2-total;
            ans1[1]= total+rep;    
        return ans1;
    }
};
// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        Solution ob;
        auto ans = ob.findTwoElement(a, n);
        cout << ans[0] << " " << ans[1] << "\n";
    }
    return 0;
}  // } Driver Code Ends