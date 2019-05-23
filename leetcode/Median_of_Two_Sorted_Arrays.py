class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) < len(nums2):
            tmp = nums1
            nums1 = nums2
            nums2 = tmp
        
        start = (len(nums1) - 1) // 2
        for bi in nums2:
            while nums1[start] != bi:
                if nums1[start] < bi:
                    start = (start + len(nums1)) // 2
                else:
                    start = (start - 1) // 2
        
        if len(nums1) % 2 == 0:
            result = (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2
        else:
            result = nums1[len(nums1) // 2]
        
        return result


if __name__ == '__main__':
    input1 = [1, 3]
    input2 = [2]
    sol = Solution()

    print(sol.findMedianSortedArrays(input1, input2))