"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

    Input: [2,2,1]
    Output: 1

Example 2:

    Input: [4,1,2,1,2]
    Output: 4
"""


class Solution:
    def singleNumber1(self, nums):
        """Hashtable (80ms)"""
        d = {}
        for num in nums:
            if num in d:
                d.pop(num)
            else:
                d[num] = 1
        
        return list(d.keys())[0]
    
    def singleNumber2(self, nums):
        """Binary Search Recursive (76ms)"""
        if len(nums) == 1:
            return nums[0]
        
        nums.sort()
        mid = len(nums) // 2
        if nums[mid] == nums[mid - 1]:
            if mid % 2 == 0:
                return self.singleNumber2(nums[:mid - 1])
            else:
                return self.singleNumber2(nums[mid + 1:])
        elif nums[mid] == nums[mid + 1]:
            if mid % 2 == 0:
                return self.singleNumber2(nums[mid + 2:])
            else:
                return self.singleNumber2(nums[:mid])
        else:
            return nums[mid]

    def singleNumber3(self, nums):
        """Binary Search loop (80ms)"""
        if len(nums) == 1:
            return nums[0]
        
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = (i + j + 1) // 2
            if nums[mid] == nums[mid - 1]:
                if mid % 2 == 0:
                    j = mid - 2
                else:
                    i = mid + 1
            elif nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    i = mid + 2
                else:
                    j = mid - 1
            else:
                return nums[mid]

        return nums[i]

    def singleNumber4(self, nums):
        """Bit Manipulation XOR (84ms)"""
        result = 0
        for num in nums:
            result ^= num        
        return result

    def singleNumber5(self, nums):    # 80ms
        return sum(set(nums)) * 2 - sum(nums)

    def singleNumber6(self, nums):
        """Hashtable 2 (84ms)"""
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        for key, val in d.items():
            if val == 1:
                return key
