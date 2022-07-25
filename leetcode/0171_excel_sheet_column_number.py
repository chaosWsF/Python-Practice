"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:

    Input: "A"
    Output: 1

Example 2:

    Input: "AB"
    Output: 28

Example 3:

    Input: "ZY"
    Output: 701
"""


class Solution:
    def titleToNumber1(self, s):
        """28ms (79.56%) 12.8MB (100%)"""
        res = 0
        for ss in s:
            res = res * 26 + ord(ss) - 64
        return res

    def titleToNumber2(self, columnTitle: str) -> int:
        d = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1,27)))
        n = len(columnTitle)
        return sum([d[s]*26**(n-1-i) for i,s in enumerate(columnTitle)])
