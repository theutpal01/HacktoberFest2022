#include<iostream>
using namespace std;

int main(){

    int arr[] = {6,4,1,9,2,5};
    int n=sizeof(arr)/sizeof(arr[0]);


    int target = 2;

bool check = false;

    for(int i=0;i<n;i++){
        if(arr[i] == target){
            cout<<target<<" , Found at "<<i+1<<" Position ."<<endl;
            check = true;
            break;
        }
    }

    if(!check){
        cout<<target << " , Not Found";
    }





// Time Comp : O(n);


}