def maxSubArray(nums):
    if len(nums) > 1:        
        current_sum = 0
        max_sum = -10000000
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum
    return nums[0]
