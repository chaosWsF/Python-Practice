class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        
        nums_all = nums1 + nums2

        nums_all = sorted(nums_all)

        mul = (len(nums_all) + 1) // 2
        re = (len(nums_all) + 1) % 2
        mid = [mul - 1, mul + re - 1]
        result = (nums_all[mid[0]] + nums_all[mid[1]]) / 2

        return result


if __name__ == '__main__':
    # input1 = [1, 3]
    # input2 = [2]
    input1 = [1, 2]
    input2 = [3, 4]
    sol = Solution()

    print(sol.findMedianSortedArrays(input1, input2))