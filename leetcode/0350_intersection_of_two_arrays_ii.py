"""
Given two arrays, write a function to compute their intersection.

Example 1:

    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]

Example 2:

    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [4,9]

Note:

    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:
    What if the given array is already sorted? How would you optimize your algorithm?    self.intersect2
    What if nums1's size is small compared to nums2's size? Which algorithm is better?    self.intersect1
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?    sub-range
"""


class Solution:
    def intersect1(self, nums1, nums2):  # 40ms
        if len(nums1) > len(nums2):
            return self.intersect1(nums2, nums1)
        
        nums1_counter = {}
        for n in nums1:
            nums1_counter[n] = nums1_counter.get(n, 0) + 1
        
        res = []
        for n in nums2:
            if (n in nums1_counter) and (nums1_counter[n] != 0):
                nums1_counter[n] -= 1
                res.append(n)

        return res

    def intersect2(self, nums1, nums2):  # 52ms
        nums1.sort()
        nums2.sort()

        res = []
        i = 0
        j = 0
        while (i < len(nums1)) and (j < len(nums2)):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            else:
                j += 1
        
        return res
