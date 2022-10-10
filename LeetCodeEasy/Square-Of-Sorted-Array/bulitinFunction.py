def sortedSquares( nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = []
    for i in nums:
        # ele = i**2
        # ans=[ele]+ans
        ans.append(i*i)
    ans.sort()
    return ans
print(sortedSquares([-7,-3,2,3,11]))