#include<bits/stdc++.h>
using namespace std;
void show(vector<int> v){
    for(int x:v){
        cout<<x<<' ';
    }
    cout<<'\n';
    return;
}
void sort(vector<int> &arr, int n){
    for(int i = 0;i<n-1;i++){
        int min = i;
        for(int j = i+1;j<n;j++){
            if(arr[j]<arr[min])
            min = j;
        }
        swap(arr[min],arr[i]);
    }
    return;
}
int main(){
    int n;
    vector<int> v;
    cout<<"Enter number of elements :\n";
    cin>>n;
    cout<<"Enter array :\n";
    for(int i = 0; i < n; i++){
        int k;
        cin>>k;
        v.push_back(k);
    }
    sort(v,n);
    show(v);
    return 0;
}