"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastZero], nums[i] = nums[i], nums[lastZero]
                lastZero += 1
    
    def moveZeroes1(self, nums):  # 44ms
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        while i < n:
            j = 0
            while nums[i + j] == 0:
                j += 1
                if i + j > n - 1:
                    break
            
            n -= j
            nums[i:i + j] = []
            nums += [0] * j
            if j == 0:
                i += 1
    
    def moveZeroes2(self, nums):  # 44ms
        tmp = list(filter(lambda x: x != 0, nums))
        nums[:len(tmp)] = tmp
        nums[len(tmp):] = [0] * (len(nums) - len(tmp))

    def moveZeroes3(self, nums):  # 40ms
        # for i in range(len(nums) - 1, -1, -1):
        for i in range(len(nums))[::-1]:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
