def sortedSquares( nums):
    
    i=0
    j=len(nums)-1
    n=0
    ans=[]
    while i<=j:
        a=nums[i]**2
        b=nums[j]**2
        if a>b:
            ans = [a]+ans
            i+=1
        else :
            ans=[b]+ans
            j-=1
    return ans

print(sortedSquares([-4,-1,0,3,10]))           
        