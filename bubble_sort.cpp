/* Optimized BUBBLE SORT */
#include<bits/stdc++.h>
#include<iostream>
#include<string>
using namespace std;
void swap(int *a,int *b)
{
    int c=*a;
    *a=*b;
    *b=c;
}
void bubble_sort(int a[],int n)
{
    int i,j;
    bool temp;
    for(i=0;i<n-1;i++)
    {
        temp=false;
       for(j=0;j<n-1-i;j++)
       {
           if(a[j]>a[j+1])
           {
               swap(&a[j],&a[j+1]);
               temp=true;
           }
       }
       if(temp==false)
       {
           break;
       }
    }

}
void print(int a[],int n)
{
    int t;
    for(t=0;t<n;t++)
    {
       cout<<a[t]<<" "; 
    }
    cout<<"\n";
}
int main()
{
    int n;
cout<<"Enter the size of array:";
cin>>n;
int a[n];
cout<<"\nEnter the elements of array:";
for(int i=0;i<n;i++)
{
    cin>>a[i];
}
bubble_sort(a,n);
cout<<"\nSorted array: ";
print(a,n);
return 0;
}

// {
//     int arr1[] = {1,2,3,98,5,6};
//     bool swap=false;
//     for(int i=0;i<6;i++){
//         for(int j=0;j-i;j++){
//             int temp;
            
//                 if((arr1[j]>arr1[j+1])&&swap==false){
//                     temp = arr1[j];
//                     arr1[j]=arr1[j+1];
//                     arr1[j+1]=temp;
//                     swap = true;
                    

            

//             }
            
//         }
//         swap = false;
//     }

//     for(int i = 0; i < 6; i++)
// {
//     cout<<arr1[i];
// }
// }


