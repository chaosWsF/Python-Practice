"""
Implement next permutation, which rearranges numbers into the lexicographically 
next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order 
(i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example 1:

    Input: nums = [1,2,3]
    Output: [1,3,2]

Example 2:

    Input: nums = [3,2,1]
    Output: [1,2,3]

Example 3:

    Input: nums = [1,1,5]
    Output: [1,5,1]

Example 4:

    Input: nums = [1]
    Output: [1]

Constraints:
    1. 1 <= nums.length <= 100
    2. 0 <= nums[i] <= 100
"""


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        
        if i == 0:
            nums.sort()
        else:
            j = i + 1
            while j < n and nums[i-1] < nums[j]:
                j += 1
            
            nums[i-1], nums[j-1] = nums[j-1], nums[i-1]
            a, b = i, n-1
            while a < b:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b -= 1
