#include <iostream>
using namespace std;

// Time Complexity:O(NLogN),N->no of elements of the array
// Space Complexity:O(N):merging into the final array
void merge(int arr[], int l, int mid, int r)
{
    int n1 = mid - l + 1;
    int n2 = r - mid;
    int a[n1], b[n2]; // temp arrays to store half of the arrays
    for (int i = 0; i < n1; i++)
    {
        a[i] = arr[l + i];
    }
    for (int j = 0; j < n2; j++)
    {
        b[j] = arr[mid + 1 + j];
    }
    int m = 0;
    int n = 0, k = l;
    while (m < n1 && n < n2)
    {
        // compare each element in both the 2 temp arrays
        // merge the smallest one into the final array
        if (a[m] < b[n])
        {
            arr[k] = a[m];
            k++;
            m++;
        }
        else
        {
            arr[k] = b[n];
            k++;
            n++;
        }
    }
    // when anyone of the list exhausts we continue with the other one
    while (m < n1)
    {
        arr[k] = a[m];
        k++;
        m++;
    }
    while (n < n2)
    {
        arr[k] = b[n];
        k++;
        n++;
    }
}
void mergeSort(int arr[], int l, int r)
{

    // divide the list until the condn. is met
    if (l < r)
    {
        int mid = (l + r) / 2;
        mergeSort(arr, l, mid);
        mergeSort(arr, mid + 1, r);

        merge(arr, l, mid, r);
    }
}
int main()
{

    int arr[] = {5, 4, 9, 6, 1, 7, 3};
    mergeSort(arr, 0, 6);
    cout << "Sorted Array:";
    for (int i = 0; i < 7; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}