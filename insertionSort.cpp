#include <iostream>
using namespace std;
int insertion(int *a, int n)
{
    for (int i = 0; i < n; i++)
    {
        int temp = a[i];
        int j = i - 1; 

        while (j >= 0 && a[j] > temp)
        {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = temp;
    }
    return 0;
}

void print(int *a, int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << ",";
    }
}
int main()
{
    int n=9;
    int a[] = {12, 13, 8, 2, 16, 5, 0, 1, 4};

    insertion(a, n);
    print(a, n);
}
