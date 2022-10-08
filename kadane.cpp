#include <iostream>
using namespace std;
int maxSumSubarray(int* arr, int n) {
	int curr_sum = 0;
	int best_sum = INT_MIN;
	for (int i = 0; i < n; i++) {
		curr_sum += arr[i];
		if (curr_sum > best_sum)
			best_sum = curr_sum;
		if (curr_sum < 0)
			curr_sum = 0;
	}
	return best_sum;
}
int main()
{
	int arr[] = {-10,10,20,30,-40,-50};
	cout << maxSumSubarray(arr, 6);
}
