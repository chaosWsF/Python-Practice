"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up 
in all strings within the list (including duplicates). For example, if a character occurs 3 times in all 
strings but not 4 times, you need to include that character three times in the final answer. You may return 
the answer in any order.

Example 1:

    Input: ["bella","label","roller"]
    Output: ["e","l","l"]

Example 2:

    Input: ["cool","lock","cook"]
    Output: ["c","o"]

Note:
    1. 1 <= A.length <= 100
    2. 1 <= A[i].length <= 100
    3. A[i][j] is a lowercase letter
"""

from collections import Counter
from functools import reduce


class Solution:
    def commonChars1(self, A):
        def helper(cnt1, cnt2):
            if len(cnt1) > len(cnt2):
                cnt1, cnt2 = cnt2, cnt1
            
            res = {}
            for key in cnt1:
                if key in cnt2:
                    res[key] = min(cnt1[key], cnt2[key])
            
            return res

        return [key for key, val in reduce(helper, map(Counter, A)).items() for _ in range(val)]
    
    def commonChars2(self, A):
        res = Counter(A[0])
        for i in range(1, len(A)):
            res &= Counter(A[i])

        return list(res.elements())
