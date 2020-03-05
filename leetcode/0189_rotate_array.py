"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

    Input: [1,2,3,4,5,6,7] and k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 step to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

    Input: [-1,-100,3,99] and k = 2
    Output: [3,99,-1,-100]
    Explanation: 
    rotate 1 step to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]

Note:
    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?
"""


class Solution:
    """
    Do not return anything, modify nums in-place instead.
    """
    def rotate1(self, nums, k):
        """move the first term (52ms)"""
        # k %= len(nums)
        tmp = nums[:len(nums)-k]
        nums[:len(nums)-k] = []
        nums += tmp

    def rotate2(self, nums, k):
        """move the last term (52ms)"""
        # k %= len(nums)
        tmp = nums[len(nums)-k:]
        nums[len(nums)-k:] = []
        nums[:0] = tmp
    
    def rotate3(self, nums, k):
        """copy the list (56ms)"""
        k %= len(nums)
        tmp = nums * 2
        del nums[:]
        nums[:] = tmp[len(nums)-k:2*len(nums)-k]

    def rotate4(self, nums, k):
        """reverse the list (52ms)"""
        k %= len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

    def rotate5(self, nums, k):
        """Cyclic Replacements (56ms)"""
        k %= len(nums)
        c = 0
        start = 0
        while c < len(nums):
            cur = start
            previous = nums[start]
            while True:
                next_index = (cur + k) % len(nums)
                tmp = nums[next_index]
                nums[next_index] = previous
                previous = tmp
                cur = next_index
                c += 1
                if cur == start:
                    break
            start += 1
