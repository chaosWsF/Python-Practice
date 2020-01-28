"""
Given an integer array nums, find the contiguous subarray (containing at 
least one number) which has the largest sum and return its sum.

Example:

    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
    If you have figured out the O(n) solution, try coding another 
    solution using the divide and conquer approach, which is more 
    subtle.
"""


class Solution:
    def maxSubArray(self, nums):
        """..."""
        return ...

    def maxSubArray2(self, nums):
        """brutal solution, bad"""
        max_sum = sum(nums)
        for n_sub in range(1, len(nums)):
            for i in range(len(nums) - n_sub + 1):
                sub_sum = sum(nums[i:i+n_sub])
                if sub_sum > max_sum:
                    max_sum = sub_sum
        return max_sum
