#include<iostream>
#include<string>
using namespace std;
int main(){
    int arr1[] = {1,2,3,98,5,6};
    bool swap=false;
    for(int i=0;i<6;i++){
        for(int j=0;j-i;j++){
            int temp;
            
                if((arr1[j]>arr1[j+1])&&swap==false){
                    temp = arr1[j];
                    arr1[j]=arr1[j+1];
                    arr1[j+1]=temp;
                    swap = true;
                    

            

            }
            
        }
        swap = false;
    }

    for(int i = 0; i < 6; i++)
{
    cout<<arr1[i];
}




    

}

// 2nd method

#include <iostream>
using namespace std;

int main()
{
    int n;
    cout<<"Enter size of array "<<endl;
    cin>>n;
    int arr[n],i,j,pass;
    cout<<"Enter the elements"<<endl;

    for(i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    cout<<"Original Array : "<<endl;
    for(i=0;i<n;i++){
        cout<<arr[i]<<endl;
    }
    for(i=0;i<n-1;i++)
    {
        for(j=0;j<n-i-1;j++)
        {
           if(arr[j]>arr[j+1])
            {
                int temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
        pass++;
    }
    cout<<"New Array : "<<endl;
    for(i=0;i<n;i++)
    cout<<arr[i]<<" ";
    cout<<endl;
    cout<<"Number of pass "<<pass;
    return 0;
}


