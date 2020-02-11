"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into
nums1 as one sorted array.

Note:

    The number of elements initialized in nums1 and nums2 are m 
    and n respectively.

    You may assume that nums1 has enough space (size that is 
    greater or equal to m + n) to hold additional elements from 
    nums2.

Example:

    Input:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3

    Output: [1,2,2,3,5,6]
"""


class Solution:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    def merge1(self, nums1, m, nums2, n):
        """Two Pointers"""
        i = 0
        j = 0
        while j < n:
            while i < m and nums1[i] <= nums2[j]:
                i += 1
            
            if i == m:
                nums1[m:] = nums2[j:]
                break

            nums1[i+1:] = nums1[i:-1]
            nums1[i] = nums2[j]
            i += 1
            m += 1         
            j += 1

    def merge2(self, nums1, m, nums2, n):
        """Builtin Method"""
        if not nums2:
            return nums1
        
        nums1[m:] = nums2
        nums1.sort()
