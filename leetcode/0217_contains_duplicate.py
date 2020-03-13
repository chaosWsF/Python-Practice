"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and 
it should return false if every element is distinct.

Example 1:

    Input: [1,2,3,1]
    Output: true

Example 2:

    Input: [1,2,3,4]
    Output: false

Example 3:

    Input: [1,1,1,3,3,4,3,2,4,2]
    Output: true
"""


class Solution:
    def containsDuplicate(self, nums):    # 120ms
        return len(set(nums)) != len(nums)
    
    def containsDuplicate2(self, nums):
        """124ms"""
        if not nums:
            return False
        
        d = {}
        for num in nums:
            if num in d:
                return True
            else:
                d[num] = 1
        
        return False
    
    def containsDuplicate3(self, nums):
        """Time Limit Exceeded"""
        while nums:
            num = nums.pop()
            if num in nums:
                return True
            
        return False

    def containsDuplicate4(self, nums):
        """120ms"""
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        
        return False
