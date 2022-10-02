#include<iostream>
using namespace std;
int count_cmp=0;
void merge_array_desc(int a[],int lb,int mid,int ub)
{
           int i=lb;
           int j=mid+1;
           int b[20],k=lb;
           while(i<=mid && j<=ub)
           {
                      if(a[i]>=a[j])
                      {
                                 count_cmp++;
                                 b[k]=a[i];
                                 i++;
                      }
                      else
                      {
                                 count_cmp++;
                                 b[k]=a[j];
                                 j++;
                      }
                      k++;
           }
           if(i>mid)
           {
                      while(j<=ub)
                      {
                                 count_cmp++;
                                 b[k++]=a[j];
                                 j++;
                      }
           }
           else
           {
                      while(i<=mid)
                      {
                                 count_cmp++;
                                 b[k++]=a[i];
                                 i++;
                      }
           }
           for(int k=lb;k<=ub;k++)
                      a[k]=b[k];
}
void merge_array(int a[],int lb,int mid,int ub)
{
           int i=lb;
           int j=mid+1;
           int b[20],k=lb;
           while(i<=mid && j<=ub)
           {
                      if(a[i]<=a[j])
                      {
                                 count_cmp++;
                                 b[k]=a[i];
                                 i++;
                      }
                      else
                      {
                                 count_cmp++;
                                 b[k]=a[j];
                                 j++;
                      }
                      k++;
           }
           if(i>mid)
           {
                      while(j<=ub)
                      {
                                 count_cmp++;
                                 b[k++]=a[j];
                                 j++;
                      }
           }
           else
           {
                      while(i<=mid)
                      {
                                 count_cmp++;
                                 b[k++]=a[i];
                                 i++;
                      }
           }
           for(int k=lb;k<=ub;k++)
                      a[k]=b[k];
}
void merge_sort(int a[],int lb,int ub,int flag)
{
           int mid;
           if(lb<ub)
                      mid=((lb+ub)/2);
           merge_sort(a,lb,mid,flag);
           merge_sort(a,mid+1,ub,flag);
           if(flag=='a' || flag=='A')
                      merge_array(a,lb,mid,ub);
           else
                      merge_array_desc(a,lb,mid,ub);
}
int main()
{
           int n,a[20];
           cout<<"Enter the number of elements:";
           cin>>n;
           cout<<"Enter the elements of array:\n";
           for(int i=0;i<n;i++)
                      cin>>a[i];
           char flag;
           cout<<"Enter the order:";
           cin>>flag;
           merge_sort(a,0,n,flag);
           cout<<"\nElements after Merge sort:";
           for(int i=0;i<n;i++)
                      cout<<a[i]<<" ";
           cout<<"\nTotal no of comparisons:"<<count_cmp;
           return 0;
}
