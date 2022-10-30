#include <iostream>
int maxElement(int arr[],int n){
    int max = arr[0];
    for(int i=1;i<n;i++){
        if(arr[i]>max){
            max = arr[i];
        }
    }
    return max;
}
void countSort(int a[],int n,int pos){
    int k=9;
    int count[k+1];
    int b[n];
    for(int i=0;i<=k;i++){
        count[i] = 0;
    }
    for(int j=0;j<k+1;j++){
        count[(a[j]/pos)%10]++;
    }
    for(int i=1;i<k+1;i++){
        count[i] = count[i] + count[i-1];
    }
    for(int j=n-1;j>=0;j--){
        count[(a[j]/pos)%10]--;
        b[count[(a[j]/pos)%10]] = a[j];
        
    }
    for(int i=0;i<n;i++){
        a[i]=b[i];
    }
}


void radixSort(int a[],int n){
    int max = maxElement(a,n);
    for(int pos = 1;(max/pos)>0;pos *= 10){
        countSort(a,n,pos);
    }

}


void printArray(int arr[],int n){
    printf("\nPrinting the Array: \n");
    for(int i=0;i<n;i++){
        printf("%d->",arr[i]);
    }
}

int main(){
    int arr[] = {432,8,530,90,88,23,11,45,677,199};
    int n = sizeof(arr)/sizeof(arr[0]);
    printArray(arr,n);
    radixSort(arr,n);
    printArray(arr,n);

                    
                  
    return 0;
}
