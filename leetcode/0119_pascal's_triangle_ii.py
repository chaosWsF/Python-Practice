"""
Given a non-negative index k where k <= 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

    Input: 3
    Output: [1,3,3,1]

Follow up:
    Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution:
    def getRow1(self, rowIndex):
        """add a zero (20ms)"""
        row = [1]
        for i in range(rowIndex + 1):
            j = i
            while j > 0:
                row[j] += row[j - 1]
                j -= 1
            row.append(0)
        return row[:-1]

    def getRow2(self, rowIndex):
        """half recurrence (24ms)"""        
        row = [1]
        for n in range(2, rowIndex + 2):
            row = [1] + [row[i] + row[i + 1] for i in range((n - 1) // 2)]
            row += row[:(n // 2)][::-1]    
        return row
