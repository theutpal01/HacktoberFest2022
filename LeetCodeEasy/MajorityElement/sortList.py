
def majorityElement(nums):
    nums.sort()
    start=0
    next = 1
    maj=1
    maxmaj=0
    ans=int()
    end=len(nums)-1
    while start<end:
        if nums[start]==nums[next]:
            maj+=1
        else:
            if maxmaj<maj:
                maxmaj=max(maxmaj,maj)
                ans = nums[start]
            maj=1
        start+=1
        next+=1
    if maxmaj<maj:
        ans = nums[start]
    return ans
        
    
ans =majorityElement([3,3,4])
print(ans)
