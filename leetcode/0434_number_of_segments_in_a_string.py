"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:
    Input: "Hello, my name is John"
    Output: 5
"""


class Solution:
    def countSegments1(self, s):
        return len(s.split())
    
    def countSegments2(self, s):
        res = 0
        for i in range(len(s)):
            if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
                res += 1
        
        return res
