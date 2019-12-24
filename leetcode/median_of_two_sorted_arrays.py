class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        
        nums_all = nums1 + nums2

        nums_all = sorted(nums_all)

        mul = (len(nums_all) + 1) // 2
        re = (len(nums_all) + 1) % 2
        mid = [mul - 1, mul + re - 1]
        result = (nums_all[mid[0]] + nums_all[mid[1]]) / 2

        return result
