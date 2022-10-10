
from re import L


# brute force solution 
def twosumbrute( nums , target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            # print(i,j)
            if nums[i]+nums[j]==target:
                return [i,j]
            
def twosum(nums , target):
    dict={}
    for i in range(len(nums)):
        temp = target - nums[i];
        if temp in list(dict.keys()):
            # print([dict[temp],i])
            return [dict[temp],i]
            # break
        dict[nums[i]]=i
twosum([3,2,4],  6)
# print(ans)