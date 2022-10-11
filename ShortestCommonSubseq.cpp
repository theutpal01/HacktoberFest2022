#include <iostream>
#include <string>
using namespace std;
 
// Function to find the length of the shortest common supersequence of
// sequences `X[0…m-1]` and `Y[0…n-1]`
int SCSLength(string X, string Y, int m, int n)
{
    // if the end of either sequence is reached, return
    // the length of another sequence
    if (m == 0 || n == 0) {
        return n + m;
    }
 
    // if the last character of `X` and `Y` matches
    if (X[m - 1] == Y[n - 1]) {
        return SCSLength(X, Y, m - 1, n - 1) + 1;
    }
    else {
        // otherwise, if the last character of `X` and `Y` don't match
        return min(SCSLength(X, Y, m, n - 1) + 1,
                    SCSLength(X, Y, m - 1, n) + 1);
    }
}
 
int main()
{
    string X = "ABCBDAB", Y = "BDCABA";
    int m = X.length(), n = Y.length();
 
    cout << "The length of the shortest common supersequence is "
         << SCSLength(X, Y, m, n);
 
    return 0;
}
