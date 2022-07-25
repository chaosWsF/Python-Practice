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
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # back assigning
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            
        if m == 0:
            nums1[:n] = nums2[:n]
        
        # if n == 0:
        #     return 
        
        # if m == 0:
        #     nums1[:n] = nums2
        
        # i, j = 0, 0
        # while i < m and j < n:
        #     if nums1[i] > nums2[j]:
        #         nums1[i+1:] = nums1[i:-1]
        #         nums1[i] = nums2[j]
        #         j += 1
        #         m += 1
            
        #     i += 1
        
        # if i == m:
            nums1[m:] = nums2[j:]

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
