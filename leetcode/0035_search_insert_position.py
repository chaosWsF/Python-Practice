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
        """binary search"""
        a = 0
        b = len(nums) - 1
        while a <= b:
            c = (a + b) // 2
            m = nums[c]
            if m < target:
                a = c + 1
            elif m == target:
                return c
            else:
                b = c - 1
        
        return a

    def searchInsert2(self, nums, target):
        """python's sorted()/list.sort()"""
        return sorted(nums + [target]).index(target)

    def searchInsert3(self, nums, target):
        """linear search"""
        if nums[0] >= target:
            return 0

        for i in range(len(nums) - 1):
            if nums[i] < target <= nums[i + 1]:
                return i + 1
        
        if nums[-1] == target:
            return len(nums) - 1
        else:
            return len(nums)
