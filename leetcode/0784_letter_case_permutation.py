"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create 
another string. Return a list of all possible strings we could create.

Examples:

    Input: S = "a1b2"
    Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

    Input: S = "3z4"
    Output: ["3z4", "3Z4"]

    Input: S = "12345"
    Output: ["12345"]

Note:
    1. S will be a string with length between 1 and 12.
    2. S will consist only of letters or digits.
"""

import itertools


class Solution:
    def letterCasePermutation1(self, S):
        res, j = [''], len(S)
        i = j - 1
        while i >= 0:
            if S[i].isalpha():
                cur = []
                for s in res:
                    cur.append(S[i].lower() + S[i+1:j] + s)
                    cur.append(S[i].upper() + S[i+1:j] + s)
                
                res, j = cur, i

            i -= 1
        
        if '' in res:
            return [S]
        elif j > 0:
            return [S[:j] + s for s in res]
        else:
            return res

    def letterCasePermutation2(self, S):
        ls = [s.lower() + s.upper() if s.isalpha() else s for s in S]
        return [''.join(s) for s in itertools.product(*ls)]


if __name__ == "__main__":

    sol = Solution()
    
    # S = 'a1b2'
    S = '3z4'
    # S = '12345'

    # print(sol.letterCasePermutation1(S))
    print(sol.letterCasePermutation2(S))
