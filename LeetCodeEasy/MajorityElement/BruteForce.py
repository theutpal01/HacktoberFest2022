# https://leetcode.com/problems/majority-element/
def majorityElement(nums):
    dict = {}
    for i in nums:
        dict[i]=dict.get(i,0)+1
    for x,y in dict.items():
        if(y>len(nums)/2):
            return x
    
print(majorityElement([3,2,3]))
    