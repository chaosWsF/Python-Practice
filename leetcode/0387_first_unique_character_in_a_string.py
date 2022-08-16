"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Example 1:

    s = "leetcode"
    return 0.

Example 2:

    s = "loveleetcode",
    return 2.

Note: You may assume the string contain only lowercase letters.
"""
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]][1] += 1
            else:
                d[s[i]] = [i, 1]
        
        for ss in d:
            if d[ss][1] == 1:
                return d[ss][0]
        
        return -1
    
    def firstUniqChar1(self, s):  # 52ms
        sc = Counter(s)
        for ss in sc:
            if sc[ss] == 1:
                return s.find(ss)
        
        return -1
