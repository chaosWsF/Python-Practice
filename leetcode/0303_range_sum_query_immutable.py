"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

    Given nums = [-2, 0, 3, -5, 2, -1]
    sumRange(0, 2) -> 1
    sumRange(2, 5) -> -1
    sumRange(0, 5) -> -3

Note:
    You may assume that the array does not change.
    There are many calls to sumRange function.
"""


class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, i, j):
        return sum(self.nums[i:j+1])


class NumArray2:
    def __init__(self, nums):
        self.cumsums = {-1: 0}
        tmp = 0
        for i, num in enumerate(nums):
            tmp += num
            self.cumsums[i] = tmp
    
    def sumRange(self, i, j):
        return self.cumsums[j] - self.cumsums[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)