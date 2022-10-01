#include<bits/stdc++.h>
using namespace std;



int findMy_Ans(int low , int high , int arr[] , int n  , int target){

    if(low > high){
        return -1;   // if u return low    ,, then in ans  it will return the appropriate pos of ele where it can be settle appropriatly
        
    }

    int mid = (low+high)/2;

    if(arr[mid] == target){
        return mid;
    }

    else if(target > arr[mid]){
        low = mid+1;
    }

    else{
        high = mid-1;
    }

    return findMy_Ans(low , high , arr , n , target);


}


int main(){


    int arr[] = {5,7,7,8,10};
    int target = 10;

    int n=sizeof(arr)/sizeof(arr[0]);

    int low = 0;
    int high = n-1;



   cout<<findMy_Ans(low , high , arr , n , target)<<endl;

    // Time Comp : O(log(n));
    
   return 0;

}