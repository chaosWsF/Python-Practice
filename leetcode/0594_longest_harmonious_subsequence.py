"""
We define a harmounious array as an array where the difference between its maximum value and its minimum 
value is exactly 1. Now, given an integer array, you need to find the length of its longest harmonious 
subsequence among all its possible subsequences.

Example 1:

    Input: [1,3,2,2,5,2,3,7]
    Output: 5
    Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Note: The length of the input array will not exceed 20,000.
"""

from collections import Counter


class Solution:
    def findLHS1(self, nums):
        res = 0
        nums = Counter(nums)
        for i in nums:
            if i + 1 in nums:
                res = max(res, nums[i+1] + nums[i])
        
        return res
    
    def findLHS2(self, nums):
        nums = Counter(nums)
        return max([nums[i] + nums[i+1] for i in nums if i + 1 in nums] or [0])
