def eromoveZeroes(nums):
     Zero_count = 0
     for i in nums:
         if i == 0:
             del nums[nums.index(i)]
             Zero_count=Zero_count+1
        
        
     for i in range(Zero_count):
            nums.append(0)
# ls = [0,0,0,0,0,1] above function is throwing error for this input
# moveZeroes(ls)

# another funtion to solve the question
# // If the current element is not 0, then we need to append it just in front of last non 0 element we found. 

def moveZeroes (nums):
    lastnonzero=0
    for i in range(len(nums)) : 
        if nums[i] !=0:
            nums[i],nums[lastnonzero]=nums[lastnonzero],nums[i]
            lastnonzero=lastnonzero+1
    print(nums)
        

ls=[0,0,0,0,0,0,1,0]
moveZeroes(ls)


# print(ls)
            