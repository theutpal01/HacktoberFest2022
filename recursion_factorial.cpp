#include <bits/stdc++.h> 
using namespace std;
 
 
 
 
void c_p_c(){
ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
 #ifndef ONLINE_JUDGE
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
#endif
}
 
 long int factorial(int n){

    if(n==0)
    return 1;

    return n*factorial(n-1);
 }
 
 //Time complexity=O(N);
 //Space complexity=O(N);worst case 
 
 
 
int main()
{
 c_p_c();
 
 int n;
 printf("Enter the number : ");
 cin>>n;

 cout<<"Factorial of the given number is"<<factorial(n)<<endl;

 return 0;
}
 
 
 