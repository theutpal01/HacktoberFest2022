#include<stdio.h>
int printFibonacci(int i)
{
    if (i == 0)
        return 0;
    else if (i == 1)
        return 1;
    else
    {
        return printFibonacci(i - 1) + printFibonacci(i - 2);
    }
}
int main()
{
    int n, x, i;
    printf("\nEnter the number : ");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        x = printFibonacci(i);
        printf("%d ", x);
    }
}