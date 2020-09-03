"""
Given an array of integers A sorted in non-decreasing order, return an array of 
the squares of each number, also in sorted non-decreasing order.

Example 1:

    Input: [-4,-1,0,3,10]
    Output: [0,1,9,16,100]

Example 2:

    Input: [-7,-3,2,3,11]
    Output: [4,9,9,49,121]

Note:
    1. 1 <= A.length <= 10000
    2. -10000 <= A[i] <= 10000
    3. A is sorted in non-decreasing order.
"""


from collections import deque


class Solution:    
    def sortedSquares1(self, A):    # 224ms
        return sorted([x * x for x in A])

    def sortedSquares2(self, A):    # 328ms
        res, i = deque(), 0
        for x in A:
            cur = x * x
            if (x >= 0) and res:
                while i < len(res) and cur >= res[i]:
                    i += 1
                
                if i == len(res):
                    res.append(cur)
                else:
                    res.insert(i, cur)
            else:
                res.appendleft(cur)
        
        return res
