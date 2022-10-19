// C program to implement Binary Search

#include <stdio.h>

int binarySearch(int ar[], int k, int low, int high)
{
    // Repeat until the pointers low and high meet each other
    while (low <= high)
    {
        int mid = low + (high - low) / 2;

        if (ar[mid] == k)
            return mid;

        if (ar[mid] < k)
            low = mid + 1;

        else
            high = mid - 1;
    }

    return -1;
}

int main(void)
{
    int ar[] = {3, 4, 5, 6, 7, 8, 9};
    int n = sizeof(ar) / sizeof(ar[0]);
    int k = 4;
    int ans = binarySearch(ar, k, 0, n - 1);
    if (ans == -1)
        printf("Not found");
    else
        printf("Found at index : %d", ans);
    return 0;
}