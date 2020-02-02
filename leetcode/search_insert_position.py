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
        """via median of nums"""
        a = 0
        b = len(nums) - 1
        while nums[a] < target < nums[b]:
            c_left = (a + b) // 2
            c_right = c_left + (a + b) % 2
            if nums[c_left] >= target:
                b = c_left
            else:
                a = c_right
        
        if nums[a] >= target:
            return a
        
        if nums[b] < target:
            return b + 1
        else:
            return b

    def searchInsert2(self, nums, target):
        """python's sorted()/list.sort()"""
        return sorted(nums + [target]).index(target)
