
def runningSum( nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    for i in range(1,len(nums)):
        nums[i]=nums[i-1]+nums[i]
    return nums

print("Running Sum : ", runningSum([1,3,5,6]))