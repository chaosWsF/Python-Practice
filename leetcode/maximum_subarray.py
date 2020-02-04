"""
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum 
and return its sum.

Example:

    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
    If you have figured out the O(n) solution, try coding 
    another solution using the divide and conquer approach, 
    which is more subtle.
"""


class Solution:
    def maxSubArray1(self, nums):
        """dynamical programming, O(n)"""
        max_sum = nums[0]
        max_sub_sum = nums[0]
        for i in range(1, len(nums)):
            max_sub_sum = max(nums[i], max_sub_sum + nums[i])
            max_sum = max(max_sub_sum, max_sum)
        return max_sum

    def maxSubArray2(self, nums):
        """brutal solution, bad"""
        max_sum = nums[0]
        for i in range(len(nums)):
            sub_sum = 0
            for j in range(len(nums) - i):
                sub_sum += nums[i + j]
                if sub_sum > max_sum:
                    max_sum = sub_sum
        return max_sum
