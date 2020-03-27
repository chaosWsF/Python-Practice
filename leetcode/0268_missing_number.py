"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

    Input: [3,0,1]
    Output: 2

Example 2:

    Input: [9,6,4,2,3,5,7,0,1]
    Output: 8

Note:
    Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""


class Solution:
    def missingNumber1(self, nums):  # 136ms, 15.6MB
        return set(range(len(nums) + 1)).difference(nums).pop()

    def missingNumber2(self, nums):  # 136ms, 14MB
        nums.sort()
        a = 0
        b = len(nums)
        while a < b:
            c = (a + b) // 2
            if nums[c] > c:
                b = c
            else:
                a = c + 1
        
        return a

    def missingNumber3(self, nums):  # 128ms, 14.9MB
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)
    
    def missingNumber4(self, nums):  # 144ms, 15.1MB
        nums.sort()        
        i = 0
        for num in nums:
            if num == i:
                i += 1
            else:
                return i
        
        return i

    def missingNumber5(self, nums):  # 140ms, 14.1MB
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i ^ num
        
        return res
