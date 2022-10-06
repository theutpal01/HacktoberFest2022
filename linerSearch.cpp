// Code contribute by Anamika Pandey


#include<iostream>

using namespace std;

bool search ( int arr[] , int size , int key){
  for(int i =0 ; i< size; i++){
if(arr[i] == key)
  return 1;

 }
 return 0;

}

 int main(){

 int  arr[8] = { 2 , 45 , 8 , 19 , -5 , 54, 91 , -3 };
 for(int i = 0; i<arr.length; i++){
 int  key ;
 cin >> key;
 }

  bool found = search( arr, 10,key );
  if ( found ){ 
    cout<<"key is found"<<endl;
  }
else{
    cout<<"key not found"<<endl;
}
 }
