"""
Given an array of integers nums sorted in ascending order, find the starting 
and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:

    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

Example 2:

    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

Example 3:

    Input: nums = [], target = 0
    Output: [-1,-1]

Constraints:
    1. 0 <= nums.length <= 105
    2. -109 <= nums[i] <= 109
    3. nums is a non-decreasing array.
    4. -109 <= target <= 109
"""


class Solution:
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        """
        Binary search: O(log n), the worst case n + log n
        Runtime: 84ms
        """
        if not nums:
            return [-1, -1]
        
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] == target:
                break
            else:
                l = m + 1
        
        if nums[m] != target:
            return [-1, -1]
        
        i = j = m
        while i >= 0 and nums[i] == target:
            i -= 1
        
        while j < len(nums) and nums[j] == target:
            j += 1

        return [i + 1, j - 1]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        """
        Linear search: O(n), the worst case 2*n
        Runtime: 80ms
        """        
        l = -1
        for i in range(0, len(nums)):
            if nums[i] == target:
                l = i
                break
        
        if l == -1:
            return [-1, -1]
        
        r = -1
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                r = j
                break
        
        return [l, r]
