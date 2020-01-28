"""
Given a sorted array and a target value, return the index if 
the target is found. If not, return the index where it would 
be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

    Input: [1,3,5,6], 5
    Output: 2

Example 2:

    Input: [1,3,5,6], 2
    Output: 1

Example 3:

    Input: [1,3,5,6], 7
    Output: 4

Example 4:

    Input: [1,3,5,6], 0
    Output: 0
"""


class Solution:
    def searchInsert(self, nums, target):
        a = 0
        b = len(nums) - 1
        while nums[a] < target < nums[b]:
            c_left = (a + b) // 2
            c_right = c_left + (a + b) % 2
            n_mid_left = nums[c_left]
            n_mid_right = nums[c_right]
            if n_mid_left > target:
                b = c_left
            elif n_mid_left == target:
                return c_left
            elif n_mid_left < target <= n_mid_right:
                return c_right
            else:
                a = c_right
        
        if nums[a] >= target:
            return a
        
        if nums[b] < target:
            return b + 1
        else:
            return b
