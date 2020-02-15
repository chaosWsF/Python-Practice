"""
There are two sorted arrays nums1 and nums2 of size m and n 
respectively.

Find the median of the two sorted arrays. The overall run time 
complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0

Example 2:

    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """Bulitin Method (Slow)"""
        nums_all = nums1 + nums2
        nums_all = sorted(nums_all)
        mul = (len(nums_all) + 1) // 2
        re = (len(nums_all) + 1) % 2
        mid = [mul - 1, mul + re - 1]
        result = (nums_all[mid[0]] + nums_all[mid[1]]) / 2
        return result
