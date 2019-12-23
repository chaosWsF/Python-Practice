class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 < n2:
            tmp = nums1
            nums1 = nums2
            nums2 = tmp
        
        start = 0
        end = n1 - 1
        for bi in nums2:
            # TODO add if statement to deal with bi overflow
            if bi <= nums1[0]:
                pass
            elif bi >= nums1[-1]:
                pass
            else:
                mid = (start + end) // 2
                while (nums1[mid] != bi) and (end - start > 1):
                    if nums1[mid] < bi:
                        start = mid + 1
                        end = end
                        mid = (start + end) // 2
                    else:
                        start = (start - 1) // 2
        
        if (n1 + n2) % 2 == 0:
            result = (nums1[(n1 + n2) // 2 - 1] + nums1[(n1 + n2) // 2]) / 2
        else:
            result = nums1[(n1 + n2) // 2]
        
        return result


if __name__ == '__main__':
    input1 = [1, 3]
    input2 = [2]
    sol = Solution()

    print(sol.findMedianSortedArrays(input1, input2))