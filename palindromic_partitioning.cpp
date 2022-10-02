/*
QUESTION_______
Given a string str, a partitioning of the string is a palindrome partitioning if every sub-string
of the partition is a palindrome. Determine the fewest cuts needed for palindrome partitioning
of given string.

EXAMPLE_______
Input: str = "ababbbabbababa"
Output: 3
Explanation: After 3 partitioning, the palidromic substrings are "a", "babbbab", "b", "ababa".
*/

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int dp[501][501];

bool isPalindrome(string s, int i, int j)
{
    while (i < j)
    {
        if (s[i] != s[j])
            return false;
        i++;
        j--;
    }
    return true;
}

int ppUtil(string s, int i, int j)
{
    // Base Condition 1 => s.length() == 1 implies it is a single letter palindrome and no cut needed.
    if (i >= j)
        return 0;

    // Base Condition 2 => If s is a Palindrome itself, no more cuts needed.
    if (isPalindrome(s, i, j))
        return 0;

    // Memoization -> Checking if we already have the answer in store
    if (dp[i][j] != -1)
        return dp[i][j];

    int minCost = INT_MAX, tmpans;

    for (int k = i; k <= j - 1; k++)
    {

        // Checking if Left and Right are computed or not.
        int left = dp[i][k], right = dp[k + 1][j];

        if (left == -1)
        {
            left = ppUtil(s, i, k);
            dp[i][k] = left;
        }
        if (right == -1)
        {
            right = ppUtil(s, k + 1, j);
            dp[k + 1][j] = right;
        }

        tmpans = left + right + 1;
        minCost = min(minCost, tmpans);
    }

    // Store the answer(Memoization) for future reference, prevent re-calculation of the same answer in future
    dp[i][j] = minCost;
    return minCost;
}

int palindromicPartition(string str)
{
    // Initializing the dp with -1
    memset(dp, -1, sizeof(dp));
    return ppUtil(str, 0, str.length() - 1);
}

int main()
{

    string str;
    cout << "\nEnter String: ";
    cin >> str;

    int res = palindromicPartition(str);
    cout << "\nLEAST Cuts Required for palindrome partitioning : " << res << endl;
}
