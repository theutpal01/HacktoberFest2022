#include <iostream>
using namespace std;

void sort(int arr[], int start, int end)
{
    for (int i = 1; i < end; i++)
    {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
void printArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
}
int main()
{
    int a[] = {4, 1, 3, 6, 7};
    int size = sizeof(a) / sizeof(a[0]);
    sort(a, 0, size);
    printArray(a, size);
}