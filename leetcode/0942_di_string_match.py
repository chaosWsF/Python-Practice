"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length. Return 
any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

    1. If S[i] == "I", then A[i] < A[i+1]
    2. If S[i] == "D", then A[i] > A[i+1]

Example 1:

    Input: "IDID"
    Output: [0,4,1,3,2]

Example 2:

    Input: "III"
    Output: [0,1,2,3]

Example 3:

    Input: "DDI"
    Output: [3,2,0,1]

Note:
    1. 1 <= S.length <= 10000
    2. S only contains characters "I" or "D".
"""


class Solution:
    def diStringMatch(self, S):
        left, right = 0, len(S)
        res = []
        for s in S:
            if s == 'I':
                res.append(left)
                left += 1
            else:
                res.append(right)
                right -= 1

        return res + [left]
