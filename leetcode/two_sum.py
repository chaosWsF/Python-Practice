# Given an array of integers, return indices of the two numbers such that they 
# add up to a specific target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    def twoSum(self, nums, target):
        # hash table
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                return [d[num], i]
            
            d[target - num] = i
    
    def twoSum2(self, nums, target):
        # first try
        for i, num in enumerate(nums):
            # if i == len(nums) - 1:
            #     return None
            
            if (target - num) in nums[i+1:]:
                return [i, len(nums) - 1 - nums[::-1].index(target - num)]
