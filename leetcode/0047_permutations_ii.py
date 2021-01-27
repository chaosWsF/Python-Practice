"""
Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.

Example 1:

    Input: nums = [1,1,2]
    Output:
        [[1,1,2],
         [1,2,1],
         [2,1,1]]

Example 2:

    Input: nums = [1,2,3]
    Output:
        [[1,2,3],
         [1,3,2],
         [2,1,3],
         [2,3,1],
         [3,1,2],
         [3,2,1]]

Constraints:
    1. 1 <= nums.length <= 8
    2. -10 <= nums[i] <= 10
"""


class Solution:
    def permuteUnique(self, nums):
        """
        48ms
        """
        if len(nums) == 1:
            return [nums]
        
        nums.sort()
        # def helper(arr: List[int]) -> List[List[int]]:
        def helper(arr):
            if len(arr) == 1:
                return [arr]
        
            res = []
            for i in range(len(arr)):
                if i == 0 or arr[i] != arr[i-1]:
                    for l in helper(arr[:i] + arr[(i + 1):]):
                        res.append([arr[i]] + l)
            
            return res

        return helper(nums)