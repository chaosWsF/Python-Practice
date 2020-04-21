"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return 
the maximum number. The time complexity must be in O(n).

Example 1:

    Input: [3, 2, 1]
    Output: 1
    Explanation: The third maximum is 1.

Example 2:

    Input: [1, 2]
    Output: 2
    Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:

    Input: [2, 2, 3, 1]
    Output: 1
    Explanation: Note that the third maximum here means the third maximum distinct number.
    Both numbers with value 2 are both considered as second maximum.

"""


class Solution:
    def thirdMax1(self, nums):    # 48ms
        # if not nums:
        #     return float('-inf')
        
        nums.sort()
        tmp = list(dict.fromkeys(nums))
        return tmp[-3] if len(tmp) > 2 else tmp[-1]

    def thirdMax2(self, nums):    # 44ms
        return sorted(list(set(nums)))[-3] if len(set(nums)) > 2 else max(nums)
    
    def thirdMax3(self, nums):
        max_1to3 = [float('-inf')] * 3
        for n in set(nums):
            if n > max_1to3[0]:
                max_1to3[1:] = max_1to3[:2]
                max_1to3[0] = n
            elif n > max_1to3[1]:
                max_1to3[2] = max_1to3[1]
                max_1to3[1] = n
            elif n > max_1to3[2]:
                max_1to3[2] = n
        
        return max_1to3[2] if max_1to3[2] != float('-inf') else max_1to3[0]
