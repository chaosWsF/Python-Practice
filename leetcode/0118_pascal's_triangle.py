"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

    Input: 5
    Output:
    [
        [1],
        [1,1],
    [1,2,1],
    [1,3,3,1],
    [1,4,6,4,1]
    ]
"""


class Solution:
    def generate1(self, numRows):
        """half recurrence (24ms)"""
        result = []
        for n in range(1, numRows + 1):
            cur = [1] + [result[-1][i - 1] + result[-1][i] for i in range(1, (n - 1) // 2 + 1)]
            result.append(cur + cur[:(n // 2)][::-1])
        return result
    
        # # faster (20ms)
        # if numRows == 0:
        #     return []
        
        # result = [[1]]
        # for n in range(2, numRows + 1):
        #     cur = [1] + [result[-1][i - 1] + result[-1][i] for i in range(1, (n - 1) // 2 + 1)]
        #     result.append(cur + cur[:(n // 2)][::-1])
        
        # return result

    def generate2(self, numRows):
        """add a zero (24ms)"""
        result = []
        cur = [1]
        for i in range(numRows):
            j = i
            while j > 0:
                cur[j] += cur[j - 1]
                j -= 1
            
            cur.append(0)
            result.append(cur[:i + 1])

        return result
