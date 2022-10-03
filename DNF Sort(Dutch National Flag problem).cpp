 // Sort an array of 0s, 1s and 2s | Dutch National Flag problem
 
//  Given an array A[] consisting of only 0s, 1s, and 2s. The task is to arrange the array in non-decreasing order.


#include <bits/stdc++.h>
using namespace std;

// Function to sort the input array
void sort(int arr[], int arr_size)
{
	int low = 0;
	int high = arr_size - 1;
	int mid = 0;
  
	while (mid <= high) {
		switch (arr[mid]) {

		// Element is 0
		case 0:
			swap(arr[low++], arr[mid++]);
			break;

		// Element is 1 .
		case 1:
			mid++;
			break;

		// Element is 2
		case 2:
			swap(arr[mid], arr[high--]);
			break;
		}
	}
}

//print array arr[]
void printArray(int arr[], int arr_size)
{
	for (int i = 0; i < arr_size; i++)
		cout << arr[i] << " ";
}

int main()
{
  int n;
  cin >> n;
  int arr[n];
  for(int i=0;i<n;i++)
    cin >> arr[i]; 
	sort(arr, n);

	printArray(arr, n);

	return 0;
}


 
