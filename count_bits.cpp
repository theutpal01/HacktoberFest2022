//program to count the number of bits in a nummber

#include<iostream>
using namespace std;

int countBits(int n){
    int count = 0;
    while(n>0){
        int last_bit = (n&1);
        count += last_bit;
        n = n>>1; 
    }
    return count;
}

//returns faster output
int countBits_hack(int n){

    int count = 0;
    while(n>0){
        //removes the last set bit from the current integer
        n = (n & (n-1));
        count++;
    }

    return count;
}

int main(){
    int n;
    cin>>n;

    cout<<"No. of bits in "<<n<<": "<<countBits(n)<<endl;
    
    return 0;
}
