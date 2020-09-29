"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t  (t concatenated with itself 1 or more times)

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"

Example 2:

    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"

Example 3:

    Input: str1 = "LEET", str2 = "CODE"
    Output: ""

Example 4:

    Input: str1 = "ABCDEF", str2 = "ABC"
    Output: ""

Constraints:
    1. 1 <= str1.length <= 1000
    2. 1 <= str2.length <= 1000
    3. str1 and str2 consist of English uppercase letters.
"""


class Solution:
    def gcdOfStrings1(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        for i in range(min(n1, n2), 0, -1):
            if n1 % i == 0 and n2 % i == 0:
                res = str1[:i]
                if res * (n1 // i) == str1 and res * (n2 // i) == str2:
                    return res
        
        return ''

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not (str1 or str2):
            return ''
        elif not str1:
            return str2
        elif not str2:
            return str1
        
        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        
        if str1[:len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):], str2)
        else:
            return ''
