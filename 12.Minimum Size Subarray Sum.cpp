class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
       long long n=nums.size();
       long long int sum=0,minLength=n+1,start=0,end=0;
       while(end<n){
           while(sum<target && end<n){
                sum+=nums[end++];   
            }
            while(sum>=target && start<n){
                if(end-start<minLength){
                   minLength=end-start;
                }
                sum-=nums[start++];    
            }
       }
       if(minLength==nums.size()+1){
           return 0;
       }
    return minLength;
    }
};