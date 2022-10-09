#include <bits/stdc++.h> 
using namespace std;
 
 
 
 
void c_p_c(){
ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
 #ifndef ONLINE_JUDGE
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
#endif
}
 
 
  void linearSearch(int arr[],int i,int n,int key){

     
    if(arr[i]==key){
    cout<<"Element found at index "<<i<<endl;
       }

       
      else if(i==n){
    cout<<"Element not found"<<endl;
 }

    else{

        linearSearch(arr,i+1,n,key);
    }

     }
     
     
  

 
 
 
 
int main()
{
// c_p_c();
 
  int n;
 cin>>n;

 int arr[n];
 for(int i=0;i<n;i++){
    cin>>arr[i];
 }

 int key;
 cin>>key;
 
 linearSearch(arr,0,n,key);
 
 return 0;
}
 
 
 