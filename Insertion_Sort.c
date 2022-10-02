#include<iostream>
using namespace std;
int main()
{
           int count_cmp=0;
           int n,a[20];
           cout<<"Enter the number of elements:";
           cin>>n;
           cout<<"Enter the elements of array:\n";
           for(int i=0;i<n;i++)
                      cin>>a[i];
           char flag;
           cout<<"Enter the order:";
           cin>>flag;
           if(flag=='a' || flag=='A')
           {
                      for(int i=1;i<n;i++)
                      {
                                 int temp=a[i];
                                 int j=i-1;
                                 while(j>=0&&a[j]>temp)
                                 {
                                            count_cmp++;
                                            a[j+1]=a[j];
                                            j--;
                                 }
                                 a[j+1]=temp;
                      }
           }
           else
           {
                      for(int i=1;i<n;i++)
                      {
                                 int temp=a[i];
                                 int j=i-1;
                                 while(j>=0&&a[j]<temp)
                                 {
                                            count_cmp++;
                                            a[j+1]=a[j];
                                            j--;
                                 }
                                 a[j+1]=temp;
                      }
           }
           cout<<"\nElements after Insertion sort:";
           for(int i=0;i<n;i++)
                      cout<<a[i]<<" ";
           cout<<"\nTotal no of comparisons:"<<count_cmp;
           return 0;
}
