def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, value in enumerate(nums):
        if target - value in seen:
            return [seen[target - value], i]
        seen[value] = i
