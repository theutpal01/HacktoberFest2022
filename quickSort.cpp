#include <iostream>
using namespace std;

int partition(int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++)
    {
        if (arr[j] < pivot)
        {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return (i + 1);
}
void sort(int arr[], int low, int high)
{
    if (low < high)
    {
        int pi = partition(arr, 0, high);
        sort(arr, low, pi - 1);
        sort(arr, pi + 1, high);
    }
}

void printArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
}

int main()
{
    int a[] = {3, 2, 5, 7, 6};
    int size = sizeof(a) / sizeof(a[0]);
    sort(a, 0, size);
    printArray(a, size);
}