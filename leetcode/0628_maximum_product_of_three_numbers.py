"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

    Input: [1,2,3]
    Output: 6

Example 2:

    Input: [1,2,3,4]
    Output: 24

Note:
    1. The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
    2. Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""


class Solution:
    def maximumProduct(self, nums):    # 280ms
        nums.sort()
        # return max(nums[0] * nums[1], nums[-3] * nums[-2]) * nums[-1]
        if nums[1] < 0:
            return max(nums[0] * nums[1], nums[-3] * nums[-2]) * nums[-1]
        else:
            return nums[-3] * nums[-2] * nums[-1]

    def maximumProduct2(self, nums):    # 252ms
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        for i in nums:
            if i > max1:
                max1, max2, max3 = i, max1, max2
            elif i > max2:
                max2, max3 = i, max2
            elif i > max3:
                max3 = i
            
            if i < min1:
                min1, min2 = i, min1
            elif i < min2:
                min2 = i
        
        if min2 < 0:
            return max(min1 * min2, max2 * max3) * max1
        else:
            return max1 * max2 * max3
