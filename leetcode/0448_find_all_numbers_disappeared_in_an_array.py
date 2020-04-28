"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
    Input: [4,3,2,7,8,2,3,1]
    Output: [5,6]
"""


class Solution:
    def findDisappearedNumbers1(self, nums):
        return list(set(range(1, len(nums) + 1)).difference(nums))

    def findDisappearedNumbers2(self, nums):
        """O(1) space by setting negative value"""
        n = len(nums)
        i = 0
        while i < n:
            j = abs(nums[i]) - 1
            nums[j] = -abs(nums[j])
            i += 1
        
        res = []
        i = 0
        while i < n:
            if nums[i] > 0:
                res.append(i + 1)
            
            i += 1
        
        return res
