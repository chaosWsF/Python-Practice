"""
Given two arrays, write a function to compute their intersection.

Example 1:

    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

Example 2:

    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]

Note:
    Each element in the result must be unique.
    The result can be in any order.
"""


class Solution:
    def intersection1(self, nums1, nums2):  # 56ms
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        
        return list(set(nums1).intersection(nums2))

    def intersection2(self, nums1, nums2):  # 40ms
        return list(set(nums1) & set(nums2))
