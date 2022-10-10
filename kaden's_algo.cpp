#include <bits/stdc++.h>
using namespace std;

int maxSubArray(vector<int> &nums)
{
    int sum = 0;
    int maximum = INT_MIN;

    for (int i = 0; i < nums.size(); i++)
    {
        sum += nums[i];

        if (maximum < sum)
            maximum = sum;

        if (sum < 0)
            sum = 0;
    }

    return maximum;
}

int main()
{
    vector<int> a = {-2, 1, -3, 4, -1, 2, 1, -5, 4};

    int max_sum = maxSubArray(a);
    cout << "Maximum contiguous sum is " << max_sum;
    return 0;
}