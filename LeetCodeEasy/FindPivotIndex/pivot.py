# https://leetcode.com/problems/find-pivot-index/submissions/
def sum(numbers):
    s=0
    for i in numbers:
        s+=i
    return s

def pivotIndex(nums):
    
    for start in range(len(nums)):
        leftsum=sum(nums[0:start])
        rightsum=sum(nums[start+1:len(nums)])
        if(leftsum==rightsum):
            return start
    return -1
print(pivotIndex([2,1,-1]))
        