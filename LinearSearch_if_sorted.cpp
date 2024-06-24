#include<iostream>
using namespace std;

int main(){

    int arr[] = {1,2,5,6,7,9};
    int n=sizeof(arr)/sizeof(arr[0]);


    int target = 2;

bool check = false;

    for(int i=0;i<n;i++){
        if(arr[i] == target){
            cout<<target<<" , Found at "<<i+1<<" Position ."<<endl;
            check = true;
            break;
        }

        if(arr[i] > target ){  // optimization
            break;
        }
    }

    


    if(!check){
        cout<<target << " , Not Found";
    }




        // Time Comp : O(n);


}