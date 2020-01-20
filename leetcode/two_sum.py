class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                return [d[num], i]
            
            d[target - num] = i
