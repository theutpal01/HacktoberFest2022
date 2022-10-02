// Given an integer array nums, return the length of the longest strictly increasing subsequence.

// A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].


class Solution {
public:
    int f(int i,int prev,vector<int>&nums,vector<vector<int>>&dp){
        if(i==nums.size()){
            return 0;
        }
        if(dp[i][prev+1]!=-1){
            return dp[i][prev+1];
        }
        int l=0;
        int r=f(i+1,prev,nums,dp);
        if(prev==-1 || nums[i]>nums[prev]){
            l=1+f(i+1,i,nums,dp);
        }
        
        return dp[i][prev+1]=max(l,r);
    }
    int lengthOfLIS(vector<int>& nums) {
        int n=nums.size();
        vector<vector<int>>dp(n+1,vector<int>(n+1,0));
        for(int i=n-1;i>=0;i--){
            for(int j=i-1;j>=-1;j--){
                    int l=0;
                    int r=dp[i+1][j+1];
                    if(j==-1 || nums[i]>nums[j]){
                        l=1+dp[i+1][i+1];
                    } 
                    dp[i][j+1]=max(l,r);
          }
        }
        return dp[0][0];
        
        // vector<int>dp(n+1,-1);
        return f(0,-1,nums,dp);
    }
};
