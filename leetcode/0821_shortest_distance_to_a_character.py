"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

    Input: S = "loveleetcode", C = 'e'
    Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

Note:
    1. S string length is in [1, 10000].
    2. C is a single character, and guaranteed to be in string S.
    3. All letters in S and C are lowercase.
"""


class Solution:
    def shortestToChar(self, S, C):
        loc = [float('-inf')]
        for i in range(len(S)):
            if S[i] == C:
                loc.append(i)
        
        loc.append(float('inf'))
        
        res = []
        j = 1
        for i in range(len(S)):
            if i < loc[j]:
                res.append(min(loc[j]-i, i-loc[j-1]))
            elif i == loc[j]:
                res.append(0)
                j += 1
        
        return res
