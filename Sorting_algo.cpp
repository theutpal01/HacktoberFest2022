#include<iostream>
using namespace std;
void print(int arr[] ,int n);

void selection_sort( int arr[], int n){
 //Non -stable
 //Time complexity-> O(n^2), omega(n^2) , thita(n^2)

    for( int i= 0; i< n ;i++){
         int min=i;
         for( int j=i+1 ;j <n;j++){
            if( arr[j] < arr[min]){
                min =j;
            }
         }
         if( min !=i){
            swap( arr[i],arr[min]);
         }
    }
}

void bubble_sort( int arr[] ,int n){
    //stable sorting
    //Time complexity-> O(n) ,omega(n^2) , thita(n^2)
     for( int i= 0; i< n ;i++){
         bool swaped = false;
         for( int j=0 ;j <n-i-1 ;j++){
            if( arr[j+1] < arr[j]){
                swap(arr[j+1],arr[j]);
                swaped =true;
                
            }
         }
         if( !swaped){
            break;
         }
    }
}

void insertion_sort(int *arr ,int n){
//stable sorting
//Time complexity-> O(n) ,omega(n^2) , thita(n^2)
 
    for( int i=1 ; i<n;i++){
        int temp = arr[i];
        int j=i-1;
        while( j >= 0 && temp < arr[j]){
             arr[j+1] = arr[j];
             j--;
        }
        arr[j+1] = temp;
    }
}
void print(int *arr ,int n){
    for( int i=0 ;i <n ;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}


int main(){
    int arr[] ={ 8,3,9,2,15,7,5,4,12};
    int n = sizeof(arr)/sizeof(arr[0]);

    // Selection sort
    selection_sort( arr,n);
    cout<<"Selection sort printing "<<endl;
    print(arr,n);
   
   //Bubble sort
    int arr1[] ={ 8,3,9,2,15,7,5,4,12};
    bubble_sort(arr1 ,n);
    cout<<"Bubble sort printing "<<endl;
    print(arr1,n);
   
    //insertion sort
     int arr2[] ={ 8,3,9,2,15,7,5,4,12};
     insertion_sort(arr2 ,n);
     cout<<"Insertion sort printing "<<endl;
     print(arr2,n);

    return 0;
}