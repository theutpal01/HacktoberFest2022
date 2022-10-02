
#include <bits/stdc++.h>
using namespace std;

int largest(int arr[], int n, int i)
{

	if (i == n - 1) {
		return arr[i];
	}
	int recMax = largest(arr, n, i + 1);

	return max(recMax, arr[i]);
}


     int main()
{
    int arr[5];
    cout<<"Enter 5 numbers: ";
    
      for(int i=0;i<5;i++){
        cin>>arr[i];}
    
	int n = sizeof(arr) / sizeof(arr[0]);
	cout << "Largest in of the 5 numbers is "
		<< largest(arr, n, 0);
	return 0;
}


