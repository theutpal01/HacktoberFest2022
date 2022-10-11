#include <iostream>
#include <string>
using namespace std;

int main(){
string str;
getline (cin, str);
int len=str.length();
int arr[len];
for(int i=0; i<len; i++){
    int j=int(str[i]);
    arr[i]=j;
}

for(int k=0; k<len; k++){
    int j=arr[k];
    int sz=8;
    int chara[sz];
    while(sz--){
        int t=j%2;
        chara[sz]=t;
        j/=2;
    }
    for(int g=0; g<8;g++){ cout<<chara[g];}
}
return 0;
}