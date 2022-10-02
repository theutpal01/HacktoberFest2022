#include<bits/stdc++.h>
#include<iostream>

using namespace std;

long numlen(long num)
{
    int count = 0;
    while (num > 0)
    {
        count++;
        num /= 10;
    }
    return count;
}
long long power(int n)
{
    int i;
    long long int p=1;
    for(i=1;i<=n;i++)
    {
        p=p*10;
    }
    return p;
}
long long karatsuba(long long a, long long b)
{
    if (a < 10 && b < 10)
        return a * b;
    int size = max(numlen(a), numlen(b));
    int n1 = (int)ceil(size / 2.0);
    long p1 = (long long)power(n1);
    long a1 = (long long)floor(a / (double)p1);
    long a2 = a % p1;
    long b1 = (long long)floor(b/ (double)p1);
    long b2 = b% p1;
    long U = karatsuba(a1, b1);
    long V = karatsuba(a2, b2);
    long W = karatsuba(a1 - a2, b1 - b2);
    long Z = U + V - W;
    return (long long)(power(2 * n1) * U+ power(n1) * Z+ V);
}

int main()
{
    int a, b;
    cout<< "Enter the first number : ";
    cin>> a;
    cout<< "Enter the second number: ";
    cin>> b;
    cout<<a<<" * "<<b<<" = ";
    cout<<karatsuba(a,b);
    
    cout<<endl;
}